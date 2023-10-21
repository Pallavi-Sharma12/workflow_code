from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("test.db")

conn.execute(
    """CREATE TABLE IF NOT EXISTS EMPLOYEE
             (Emp_Id INT PRIMARY KEY  NOT NULL,
             Emp_Name TEXT  NOT NULL);
             """
)


@app.route("/result")
def result():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM EMPLOYEE;")
    data = cur.fetchall()
    return data


@app.route("/results", methods=["POST"])
def results():
    conn = sqlite3.connect("test.db")
    data = [request.get_json()["Emp_Id"], request.get_json()["Emp_Name"]]
    conn.execute("INSERT INTO EMPLOYEE (Emp_Id, Emp_Name) VALUES (?, ?);", data)
    conn.commit()
    return "Data Added"


if __name__ == "__main__":
    app.run(debug=True)

conn.close()
