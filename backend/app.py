from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import content as cnt
import json
app = Flask(__name__)
cors = CORS(app)

# render specific num of questns in maths subject whose chapterName is specified - practice maths
@app.route('/practice/maths/<chapterName>/<num_quest>')
def all_questions_in_chapter_of_maths(chapterName, num_quest):
    result = cnt.all_questions_in_chapter_of_maths(chapterName,int(num_quest) )
    print(result)
    return jsonify({"result":result})

# pick only few questions in each chapter - exam in maths
@app.route('/exam/maths')
def specific_question_in_chapter_maths():
    num_quest = {"Conic Section":3}     # from each chapter how many questions need to be picked
    ques = []
    for chapter in num_quest:
        ques = cnt.specific_question_in_chapter_maths(chapter,num_quest[chapter]) 
    return jsonify({"result":ques})

# based on specified subject and chapter name notes is updated - learning
@app.route('/learning/<subject>/<chapterName>/notes/<userid>',methods=['POST','GET'])
def store_notes_of_chapter(subject,chapterName,userid):
    if request.method == 'POST':
        notes = request.form['notes']   # <form> <p name="notes"> ...  </p> </form>
        cnt.store_notes_of_chapter(userid,subject[0]+"_"+chapterName,notes)
    res = cnt.get_notes(userid,subject[0]+"_"+chapterName)     # updated notes is obtained not necessary to be sent
    return jsonify({"notes":res})

@app.route('/learning/<subject>/<chapterName>/getnotes/<userid>')
def get_notes(subject, chapterName, userid):
    res = cnt.get_notes(userid,subject+"_"+chapterName)     # updated notes is obtained not necessary to be sent
    return jsonify({"notes":res})
    
# take a test, produce test report with data analytics





app.run()
# all_questions_choosen_chapter()
# specific_question_in_chapter()