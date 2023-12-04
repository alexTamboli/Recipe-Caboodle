echo "BUILD START"
python3.10 -m pip install poetry
python3.10 manage.py collectstatic --noinput --clear
poetry install
echo "BUILD END"

