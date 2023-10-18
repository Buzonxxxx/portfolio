# Flask Server Development and Deployment

#### Flask Server
1. Create virtual env
`python3 -m venv venv`
2. Activate venv
`. venv/bin/activate`
3. Install Flask
`pip3 install Flask`
4. Launch the web server in the localhost
`flask --app server run --debug`

#### Deployment
1. Export packages info
`pip3 freeze > requirements.txt`
2. Register and go to Dashboard on https://www.pythonanywhere.com/
3. Create a web project
4. Go to bash and git clone your Flask project
5. Setup virtual env
`mkvirtualenv --python=/usr/bin/python3.9 my-virtualenv`
6. Install Flask
`pip install flask`
7. Go to the project directory and install packages
`pip install -r requirements.txt`
 - pip install flask
8. Go to the web tab and set the virtualenv path
9. Reload the path and open it

#### Reference
- Website Template
  - https://themewagon.com/
  - https://html5up.net/
- Doc
    - https://docs.python.org/3/library/venv.html
    - https://flask.palletsprojects.com/en/3.0.x/
    - https://github.com/Buzonxxxx/portfolio
    - https://www.pythonanywhere.com/
    - https://help.pythonanywhere.com/pages/Flask/
- Sample
    - http://buzonxxxx.pythonanywhere.com/