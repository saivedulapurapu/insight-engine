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

    cur.execute("SELECT id, title, genre, rating FROM movies;")
    rows = cur.fetchall()

    print("🎬 Movies in database:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Failed to read movies")
    print(e)
