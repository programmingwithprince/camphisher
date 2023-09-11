from flask import Flask,render_template,request
import base64, os,time,requests
from binascii import a2b_base64
from flask_ngrok import run_with_ngrok

index='index.html'
url ='https://www.cuemath.com/maths/maths-formulas-for-class-10/'

with open('est.html','r') as f:
	est = f.read()

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def home():
	return render_template(index)
@app.route('/est')
def ester():
	req= requests.get(url)
	text= req.text
	return est
@app.route('/post',methods=["POST",'GET'])
def post():
		if request.method == 'POST':
			datauri = request.get_json()['data']
			pos = datauri.find(',')+1
			data=datauri[pos:]
			print('doing')
			binary_data = a2b_base64(data)
			print('confirm')
			fd = open(f'image_{time.time()}.jpeg', 'wb')
			fd.write(binary_data)
			fd.close()
			print('Done')
			print(os.listdir())
		return 'posted'
		
if __name__ == "__main__":
    app.run()