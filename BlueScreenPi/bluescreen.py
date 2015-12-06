
from flask import Flask, render_template,Response,redirect,request,url_for,send_from_directory
from bluenode import blueNode

app = Flask(__name__)
node=blueNode('/dev/ttyAMA0')

@app.route("/auto",methods=['GET'])
def doAutoGet():
    return render_template('index.html',msg='wellcome');

@app.route("/",methods=['GET'])
@app.route("/stream")
def stream():
    global node	
    tData={
    'msg':node.getResource('Hello World')
    }
    return render_template('index.html',**tData)
    	
if __name__ == "__main__":
    
   #thread.start_new_thread(notify,())
   app.run(host='0.0.0.0', port=80, debug=True)	
	
	
