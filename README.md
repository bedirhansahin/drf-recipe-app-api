# recipe-app-api

### This project made by [Bedirhan Şahin](https://www.linkedin.com/in/bedirhan-sahin/) to impenetration the architecture of REST API


:point_up: **You can cast a look at Swagger by [click here](http://ec2-34-228-80-140.compute-1.amazonaws.com/api/docs/)**

:point_up: **You can view the admin page after creating a user by [click here](http://ec2-34-228-80-140.compute-1.amazonaws.com/admin/)**

You can look to test codes of the project in /app/core/tests and /app/recipe/tests

## Technologies I used while designing the project:

```diff
! Django Rest Framework
! DRF Spectecular
! Rest Framework Authtoken
! Docker
! Amazon Web Services to deploy
! Github Actions
! PostgreSQL
```

## You can:

```diff
+ Create a new user
+ Create a new token of the user you created
+ Update and List all user
+ Create, Update, Delete and List all recipes
+ Create a new tag and ingredient when u create a new recipe
+ Filter the recipe by tag and ingredient
+ Delete or Update ingredient and tags
+ Upload an image for recipes
```

## Download the project

First, create a folder and run ```git clone https://github.com/bedirhansahin/recipe-app-api.git ```

After, run the following commands from CMD:
``` docker build . ```
``` docker-compose build . ```
``` docker-compose up ```

and you can go to [this address](http://127.0.0.1:8090/) on your own browser. You will also see endpoints there.

:warning: **Don't forget use Docker on your computer**:

## If you want to run any command:

``` docker-compose run --rm app sh -c "..." ```

Like

```docker-compose run --rm app sh -c "python manage.py createsuperuser" ```

Thanks Mark Winterbottom for this [valuable course](https://www.udemy.com/course/django-python-advanced/)and help.
