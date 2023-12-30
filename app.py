from flask import Flask, render_template, request

# Import necessary libraries for model and encoding
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
model = joblib.load('depression_model.pkl')
# Custom label mapping for 'Label'
label_mapping = {
    0: "Mild Depression",
    1: "Minimal Depression",
    2: "Moderate Depression",
    3: "Moderately Severe Depression",
    4: "Severe Depression"
}

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        gender = request.form['gender']
        if(gender == 'Male'):
            gender = 1
        
        else:
            gender = 0


        question1 = int(request.form['question1'])
        question2 = int(request.form['question2'])
        question3 = int(request.form['question3'])
        question4 = int(request.form['question4'])
        question5 = int(request.form['question5'])
        question6 = int(request.form['question6'])
        question7 = int(request.form['question6'])
        question8 = int(request.form['question8'])
        question9 = int(request.form['question9'])
        
        

        # Create a list of question scores
        question_scores = [question1, question2, question3, question4, question5, question6, question7, question8, question9]

        # Calculate the total score
        total_score = sum(question_scores)

        # Make a prediction using the model
        label = model.predict([[age,gender,question1,question2,question3,question4,question5,question6,question7,question8,question9,total_score]])
        print(label)
        # Convert predicted_label to an integer
        predicted_label = int(label)
        print(predicted_label)
        # Map the label to its corresponding text value
        predicted_text = label_mapping[predicted_label]
        return render_template('index.html', prediction_result=predicted_text)

if __name__ == '__main__':
    app.run(debug=True)
