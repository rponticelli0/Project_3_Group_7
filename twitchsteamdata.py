from flask import Flask, request, jsonify, render_template
import sqlite3
from pathlib import Path

twitchsteamdata = Flask(__name__)

@twitchsteamdata.route('/')
def home():
    return render_template('index.html')

@twitchsteamdata.route('/search')
def search():
    # Get the search term from the URL
    search_term = request.args.get('search_term')

    # Connect to the database
    conn = sqlite3.connect(Path(''))
    c = conn.cursor()

    # Generate and run search query, need to create script.js to handle the search

    # Close the database connection
    conn.close()

    # Return the results as JSON
    return jsonify(results)





if __name__ == "__main__":
    app.run(debug=True)