# CFG-Bahasa-Parser

cfg.txt -> contains the CFG form of grammar
init.py -> contains function to move CFG from text file into a dictionary
converter.py -> converts the CFG into CNF form and stores it in cnf.txt
cnf.txt -> stores the CNF form of grammar to be accessed for CYK algorithm
cyk.py -> uses CNF to implement CYK Algorithm and determine whether a string is accepted in that language or not
app.py -> frontend file
app url : https://fylnnx-cfg-bahasa-parser-main-sagqcu.streamlit.app/
