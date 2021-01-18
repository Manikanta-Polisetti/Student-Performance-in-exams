from flask import Flask, request,render_template
from joblib import load
app = Flask(__name__)
model = load('performance.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if output>=80:
        output='A'
    elif output>=70:
        output='B'
    elif output>=60:
        output='C'
    elif output>=50:
        output='D'
    else:
        output='E'
    return render_template('index.html', prediction_text='Grade: {}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    #For direct API calls trought request
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
