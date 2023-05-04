from flask import Flask, request, jsonify
import cv2
import os
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    
    return "Flask hello world heroku"
if __name__ == '__main__':
    app.run()
