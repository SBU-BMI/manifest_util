import os
import sys
import argparse
import collections

to_be_uploaded = []


def check_if_duplicates(list_of_elems):
    # Check if given list contains any duplicates
    dupe = [item for item, count in collections.Counter(list_of_elems).items() if count > 1]
    if len(dupe) > 0:
        print('THE FOLLOWING FILES ARE ATTACHED TO MORE THAN ONE IMAGE!!')
        for d in dupe:
            print(str(d))  # stringify just in case


def check_if_not_found(list_of_elems):
    if len(list_of_elems) > 0:
        print('DID NOT FIND!!')
        for i in list_of_elems:
            print(str(i))  # stringify.
        print('DID NOT FIND.')


def find_row(replace_str, search, image_list, manifest_type, f, collection=""):
    found1 = 0
    search_term = ""
    if replace_str:
        search_term = search.replace(replace_str, "")
    # Search httplinks file for item
    with open(image_list) as fb:
        next(fb)  # Skip header row
        for search_row in fb:

            row = search_row.strip().split(',')

            key1 = search_term[:search_term.find(".")].strip()  # Substring to the extension
            # temp = search_row[:search_row.find(".")].strip().split("/")  # Strips the extension and splits to array

            temp = row[0].split("/")
            slide_name = temp[len(temp) - 1]
            val = slide_name[:slide_name.find(".")].strip()  # potential value minus the extension

            if key1.lower() == val.lower():
                found1 = 1
                # Write to file
                if manifest_type == 'map':
                    f.write(collection + "," + row[1] + "," + row[2] + "," + row[3] + "," + search.strip() + "\n")
                    to_be_uploaded.append(search_term.strip())
                else:
                    if manifest_type == 'segmentation':
                        f.write(search_term.strip() + "," + row[1] + "," + row[2] + "," + row[3].strip())
                        to_be_uploaded.append(row[3].strip())
                break
    return found1, search.rstrip()


def main(my_args):
    image_list = my_args['download']
    manifest_type = my_args['type']
    collection_name = my_args['collection']
    replace_str = ''
    if my_args['string']:
        replace_str = my_args['string']

    if my_args['file']:
        my_list = my_args['file']
        if not os.path.isfile(my_list):
            print("File path {} does not exist. Exiting.".format(my_list))
            sys.exit()

    if my_args['directory']:
        my_list = my_args['directory']
        my_list = [x for x in os.listdir(my_list)]
        length = len(my_list)
        if length == 0:
            print("No files in folder {}".format(my_list))
            sys.exit()

    if not os.path.isfile(image_list):
        print("File path {} does not exist. Exiting.".format(my_list))
        sys.exit()

    try:
        f = open('manifest1.csv', 'w')
        if manifest_type == 'segmentation':
            f.write('segmentdir,studyid,clinicaltrialsubjectid,imageid\n')

        if manifest_type == 'map':
            f.write('collectionname,studyid,clinicaltrialsubjectid,imageid,filename\n')

        not_found = []
        if my_args['file']:
            with open(my_list) as fa:
                for search_term in fa:
                    found = False
                    key = search_term
                    # skip blank lines
                    if len(search_term.strip()) > 0:
                        found, key = find_row(replace_str, search_term, image_list, manifest_type, f, collection_name)
                    if not found:
                        not_found.append(key)
        else:
            if my_args['directory']:
                for search_term in my_list:
                    found, key = find_row(replace_str, search_term, image_list, manifest_type, f)
                    if not found:
                        not_found.append(key)
        f.close()

        # Check not found
        check_if_not_found(not_found)

        # Check duplicates
        check_if_duplicates(to_be_uploaded)

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create manifest file.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Path to input file", type=str)
    group.add_argument("-d", "--directory", help="Path to input directory", type=str)
    parser.add_argument("-dl", "--download", help="Path to downloaded quip file", required=True, type=str)
    parser.add_argument("-c", "--collection", help="Collection name", required=False, type=str)
    parser.add_argument("-t", "--type", help="Type of manifest", required=True, type=str)
    parser.add_argument("-s", "--string", help="Substring to replace", required=False, type=str)

    args = vars(parser.parse_args())

    if not args['collection'] and ("map" in args['type'].lower()):
        parser.error("\n--type map requires --collection")

    # 1) Download httplinks.csv from PathDB
    # 2) ls -l | awk '{print $9}' > ~/myList.list
    main(args)
    print('Done.')
    exit(0)
