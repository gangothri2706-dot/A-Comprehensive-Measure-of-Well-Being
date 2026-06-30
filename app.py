from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Human Development Index Project</h2>"

if __name__ == "__main__":
    app.run(debug=True)
    