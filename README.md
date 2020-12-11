Below are the two API which can be tested using Postman

1. GET /users => For getting List of all the users.

2. POST /users => For adding a new user.

# DevDependency => autopep8-1.5.4 pycodestyle-2.6.0 toml-0.10.2

As the part of dynamic port setting the user can change FLASK_RUN_PORT(set to 5000) from .flaskenv file.

For database, MySQL database is used which is hosted on AWS RDS.

Library used for interacting with database is PyMySQL and interaction is done by procedure calls.

A user Table is created which is having all the details of the user.

GET /users route will get list of all the users

response format in status code 200:
{
    "data":
    [
        {
            "address": {
                "address_line_one": "something",
                "address_line_two": null,
                "city": "ahmn",
                "flat_number": "785",
                "pincode": "361001",
                "state": "Gujarat"
            },
            "email": "leam@email.com",
            "mobile": "7778889898",
            "name": "leam",
            "user_id": 14
        }
    ],
    "success": true
}

POST /users route create a new user in database

For Validating the request data Cerberus library is used.

request_body:
{
    "address": {
        "address_line_one": "something",
        "address_line_two":"optional",
        "city": "Ahmedabad",
        "flat_number": "785",
        "pincode": "361001",
        "state": "Gujarat"
    },
    "email": "leam@email.com",
    "mobile": "7778889898",
    "name": "leam"
}

response_body:
{
    "address": {
        "address_line_one": "something",
        "address_line_two":"optional",
        "city": "Ahmedabad",
        "flat_number": "785",
        "pincode": "361001",
        "state": "Gujarat"
    },
    "email": "leam@email.com",
    "mobile": "7778889898",
    "name": "leam",
    "user_id": 15
}

# Procedure For Creating `user` Table

./procedures/create_user_table.sql

#

# Procedure For Inserting row in `user` Table

./procedures/insert_new_user.sql

#

# Get All Users from `user` table

./procedures/get_all_users.sql

#

# Check for existing email and mobile number

./procedures/check_existing_email_mobile.sql

#

# Deployment Procedure 

Deployed my flask app on AWS EC-2. The App is currently hosted on 13.235.51.69 (Public IP)

Used Gunicorn as a service for deployment and nginx as a webserver.

# service file
[Unit]
Description=Service File
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/unizyr
ExecStart=/home/ec2-user/unizyr/venv/bin/gunicorn -b localhost:5000 -w 4 app:app
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true

[Install]
WantedBy=multi-user.target

# Nginx conf file

server {
    listen 80;
    server_name 13.235.51.69;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}