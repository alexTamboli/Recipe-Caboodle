echo "BUILD START"
pip install poetry
python manage.py collectstatic --noinput --clear
python manage.py migrate
poetry install
echo "BUILD END"