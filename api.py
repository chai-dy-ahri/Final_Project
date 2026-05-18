from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

FILE = "employees.csv"


# GET ALL EMPLOYEES
@app.route("/employees", methods=["GET"])
def get_employees():

    df = pd.read_csv(FILE)

    return jsonify(df.to_dict(orient="records"))


# ADD EMPLOYEE
@app.route("/employees", methods=["POST"])
def add_employee():

    df = pd.read_csv(FILE)

    data = request.json

    new_row = pd.DataFrame([data])

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(FILE, index=False)

    return jsonify({
        "message": "Employee added successfully"
    })


# DELETE EMPLOYEE
@app.route("/employees/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):

    df = pd.read_csv(FILE)

    df = df[df["id"].astype(str) != emp_id]

    df.to_csv(FILE, index=False)

    return jsonify({
        "message": "Employee deleted successfully"
    })


# RUN SERVER
if __name__ == "__main__":

    app.run(debug=True)