echo "BUILD START"

pip install poetry
poetry install

echo "DEPENDENCY INSTALL END/n"

echo "COLLECTSTATIC START"
python manage.py collectstatic --no-input
echo "COLLECTSTATIC END/n"

echo "MIGRATE DB"
python manage.py migrate
echo "MIGRATE DB END"

echo "BUILD END"