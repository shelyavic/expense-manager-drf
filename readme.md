## Requirements:
- Miniconda
- Redis
- Google Mail account

## Configuration guide
1. Create an [app-password](https://support.google.com/accounts/answer/185833)
2. Set your email and password in main/settings.py

## Installation guide
1. Create conda environment:  
`conda env create --prefix=./env -f environment.yml`  
2. Activate created environment:  
`conda activate ./env`  
3. Apply migrations:  
`python manage.py migrate`  
4. Start server:  
`python manage.py runserver`  
5. Start celery worker in a new terminal tab (_run_ `conda activate ./env` _if needed_):  
`celery -A main worker -l info -P eventlet`  
6. Start celery beat in a new terminal tab (_run_ `conda activate ./env` _if needed_):  
`celery -A main beat -l info`  

## Documentation
The project has a swagger integration.  
Open `127.0.0.1:8000/swagger` to see all available urls.  