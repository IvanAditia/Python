from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

def insert_data():
  cursor.execute('INSERT INTO users (nama, email) VALUES (?, ?)', (nama, email))

  conn.commit()
  conn.close()

@app.route("/")
def main():
  return render_template('index.html') 

@app.route("/input", methods=["POST"])
def receive_json():
  data = request.get_json()
  nama = data.get('name')
  email = data.get('email')
  print(nama)
  print(email)
  return jsonify({"status": "succes", "nama": nama, "email": email})

if __name__ == "__main__":
  app.run(debug=True)