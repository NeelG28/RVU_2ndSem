#!/bin/bash
mkdir ~/Documents/Backup
cp ~/Documents/*.c ~/Documents/Backup/
cd ~/Documents
tar -czf Backup.tar.gz Backup/
rm -rf ~/Documents/Backup
echo "Backup process completed successfully!"

