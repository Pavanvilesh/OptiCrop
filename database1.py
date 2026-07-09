import sqlite3


# Create Database

def create_database():

    conn = sqlite3.connect("opticrop.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        crop TEXT

    )
    """)

    conn.commit()

    conn.close()



# Save Prediction

def save_prediction(crop):

    conn = sqlite3.connect("opticrop.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO predictions(crop)
        VALUES(?)
        """,
        (crop,)
    )


    conn.commit()

    conn.close()



# Get All Predictions

def get_predictions():

    conn = sqlite3.connect("opticrop.db")

    cursor = conn.cursor()


    cursor.execute("""
    SELECT * FROM predictions
    ORDER BY id DESC
    """)


    data = cursor.fetchall()


    conn.close()


    return data




# Total Prediction Count

def get_crop_count():

    conn = sqlite3.connect("opticrop.db")

    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM predictions"
    )


    count = cursor.fetchone()[0]


    conn.close()


    return count




# Crop Statistics

def get_crop_statistics():

    conn = sqlite3.connect("opticrop.db")

    cursor = conn.cursor()


    cursor.execute("""
    SELECT crop, COUNT(*)
    FROM predictions
    GROUP BY crop
    """)


    data = cursor.fetchall()


    conn.close()


    return data