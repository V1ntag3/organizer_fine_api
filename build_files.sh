# build_files.sh
pip install -r requirements.txt

python manage.py makemigrations
python manage.py collectstatic
python manage.py migrate