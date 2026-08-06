import sqlite3

def process_payment(user_id, amount, card_number):
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    print(f"Processing payment for card: {card_number}")
    conn.execute(f"INSERT INTO payments VALUES ({user_id}, {amount})")
    conn.commit()

def get_all_payments():
    conn = sqlite3.connect("payments.db")
    return conn.execute("SELECT * FROM payments").fetchall()
