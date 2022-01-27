# Game Room


## About

* ...
* ...


## Initial Setup

* Install Python


### Getting Started

* Open cmd

Clone the repository using:

 `git clone https://github.com/Ario124/Game_Room`


 Navigate to the 'Game_Room'
 `cd Game_Room`

Once inside the Game_Room folder
`pip install virtualenv` followed by `virtualenv env` to create virtual env named 'env'


### Virtual Studio Code

* Open Virtual Studio Code and open the folder 'Game_Room'
* Open a terminal and use:
 `& env/Scripts/Activate.ps1` if not already activated

* Install requirements using:
 `python -m pip install -r ./requirements.txt`
* Create a file named `.env` inside 'gameroom' folder

* Open .env and put the secret key like in this example: 
`SECRET_KEY=60e162937ce271c25fed969153b9dbb6085ba44315cb4c`

* You can generate a key using terminal: 
 `python -c 'import secrets; print(secrets.token_hex(75))'`

* Migrate using: `python manage.py migrate`

If everything went according to the instructions without major problems you should be able to run the application using: 
`python manage.py runserver`



