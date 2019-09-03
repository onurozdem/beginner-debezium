import mysql.connector
from faker import Faker

db = mysql.connector.connect(user='user', password='pw', host='0.0.0.0', database='inventory', ssl_disabled=True)
cur = db.cursor()

faker = Faker()

for i in range(0,10000):
    query =  "insert into customers(first_name, last_name, email) values(%s, %s,%s)"
    args = (faker.name(), faker.last_name(), faker.email())
    cur.execute(query, args)
    db.commit()

cur.close()
db.close()

