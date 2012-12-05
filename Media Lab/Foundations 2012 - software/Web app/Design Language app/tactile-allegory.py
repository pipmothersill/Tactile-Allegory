from flask import Flask, render_template
import json
import feedparser
import emotional_adjectives

app = Flask(__name__)

@app.route("/")
def index():
    '''render page
        and then put data at disposal of page
        country_list is variable in globalvoices.py'''
    return render_template("stories.html",
        adjective_list_json_text=json.dumps(emotional_adjectives.adjective_list())
    )

@app.route("/adjective/<adjective>")
def adjective(adjective):
    grammar = emotional_adjectives.recent_stories_from( adjective )
    return render_template("stories.html",
        adjective_list_json_text=json.dumps(emotional_adjectives.adjective_list()),
        adjective_name=adjective,
        grammar=grammar
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
