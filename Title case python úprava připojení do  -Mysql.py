import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="xxxx",
    user="xxxxx",
    password="xxxxx",
    database="xxxxx"
)
# Načtení dat z MySQL do pandas
query = "SELECT * FROM members;"
df = pd.read_sql(query, conn)

# Oprava jmen: odstraní podtržítka a převede na Title Case
df['name_cleaned'] = df['name'].str.replace('_', ' ', regex=False).str.title()

# Aktualizace zpět do MySQL
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        "UPDATE members SET name = %s WHERE member_id = %s",
        (row['name_cleaned'], row['member_id'])
    )

conn.commit()
cursor.close()
conn.close()
