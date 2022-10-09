# recipe-app-api

### This project made to get a better understanding the architecture of REST API


:point_up: **[Swagger Documentation](http://ec2-34-228-80-140.compute-1.amazonaws.com/api/docs/) is avaliable**

:point_up: **You can view the [admin page](http://ec2-34-228-80-140.compute-1.amazonaws.com/admin/) after creating a user**

You can look to test codes of the project in **/app/core/tests** and **/app/recipe/tests**

## Technologies I used while designing the project:


- Django Rest Framework
- DRF Spectecular
- Rest Framework Authtoken
- Docker
- Amazon Web Services
- Github Actions
- PostgreSQL


## You can:


- Create a new user
- Create a new token of the user you created
- Update and List all user
- Create, Update, Delete and List all recipes
- Create a new tag and ingredient when u create a new recipe
- Filter the recipe by tag and ingredient
- Delete or Update ingredient and tags
- Upload an image for recipes


## Download the project

First, create a folder and run
```
git clone https://github.com/bedirhansahin/recipe-app-api.git
cd recipe-app-api
```

After, run the following commands from CMD:
```
docker build .
docker-compose build .
docker-compose up
```

and you can go to [http://127.0.0.1:8090/](http://127.0.0.1:8090/) on your own browser. You will also see endpoints there.

:warning: **Don't forget install Docker on your computer**:

## If you want to run any command:

``` docker-compose run --rm app sh -c "..." ```

Like

```docker-compose run --rm app sh -c "python manage.py createsuperuser" ```

## How to get use swagger?

--> You need to open [Swagger Documentation](http://ec2-34-228-80-140.compute-1.amazonaws.com/api/docs/)
--> Create a new user
--> Create a new token using the user you just created
--> Click the autherize button which on the top right of the page
--> Type Token 'token key you copied' in tokenAuth (apiKey) like **Token a3da72a2257...**
--> After clicking the Autherize Button, you can do whatever you want. Have fun :)


