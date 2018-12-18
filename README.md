# iTransport

Within the project, **Pujan Chamani Cheri**, **Kevin Wienzek** and **Cihan Öztürk** developed a plattform based on python. In the course of this they made use of the python framework: Django. It is a high-level Web framework that encourages rapid development and clean, pragmatic design.

The plattform they build is called iTransport. It is made for two kind of Users: client and contractors. On the one hand you can earn money and on the other hand you can have your packages sent. In order to have your packages sent, you need to create a job on the iTransport plattform, as a user: client. As the user: contractor, you are able to apply on the jobs, created by other users of the plattform. Upon confirmation of your application you can sent the packages of the other users, to earn money.

All in all the plattform: iTransport makes the lifes of two kind of people easier, the once who are too lazy to sent their packages and the once who want to earn money.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Confirm your Python version
```
$ python --version
```

If the output is different to: Python 3.7.0, you need to install the correct version for this project.

If you already installed brew on your system install the correct version of Python, run the following command:

```
$ brew install python3
```

else visit https://brew.sh/index_de, in order to install brew.

Now let’s confirm which version was installed:

```
$ python3 --version
Python 3.7.0
```

You need to install more:

```
$ pip install django-crispy-forms
$ pip install Pillow
$ pip install django-mathfilters
```

### Installing

A step by step series of examples that tell you how to get a development env running
Clone this project into a directory you want and change into this directory.

First start the virtual enviroment:

```
$ pipenv shell
```

Now you need to run the local server:

```
$ python manage.py runserver
```
The terminal outputs the starting development server. Call the server.

## Users
```
admin, admin
xatar, testo1234
arafat, testo1234
cihanKind, testo1234 
kevinKind, testo1234
testUser, testo1234
NewUser, testo1234
```

## Authors

* **Pujan Chamani Cheri** - [PatronPJ](https://github.com/PatronPj)
* **Kevin Wienzek** - [kWienzek](https://github.com/kWienzek)
* **Cihan Öztürk** - [coz1](https://github.com/coz1)

## License

This project is an open source project
