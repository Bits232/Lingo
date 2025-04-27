import sqlite3

def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS language (
            id INTEGER PRIMARY KEY,
            lang TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert(lang):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM language')  # Ensure only one language
    cursor.execute('INSERT INTO language (lang) VALUES (?)', (lang,))
    conn.commit()
    conn.close()

def load_lang():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT lang FROM language LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def delete_lang():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM language')
    conn.commit()
    conn.close()
