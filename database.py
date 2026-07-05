import sqlite3

DB_NAME = "eco_buddy.db"


def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                transport TEXT,
                distance REAL,
                electricity REAL,
                diet TEXT,
                flights INTEGER,
                footprint REAL,
                eco_score INTEGER
            )
        """)

        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Database init error: {e}")
        return False


def save_assessment(
    transport,
    distance,
    electricity,
    diet,
    flights,
    footprint,
    eco_score
):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO assessments (
                transport,
                distance,
                electricity,
                diet,
                flights,
                footprint,
                eco_score
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transport,
            distance,
            electricity,
            diet,
            flights,
            footprint,
            eco_score
        ))

        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Database save error: {e}")
        return False


def get_assessments():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM assessments
            ORDER BY date DESC
        """)

        data = cursor.fetchall()

        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"Database read error: {e}")
        return []