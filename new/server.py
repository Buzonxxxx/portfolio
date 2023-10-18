from flask import Flask, render_template, request, redirect
import csv

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

@app.route('/submit_contact_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Form submitted successfully'
        except:
            return 'Something went wrong'
    else:
        return 'Invalid request method'
