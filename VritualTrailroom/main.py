

from flask import Flask, render_template, Response,redirect,request
from camera import VideoCamera
import os
app = Flask(__name__)

CART=[]

@app.route('/checkOut')
def checkOut():
    return render_template('checkout.html')

@app.route('/tryon/<file_path>',methods = ['POST', 'GET'])
def tryon(file_path):
    file_path = file_path.replace(',','/')
    print("File path="+file_path)
    os.system('python tryOn.py ' + file_path)
    return redirect('http://127.0.0.1:5000/',code=302, Response=None)

@app.route('/tryall',methods = ['POST', 'GET'])
def tryall():
        CART = request.form['mydata'].replace(',', '/')
        print("Cart=="+CART)
        os.system('python test.py ' + CART)
        render_template('checkout.html', message='')


@app.route('/')
def indexx():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/cart/<file_path>",methods = ['POST', 'GET'])
def cart(file_path):
    global CART
    file_path = file_path.replace(',','/')
    print("ADDED", file_path)
    CART.append(file_path)
    return render_template("checkout.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
    
