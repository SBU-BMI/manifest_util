# quip manifest file generator
PURPOSE: FIND IN PathDB httplinks.csv, CREATE manifest.csv

#### Disclaimer: check the output file for accuracy. If not accurate, tweak python file to your needs.

### Usage
1) Download httplinks.csv from PathDB
2) `ls -l | awk '{print $9}' > ~/myList.list  # Make sure no blank lines or 'extra' files that don't belong.`
3) Run `python manifest_file_generator.py "/path/to/myList.list" "/path/to/httplinks.csv" [manifest_type <map | image | segmentation>]`
4) Redirect output to file
