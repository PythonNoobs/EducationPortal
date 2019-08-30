# EducationPortal
This project is a useful education portal to learn different techologies. PythonNoobs is a very friendly communication in telegram. We belive that an education may be free and access. You may join to our project, we will be glad to see you in this project.

# About project
The creator our channel formulated the idea of our project next sentenses:

На сайте пользователь может добавлять учебные материалы(прямые ссылки на материалы или ссылки только на ресурс автора) - книги, видео, курсы. НЕ обязательно тематика будет ограничиваться учебными материалами только по питону или программированию. Для каждого учебного материала формируется своя страница. Соответственно каждый пользователь может проставить оценку учебному материалу по нескольким критериям. Если юзер пользовался каким-то учебным контентом - посещал курсы, читал книгу итд, то он может добавить их к себе на страницу в качестве "использованных для обучения". Соответственно у каждого пользователя в личном кабинете формируется "дорожная карта" его скилов и тех учебных материалов, что он использовал в процессе обучения. В итоге: на сайте будут учебные материалы(ссылки на них) с  рейтингом, список пользователей со скилами и их дорожной картой + можно сделать функционал для поиска людей под проект.


# Authors
Authors this project are members [python-noobs](https://telegram.im/info/python_noobs?lang=ru) channel in the Telegram.

# Project Structure
[Open structure](https://github.com/PythonNoobs/EducationPortal/blob/dev/Basic%20project%20structure.pdf)

## Quick start: 
* Clone repository:
`git clone https://github.com/PythonNoobs/EducationPortal.git <folder name>`
* Create virtual environment: `virtualenv -p python3.7 <name>`
* Activate virtualenv(Linux): `/path/to/env/bin/activate`
* Activate virtualenv(Windows): `\path\to\env\Scripts\activate`
* Install requarements: `pip3 install -r requirements.txt`
* Rename file: *_local_settings.py* to *local_settings.py*
* Need to install PostgreSQL 10 or higher
* Create and apply migrations: `python manage.py makemigrations` & `python manage.py migrate`
* Start project: `python manage.py runserver`

## Branches
**dev, master and prod** branches closed for push. You can make only pull request with 2 reviews from current repository participants.


