from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the CSV data using Pandas
df = pd.read_csv(r'C:\Users\alexw\Documents\Python Projects\flask_test\personnel.csv')

class Person:
    __slots__ = ['name', 'age', 'occupation']

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Occupation: {self.occupation})"

@app.route('/')
def index():
    # Convert the DataFrame to a list of dictionaries for easy handling in the frontend
    personnel_data = df.to_dict(orient='records')
    return render_template('index.html', data=personnel_data)

@app.route('/create_person', methods=['POST'])
def create_person():
    row_data = request.json
    # Create a Person instance using the row data
    person = Person(row_data['Name'], row_data['Age'], row_data['Occupation'])
    print(f"Created Person object: {person}")
    return jsonify({"message": "Person object created successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
