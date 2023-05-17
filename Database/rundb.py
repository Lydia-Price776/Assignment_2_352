import sqlite3

conn = sqlite3.connect('flights.db')

sql = 'SELECT * FROM Plane'

print("Plane:")
curs = conn.execute(sql)
for row in curs:
    print(row)

sql = 'SELECT * FROM Airport'

print("\nAirport:")
curs = conn.execute(sql)
for row in curs:
    print(row)

sql = 'SELECT * FROM Route'

print("\nRoute:")
curs = conn.execute(sql)
for row in curs:
    print(row)
