import sqlite3
import datetime

conn = sqlite3.connect('flights.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM Flight')


def daily_flight(id_plane, id_route, date, current_price):
    days = 1
    for x in range(365):
        cursor.execute('INSERT INTO Flight (plane, route, date, price) VALUES (?,?,?,?)',
                       (id_plane, id_route, date, current_price))
        days += 1
        if days <= 5:
            date = date + datetime.timedelta(1)
        else:
            date = date + datetime.timedelta(3)
            days = 1


def three_weekly_flight(plane_id, route_id, date, price):
    days = 1
    for x in range(55):
        cursor.execute('INSERT INTO Flight (plane, route, date, price) VALUES (?,?,?,?)',
                       (plane_id, route_id, date, price))
        days += 2
        if days <= 5:
            date = date + datetime.timedelta(2)
        else:
            date = date + datetime.timedelta(3)
            days = 1


def twice_weekly_flight(plane_id, route_id, date, price):
    days = 2
    for x in range(112):
        cursor.execute('INSERT INTO Flight (plane, route, date, price) VALUES (?,?,?,?)',
                       (plane_id, route_id, date, price))
        days += 3
        if days <= 5:
            date = date + datetime.timedelta(3)
        else:
            date = date + datetime.timedelta(4)
            days = 2


def weekly_flight(plane_id, route_id, date, price):
    for x in range(55):
        cursor.execute('INSERT INTO Flight (plane, route, date, price) VALUES (?,?,?,?)',
                       (plane_id, route_id, date, price))
        date = date + datetime.timedelta(7)


# DAIRY FLAT TO HOBART
weekly_flight(1, 'DFHO06', datetime.date(2023, 5, 26), 449.99)

# HOBART TO DAIRY FLAT
weekly_flight(1, 'HODF14', datetime.date(2023, 5, 28), 449.99)

# DAIRY FLAT TO ROTORUA 0600
daily_flight(2, 'DFRO06', datetime.date(2023, 5, 22), 69.99)

# ROTORUA TO DAIRY FLAT 1200
daily_flight(2, 'RODF12', datetime.date(2023, 5, 22), 69.99)

# DAIRY FLAT TO ROTORUA 1600
daily_flight(2, 'DFRO16', datetime.date(2023, 5, 22), 69.99)

# ROTORUA TO DAIRY FLAT 1900
daily_flight(2, 'RODF19', datetime.date(2023, 5, 22), 69.99)

# DAIRY FLAT TO GREAT BARRIER
three_weekly_flight(3, 'DFGB09', datetime.date(2023, 5, 22), 129.49)

# GREAT BARRIER TO DAIRY FLAT
three_weekly_flight(3, 'GBDF09', datetime.date(2023, 5, 23), 129.49)

# DAIRY FLAT TO CHATHAMS
twice_weekly_flight(4, 'DFCI10', datetime.date(2023, 5, 23), 334.99)

# CHATHAMS TO DAIRY FLAT
twice_weekly_flight(4, 'CIDF10', datetime.date(2023, 5, 24), 334.99)

#  DAIRY FLAT TO LAKE TEKAPO
weekly_flight(5, 'DFLT13', datetime.date(2023, 5, 22), 95.49)

# LAKE TEKAPO TO  DAIRY FLAT
weekly_flight(5, 'LTDF13', datetime.date(2023, 5, 23), 95.49)
conn.commit()
conn.close()
