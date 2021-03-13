''' functions related to what needs to be displayed. Fetch video's, text regarding chapter in a subject, exam 
etc.Ex: when you login to the app, chapters available on different subjects, assessments needs to be shown.
'''
from pymongo import MongoClient
from random import randint
db = MongoClient()
mydb = db.Exam_Analyzer_DB
math_collection = mydb['Mathematics']

def all_questions_in_chapter_of_maths(chapterName = "Conic Section"):
    q = math_collection.find({ "ChapterName": chapterName },{"_id":0})
    return [ele for ele in q]

def specific_question_in_chapter_maths(chapterName, num_quest):
    res = []
    for i in range(num_quest):
        i = randint(1,61)
        q = math_collection.aggregate([
            {"$match":{"ChapterName":chapterName}},
            {"$unwind": "$questionSet"},
            {"$match": {"questionSet.questionNumber":i}},
            {"$project": {"_id":0}}
        ])
        res.append([ele for ele in q])
        pprint(res)
    return res