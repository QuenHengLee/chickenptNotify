from sqlalchemy import true
from  dbConn import connect_db
import email.message
import smtplib

def sendMail(subject,content):
    msg = email.message.EmailMessage()
    msg["From"] = "haha89725@gmail.com"
    msg["To"] = "heats99@hotmail.com"
    #msg["To"] = "haha89725@gmail.com"
    #msg["To"] = "ymt40225@gmail.com"
    msg["Subject"] = subject

    msg.set_content(content)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("haha89725@gmail.com","aloiuquaijgiyatf")
    server.send_message(msg)
    server.close()

#sendMail("我是主旨","我是內容")


def insertCases(id, content, price, place, boss, href):
        # 匯入資料庫
        cursor = connect_db.cursor()
        sql = "INSERT INTO cases (id, content, price, place, boss, href) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (id, content, price, place, boss, href)           
        # 執行 SQL 指令
        cursor.execute(sql, val)
        # 提交至 SQL
        connect_db.commit()





# def checkExist(id):
#         # 匯入資料庫
#         cursor = connect_db.cursor()
#         sql = "SELECT * FROM cases WHERE id= '%s'  "
#         val =(id)
#         # 執行 SQL 指令
#         cursor.execute(sql,val)
#         # 提交至 SQL
#         staff_data = cursor.fetchall()
#         if(len(staff_data) == 1):
#                 print(staff_data)
#                 return 1
#         else:
#                 print(staff_data)
#                 return 0

# if(checkExist('bAn5EgQNEmvW')==0):
#         print("NOT")
# else:
#         print("Exist")
