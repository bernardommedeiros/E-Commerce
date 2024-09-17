import pymysql

DEBUG = True

MYSQL_CONN = pymysql.connect(host='nicollasprado.mysql.pythonanywhere-services.com', port=3306, user='root', password='ecommerce14', database='ecommerce')