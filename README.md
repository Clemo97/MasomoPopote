# MasomoPopote

Masomo Popote is an online platform that enables learners access content from the safety/comfort of their homes, and for tutors, it gives them the platform to share their content with an audience.

## Author

* [Atieno Obwanda](https://github.com/AtienoObwanda)


## Getting Started

To get a copy of Masomo Popote running locally on your end, you can:

1. Clone this repository, by running git clone then:

for ssh:
```
git@github.com:AtienoObwanda/MasomoPopote.git
```

or for https: 
```
https://github.com/AtienoObwanda/MasomoPopote.git
```

2. Set up a python environment to run the application:
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install Django
```

### Prerequisites

Before you begin running the application, you must first install all the dependencies listed in the requirements.txt file.

```
 (env) $ pip install -r requirements.txt

```

### Installing

1. Create a database:
  ```
(env) $ psql CREATE DATABASE *DATABASE_NAME*;
(env) $ pip install psycopg2
```

2. Create a new .env file and set up the following configurations:

 * Database name, host, password and user.

3. Make your first migrations: 


```
(env) $ python manage.py migrate 
```


4. Make migrations for the tutors application: 

```
(env) $ python manage.py makemigrations tutors
(env) $ python manage.py migrate
```
5. Create a super user / admin:


```
(env) $ python manage.py createsuperuser
```

## Running the tests

To test the two applications, you can:

```

 Test the  application (tutors):

```
(env) $ python3 manage.py test tutors
```

## Deployment

To get this application deployed live on a server, you can follow the following guide: [How to Deploy Django Applications on Heroku
](https://gist.github.com/AtienoObwanda/5c506e167e3672a1cc93bbf55fac984b)

## Built With

* Python3.9 - Backend

* Django4 - Python Framework

* PostgreSQL - Database 

* Heroku - Deployment

## User Stories:
**As as learner, you can be able to:**
*  Sign up/sign in to the application.
*  Upon signing in, see a list of available courses
*  Enroll for a course of your preference.
* Get access to posted tests.

**As as tutor, you can be able to:**

*  Sign up/sign in to the application.
* Upon login, add courses and tests
* Your course is automatically made available to learners
* As soon as you get an enrollment on your course, you will be able to see the list of enrolled students on your dashboard.

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **Choose** to login or sign up, as a tutor or a learner | Login / Sign up page. User your credentials to access the application|
|Learners: View available courses| Enroll in your desired course| Upon completion, attemp the tests to test your knowledge|
|Tutors: Add new courses and tests|See your added courses and tests| See the list of enrolled students| 

# Contributors:
* [Atieno Obwanda](https://github.com/AtienoObwanda)
* [Moses Karani](https://github.com/Morces)
* [Agnes Mbiti](https://github.com/Agnes-Kalunda)
* [Clement Lumumba](https://github.com/Clemo97)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

