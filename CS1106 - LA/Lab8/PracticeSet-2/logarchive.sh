sudo mkdir /var/log/backups

cd /var/log

sudo cp *.log backups
sudo tar -czf backup_YYYYMMDD.tar.gz backups
sudo tar -tvf backup_YYYYMMDD.tar.gz

