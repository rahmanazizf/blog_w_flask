import csv
from flask import Flask, render_template, request

# configure app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("welcome.html")

@app.route('/register')
def register_get():
    return render_template("login.html")

@app.route('/register', methods=['POST'])
def register_post():
    name = request.form.get("name", False)
    dorm = request.form.get("dorm", False)
    mail = request.form.get("email", False)
    
    # handling null fields
    if not all([name, dorm, mail]):
        return render_template("failure.html")
    
    # handling invalid mail address format
    # TODO: this could be integrated with null fields
    mail_domain = mail[mail.find('@'):]
    correct_mail_domain = '@hogwarts.wiz'
    if mail_domain != correct_mail_domain:
        return render_template('invalid mail.html', incorrect_mail=mail)

    # handling existed member of hogwarts
    with open('wizards.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Wizard'] == name:
                return render_template("duplicate.html", available_name=name)
    
    with open('wizards.csv', 'a') as csvfile:
        fieldnames = ['Wizard', 'Dormitory', 'email']
        # TODO: need to write column names automatically
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Wizard': name, 'Dormitory': dorm, 'email': mail})
    
    return render_template("success.html")

@app.route('/registered')
def registered():
    with open('wizards.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        wiz_names = [row['Wizard'] for row in reader]
        return render_template("registered.html", wizards=wiz_names)

if __name__=='__main__':
    app.run(port=10011)