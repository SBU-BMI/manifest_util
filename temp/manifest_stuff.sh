#!/usr/bin/env bash
# Use if you have a list of stuff to do
# Program modifications necessary

folder_array=("results.005"
  "results.006"
  "results.007"
  "results.008_9"
  "results.010_11")

get_lists_for_manifest() {
  dir="/path/to/json/output/dir/"
  for i in "${folder_array[@]}"; do
    :
    echo "$i"
    cd "$dir/$i"
    ls -l | awk '{print $9}' >"$HOME/$i.list"
  done
  echo "Lists created."
}
# get_lists_for_manifest

create_manifests() {
  for i in "${folder_array[@]}"; do
    :
    echo "$i"
    python file_gen_util.py -f "$i.list" -dl httplinks.csv -t map -s "\-multires" -c myCollection -op "$i.csv"
    # python file_gen_util.py -f "$i.list" -dl httplinks.csv -t map -s prediction- -c myCollection -op "$i.csv"
  done
  echo "Manifests created."
}
# create_manifests

move_manifests() {
  target="/path/to/target/dir"
  for i in "${folder_array[@]}"; do
    :
    mv "$i.csv" "$target/$i/"
  done
  echo "Files moved."
}
# move_manifests

load_jsons() {
  for i in "${folder_array[@]}"; do
    echo "$i"
    source="/path/to/source/dir"
    docker exec -it quip-imageloader maploader -src "$source/$i/$i.csv" -collectionname myCollection -username xxxxx -password xxxxx -type xxx
  done
}
# load_jsons
