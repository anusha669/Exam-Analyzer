''' functions related to what needs to be displayed. Fetch video's, text regarding chapter in a subject, exam 
etc.Ex: when you login to the app, chapters available on different subjects, assessments needs to be shown.
'''
from pymongo import MongoClient
from random import randint
db = MongoClient()
mydb = db.Exam_Analyzer_DB
math_collection = mydb['Mathematics']
user_collection = mydb["UserData"]

# practice section

def all_questions_in_chapter_of_maths(chapterName,num_quest):
    q = math_collection.aggregate([
    {'$match':{"ChapterName":chapterName}},
    {'$unwind':"$questionSet"},{"$project": {"_id":0}},
    { "$sample": { "size": num_quest }}
    ])
    return [ele for ele in q]

# exam section

def specific_question_in_chapter_maths(chapterName, num_quest):
    ques= []
    q = math_collection.aggregate([
            {"$match":{"ChapterName":chapterName}},
            {"$unwind": "$questionSet"},
            {"$project": {"_id":0}},
            { "$sample": { "size": num_quest } }
    ])
    ques.append([ele for ele in q])
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
