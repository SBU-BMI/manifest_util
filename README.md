# manifest file generator
What this does is it looks through your directory of things-to-upload, and it uses each "thing" as a search string to find a matching entry in httplinks.csv

### Disclaimer: 
1.  Check the output file for accuracy.
2.  This program (as well as PathDB) are a work in progress. Updates will be made accordingly.

### Usage
```
python file_gen_util.py -h

usage: file_gen_util.py [-h] (-f FILE | -d DIRECTORY) -dl DOWNLOAD -t TYPE
                        [-s STRING]

Create manifest file.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to input file
  -d DIRECTORY, --directory DIRECTORY
                        Path to input directory
  -dl DOWNLOAD, --download DOWNLOAD
                        Path to downloaded quip file
  -t TYPE, --type TYPE  Type of manifest
  -s STRING, --string STRING
                        Substring to replace
```

For the first parameter, you may give it either a file containing a list of the names of your files to be uploaded, OR you may give it the path to the directory itself.

### By file

1) Download httplinks.csv from PathDB
Click the Collections tab, then go to the collection, and there will be a link that says "download".
2) `ls -l | awk '{print $9}' > ~/myList.list`
3) Run the following command, replacing the (4) input parameters with your appropriate information:

```
python file_gen_util.py "/path/to/upload_dir" "/path/to/httplinks.csv" "manifest_type" "substring_to_replace" > manifest.csv
```


### By directory

Example:

```
python file_gen_util.py -d "/path/to/upload_dir" -dl "/path/to/httplinks.csv" -t "manifest_type"
```

**Parameter:** `manifest_type` <br>
"map" or "segmentation"

**Parameter:** `substring_to_replace` (optional)<br>
If there is a part of the filename that needs to be stripped out (for example, file ends in "-test") then pass "-test" as the last argument.<br>
"-test" will be stripped out of the search string so we can find its match in httplinks.csv