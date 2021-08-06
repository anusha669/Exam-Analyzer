''' functions related to what needs to be displayed. Fetch video's, text regarding chapter in a subject, exam 
etc.Ex: when you login to the app, chapters available on different subjects, assessments needs to be shown.
'''
from pymongo import MongoClient
from random import randint
db = MongoClient()
mydb = db.Exam_Analyzer_DB
math_collection = mydb['Mathematics']
user_collection = mydb["UserData"]

# login
def verify_user(userid, password):
    print(userid, password)
    q = user_collection.find({"userid":userid,"password":password}, 
    {"_id":0,"userid":1, "username":1, "class":1, "test_scores":1})
    return [ele for ele in q]

def userdata_update(uid, array, subject):
    field = "test_scores." + subject
    q = user_collection.update(
        {"userid":uid},
        {'$set':{
            field: array
        }}
    )
    return q
# practice section
def all_questions_in_chapter_of_subject(subjectName,chapterName,num_quest):
    q = mydb[subjectName].aggregate([
    {'$match':{"ChapterName":chapterName}},
    {'$unwind':"$questionSet"},{"$project": {"_id":0}},
    { "$sample": { "size": num_quest }}
    ])
    return [ele for ele in q]

def get_list_chapters(subject):
    chapterNames = mydb[subject].find({}, {'_id':0, 'ChapterName':1} )
    return [chapterName['ChapterName'] for chapterName in chapterNames]
# exam section

def specific_question_in_chapter_maths(chapterName, num_quest):
    ques= []
    q = math_collection.aggregate([
            {"$match":{"ChapterName":chapterName}},
            {"$unwind": "$questionSet"},
            {"$project": {"_id":0}},
            { "$sample": { "size": num_quest } }
    ])
    for ele in q:
        ques.append(ele)
    # ques.append([ele for ele in q])
    return ques

# learning

def store_notes_of_chapter(userid,chapterName,notes):
    result = user_collection.update(
        {"userid":userid, "progress.chapterName":chapterName},
        {'$set': {"progress.$.notes":notes}}
    )

def get_notes(userid,chapterName):
    res = user_collection.find(
        {"userid":userid,"progress.chapterName":chapterName},{"_id":0,"progress.$.notes":1})
    return [ele for ele in res]
