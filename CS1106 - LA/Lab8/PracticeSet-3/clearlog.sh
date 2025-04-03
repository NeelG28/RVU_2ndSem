ls /var/log | grep ".log"
mkdir -p archive
sudo cp /var/log/*.log archive 
sudo tar -cf archive.tar archive
sudo truncate -s 1M /var/log/*.log
if [ $? -eq 0 ]; then
    echo "Operation successful!"
else
    echo "Operation failed!"
fi

