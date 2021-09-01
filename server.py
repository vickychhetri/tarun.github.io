# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, make_response

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, template_folder='template')
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
	    user = request.form['nm']
	
    resp = make_response(render_template('cookie.html'))
    resp.set_cookie('userID', user)
	
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'



# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name
   
# @app.route('/')   
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'

# def gfg():
#    return 'geeksforgeeks'

# app.add_url_rule('/', 'g2g', gfg)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
