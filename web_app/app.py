from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import joblib

app = Flask(__name__)

clf=pickle.load(open('.\model\\finalized_model.sav','rb'))

# Load the scaler
scaler = pickle.load(open('.\model\scaler.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/detect',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final= np.array(int_features).reshape(1, -1) 

    final_num = np.array(final[0][0:7]).reshape(1,-1)
    final_cat = np.array(final[0][7:]).reshape(1,-1)
    final_num_scaled = scaler.transform(final_num)

    # Apply the scaler
    final_scaled = np.concatenate((final_num_scaled[0], final_cat[0]))
    final_scaled = np.array(final_scaled).reshape(1,-1)

    print(int_features)
    print(final_scaled)

    prediction=clf.predict(final_scaled)

    prediction_exp = np.exp(prediction)  

    print(np.exp(prediction_exp))
    return render_template('index.html', pred=prediction_exp)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=33)

