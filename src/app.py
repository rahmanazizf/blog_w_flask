from flask import Flask, render_template, request

# configure app
app = Flask(__name__)

@app.route('/')
def home():
    # request.get.args getting the value of parameter for ?name key, if contains nothing then it will return World!
    name = request.args.get('name', 'World')
    # passing the value of name into name variable inside layout.html
    return render_template('layout.html', name = name)

@app.route('/login')
def login():
    return render_template('login1.html')

if __name__=='__main__':
    app.run(port=10011)