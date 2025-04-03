echo "Before deletion:"
ls /tmp | grep ".tmp"
cd /tmp
rm *.tmp 
echo "After deletion : "
ls /tmp | grep ".tmp"
