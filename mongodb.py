from pymongo import MongoClient
import datetime

def save_text_mongo(path, page, layout, text):
    connection = MongoClient()
    db = connection.db_pdftomongo.col_text_dump
    post = {'file':path, 'pagenumber':page, 'layout':layout, 'text':text, 'createdon':datetime.datetime.now()}
#    print(post)
    post_id = db.insert_one(post).inserted_id
    connection.close()
    return post_id

def save_image_mongo(path, page, layout, imagename, imagesize, imagestream):
    connection = MongoClient()
    db = connection.db_pdftomongo.col_image_dump
    post = {'file':path, 'pagenumber':page, 'layout':layout, 'imagename':imagename, 'imagesize': imagesize, 'imagestream':imagestream, 'createdon':datetime.datetime.now()}
    post_id = db.insert_one(post).inserted_id
    connection.close()
    return post_id

def check_file_exist(path):
    connection = MongoClient()
    db = connection.db_pdftomongo.col_text_dump
    ans =  bool(db.find_one({'file': path}))
    connection.close()
    return ans

def get_image_stream(path, pagenumber, imagename):
    connection = MongoClient()
    db = connection.db_pdftomongo.col_image_dump
    ans =  db.find_one({'file': path, 'pagenumber':pagenumber, 'imagename':imagename})
#    print(ans)
    connection.close()
    return ans['imagesize'], ans['imagestream']
