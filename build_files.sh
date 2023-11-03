echo " BUILD START "
pip install -r requirements.txt
manage.py collectstatic --noinput --clear
echo " BUILD END "