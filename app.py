from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    res = '''
    <!DOCTYPE html>
<html>
<head>
	<title>Cassavazone - Just A Carbon-based Organism</title>
<style>
		p {
			margin: 20;
			padding: 20;
			text-align: center;
		}
</style>
</head>
<body>
	<center>
		<h1>Creating Blog Page with Flask</h1>
		<p>This is the first line</p>
	</center>
</body>
</html>
    '''
    return res

@app.route('/1stpage')
def fst_page():
    res = '''
    <!DOCTYPE html>
<html>
<head>
	<title>Cassavazone - Just A Carbon-based Organism</title>
<style>
		p {
			margin: 20;
			padding: 20;
			text-align: center;
		}
</style>
</head>
<body>
	<center>
		<h1>First Page at Cassavazone</h1>
		<p>This is the first line</p>
	</center>
</body>
</html>
    '''
    return res

@app.route('/2ndpage')
def sec_page():
    res = '''
    <!DOCTYPE html>
<html>
<head>
	<title>Cassavazone - Just A Carbon-based Organism</title>
<style>
		p {
			margin: 20;
			padding: 20;
			text-align: center;
		}
</style>
</head>
<body>
	<center>
		<h1>Second Page at Cassavazone</h1>
		<p>This is the first line</p>
	</center>
</body>
</html>
    '''
    return res

if __name__=='__main__':
    app.run(port=10011)