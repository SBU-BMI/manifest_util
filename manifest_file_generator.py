import os
import sys


def main(my_args):
    arr_len = len(my_args)
    my_dir = my_args[0]
    image_list = my_args[1]
    manifest_type = my_args[2]
    replace_str = ''
    if arr_len == 4:
        replace_str = my_args[3]

    if not os.path.exists(my_dir):
        print("File path {} does not exist. Exiting...".format(my_dir))
        sys.exit()

    my_list = [x for x in os.listdir(my_dir)]
    length = len(my_list)
    if length == 0:
        print("No files in folder {}".format(my_dir))
        sys.exit()

    if not os.path.isfile(image_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    try:
        if manifest_type == 'segmentation':
            print('segmentdir,studyid,clinicaltrialsubjectid,imageid')

        if manifest_type == 'map':
            print('studyid,clinicaltrialsubjectid,imageid,filename')

        if manifest_type == 'image':
            print('path,studyid,clinicaltrialsubjectid,imageid')

        for line_a in my_list:
            if replace_str:
                line_a = line_a.replace(replace_str, "")
            with open(image_list) as fb:
                next(fb)  # Skip header row
                for line_b in fb:
                    key = line_a[:line_a.find(".")].strip()
                    val = line_b[:line_b.find(".")].strip()
                    row = line_b.strip().split(',')
                    if key in val:
                        if manifest_type == 'map':
                            print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                        if manifest_type == 'segmentation':
                            print(line_a.strip() + "," + row[1] + "," + row[2] + "," + row[3])
                        if manifest_type == 'image':
                            print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                        continue

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('\nUSAGE:\n    python ' + os.path.basename(
            __file__) + ' /path/to/upload_dir /path/to/httplinks.csv manifest_type [map | segmentation] '
              + '<optional: substring_to_replace>')
    else:
        main(sys.argv[1:])
