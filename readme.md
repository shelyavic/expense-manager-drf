# Requirements:
- Miniconda
- Redis

# Installation guide
1. Create conda environment
`conda env create --prefix=./env -f environment.yml`
2. Activate created environment:
`conda activate ./env`
3. Apply migrations:
`python manage.py migrate`
4. Start the server:
`python manage.py runserver`
5. Start a celery worker in a new terminal tab (_run_ `conda activate ./env`_if needed_)
`celery -A main worker -l info -P eventlet`
6. Start a celery beat in a new terminal tab (_run_ `conda activate ./env`_if needed_)
`celery -A main beat -l info`