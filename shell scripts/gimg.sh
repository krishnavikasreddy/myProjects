#!/bin/bash

url=$(cat "a.html")

echo $url

vik=$(echo a.html|grep '<div class="rg_meta'||sed -ne 's/.*\(http[^"]*\).*/\1/p')

echo $vik

