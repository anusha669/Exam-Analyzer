from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import content as cnt
import json
from pprint import pprint
app = Flask(__name__)
cors = CORS(app)

# render all questions in maths subject whose chapterName is specified - learning in maths
@app.route('/learnig/maths/chapterName')
def all_questions_in_chapter_of_maths():
    result = cnt.all_questions_in_chapter_of_maths(chapterName = "Conic Section")
    pprint(result)
    return jsonify({"result":result})

# pick only few questions in each chapter - exam in maths
@app.route('/exam/maths')
def specific_question_in_chapter_maths():
    num_quest = {"Conic Section":2}     # from each chapter how many questions need to be picked
    res = []
    for chapter in num_quest:
        res.extend( cnt.specific_question_in_chapter_maths(chapter,num_quest[chapter]) )
    pprint(res)
    return jsonify({"result":res})

app.run()
# all_questions_choosen_chapter()
# specific_question_in_chapter()