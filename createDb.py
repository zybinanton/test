import json
import requests
import sqlite3
import random

BASE_URL = "https://jsonplaceholder.typicode.com/"
db = sqlite3.connect("placeholder.db")
cur = db.cursor()

try:
    cur.execute("DROP TABLE IF EXISTS `users`")
    cur.execute("CREATE TABLE `users`(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(64), username VARCHAR(64), email VARCHAR(64))")
    resp = requests.get(BASE_URL+"users")
    arr = json.loads(resp.text)
    random.shuffle(arr)
    for obj in arr:
        query = "INSERT INTO `users` VALUES(NULL, '{0}', '{1}', '{2}')".format(obj["name"],obj["username"],obj["email"])
        cur.execute(query)
    db.commit()

    cur.execute("DROP TABLE IF EXISTS `comments`")
    cur.execute("CREATE TABLE `comments`(id INTEGER PRIMARY KEY AUTOINCREMENT, postId INTEGER, name TEXT, email VARCHAR(64), body TEXT)")
    resp = requests.get(BASE_URL+"comments")
    arr = json.loads(resp.text)
    random.shuffle(arr)
    for obj in arr:
        query = "INSERT INTO `comments` VALUES(NULL, '{0}', '{1}', '{2}', '{3}')".format(obj["postId"],obj["name"],obj["email"],obj["body"])
        cur.execute(query)
    db.commit()

    cur.execute("DROP TABLE IF EXISTS `posts`")
    cur.execute("CREATE TABLE `posts`(id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER, title TEXT, body TEXT)")
    resp = requests.get(BASE_URL+"posts")
    arr = json.loads(resp.text)
    random.shuffle(arr)
    for obj in arr:
        query = "INSERT INTO `posts` VALUES(NULL, '{0}', '{1}', '{2}')".format(obj["userId"],obj["title"],obj["body"])
        cur.execute(query)
    db.commit()

    print("Done!")

except sqlite3.Error as dbError:
    db.rollback()
    print("DB ERROR - ",dbError)
except:
    print("Error")

finally:
    cur.close()
    db.close()