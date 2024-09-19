run: env
	env/scripts/activate

env: requirements.txt
	pip install -r requirements.txt && python manage.py runserver