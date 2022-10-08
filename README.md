# recipe-app-api

This project made by [Bedirhan Şahin](https://www.linkedin.com/in/bedirhan-sahin/) to impenetration the architecture of REST API

You can cast a look at Swagger by [click here](http://ec2-34-228-80-140.compute-1.amazonaws.com/api/docs/)


You can look to test codes of the project in /app/core/tests and /app/recipe/tests


```diff
- Technologies I used while designing the project:
! Django Rest Framework
! DRF Spectecular
! Rest Framework Authtoken
! Docker
! Amazon Web Services to deploy
! Github Actions
```


```diff
- You can:
+ Create a new user
+ Update and List all user
+ Create a new token of the user you created
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

## If you want to look test codes you can run:
``` docker-compose run --rm app sh -c "python manage.py test" ```