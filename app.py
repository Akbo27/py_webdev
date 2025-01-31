from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

FUNCTIONS = {
    'sin': np.sin,
    'cos': np.cos,
    'x^2': lambda x: x ** 2,
    'sqrt(x)': np.sqrt,
}

@app.route('/')
def index():
    return render_template('index.html', functions=FUNCTIONS.keys())

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

@app.route('/histogram', methods=['POST'])
def histogram():
    data = request.form['data']
    color = request.form.get('color', 'blue')

    values = list(map(float, data.split(',')))

    plt.figure()
    plt.hist(values, bins=10, color=color)
    plt.title("Histogram")
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    hist_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'histogram.png')
    plt.savefig(hist_filename)
    plt.close()

    return render_template('plot.html', plot_url=hist_filename)