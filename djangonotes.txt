Djnago postgres

sudo apt-get install postgresql-server-dev-9.1-server-dev-9.1
and then install 

pip install psycopg2
if this throws error install all dev packages:

sudo apt-get install python-dev

and then try 
pip install psycopg2 
again


in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',                      
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': ''
    }
}

mydb=# DROP ROLE ubuntu;
DROP ROLE
mydb=# CREATE role ubuntu SUPERUSER LOGIN
mydb-# ;
CREATE ROLE
mydb=# CREATE role root SUPERUSER LOGIN
;
CREATE ROLE
mydb=# \q

after this run syncdb
python manage.py syncdb
ubuntu/ubuntu passwords

sudo service postgresql reload

ubuntu@ip-10-179-2-6:~/djangofun$ python manage.py syncdb
Creating tables ...
Creating table testapp_question
Creating table testapp_answer
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)
ubuntu@ip-10-179-2-6:~/djangofun$ python manage.py sql testapp/
CommandError: App with label testapp/ could not be found. Are you sure your INSTALLED_APPS setting is correct?
ubuntu@ip-10-179-2-6:~/djangofun$ ls
build  djangofun  manage.py  README.md  testapp
ubuntu@ip-10-179-2-6:~/djangofun$ python manage.py sql testapp
BEGIN;
CREATE TABLE "testapp_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "subject" varchar(200) NOT NULL,
    "description" text NOT NULL,
    "publication_date" timestamp with time zone NOT NULL
)
;
CREATE TABLE "testapp_answer" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_id" integer NOT NULL REFERENCES "testapp_question" ("id") DEFERRABLE INITIALLY DEFERRED,
    "content" text NOT NULL,
    "best_answer" boolean NOT NULL
)
;

COMMIT;
