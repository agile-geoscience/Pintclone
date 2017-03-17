echo "Deleting images"
rm static/img/*

echo "Deleting database"
rm pin.db

echo "Initializing new db"
source activate python3
python init.py

echo "DONE"
