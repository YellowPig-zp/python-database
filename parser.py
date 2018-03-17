import re

class Parser:

    REST = "\\s*(.*)\\s*"
    COMMA = "\\s*,\\s*"
    AND = "\\s+and\\s+"

    CREATE_CMD = re.compile("create table " + REST)
    LOAD_CMD = re.compile("load " + REST)
    STORE_CMD = re.compile("store " + REST)
    def __init__(self):
        pass
    def


