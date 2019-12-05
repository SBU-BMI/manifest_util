import os
import sys
import argparse


def find_row(replace_str, search_term, image_list, manifest_type, f):
    found = 0
    if replace_str:
        search_term = search_term.replace(replace_str, "")
    # Search httplinks file for item
    with open(image_list) as fb:
        next(fb)  # Skip header row
        for search_row in fb:

            row = search_row.strip().split(',')

            key = search_term[:search_term.find(".")].strip()  # Substring to the extension
            # temp = search_row[:search_row.find(".")].strip().split("/")  # Strips the extension and splits to array

            temp = row[0].split("/")
            slide_name = temp[len(temp) - 1]
            val = slide_name[:slide_name.find(".")].strip()  # potential value minus the extension

            if key.lower() == val.lower():
                found = 1
                # Write to file
                if manifest_type == 'map':
                    f.write(row[1] + "," + row[2] + "," + row[3] + "," + search_term.strip() + "\n")
                if manifest_type == 'segmentation':
                    f.write(search_term.strip() + "," + row[1] + "," + row[2] + "," + row[3])
                break
    return found, key


def main(my_args):
    image_list = my_args['download']
    manifest_type = my_args['type']
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
        f = open('manifest.csv', 'w')
        if manifest_type == 'segmentation':
            f.write('segmentdir,studyid,clinicaltrialsubjectid,imageid\n')

        if manifest_type == 'map':
            f.write('studyid,clinicaltrialsubjectid,imageid,filename\n')

        not_found = []
        if my_args['file']:
            with open(my_list) as fa:
                for search_term in fa:
                    # Ignore blank lines
                    if len(search_term.strip()) > 0:
                        found, key = find_row(replace_str, search_term, image_list, manifest_type, f)
                    if not found:
                        not_found.append(key)
        else:
            if my_args['directory']:
                for search_term in my_list:
                    found, key = find_row(replace_str, search_term, image_list, manifest_type, f)
                    if not found:
                        not_found.append(key)
        f.close()

        if len(not_found) > 0:
            print('Did not find:')
            for i in not_found:
                print(i)

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create manifest file.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Path to input file", type=str)
    group.add_argument("-d", "--directory", help="Path to input directory", type=str)
    parser.add_argument("-dl", "--download", help="Path to downloaded quip file", required=True, type=str)
    parser.add_argument("-t", "--type", help="Type of manifest", required=True, type=str)
    parser.add_argument("-s", "--string", help="Substring to replace", required=False, type=str)
    args = vars(parser.parse_args())

    # 1) Download httplinks.csv from PathDB
    # 2) ls -l | awk '{print $9}' > ~/myList.list
    main(args)
