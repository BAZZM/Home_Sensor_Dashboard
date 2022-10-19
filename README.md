how to run website:

- set up venv: 
py -m venv venv | 
cd venv | 
cd scripts | 
activate

- install requirements: 
py -m pip install -r requirements.txt

- lastly: 
set FLASK_DEBUG="1" | 
set FLASK_APP=website | 
flask run

- check webserver
127.0.0.1:5000
