#!/bin/bash
dir_spaceless=`echo $1 | tr " " - `
save_path="$HOME/Music/1/.1/$dir_spaceless/"
echo "Default save path is $save_path"
keyword=`echo $1 | sed 's/ /%20/g'`
google_url="https://www.google.com/search?site=&tbm=isch&q=$keyword"

echo $save_path
echo $google_url

header="Accept: text/html"
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/46.0"

if [[ -d "$save_path" ]]; then
    echo "You already download these files"
    exit;
else
    mkdir -p $save_path
    wget -q -O- --header="$header" --user-agent="$user_agent" $google_url | grep -oP '<div class=\"rg_meta(.*?)\">(.*?)\}' |grep -oP "(\w+)\:(\/{2})(.*?)(.jpg|.png)" | wget -t1 --connect-timeout=4 -i - -P "$save_path"
fi
