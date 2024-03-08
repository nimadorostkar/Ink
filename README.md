# Ink


[![](https://img.shields.io/badge/python-3.10-orange)](https://www.python.org/)
[![](https://img.shields.io/badge/Django-4.1-green)](https://www.djangoproject.com/)


## How to run

1. Clone this repository

```bash
git clone https://github.com/nimadorostkar/Ink.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Make .env file (use either prod.env.template or dev.env.template to create .env file)

4. Run the following commands to get started (Development)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

5. Make sure you have Postgredb running (Production)

6. you can run them manually, after the containers spin up, like so:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate   
docker exec -it container_id python manage.py createsuperuser
```

7. Build the image and spin up the two containers

```bash
docker-compose up -d --build
```

 enjoy!




<br>
<hr>

https://themewagon.com/themes/free-bootstrap-4-html5-responsive-portfolio-website-template-unfold/

https://demo.templatemonster.com/demo/53507.html?aff=dazzlersoft

https://demo.templatemonster.com/demo/59091.html?aff=dazzlersoft

https://preview.themeforest.net/item/tattoo-studio-responsive-html5-template/full_screen_preview/5405457?ref=dazzlersoft

https://preview.themeforest.net/item/ink-arts-tattoo-salon-html-template/full_screen_preview/17516884?ref=dazzlersoft


https://www.google.com/search?q=A+variety+of+different+tattoo+styles&rlz=1C5CHFA_enIR930IR930&oq=A+variety+of+different+tattoo+styles&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEHMzM2ajBqNKgCALACAA&sourceid=chrome&ie=UTF-8