# DOCs Parser

![Version](https://img.shields.io/pypi/v/1)
![Python](https://img.shields.io/pypi/pyversions/django) 
![Pull request](https://img.shields.io/github/issues-pr/AntiPetrun/pdf_parser)
![License](https://img.shields.io/github/license/AntiPetrun/pdf_parser)
![Forks](https://img.shields.io/github/forks/AntiPetrun/pdf_parser?style=social)

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [FAQs](#faqs)
5. [Updating classroom availabilities](#Updating-classroom-availabilities)

### General Info
***
**DOCs Parser.** 
Web-tool is to created to parse files and return content. This application is in its raw
state and needs further development. In fact, the minimum functionality is implemented. 
An application at this stage of development loads text files and simply displays their 
contents. 

**Restrictions that the application carries on this version:**
1. to upload txt file or any file formats locally
2. for local files use file path to upload
3. pdf files are uploaded locally

## Technologies
***
![Django](https://img.shields.io/pypi/v/django?label=django)
![Django REST framework](https://img.shields.io/pypi/v/djangorestframework?label=djangorestframework)

A list of technologies used within the project:

[Django](https://www.djangoproject.com/): Version 4.2.3, 
[Django REST framework](https://www.django-rest-framework.org/): Version 3.14.0

## Installation
***
1. Clone the repo 
```
$ git clone https://github.com/AntiPetrun/pdf_parser.git
```
2. Install dependencies of your project
```
$ pip install -r requirements.txt
```
3. Go to **src** folder and run server
```
$ python manage.py runserver
```
4. Choose right route according to your needs. Before this look at the views.py
documentation
