from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)
app=Flask(__name__,template_folder="template")
model=pickle.load(open('model_churn.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    a=float(request.form.get(  'accountlength'  ))
    b=float(request.form.get(  'internationalplan'  ))
    c=float(request.form.get(  'voicemailplan'  ))
    d=float(request.form.get(  'numbervmailmessages'  ))
    e=float(request.form.get(  'totaldayminutes'  ))
    f=float(request.form.get(  'totaldaycalls'  ))
    g=float(request.form.get(  'totaldaycharge'  ))
    h=float(request.form.get(  'totaleveminutes'  ))
    i=float(request.form.get(  'totalevecalls'  ))
    j=float(request.form.get(  'totalevecharge'  ))
    k=float(request.form.get(  'totalnightminutes'  ))
    l=float(request.form.get(  'totalnightcalls'  ))
    m=float(request.form.get(  'totalnightcharge'  ))
    n=float(request.form.get(  'totalintlminutes'  ))
    o=float(request.form.get(  'totalintlcalls'  ))
    p=float(request.form.get(  'totalintlcharge'  ))
    q=float(request.form.get(  'numbercustomerservicecalls'  ))

    result=model.predict(np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]]))
    if result==1:
        return "<h1 style='color:green'>Costomer churn prediction : Yes churn</h1>"
        #return render_template('churn_yes.html',prediction_text='Costomer churn prediction : Yes churn')
    else:
        return "<h1 style='color:red'>Costomer churn prediction : No churn</h1>"
        #return render_template('churn_no.html',prediction_text='Costomer churn prediction : No churn')

#app.run(debug=True,port=5001)