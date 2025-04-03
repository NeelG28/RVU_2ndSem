sudo tar -cf archive.tar /var/log
gzip archive.tar
tar -tvf archive.tar.gz
