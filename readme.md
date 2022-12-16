## Requirements:
- Miniconda or venv (python 3.10)
- Redis
- Google Mail account 

## Configuration guide
1. Create an [app-password](https://support.google.com/accounts/answer/185833)
2. Set your email and password in main/settings.py

## Installation guide

### Create virtual environment (Miniconda)
1. Create conda environment:  
`conda env create --prefix=./env -f environment.yml`  
2. Activate created environment:  
`conda activate ./env`  

### Create virtual environment (venv)
1. Create venv environment:  
`python -m venv ./env`  
2. Activate created environment:  
`.\env\Scripts\activate`(Windows)
`source env/bin/activate`(Unix/macOS)

3. Apply migrations:  
`python manage.py migrate`  
4. Start server:  
`python manage.py runserver`  
5. Start celery worker in a new terminal tab (_run_ `conda activate ./env` _if needed_):  
`celery -A main worker -l info -P eventlet`  
6. Start celery beat in a new terminal tab (_run_ `conda activate ./env` _if needed_):  
`celery -A main beat -l info`  

## Docker
1. Fresh start:
`docker compose up -d --build`
2. To stop docker containers:
`docker compose down`
3. To start already built containers:
`docker compose up -d`

## Documentation
The project has a swagger integration.  
Open `scheme/swagger` to see all available urls.  

## Demo
http://shelyavic.pythonanywhere.com/
(No email delivery, session authentication instead of JWT)