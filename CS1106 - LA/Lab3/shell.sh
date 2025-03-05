#!/bin/bash

#gedit the file
gedit test_file.sh &
disown

#opening firefox and then github
firefox https://github.com &
disown
