#!/bin/bash
# convert MarkMonitor AXFR export to Bind format
# usage: sh axfr2bind.sh domain.ext axfr_export_file

cat $2 | grep -v "=====" >> /tmp/tmpfile
cat /tmp/tmpfile > $2
named-compilezone -f text -F raw -o $1.raw $1 $2
named-compilezone -f raw -F text -o $1.bind.txt $1 $1.raw
echo ''
echo 'File: '$1.bind.txt
