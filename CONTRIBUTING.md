2021-06-02 
Author: Adrian Papineau

# Intro
Making this in Python only because it is the only language I am comfortable with. I plan on using pyqt for the GUI, and sqlite3 for the database storage.

Intended to be cross-platform (Windows/OSX/Linux)

**If you know a better suited language**, like lets say Clojure and ClojureScript, please don't hesitate to start programming this project in it. The basis of how it should work should be about the same from language to language.

# File structure
## (Just a rough outline, change as nessisary)

* __FILE 1: main.py__---------------main with all initilizations 
* __FILE 2: ndDb.py__ --------------database init (sqlite3)
* __FILE 3: ndGUImain.py__----------pyqt base frontend
* __FILE 4: ndGUIstatic.py__--------pyqt static frontend
* __FILE 5: ndGUIdynamic.py__-------pyqt dynamic frontend
* __FILE 6: ndLANG.py__-------------NLTK language processing
