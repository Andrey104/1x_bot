import sqlite3

def create():
    db = sqlite3.connect('1x.sqlite3')
    c = db.cursor()
    c.execute("CREATE TABLE event (id INTEGER PRIMARY KEY AUTOINCREMENT,type BOOLEAN NOT NULL, idn TEXT);")
    db.commit()
    c.close()
    db.close()
    return 'ok'

def save_event_line():
    db = sqlite3.connect('payment.sqlite3')
    c = db.cursor()
    # c.execute("INSERT INTO event (type) VALUES (?, ?, ?, ?, ?);", (type_value, str(now), client_value, str(sum_value), order_id_value))
    db.commit()
    c.close()
    db.close()
    return 'ok'

create()