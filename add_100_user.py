import pymysql
import random

db = pymysql.connect("127.0.0.1", "goods", "goods", "meiduo_goods", charset='utf8')
cursor = db.cursor()
print("sql链接成功")

j = 301
for num in range(0,100):


    demo = "qwera"
    temp = "start"
    for i in range(5):
        random_demo =random.randint(1,16)
        if random_demo < 10:
            temp = temp+"0"+str(random_demo)
        else:
            temp += str(random_demo)
    print(temp)
    h = str(j)
    try:

        sql = "INSERT INTO auth_user (id, password,username,history_goods) VALUES (%s,%s,%s,%s)"


        j += 1
        cursor.execute(sql, (j, demo, h, temp))
    except Exception as e:
        print(e)
    db.commit()

db.close()
