import psycopg2


def generate_insights():
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

    insights = []

    for title, genre, rating in rows:
        if rating >= 8.0:
            text = f"{title} is a high-rated {genre} movie with a rating of {rating}."
        else:
            text = f"{title} is a {genre} movie with a rating of {rating}."

        insights.append(text)

    cur.close()
    conn.close()

    return insights
