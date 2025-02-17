from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# File to store the happiness index
HAPPINESS_FILE = "happiness_index.txt"

def read_happiness_index():
    """Read the happiness index from the file."""
    if os.path.exists(HAPPINESS_FILE):
        with open(HAPPINESS_FILE, "r") as file:
            return int(file.read().strip())
    return 50  # Default value if file doesn't exist

def write_happiness_index(index):
    """Write the happiness index to the file."""
    with open(HAPPINESS_FILE, "w") as file:
        file.write(str(index))

@app.route('/')
def index():
    happiness_index = read_happiness_index()
    return render_template('index.html', happiness_index=happiness_index)

@app.route('/get_time')
def get_time():
    now = datetime.now()
    end_of_year = datetime(now.year, 12, 31, 23, 59, 59)
    time_left = end_of_year - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return jsonify(days=days, hours=hours, minutes=minutes, seconds=seconds)

@app.route('/update_happiness', methods=['POST'])
def update_happiness():
    happiness_index = request.json.get('happiness_index')
    write_happiness_index(happiness_index)  # Save the new happiness index
    return jsonify(success=True)

@app.route('/get_year_progress')
def get_year_progress():
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year, 12, 31, 23, 59, 59)
    total_seconds = (end_of_year - start_of_year).total_seconds()
    elapsed_seconds = (now - start_of_year).total_seconds()
    progress = (elapsed_seconds / total_seconds) * 100
    progress_whole_number = int(progress)
    return jsonify(progress=progress_whole_number)

if __name__ == '__main__':
    app.run(debug=True)