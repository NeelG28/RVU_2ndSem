mkdir /tmp
mkdir /tmp/backup
cp *.c ~/tmp/backup
cp *.py ~/tmp/backup
cd ~/tmp
tar -czf Backup-2025-03-28 Backup

udisksctl mount -b /dev/sda1
mv Backup-2025-03-28.tar.gz /media/RVU/Pendrive
udisksctl unmount -b /dev/sda1
rm -rf Backup


