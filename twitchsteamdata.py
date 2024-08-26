from flask import Flask, request, jsonify, render_template
import sqlite3
from pathlib import Path
import pandas as pd

# Initialize Flask app with the correct template folder
twitchsteamdata = Flask(__name__, template_folder='templates')

# Define the route for the home page
@twitchsteamdata.route('/')
def home():
    return render_template('index.html')

# Define the route to get data
@twitchsteamdata.route('/data')
def get_data():
    df = load_data()
    data = df[['twitch_monthly', 'steam_twitch_agg', 'tags']].to_dict(orient='records')
    return jsonify(data)

def load_data():
    conn = sqlite3.connect('Project_3_Group_7/resources/data.sqlite')
    df = pd.read_sql_query("SELECT * FROM merged_table", conn)
    df = df.dropna(subset=['steam_twitch_agg', 'tags', 'twitch_monthly'])
    conn.close()
    return df

# Main driver
if __name__ == "__main__":
    twitchsteamdata.run(debug=True)
