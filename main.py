import sys; import sqlite3; import uuid
from PyQt5.QtGui import QFontMetrics;
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QTextEdit, QPushButton, QScrollArea
import time; import datetime


path = "nDdb.db"
con = sqlite3.connect(path)     
c = con.cursor()

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS blockdb(BlockID TEXT, InflectionID TEXT, InstanceID TEXT, Alternate TEXT, DateCreated TEXT, DateModified TEXT, Content TEXT, PreRelation TEXT, BlockType BOOLEAN, Notable BOOLEAN, AproxMem NUMBER, BgColour TEXT, BulletStyle TEXT, Judgement TEXT, RootedStrength TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 


def new_entry():
    global block_id
    Time = time.time()   
    date = str(datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %I:%M %p')) #Automatically ads the datestamp | May vary depending on timezone
    block_id = str(uuid.uuid4()) #generates a sring of random characters to be used as an id
    spec_id = block_id + str(uuid.uuid4())
    instance_id = spec_id + str(uuid.uuid1())
    c.execute("INSERT INTO blockdb (dateCreated, BlockID, InflectionID, InstanceID) VALUES (?,?,?,?)", (date,block_id,spec_id,instance_id))
    con.commit()

create_table()
new_entry()


def fetch_all_content():#also returns a list of tuples.
	c.execute('SELECT Content FROM blockdb ORDER BY dateCreated')
	list_of_tuples =c.fetchall()
	return list_of_tuples

def convert_list(xlist): #converts list(tuples) to list(strings).
	new_list = [] 
	fetchtuples = xlist	
	for i in fetchtuples:
	    if i == (None,): #DO NOT REMOVE COMMA 
	        continue
	    new_list.append(' '.join(i))
	return(new_list)


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.listnumA = convert_list(fetch_all_content())
		self.widget = QWidget(self)
		self.layout = QVBoxLayout(self.widget)
		self.area = QScrollArea(self)
		self.area.resize(720,720)
		self.area.setWidget(self.widget)
		self.area.setWidgetResizable(True)

	def Test(self):
		for i in self.listnumA:
			text = QTextEdit(self)
			text.document().setPlainText(i)
			font = text.document().defaultFont()
			fontMetrics = QFontMetrics(font)
			textSize = fontMetrics.size(0, text.toPlainText())
			w = 720
			h = textSize.height() + 20
			text.setMinimumSize(w,h)
			text.setMaximumSize(w,h)
			text.resize(w,h)
			text.setReadOnly(False)
			self.layout.addWidget(text)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mn = MainWindow()
	mn.show()
	mn.Test()
	mn.resize(800,800)
	sys.exit(app.exec_())