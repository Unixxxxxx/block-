from flask import Flask, request, jsonify 

app=Flask(__name__)

#home
@app.route('/')
def home():
    return "welcome to the Flask"

#GET route
@app.route('api/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "Hello This is me and my data",
        "status": "success"
    })

#POST route 
@app.route("/api/submit",method=['POST'])
def submit_data():
    data = request.get_json()
    if not data:
        return jsonify({
            "received_data":data,
            "message":"Data received successfully"
        })

if __name__=='__main__':
    app.run(debug=True)
