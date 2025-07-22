from flask import Flask, request, jsonify 

app=Flaks(__name__)

#home
@app.route('/')
def home():
    return "welcome to the Flask"

#get route
