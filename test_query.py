import mysql.connector
import time
from datetime import datetime

config = {
    "host": "49.13.162.106",
    "user": "zap638722-3",
    "password": "cWFaBfqBjjX6Yy32",
    "database": "zap638722-3",
    "charset": "utf8mb4"
}

query = """
SELECT
  d.*,
  e.identifier,
  e.role
FROM
  dealership_data d
  LEFT JOIN dealership_employees e
    ON d.name = e.dealership AND e.identifier = false
WHERE
  d.name = 'saxony_bikes';
"""

try:
    start_total = time.time()
    print(f"[{datetime.now().isoformat()}] ⏳ Starte Verbindung...")

    conn_start = time.time()
    conn = mysql.connector.connect(**config)
    conn_end = time.time()
    print(f"✅ Verbindung aufgebaut in {conn_end - conn_start:.3f}s")

    cursor = conn.cursor(dictionary=True)

    print(f"[{datetime.now().isoformat()}] 🧠 Führe Query aus...")
    query_start = time.time()
    cursor.execute(query)
    rows = cursor.fetchall()
    query_end = time.time()

    print(f"✅ Query erfolgreich in {query_end - query_start:.3f}s")
    print(f"🔢 Anzahl Ergebnisse: {len(rows)}")

    print("\n🔍 Beispiel-Datensatz:")
    if rows:
        print(rows[0])
    else:
        print("⚠️ Keine Daten gefunden.")

    # Server-Infos
    print("\n📡 Verbindungsinformationen:")
    print(f"- Server: {conn.server_host}")
    print(f"- Datenbank: {conn.database}")
    print(f"- Server-Version: {conn.get_server_info()}")

except mysql.connector.Error as err:
    print(f"❌ Fehler: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print(f"✅ Verbindung geschlossen nach {time.time() - start_total:.3f}s Gesamtzeit")
