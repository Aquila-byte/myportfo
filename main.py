from flask import Flask, render_template, request, redirect
import random
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/random.html')
def random_gen():
    with open('facts.csv', mode='r', encoding='windows-1252') as inp:
        reader = csv.reader(inp)
        my_dict = {rows[0]: rows[1] for rows in reader}
        my_list = list(my_dict.items())
        random_entry = random.choice(my_list)
        new_dict = {random_entry[i]: random_entry[i + 1] for i in range(0, len(random_entry), 2)}
        for key, value in new_dict.items():
            my_key = key
            val = value

    return render_template('random.html', my_key =my_key, val =val )


@app.route('/about.html')
def random_gen2():
    my_file = open('about.txt', mode='r')
    the_list = my_file.readlines()
    random_about = random.choice(the_list)
    random_about = random_about

    return render_template('about.html', random_about=random_about)


def write_to_file(data):
    with open('database.txt', mode='a') as base:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(email, message, subject)
        base.write(str(f'\n {name}, {email},{subject},{message}'))
        base.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('thanks.html')
    else:
        return 'something went wrong'
