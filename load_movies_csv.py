import csv
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="insight_engine",
    user="postgres",
    password="$aiRushi123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1. Get last ingestion time
cur.execute(
    "SELECT last_ingested_at FROM ingestion_state WHERE source = %s;",
    ("movies_csv",)
)
last_ingested_at = cur.fetchone()[0]

rows_inserted = 0

# 2. Read CSV and ingest
with open("movies.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            """
            INSERT INTO movies (title, genre, rating, created_at)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (title, genre) DO NOTHING;
            """,
            (
                row["title"],
                row["genre"],
                row["rating"],
                datetime.utcnow()
            )
        )
        rows_inserted += cur.rowcount

# 3. Update ingestion state
cur.execute(
    """
    UPDATE ingestion_state
    SET last_ingested_at = %s
    WHERE source = %s;
    """,
    (datetime.utcnow(), "movies_csv")
)

conn.commit()
cur.close()
conn.close()

print(f"✅ Incremental ingestion complete ({rows_inserted} new rows)")
