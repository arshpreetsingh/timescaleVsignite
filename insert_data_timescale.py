#!/usr/bin/python

import psycopg2
from datetime import datetime
import time
import random

# connecting throug docke r as well
conn = psycopg2.connect(database = "relay", user = "maropost", password = "Maro123!", host = "0.0.0.0", port = "5432")
print ("Opened database successfully")
cur = conn.cursor()

query_timescale = """CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"""

schema_create_table = """
CREATE TABLE bounces123456 (
time 		TIMESTAMP		NOT NULL,
account_id	CHAR			NOT NULL,
sub_account_id	CHAR			NOT NULL,
to_email	CHAR			NOT NULL,
from_email	CHAR			NOT NULL,
from_domain	CHAR			NOT NULL, 
injection_ip	CHAR	NOT NULL,
remote_ip	CHAR	NOT NULL,
bounce_type	CHAR			NOT NULL,
bounce_class_name	CHAR		NOT NULL,
bounce_class_desc       CHAR            NOT NULL,
classification_id	CHAR		NOT NULL,
transmission_id		CHAR		NOT NULL,
message_id		CHAR		NOT NULL,
bounce_reason		CHAR		NOT NULL, 
STATUS			CHAR		NOT NULL 
);

"""

create_hypertable = """SELECT create_hypertable('bounces123456','time','bounce_reason',4);"""

#cur.execute(schema_create_table);
#conn.commit()
#print ("table created success fully")
#cur.execute(create_hypertable);
#print ("Hyper table created success fully")


random_list_email = ["3636@maorpost.com","346@maorpost.com","36@maorpost.com","346@maorpost.com","3463@maorpost.com","346@maorpost.com","346@maorpost.com","3453@maorpost.com","34@maorpost.com","3245@maorpost.com","324345@maorpost.com","23@maorpost.com"]
random_list_domain = ["345435.com","435634.biz","43645.net","45654.co.in","4565436.hello"]
bounce_type = ["hard","soft"]
bounce_reason = ["email not exist","blocked attachment","mailbox full","message too large","auto reply"] 
bounce_class_type = ["bounce class one","bounce class two","bounce class three"]
bounce_code = [200,400,500,800]


for i in range(1000000):
    timestamp = time.time()
    dt_object = datetime.fromtimestamp(timestamp)
    cur.execute("INSERT INTO bouncefinaldata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dt_object,str(123*i),str(1234*i),random.choice(random_list_email),
    random.choice(random_list_domain),str(i*2.0),str(i*4.0),str(i),random.choice(bounce_type),random.choice(bounce_class_type),str(i),str(i*11),str(i*22),str(i*123),random.choice(bounce_reason),str(i)))
    print ("doing things here as well")
    conn.commit()
