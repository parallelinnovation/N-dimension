import sqlite3

path = "nDdb.db"
con = sqlite3.connect(path)     
c = con.cursor()

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS BlockdbTable(BlockID TEXT, SpecificID TEXT, InstanceID TEXT, Alternate TEXT, DateCreated TEXT, DateModified TEXT, Content TEXT, PreRelation TEXT, BlockType BOOLEAN, Notable BOOLEAN, AproxMem NUMBER, BgColour TEXT, BulletStyle TEXT, Judgement TEXT, RootedStrength TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 


