install:
	pip install -r requirements.txt
	python storm/manage.py migrate
	python storm/manage.py createsuperuser
	python storm/manage.py collectstatic

migrations:
	python storm/manage.py makemigrations
	python storm/manage.py migrate

run:
	python storm/manage.py runserver
