import sqlite3

# Initialize database connection
def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    # Create table for chat history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Insert chat into the database
def save_chat(user_message, bot_response):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)', 
                   (user_message, bot_response))
    conn.commit()
    conn.close()

# Fetch all chat history
def fetch_chat_history():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM chat_history')
    rows = cursor.fetchall()
    conn.close()
    return rows
