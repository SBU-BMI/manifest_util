#!/usr/bin/env bash
# "Mess" example:
# Someone says: I mixed the results files together, good luck figuring it out. :\

concat_csvs () {
  echo "Help is on the way! :)"

  # Download SEER:Rutgers:Lung
  S="http://localhost/csvdownload"
  wget --user $USER --password $PASS "$S/3"  # TODO: Find alternate! Site too secure! :\
  mv manifest.csv seer_rutgers_lung.csv
  # Download SEER:Rutgers:Prostate
  wget --user $USER --password $PASS "$S/4"  # TODO: Find alternate!
  mv manifest.csv seer_rutgers_prostate.csv
  cp seer_rutgers_prostate.csv temp.txt
  # Remove first line
  sed '1d' temp.txt > tmpfile; mv tmpfile temp.csv
  # Concatenate
  cat seer_rutgers_lung.csv temp.csv > lung_and_prostate.csv
  echo "CONCATENATED CSV: lung_and_prostate.csv"
}
concat_csvs

./crt_man.sh
