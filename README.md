# Recipe Caboodle API

This API allows users to share recipes and find recipes. It is developed using Django rest framework. You can find the api [here](https://recipe-caboodle-backend-server.onrender.com/).

## Basic Features

- Custom `User` model and authentication using email and password.
- JWT authentication.
- CRUD endpoints for recipe.
- Search functionality for recipes.
- Password reset functionality.
- Documentation using `drf_spectacular` which support OAS3.
- Unit test using coverage and factory boy.
- Frontend is being built using React.js and can be found [here](https://github.com/alexTamboli/Recipe-Caboodle-Client).

## About

- Tech stach used: 
    - Python
    - Django
    - Django Rest Framework
    - postgreSQL
    - React ( [frontend](https://github.com/alexTamboli/Recipe-Caboodle-Client) )
- For hosting
    - The Web service itself is hosted on [Render](https://render.com/).
    - Media files storage and management is done using Cloudinary.
    - PostgreSQL databse is hosted on render too.
    - Static files are served using whitenoise from local storage of web service only.
- This api has 30 endpoints, which can be accessed using django rest framework's module spectacular.
- Total of 18 schemas are returned as JSON from all the api.


## Quick Start

To get this project up and running locally on your computer follow the following steps.

1. Clone this repository to your local machine.
2. Create a python virtual environment and activate it. We have used Poetry here.
3. Open up your terminal and run the following command to install the packages used in this project.


```
$ pip install poetry
$ poetry install
```

4. Set up a Postgres database for the project.
5. Rename the `.env.example` file found in the root directory of the project to `.env` and update
   the environment variables accordingly. **Note:** For local development, leave the Cloudinary configs empty.
6. Run the following commands to setup the database tables and create a super user.

```
$ python manage.py migrate
$ python manage.py createsuperuser
```

7. Run the development server using:

```
$ python manage.py runserver
```

8. Open a browser and go to http://localhost:8000/.

## License

Usage is provided under the [MIT License](http://opensource.org/licenses/mit-license.php). See LICENSE for the full details.