import sqlite3
import time

conn = sqlite3.connect("data/bot.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        xp INTEGER DEFAULT 0,
        level INTEGER DEFAULT 0,
        last_daily INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS restricted_words (
        server_id INTEGER,
        word TEXT,
        added_by INTEGER,
        PRIMARY KEY (server_id, word))""") # user id of the person who added the word 
    conn.commit()

def get_user(user_id):
    print("rank command triggered")
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

def create_user(user_id):
    print("leaderboard command triggered")
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def add_xp(user_id, amount):
    create_user(user_id)
    cursor.execute("UPDATE users SET xp = xp + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()

def get_leaderboard():
    cursor.execute("SELECT user_id, xp FROM users ORDER BY xp DESC LIMIT 10")
    return cursor.fetchall()

def claim_daily(user_id, amount):
    print("daily command triggered")
    create_user(user_id)
    now = time.time()

    cursor.execute("SELECT last_daily FROM users WHERE user_id = ?", (user_id,))
    last = cursor.fetchone()[0]

    if now - last < 86400:
        return False
    
    cursor.execute("""
        UPDATE users
        SET xp = xp + ?, last_daily = ?
        WHERE user_id = ?
    """, (amount, now, user_id))

    conn.commit()
    return True

def add_restricted_word(server_id, word, added_by):
    cursor.execute("""
        INSERT OR IGNORE INTO restricted_words
        (server_id, word, added_by)
        VALUES (?, ?, ?)
    """, (server_id, word, added_by))

    conn.commit()
    return cursor.rowcount > 0

def remove_restricted_word(server_id, word):
    cursor.execute("""
        DELETE FROM restricted_words
        WHERE server_id = ? AND word = ?
    """, (server_id, word))

    conn.commit()

    return cursor.rowcount > 0

def is_word_restricted(server_id, word):
    cursor.execute("""
        SELECT 1 FROM restricted_words
        WHERE server_id = ? AND word = ?
    """, (server_id, word.lower()))

    return cursor.fetchone() is not None

def get_restricted_words(server_id):
    cursor.execute("""
        SELECT word FROM restricted_words
        WHERE server_id = ?
            """, (server_id,)) 

    return [row[0] for row in cursor.fetchall()]