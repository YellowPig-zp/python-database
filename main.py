from database import Database

EXIT = "exit"
PROMPT = ">"

db = Database()

while True:
    line = input(PROMPT)
    if line == EXIT:
        break
    if not line == "":
        result = db.transact(line)
        if len(result) > 0:
            print(result)
