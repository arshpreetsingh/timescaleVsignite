from pyignite import Client
from datetime import datetime
import time
import random

schema_create_table = """
CREATE TABLE bouncesdatas (
time 		CHAR		PRIMARY KEY,
account_id	CHAR			NULL,
sub_account_id	CHAR			NULL,
to_email	CHAR			NULL,
from_email	CHAR			NULL,
from_domain	CHAR			NULL, 
injection_ip	CHAR	NULL,
remote_ip	CHAR	NULL,
bounce_type	CHAR			NULL,
bounce_class_name	CHAR		NULL,
bounce_class_desc       CHAR            NULL,
classification_id	CHAR		NULL,
transmission_id		CHAR		NULL,
message_id		CHAR		NULL,
bounce_reason		CHAR		NULL, 
STATUS			CHAR		NULL 
);

"""

insert_query = '''INSERT INTO bouncesdatas (
time,account_id,sub_account_id,to_email,from_email,from_domain,
injection_ip,remote_ip,bounce_type,bounce_class_name,bounce_class_desc,
classification_id,transmission_id,message_id,bounce_reason,STATUS)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
'''

# establish connection
client = Client()
client.connect('127.0.0.1', 10800)

# Create table
client.sql(schema_create_table)

# generate some Random data
random_list_email = ["3636@maorpost.com","346@maorpost.com","36@maorpost.com","346@maorpost.com","3463@maorpost.com","346@maorpost.com","346@maorpost.com","3453@maorpost.com","34@maorpost.com","3245@maorpost.com","324345@maorpost.com","23@maorpost.com"]
random_list_domain = ["345435.com","435634.biz","43645.net","45654.co.in","4565436.hello"]
bounce_type = ["hard","soft"]
bounce_reason = ["email not exist","blocked attachment","mailbox full","message too large","auto reply"] 
bounce_class_type = ["bounce class one","bounce class two","bounce class three"]
bounce_code = [200,400,500,800]

test_million = []
# insert-data
for i in range(1000000):
    test_million.append(i)
    timestamp = time.time()
    dt_object = datetime.fromtimestamp(timestamp)
    data = [str(dt_object)+str(i).split()[0]+str(i),str(123*i),str(1234*i),random.choice(random_list_email),random.choice(random_list_domain),
    str(i*2),str(i*4),str(i),random.choice(bounce_type),random.choice(bounce_class_type),
    str(i),str(i*11),str(i*22),str(i*123),random.choice(bounce_reason),str(i)]
    print (data)
    client.sql(insert_query, query_args=data)
