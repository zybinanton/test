import sqlite3

db=sqlite3.connect("database.db")

cursor=db.cursor()

# cursor.execute()
# cursor.executemany()
# cursor.executescript()

list_users=[ (1, "Anton", "qwe"),
             (2, "Kiril", "rty"),
             (3, "Bob", "erw")]


try:
    cursor.execute("Drop  table if exists `users`")
    cursor.execute ("create table `users` (id intenger, login text, password text)")
    cursor.executemany("insert into `users` values(?,?,?)", list_users)
    with open("lesson.sql", "r") as file:
        st=file.read()
        cursor.executescript(st)
    db.commit()
    cursor.execute("select * from `users`")
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    # print(cursor.fetchone())
    print(cursor.fetchmany(2))
    print(cursor.fetchmany(2))

except sqlite3.Error as e:
    print("db error - ", e)
# except:
    # print('eror')
finally:
    cursor.close()
    db.close()



