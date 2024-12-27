from flask import Flask, request, jsonify
#run with pip 
app = Flask(__name__) #create flask application 

@app.route("/")#default route ; location on api 

def home():
    return "Home"
#methods get, post, push , delete
#create get route
@app.route("/get-user/<user_id>")

def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Dior",
        "email": "dior@gmail.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    #in flask, we create a dictionary and jsonify dictionary to return it; 200 = success
    return jsonify(user_data), 200

#post route
@app.route("/create_user",methods=["POST"])

def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)