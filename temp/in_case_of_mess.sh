#!/usr/bin/env bash
# "Mess" example:
# Someone says: I mixed the results together, good luck figuring it out. :\

echo "Help is on the way! :)"

USER="$1"
# Will request password:
TOKEN=$(curl -u $USER http://localhost/jwt/token | python -c "import sys, json; print json.load(sys.stdin)['token']")
# Download SEER:Rutgers:Lung
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" -o seer_rutgers_lung.csv http://localhost/csvdownload/3
# Download SEER:Rutgers:Prostate
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" -o seer_rutgers_prostate.csv http://localhost/csvdownload/4
cp seer_rutgers_prostate.csv temp.txt
# Remove first line
sed '1d' temp.txt > tmpfile
mv tmpfile temp.csv
# Concatenate
cat seer_rutgers_lung.csv temp.csv > lung_and_prostate.csv
# rm "temp.*"
echo "CONCATENATED CSV: lung_and_prostate.csv"

./crt_man.sh
