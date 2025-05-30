from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def insert_data(nama, email):
  conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
  cursor = conn.cursor()
  cursor.execute('INSERT INTO users (nama, email) VALUES (?, ?)', (nama, email))

  conn.commit()
  conn.close()

def tampil_data():
  conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users")
  rows = cursor.fetchall()
  conn.close()
  return rows

@app.route("/")
def main():
  users = tampil_data()
  return render_template('index.html', users=users)
  

@app.route("/input", methods=["POST"])
def receive_json():
  data = request.get_json()
  nama = data.get('name')
  email = data.get('email')
  
  insert_data(nama, email)
  return jsonify({"status": "succes", "nama": nama, "email": email})

if __name__ == "__main__":
  app.run(debug=True)