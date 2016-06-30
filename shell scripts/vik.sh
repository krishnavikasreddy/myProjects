#!/bin/bash

for i in {357780..357790};do
url=$(wget -qO- "http://gallery.greatandhra.com/heroines/top-10-hottest-of-the-week/albumdetail-"$i".html")
vik=$(echo "$url" | grep '<meta property="og:image"'|sed -ne 's/.*\(http[^"]*\).*/\1/p')
wget "$vik"
done


