import pymysql

db_host = "bdpaginaweb.cza6y06uwe8e.us-east-1.rds.amazonaws.com"
db_user = "pablo"
db_password = "30071989Vale*"

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
        )
        print("Successfull connection to the database")
    except:
        print("Error connecting to the database")
        