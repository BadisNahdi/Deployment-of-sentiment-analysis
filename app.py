from flask import Flask, render_template, request
from textblob import TextBlob
def predict_fct(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        my_prediction = predict_fct(str(data))
    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(port=4000, debug=True)