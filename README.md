# quip manifest file generator
PURPOSE: FIND match in PathDB httplinks.csv, and CREATE manifest.csv

#### Disclaimer: check the output file for accuracy. If not accurate, tweak Python file to your needs.

### Usage
1) Download httplinks.csv from PathDB
Click the Collections tab, then go to the collection, and there will be a link that says "download".

2) `ls -l | awk '{print $9}' > ~/myList.list`

3) Run `python manifest_file_generator.py "/path/to/myList.list" "/path/to/httplinks.csv" manifest_type substring_to_replace > manifest.csv`

What this does is it looks through your file of things-to-upload,
and it uses the "thing" as a search string to search for that entry
in httplinks.csv

If there is a part of the filename that needs to be stripped out
(for example, file ends in "-test")
then pass "-test" as the last argument.
"-test" will be stripped out of the input file name so we can find its match in httplinks.csv
