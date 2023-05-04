import sqlite3
def intialise_db():
    global con,cursor
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (name varchar(48),score int);")
    con.commit()

def get_user(user):
    cursor.execute("SELECT EXISTS (SELECT * FROM data WHERE name=(?))",(user,))
    call=cursor.fetchall()
    for tuple in call:
        for i in tuple:
            flag=i

    if flag==0:
        cursor.execute("INSERT INTO data VALUES ((?),0)",(user,))
        print('Your username has been successfully registered.')
    else:
        print(f"Welcome back {user}!")
    con.commit()

def update_score(user,points):
    cursor.execute("SELECT score FROM data WHERE name=(?)",(user,))
    call=cursor.fetchall()
    for tuple in call:
        for i in tuple:
            previous_score=i
    new_score=(previous_score)+(points)
    cursor.execute("UPDATE data SET score=(?) WHERE name=(?)",(new_score,user,))
    con.commit()
    print(f"You\'ve earned {points} points. Your new total score is {new_score}")

def get_score(user):
    cursor.execute("SELECT score FROM data WHERE name=(?)",(user,))
    call=cursor.fetchall()
    for tuple in call:
        for i in tuple:
            score=i
    return score
