# manifest file generator
PURPOSE: FIND match in PathDB httplinks.csv, and CREATE manifest.csv<br>
*Note: Depending on what version of PathDB you're using, downloaded file will initially be named `httplinks.csv` or `manifest.csv`.  This "manifest.csv" is not the manifest!  Please rename.*

#### Disclaimer: 
1.  Check the output file for accuracy.
2.  This program (as well as PathDB) are a work in progress. Updates will be made accordingly.

### Usage
1) Download httplinks.csv from PathDB
Click the Collections tab, then go to the collection, and there will be a link that says "download".

2) Run the following command, replacing the (4) input parameters with your appropriate information:

```
python manifest_file_generator.py "/path/to/upload_dir" "/path/to/httplinks.csv" "manifest_type" [map | image | segmentation] "substring_to_replace" > manifest.csv
```

What this does is it looks through your directory of things-to-upload, and it uses each "thing" as a search string to find a matching entry in httplinks.csv

Parameter: `substring_to_replace` (optional)
If there is a part of the filename that needs to be stripped out (for example, file ends in "-test") then pass "-test" as the last argument.<br>
"-test" will be stripped out of the search string so we can find its match in httplinks.csv
