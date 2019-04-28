'''
CREATE database tutorial;
Lastly add TimescaleDB:

-- Connect to the database
\c tutorial

-- Extend the database with TimescaleDB
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

connection_string = "user=test dbname=test password=test host=0.0.0.0 sslmode=disable port=5000"
'''


#select bounce_reason,bounce_class_name,classification_id,bounce_type,bounce_class_desc,account_id,count(*) from bounceautodata123 WHERE time='2019-03-18 11:32:22.987938+00' GROUP BY bounce_reason,bounce_class_name,classification_id,bounce_type,bounce_class_desc,account_id;

# ceate your DB acording to this one as well:
#{"account_id":"","from":"jj@jj.com","rcpt":"jj@jj.com","domain":"jj.com","status":"bounced","bounce_type":"soft","diagnostic":"[internal] Domain Lookup Failed.","retry":1,"ip":"127.0.0.1"}


#!/usr/bin/python

import psycopg2

# connecting throug docke r as well
conn = psycopg2.connect(database = "relay", user = "maropost", password = "Maro123!", host = "0.0.0.0", port = "5432")
print ("Opened database successfully")
cur = conn.cursor()

#cur.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")


schema_create_table = """
CREATE TABLE bouncefinaldata (
time 		TIMESTAMPTZ		NOT NULL,
account_id	INT			NOT NULL,
sub_account_id	INT			NOT NULL,
to_email	TEXT			NOT NULL,
from_email	TEXT			NOT NULL,
from_domain	TEXT			NOT NULL, 
injection_ip	DOUBLE PRECISION	NOT NULL,
remote_ip	DOUBLE PRECISION	NOT NULL,
bounce_type	TEXT			NOT NULL,
bounce_class_name	TEXT		NOT NULL,
bounce_class_desc       TEXT            NOT NULL,
classification_id	INT		NOT NULL,
transmission_id		INT		NOT NULL,
message_id		INT		NOT NULL,
bounce_reason		TEXT		NOT NULL, 
STATUS			TEXT		NOT NULL 
);

"""
from datetime import datetime
import time
import random
#cur.execute(schema_create_table);
#conn.commit()
#time.sleep(2)

print ("table created success fully")

import time
data_insert_string = """

"""

read_data_query = """SELECT * from bouncestest3"""

random_list_email = ["3636@maorpost.com","346@maorpost.com","36@maorpost.com","346@maorpost.com","3463@maorpost.com","346@maorpost.com","346@maorpost.com","3453@maorpost.com","34@maorpost.com","3245@maorpost.com","324345@maorpost.com","23@maorpost.com"]
random_list_domain = ["345435.com","435634.biz","43645.net","45654.co.in","4565436.hello"]
bounce_type = ["hard","soft"]
bounce_reason = ["email not exist","blocked attachment","mailbox full","message too large","auto reply"] 
bounce_class_type = ["bounce class one","bounce class two","bounce class three"]
bounce_code = [200,400,500,800]

# now based on bounce code I have to update the column name indside the things as well.

#rows = cur.fetchall()
for i in range(10,1000):
    timestamp = time.time()
    dt_object = datetime.fromtimestamp(timestamp)
    cur.execute("INSERT INTO bouncefinaldata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dt_object,123*i,1234*i,random.choice(random_list_email),
    random.choice(random_list_domain),float(i)*2.0,float(i)*4.0,str(i),random.choice(bounce_type),random.choice(bounce_class_type),str(i),i*11,i*22,i*123,random.choice(bounce_reason),str(i)))
    print ("doing things here as well")
    time.sleep(2)
    #print ("inserting data here as well")
    #print ("this is new string we need to look for")	
    #print (new_string)
    #cur.execute(new_string)
    conn.commit()
    #print ("Reading data here as well")
    #cur.execute(read_data_query)
    #rows = cur.fetchall()
    #print ("these are the rows we need to look ")
    #print rows

'''
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
'''
#conn.commit()
#print ("Records created successfully")
#conn.close()
