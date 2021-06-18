# See the documentation about the block database table: https://roamresearch.com/#/app/NDdatabase/page/PAiymHCFy

import sqlite3
import uuid
import time; import datetime


path = "nDdb.db"
con = sqlite3.connect(path)     
c = con.cursor()

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS blockdb(BlockID TEXT, inflectionID TEXT, InstanceID TEXT, Alternate TEXT, DateCreated TEXT, DateModified TEXT, Content TEXT, PreRelation TEXT, BlockType BOOLEAN, Notable BOOLEAN, AproxMem NUMBER, BgColour TEXT, BulletStyle TEXT, Judgement TEXT, RootedStrength TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 


def new_entry():
    global block_id
    Time = time.time()   
    date = str(datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %I:%M %p')) #Automatically ads the datestamp | May vary depending on timezone
    block_id = str(uuid.uuid4()) #generates a sring of random characters to be used as an id
    spec_id = block_id + str(uuid.uuid4())
    instance_id = spec_id + str(uuid.uuid1())
    c.execute("INSERT INTO blockdb (dateCreated, BlockID, SpecificID, InstanceID) VALUES (?,?,?,?)", (date,block_id,spec_id,instance_id))
    con.commit()

create_table()
new_entry()



