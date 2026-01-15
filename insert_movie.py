import psycopg2

try:
    conn = psycopg2.connect(
        dbname="insight_engine",
        user="postgres",
        password="$aiRushi123",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO movies (title, genre, rating)
        VALUES (%s, %s, %s);
        """,
        ("Inception", "Sci-Fi", 8.8)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Movie inserted successfully")

except Exception as e:
    print("❌ Failed to insert movie")
    print(e)
