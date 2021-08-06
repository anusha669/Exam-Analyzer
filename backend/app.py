from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import content as cnt
import json

from scipy.interpolate import interp1d

app = Flask(__name__)
cors = CORS(app)
y = [72, 75, 80, 70, 110]
# login
@app.route('/login/<uid>/<pwd>')
def verify_user(uid, pwd):
    print("call being made")
    result = cnt.verify_user(uid, pwd)
    return jsonify({"result":result})

@app.route('/update/userdata/<subject>', methods=["POST","GET"])
def userdata_update(subject):
    if request.method == 'POST':
        userid = request.form["userid"]
        array = request.form["marks_array"] 
        result = cnt.userdata_update(userid, array.split(','), subject)

@app.route('/expected_marks/<uid>/<subject>/<marks_obtained>/<arry>')
def expected_marks(uid, subject, marks_obtained, arry):
    test, x, y = 1, [], []
    for ele in arry.split(','):
        y.append(int(ele))
        x.append(test)
        test += 1
    y.append(120)
    x.append(test+1)
    interpolate_x = 5
    # Finding the interpolation
    y_interp = interp1d(x,y)
    res = y_interp(interpolate_x)
    print("Value of Y at x = {} is".format(interpolate_x), res)
    y.pop(0)
    y.pop(-1)
    y.insert(3,int(marks_obtained))
    print(y)
    cnt.userdata_update(uid, y, subject)
    return jsonify({"Expected_marks": res.tolist()})

# render specific num of questns in maths subject whose chapterName is specified - practice maths
@app.route('/practice/<subjectName>/<chapterName>/<num_quest>')
def all_questions_in_chapter_of_subject(subjectName, chapterName, num_quest):
    result = cnt.all_questions_in_chapter_of_subject(subjectName, chapterName,int(num_quest) )
    print(result)
    return jsonify({"result":result})

# pick only few questions in each chapter - exam in maths
@app.route('/exam/maths')
def specific_question_in_chapter_maths():
    num_quest = {"Conic Section":3, "Sets":2, "Relations and Functions":1}     # from each chapter how many questions need to be picked
    ques = []
    for chapter in num_quest:
        q = cnt.specific_question_in_chapter_maths(chapter,num_quest[chapter]) 
        ques.extend(q)
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
    
@app.route('/practice/<subject>')
def get_list_chapters(subject):
    res = cnt.get_list_chapters(subject)
    return jsonify({"chapters":res})
# take a test, produce test report with data analytics



# expected_marks()

app.run()
# all_questions_choosen_chapter()
# specific_question_in_chapter()