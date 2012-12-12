import json
import feedparser

# read in mapping of adjectives to paths of related design language variables
f = open('data/emotional_design_language_grammar.json', 'r')
# contents of emotional_design_language_grammar.json
emotional_data = json.loads(f.read())

'''this returns all the adjectives - the top layer "keys" in the json file'''
def adjective_list():
    return emotional_data.keys()

'''this reads in the selective adjective into the json file and returns the related emotional category'''
def emotional_category(adjective):
    emotional_category = emotional_data[adjective]['Emotional Category']
    return emotional_category

'''this reads in the selective adjective into the json file and returns the related design languages'''
def design_language(adjective):
    design_language = emotional_data[adjective]['Design Language Adjective']
    #    design_language_1 = design_language[0]
#    design_language_2 = design_language[1]
#    design_language_3 = design_language[2]
    return design_language

'''this reads in the selective adjective into the json file and returns the related design language colour'''
def design_language_colour(adjective):
    design_language_colour = emotional_data[adjective]['Design Language Colour']
    return design_language_colour

'''this reads in the selective adjective into the json file and returns the related design language image'''
def design_language_image(adjective):
    design_language_image = emotional_data[adjective]['Design Language Image']
    return design_language_image