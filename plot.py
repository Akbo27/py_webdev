from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['UPLOAD_FOLDER'] = 'static/images'

FUNCTIONS = {
    'sin': np.sin,
    'cos': np.cos,
    'x^2': lambda x: x ** 2,
    'sqrt(x)': np.sqrt,
}

COLORS = ['blue', 'red', 'green', 'purple', 'orange']

@app.route('/')
def hello():
    return render_template('main.html', 
                         functions=list(FUNCTIONS.keys()),
                         colors=COLORS)

@app.route('/plot', methods=['POST'])
def plot():
    x_from = float(request.form['x_from'])
    x_to = float(request.form['x_to'])
    selected_function = request.form['function']
    color = request.form.get('color', 'blue')  

    x = np.linspace(x_from, x_to, 500)
    y = FUNCTIONS[selected_function](x)

    plt.figure()
    plt.plot(x, y, color=color)
    plt.title(f"Plot of {selected_function}")
    plt.xlabel('x')
    plt.ylabel('y')
    
    plot_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'plot.png')
    plt.savefig(plot_filename)
    plt.close()

    return render_template('plot.html', plot_url=plot_filename)
