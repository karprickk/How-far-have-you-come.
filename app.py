from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Define your custom start date
    custom_start_date = datetime(2024, 11, 14, 22, 0, 0)  # November 14, 2024, 10:00 PM

    # Pass the start date to the template
    return render_template('index.html', start_date=custom_start_date.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    app.run(debug=True)