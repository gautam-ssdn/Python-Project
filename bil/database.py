import pymysql
db=pymysql.connect("localhost","root","","gautam")
cursor=db.cursor()
sql="UPDATE `menu` SET `PRICE`=150 WHERE `ITEM_NAME` ='burger'"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e :
    print(e)
    db.rollback()

db.close()    
