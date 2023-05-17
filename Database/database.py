import sqlite3

conn = sqlite3.connect("flights.db")

conn.execute(
    '''
    CREATE TABLE Plane(
    ID     INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
    seats  INT         NOT NULL,
    type   VARCHAR(30) NOT NULL
    )
    ''')

conn.executemany(
    'INSERT INTO Plane(seats,type) VALUES (?,?)', [
        (6, 'SyberJet SJ30i'),
        (4, 'Cirrus SF50'),
        (4, 'Cirrus SF50'),
        (5, 'HondaJet Elite'),
        (5, 'HondaJet Elite')
    ])

conn.execute(
    '''
    CREATE TABLE Passenger(
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    emailAddress VARCHAR(100) NOT NULL PRIMARY KEY,
    phoneNumber INT
    )
    '''
)
conn.execute(
    '''
    CREATE TABLE Airport(
    name VARCHAR(100) NOT NULL,
    code VARCHAR NOT NULL PRIMARY KEY,
    timeZone VARCHAR(100) NOT NULL 
    )
    '''
)

conn.executemany(
    'INSERT INTO Airport (code, name, timezone) VALUES (?, ?, ?)',[
        ('NZNE', 'Dairy Flat', 'UTC+12'),
        ('YMHB', 'Hobart', 'UTC+10'),
        ('NZRO', 'Rotorua', 'UTC+12'),
        ('NZCI', 'Tuuta', 'UTC+12:45'),
        ('NZGB', 'Claris', 'UTC+12'),
        ('NZTL', 'Lake Tekapo', 'UTC+12'),
    ]
)
conn.execute(
    '''
    CREATE TABLE Route(
        ID VARCHAR(100) NOT NULL PRIMARY KEY,
        depatureTime VARCHAR(5) NOT NULL,
        arrivalTime VARCHAR(5) NOT NULL,
        stopOverTime VARCHAR(5) NOT NULL,
        depatureLocation VARCHAR NOT NULL,
        arrivalLocation VARCHAR NOT NULL,
        stopoverLocation VARCHAR,
        FOREIGN KEY (depatureLocation) REFERENCES Airport(code),
        FOREIGN KEY (arrivalLocation) REFERENCES Airport(code),
        FOREIGN KEY (stopoverLocation) REFERENCES Airport(code)
    )
    '''
)

conn.executemany(
    'INSERT INTO Route (ID,depatureTime,arrivalTime,stopOverTime,depatureLocation,arrivalLocation,stopoverLocation) Values(?,?,?,?,?,?,?)',[
        ('DFHO06', '0600', '0840', '40', 'NZNE', 'YMHB', 'NZRO'),
        ('HODF14', '1400', '1900', '', 'YMHB', 'NZNE', ''),
        ('DFRO06', '0600', '0645', '', 'NZNE', 'NZRO', ''),
        ('RODF12', '1200', '1245', '', 'NZRO', 'NZNE', ''),
        ('DFRO16', '1600', '1645', '', 'NZNE', 'NZRO', ''),
        ('RODF19', '1900', '1945', '', 'NZRO', 'NZNE', ''),
        ('DFGB09', '0900', '0940', '', 'NZNE', 'NZGB', ''),
        ('GBDF09', '0900', '0940', '', 'NZGB', 'NZNE', ''),
        ('DFCI10', '1030', '1300', '', 'NZNE', 'NZCI', ''),
        ('CIDF10', '1030', '1230', '', 'NZCI', 'NZNE', ''),
        ('DFLT13', '1300', '1415', '', 'NZNE', 'NZLT', ''),
        ('LTDF13', '1300', '1415', '', 'NZLT', 'NZNE', ''),
    ]
)

conn.execute(
    '''
    CREATE TABLE Flight(
    ID     INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT,
    plane  VARCHAR      NOT NULL,
    route  VARCHAR      NOT NULL,
    date   VARCHAR      NOT NULL,
    price  FLOAT        NOT NULL,
    FOREIGN KEY (plane) REFERENCES Plane(ID),
    FOREIGN KEY (route) REFERENCES Route(ID)
    )
    '''
)
conn.execute(
    '''
    CREATE TABLE Bookings(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    passenger VARCHAR(100) NOT NULL,
    flight VARCHAR(100) NOT NULL,
    FOREIGN KEY (passenger) REFERENCES Passenger(emailAddress),
    FOREIGN KEY (flight) REFERENCES Flight(ID) 

    )
    '''

)

conn.commit()
conn.close()