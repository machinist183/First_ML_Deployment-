from flask import render_template ,url_for ,request ,flash
from ml_app import app
from ml_app.forms import Predict_Form
import joblib

@app.route('/', methods = ['GET','POST'])
def Home_Page():
    return render_template('home.html')

@app.route('/predict',methods = ['GET','POST'])
def Predict():
    form = Predict_Form()
    if request.method =='POST':
        if form.validate_on_submit:
            sepal_length = int(form.sepal_length.data)
            petal_length = int(form.petal_length.data)
            sepal_width = int(form.sepal_width.data)
            petal_width = int(form.petal_width.data)
            my_model_loaded = joblib.load("my_model.pkl")
            index = my_model_loaded.predict([[sepal_length , petal_length , sepal_width , petal_width]])
            target_names =['setosa', 'versicolor', 'virginica']
            post = target_names[index[0]]
            return render_template('predict.html',form = form ,post = post)
    else:
        return render_template('predict.html' , form = form)

