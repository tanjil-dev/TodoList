rm -f "db.sqlite3"

# Run the migration
python3 manage.py makemigrations
python3 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('tanjil95', 'tanjil.ivo@gmail.com', 'Lumia@578')" | python3 manage.py shell

python3 manage.py runserver