from flask import Flask, request, jsonify, render_template
from pathlib import Path
import pandas as pd
import altair as alt

# Initialize Flask app with the correct template folder
twitchsteamdata = Flask(__name__, template_folder='templates')

# Define the route for the home page
@twitchsteamdata.route('/')
def home():
    return render_template('index.html')

    # Convert the Altair chart to a JSON format
    chart_json = chart.to_json()

    return render_template('index.html', chart=chart_json)

# Define the route to get the Altair chart
@twitchsteamdata.route('/chart')
def get_chart():
    df = load_data()
    chart = create_chart(df)
    return chart.to_json()

# Route to serve hunt_stream_analysis.html
@twitchsteamdata.route('/hunt_stream_analysis')
def serve_hunt_stream_analysis():
    return render_template('hunt_stream_analysis.html')

# Route to serve top_10_interactive.html
@twitchsteamdata.route('/top_10_interactive')
def serve_top_10_interactive():
    return render_template('top_10_interactive.html')

if __name__ == '__main__':
    twitchsteamdata.run(debug=True)
