from flask import Flask, render_template
from markupsafe import escape
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

FUNCTIONS = {
    'sin': np.sin,
    'cos': np.cos,
    'x^2': lambda x: x ** 2,
    'sqrt(x)': np.sqrt,
}

COLORS = ['blue', 'red', 'green', 'purple', 'orange']

@app.route('/')
def hello():
    return render_template('plot.html', 
                         functions=list(FUNCTIONS.keys()),
                         colors=COLORS)