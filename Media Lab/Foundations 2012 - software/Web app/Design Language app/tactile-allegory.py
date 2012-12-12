from flask import Flask, render_template
from pprint import pprint
import json
import feedparser
import emotional_adjectives

app = Flask(__name__)

'''render page using grammar_data (and through this base) html files
    and then read in and return to the specified table entries in grammar_data html file the output from adjective_list function in emotional_adjectives file'''
@app.route("/")
def index():
    adjective_list_json_text=json.dumps(emotional_adjectives.adjective_list())
    return render_template("grammar_data.html",
        adjective_list_json_text=adjective_list_json_text
    )

'''render page using grammar_data (and through this base) html files
    and then read in return to the specified table entries in grammar_data html file the outputs from emotional_category, design_language, design_language_colour, and design_language_image functions in emotional_adjectives file '''
@app.route("/adjective/<adjective>")
def adjective(adjective):
    emotional_category=json.dumps(emotional_adjectives.emotional_category(adjective))
    design_language=json.dumps(emotional_adjectives.design_language(adjective))
    pprint(design_language)
#    design_language_1=design_language[0]
#    design_language_2=design_language[1]
#    design_language_3=design_language[2]
    design_language_colour=json.dumps(emotional_adjectives.design_language_colour(adjective))
    design_language_image=json.dumps(emotional_adjectives.design_language_image(adjective))
    return render_template("grammar_data.html",
        emotional_category=emotional_category,
        design_language=design_language,
#        design_language_2=design_language_2,
#        design_language_3=design_language_3,
        design_language_colour=design_language_colour,
        design_language_image=design_language_image
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
