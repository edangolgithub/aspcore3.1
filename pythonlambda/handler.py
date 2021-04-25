import json
import mysql.connector


#import MySQLdb
#import pymysql
def hello(event, context):

    mydb = mysql.connector.connect(host="remotemysql.com",
                                   user="zZHNrdILlq",
                                   password="hnmJyMt02K",
                                   database="zZHNrdILlq")

    #print(mydb)
    mycursor = mydb.cursor()

    sql = "INSERT INTO evan (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    

    mycursor.execute("SELECT * FROM evan")

    myresult = mycursor.fetchall()

    #for x in myresult:
      #print(x)
      
    mydb1 = mysql.connector.connect(host="freedb.tech",
                                   user="freedbtech_mysqluser",
                                   password="mysqlpassword",
                                   database="freedbtech_freedbmysql")
    mycursor1 = mydb1.cursor()
    mycursor1.execute("SELECT * FROM evan")

    myresult1 = mycursor1.fetchall()
    print(myresult1)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "data": myresult
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
