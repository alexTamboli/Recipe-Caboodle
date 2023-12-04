echo "BUILD START"
pip install poetry
python manage.py collectstatic --no-input
python manage.py migrate
poetry install
echo "BUILD END"