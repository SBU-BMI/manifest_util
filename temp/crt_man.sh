#!/usr/bin/env bash
# Create manifest

ls -lt

echo "your list?"
read LIST
echo "downloaded file?"
read DL
echo "string (or none)?"
read STR
echo "collection?"
read COLL

if [[ "$STR" == "none" ]]; then
  cmd="python file_gen_util.py -f $LIST -dl $DL -t map -c $COLL"
else
  cmd="python file_gen_util.py -f $LIST -dl $DL -t map -s $STR -c $COLL"
fi
$cmd
echo $cmd
