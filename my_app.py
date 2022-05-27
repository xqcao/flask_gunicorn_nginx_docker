from flask import Flask,jsonify,render_template
import json
from users import users

app = Flask(__name__)



def get_user_by_id(user_id):
  
  uu = list(filter(lambda x:x['id']==user_id,users))
  print(uu)
  return uu[0] if len(uu) > 0 else None

@app.route("/users")
def get_all():
  # print(users)
  return jsonify({"users":users})

@app.route("/user/<id>")
def get_one(id):

  u =list(filter(lambda x:x['id']==int(id),users))
  return u[0] if len(u)>0 else {"error":f"user id:{id} not existed"}

@app.route("/")
def home():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=False,port=5001,host='0.0.0.0')