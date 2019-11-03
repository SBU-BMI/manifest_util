# quip manifest file generator
PURPOSE: FIND match in PathDB httplinks.csv, and CREATE manifest.csv
<p style="color:red">Note: Depending on what version of PathDB you're using, downloaded file will initially be named httplinks.csv or manifest.csv</p>

#### Disclaimer: check the output file for accuracy. If not accurate, tweak Python file to your needs.

### Usage
1) Download httplinks.csv from PathDB
Click the Collections tab, then go to the collection, and there will be a link that says "download".

2) Run `python manifest_file_generator.py "/path/to/upload_dir" "/path/to/httplinks.csv" manifest_type substring_to_replace > manifest.csv`

What this does is it looks through your directory of things-to-upload, and it uses each "thing" as a search string to find a matching entry in httplinks.csv

If there is a part of the filename that needs to be stripped out (for example, file ends in "-test") then pass "-test" as the last argument.<br>
"-test" will be stripped out of the search string so we can find its match in httplinks.csv
