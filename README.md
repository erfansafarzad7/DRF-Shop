hi, this is an API-Shop with django-rest-framework 3.15.1

for use this project:

install python

create an virtual environment, then activate it

run these cmds : 

pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
pu manage.py runserver


for create a superuser(admin):
py manage.py createsuperuser
then fill the inputs




accounts:

  "auth/login"
  methods : ["POST", ]
    body(required) : ["phone_number", "password"]
    response : a json includs "accsess" and "refresh" with values


  "auth/login/refresh/"
  methods : ["POST", ]
  body(required) : ["refresh-token", ]
  response : refresh token


  "auth/logout/"
  methods : ["POST", ]
  body : ["", ]
  header : Bearer {token}
  response : ""


  "auth/register/"
  methods : ["POST", ]
  body(required) : ["phone_number", "password"]
  response : ""


  "auth/forgot_password/"
  methods : ["POST", ]
  body(required) : ["phone_number", ]
  response : ""


  "auth/confirm/"
  methods : ["PUT", ]
  body : ["", ]
  session : ["otp", "user"]    *otp is a 4 digits one time password that sends by email or sms
  response : ""
  


  "auth/change_password/{user_id}/"
  methods : ["PUT", ]
  body : ["old_password", "password1", "password2"]
  response : ""












