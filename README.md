# manifest file generator

Facilitates the creation of a manifest file for uploading files to QuIP/PathDB.

If you have a directory of files to upload (eg. featuremaps, heatmaps, or
segmentations), it scans the directory and uses each filename as a search string, in order to find a matching entry in a collection manifest file (httplinks.csv) previously downloaded from QuIP.

## Disclaimer: 
1.  Check the output file for accuracy.
2.  This program (as well as PathDB) are a work in progress. Updates will be made accordingly.

## Usage
```
python file_gen_util.py -h

usage: file_gen_util.py [-h] (-f FILE | -d DIRECTORY) -dl DOWNLOAD -t TYPE
                        [-s STRING]

Create manifest file.

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to input file
  -d DIRECTORY, --directory DIRECTORY (optional)
                        Path to input directory
  -dl DOWNLOAD, --download DOWNLOAD
                        Path to downloaded quip file
  -c COLLECTION, --collection COLLECTION
                        Collection name
  -t TYPE, --type TYPE  Type of manifest
  -s STRING, --string STRING (optional)
                        Substring to replace
```

For the first parameter, you may give it either a file containing a list of the names of your files to be uploaded, OR you may give it the path to the directory itself.

## By file

1) Download httplinks.csv from PathDB

Click the Collections tab, then go to the collection, and there will be a link that says "download".

2) List your directory contents, using a long listing format, and print the filename to a file called myList.list

```
ls -l | awk '{print $9}' > ~/myList.list
```

3) Run the following command, replacing the (4) input parameters with your appropriate information:

**Note:** If your search-replace string begins with a special character, you must escape it.

```
Example:
python file_gen_util.py -f myList.list -dl rutgers_lung.csv -t map -c collection:blah -s "\-multires"
```

<!--
```
python file_gen_util.py -f "/path/to/myList.list" -dl "/path/to/httplinks.csv" -t "manifest_type"
```
-->


## By directory

Example:

```
python file_gen_util.py -d "/path/to/upload_dir" -dl "/path/to/httplinks.csv" -t "manifest_type"
```

**Parameter:** `manifest_type`

- map
- heatmap
- segmentation

**Parameter:** `substring_to_replace` (optional)

If there is a part of the filename that needs to be stripped out (for example, file ends in "-test") then pass "\-test" (note the '-' is escaped) as the last argument.

"-test" will be stripped out of the search string so we can find its match in httplinks.csv
