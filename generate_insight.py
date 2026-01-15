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
    cur.execute("SELECT title, genre, rating FROM movies;")
    rows = cur.fetchall()

    print("📊 Generated Insights:\n")

    for title, genre, rating in rows:
        if rating >= 8.0:
            insight = f"{title} is a high-rated {genre} movie with a rating of {rating}."
        else:
            insight = f"{title} is a {genre} movie with a rating of {rating}."

        print("Insight:", insight)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Failed to generate insight")
    print(e)
