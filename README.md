# IoT Visual

This repository serves the website of IoT class. This project is open source and the license can be found in LICENSE.

## Getting Started


### Set up Development Environment % Run Server

#### Method 1: `Quick Start`

##### Requirements
- Docker Engine 1.13.1+
- Docker Compose 1.10.0+

##### Containerized Development Environment

1. Edit the `DATABASE_URL` in `src/aquaVisual/settings/local.env`(Copy from [`local.sample.env`](./src/aquaVisual/settings/local.sample.env)). Use the Postgres username, password, database name, and port configured in [`./docker-compose-dev.yml`](./docker-compose-dev.yml).

    ```
    DATABASE_URL=postgres://postgres:postgres@db:5432/aquavisual
    ```

2. Simply run the following command to install all dependencies, activate a containerized Postgres server, and activate a containerized mqtt broker, and run the Django server (`ctrl+c` to stop).

    ```
    docker-compose -f docker-compose-dev.tml up --build
    ```

#### Method 2: `Step by step`

##### Requirements
- Git 1.8+
- Python 3.7+

Create your virtual environment:
`python3 -m venv venv`

And enable it:
`. venv/bin/activate`

##### Install Dependencies

Use pip to install Python dependencies:
`pip3 install -r requirements.txt`

##### Set up Local Environment Variables for Database

Settings are stored in environment variables via [django-environ](http://django-environ.readthedocs.org/en/latest/). The quickest way to start is to copy `local.sample.env` into `local.env`:
    cp src/aquaVisual/settings/local.sample.env src/aquaVisual/settings/local.env

Default is sqlite3, you can change to connect `postgres`. Copy `local.sample.env` and change its parameters to your personal setting.
Then edit the `SECRET_KEY` line in `local.env`, replacing `{{ secret_key }}` into any [Django Secret Key](http://www.miniwebtool.com/django-secret-key-generator/) value. An example:

    SECRET_KEY=&@nn2p)i+ou8rdlddsa(nr$$yd_5&ut#b+p15aj_pr9-h#*o7s

After that, just run the migration.

##### Get Ready for Development

`cd` into the `src` directory:

    cd src

##### Migrate the database:

    python manage.py migrate

##### Create Super User

    python manage.py createsuperuser

Now you’re all set!

##### Run the Development Server

    python manage.py runserver
