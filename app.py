from flask import Flask, render_template, request, redirect, url_for
import pyautogui as pag
import random
import time
from TimeCalc import *

app = Flask(__name__)

# The function to move the mouse for a certain time
def move_mouse(t):
    duration = timeRequested(t)  # Convert t to the required duration in seconds
    end_time = time.time() + Calc(duration)

    while time.time() < end_time:
        x = random.randint(650, 750)
        y = random.randint(50, 150)
        pag.moveTo(x, y, 0.5)
        time.sleep(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the time value from the form input
        t = float(request.form.get('time_value'))  # Getting time input from the user
        move_mouse(t)  # Call the function to move the mouse
        return redirect(url_for('success'))  # Redirect to a success page or message

    return render_template('index.html')  # Render the form

@app.route('/success')
def success():
    return render_template('complete.html')

if __name__ == '__main__':
    app.run()
