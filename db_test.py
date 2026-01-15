import psycopg2

try:
    conn = psycopg2.connect(
        dbname="insight_engine",
        user="postgres",
        password="$aiRushi123",
        host="localhost",
        port="5432"
    )
    print("✅ Connected to PostgreSQL successfully")
    conn.close()
except Exception as e:
    print("❌ Connection failed")
    print(e)
