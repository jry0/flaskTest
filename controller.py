import sqlite3


def getDbConnection():
    conn = sqlite3.connect('testDatabase.db')
    return conn


def getResidents():
    conn = getDbConnection()
    cur = conn.cursor()
    statement = "SELECT * FROM residents"
    cur.execute(statement)
    conn.commit()
    return cur.fetchall()


def getResidentsById(id):
    conn = getDbConnection()
    cur = conn.cursor()
    statement = "SELECT * FROM residents WHERE id = ?"
    cur.execute(statement, [id])
    conn.commit()
    return cur.fetchall()

def deleteResidentsById(id):
    conn = getDbConnection()
    cur = conn.cursor()
    statement = "DELETE FROM residents WHERE id = ?"
    cur.execute(statement, [id])
    conn.commit()
    return True

def updateResidentById(id, name, age):
    conn = getDbConnection()
    cur = conn.cursor()
    statement = "UPDATE residents SET residentName = ?, age = ?, updatedAt = CURRENT_TIMESTAMP WHERE id = ?"
    cur.execute(statement, [name, age, id])
    conn.commit()
    return True

def insertResident(name, age):
    conn = getDbConnection()
    cur = conn.cursor()
    statement = "INSERT INTO residents (residentName, age) VALUES (?, ?)"
    cur.execute(statement, [name, age])
    conn.commit()
    return True