from flask import Flask, request, render_template
import pymysql as pms
app = Flask(__name__)
l=[]
from model import pickle
model=pickle.load(open("model.pkl","rb"))
@app.route("/")
def main():
    return render_template("login.html")



@app.route("/login",methods=['post'])
def login():
    nam=request.form["email"]
    pas=request.form["password"]

    conn=pms.connect(user="root",host="localhost",password="Niranju+6",db="pythonlogin")
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE email=%s and password=%s',(nam,pas))
    
    rows=cursor.fetchone()
    if rows:
     return render_template("index.html")
    else:
        error="Invalid Username or Password"
        return render_template("login.html",error=error)

@app.route("/predict",methods=["post"])
def predict():
    try:
        features= []
        n = 6
        for i in range(0, n):
            ele = float(input())
            features.append(ele)  
            features = [float(i) for i in (request.form.values())]
            pred = model.predict(features)
            print(pred)
        return render_template("index.html",users=l)
    except:
        return render_template("index.html",err="Check the input")


if __name__=='__main__':
    app.run(host='localhost',port=5000, debug=True)