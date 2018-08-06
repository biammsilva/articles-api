# Articles API

## Run in a docker:

__Em linux__: in the application path, type on terminal:
```
sudo docker build -t test .
```

After the build:
```
sudo docker run -p 8000:8000 test
```

Now, access the http://localhost:8000.

## Running in a python env:
__requirements:__
* Having Python3;
* Having python3-pip installed;

If you dont have a virtualenv, do:

```
pip3 install virtualenv
```

Open terminal in project main path and type:

```
virtualenv -p python3 env
```

Activate your:

__linux:__
```
source env/bin/activate
```

__windows:__
```
env\Scripts\activate
```

Install dependencies with your env activated:
```
pip install -r requirements.txt
```

To execute, type:
```
python manage.py runserver
```
Using a virtual env you'll always have to activate it to run your application, this guarantee that you have all dependencies in your environment. Obs: Inside an environment you don't have to say what python version are you using as you started it with a base version.

## Endpoints

__Create a User__
```
POST http://localhost:8000/user
{
  'name': str,
  'email': str,
  'password': str
}
```

__Authenticate User__
```
POST http://localhost:8000/user/auth
{
  'email': str,
  'password': str
}
```
it will return an authentication hash

__Create a post__
```
POST http://localhost:8000/user/article
header "Authorization": str
{
	"title": str,
	"content": "str
}
```
For authorization, use the returned hash

__Like a post__
```
POST http://localhost:8000/user/article
header "Authorization": str
{
	"id": str
}
```
In id, put the article ID

__Get likes number__
```
GET http://localhost:8000/article/like/<article_id>
header "Authorization": str
```

__Get articles__
```
GET http://localhost:8000/article/like
header "Authorization": str
```

__Logout__
```
GET http://localhost:8000/user/logout
header "Authorization": str
```
