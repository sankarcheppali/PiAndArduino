from flask import Flask, render_template,redirect,request,url_for,send_from_directory
from  SerialPublish import SerialPublish
import string
app = Flask(__name__,static_folder='static') # you can place all your static content like javascript,css and images in static folder.
uno=SerialPublish('COM3');
@app.route("/",methods=['GET']) # catch the get request and serve the index.html page
def doGet():
	data={
	'minT':uno.getResource('minT'),
	'maxT':uno.getResource('maxT')
	}
	return render_template('index.html',**data)
@app.route("/minT",methods=['GET'])
def getMinT():
	return uno.getResource('minT')
@app.route("/minT",methods=['POST'])
def setMinT():
	return uno.setResource('minT',str(request.form['minT']))
@app.route("/maxT",methods=['GET']) 
def getMaxT():
	return uno.getResource('maxT')
@app.route('/maxT',methods=['POST'])
def setMaxT():
	return uno.setResource('maxT',str(request.form['maxT']))	
@app.route("/T",methods=['GET'])
def getT():
	return uno.getResource('T')
@app.route("/heaterState",methods=['GET'])
def getHeaterS():
	return uno.getResource('heaterS')

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=80, debug=True)