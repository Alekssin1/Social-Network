# social_network

Щоб запустити проєкт необхідно включити сервер з базою даних(MySQL) прописати наступні команди в корені директорії Social-Network:
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver