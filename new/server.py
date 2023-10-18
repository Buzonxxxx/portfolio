from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('./index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csvfile:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

def send_email(data):
    html = Template(Path('mail_template.html').read_text())

    name = data['name']
    sender_email = data['email']
    message = data['message']

    email = EmailMessage()
    email['from'] = sender_email
    email['to'] = 'buzonliao@gmail.com'
    email['subject'] = 'New message from http://buzonxxxx.pythonanywhere.com/'
    email.set_content(html.substitute({'name': name, 'message': message }), 'html')

    with open('pw/pw.txt', mode='r') as my_file:
        pw = my_file.read()
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('buzonxxxx@gmail.com', pw)
        smtp.send_message(email)
        print('all good boss!')

@app.route('/submit_contact_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            send_email(data)
            return 'Form submitted successfully'
        except:
            return 'Something went wrong'
    else:
        return 'Invalid request method'
