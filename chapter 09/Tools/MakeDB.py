#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     MakeDB.py
#  ------------------------------------------------------
# Created for Learning Page
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

import sqlite3
import sys
import os


_script = sys.argv[0]
location = os.path.dirname(_script)


def startup():
    global connection, cursor, database_name
    database_name = "Company.db"
    open_database()
    make_employee()
    make_company()
    make_departments()
    fill_company()
    fill_employees()
    fill_departments()


def open_database():
    global connection, cursor
    dbpath = os.path.join(location, database_name)
    connection = sqlite3.Connection(dbpath)
    cursor = connection.cursor()


def make_employee():
    sql1 = """CREATE TABLE "Employees" (
	"EmpID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"FirstName"	TEXT,
	"MiddleName"	TEXT,
	"LastName"	TEXT,
	"Address1"	TEXT,
	"Address2"	TEXT,
	"City"	TEXT,
	"State"	TEXT,
	"PostalCode"	TEXT,
	"DateOfBirth"	TEXT,
	"PhoneNumber"	TEXT,
	"DepartmentID"	INTEGER,
    "Active"        INTEGER
)"""
    cursor.execute(sql1)


def make_company():
    sql1 = """CREATE TABLE IF NOT EXISTS "Company" (
	"CompanyID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"CompanyName"	TEXT,
	"CompanyAddress1"	TEXT,
	"CompanyAddress2"	TEXT,
	"CompanyCity"	TEXT,
	"CompanyState"	TEXT,
	"CompanyPostalCode"	TEXT,
	"CompanyPhone"	TEXT
    )"""
    cursor.execute(sql1)


def make_departments():
    sql1 = """CREATE TABLE IF NOT EXISTS "Department" (
	"DepartmentID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"DeptName"	TEXT,
	"DeptPhone"	TEXT,
	"DeptBuilding"	TEXT
    )"""
    cursor.execute(sql1)


def fill_employees():
    data = [
        [
            "Estelle",
            "Lamar",
            "Vipond",
            "1 Coach House Rd",
            "",
            "Austin",
            "Texas",
            "78745",
            "09/10/1958",
            "512-555-0291",
            6,
            1,
        ],
        [
            "Linden",
            "Patrick",
            "Chadwick",
            "6104 Old Fredricksburg Rd",
            "Unit 301",
            "Austin",
            "Texas",
            "78371",
            "04/09/2000",
            "512-555-2901",
            1,
            1,
        ],
        [
            "Delphia",
            "Elenora",
            "Murgatroyd",
            "10507 Mellow Pines",
            "",
            "Austin",
            "Texas",
            "78371",
            "06/19/1991",
            "512-555-2298",
            5,
            1,
        ],
        [
            "Bennett",
            "Joetta",
            "Ellsworth",
            "7901 Cameron Rd",
            "Unit 102",
            "Austin",
            "Texas",
            "78123",
            "02/08/1964",
            "512-555-9827",
            4,
            1,
        ],
        [
            "Karyn",
            "Cecil",
            "Franklin",
            "6023 Melrose Circle",
            "",
            "Austin",
            "Texas",
            "78201",
            "01/16/1964",
            "512-555-6438",
            4,
            1,
        ],
        [
            "Gabby",
            "Matt",
            "Chapman",
            "101 E 15th Street",
            "",
            "Austin",
            "Texas",
            "78921",
            "10/10/1996",
            "512-555-5329",
            3,
            1,
        ],
        [
            "Des",
            "Jamey",
            "Beverly",
            "521 West FM 1612",
            "Unit 602",
            "Austin",
            "Texas",
            "79748",
            "11/15/2000",
            "512-555-8291",
            2,
            1,
        ],
        [
            "Matthew",
            "Cy",
            "Bridges",
            "5201 Rose Hill Circle",
            "Unit 2018",
            "Austin",
            "Texas",
            "78367",
            "08/04/1974",
            "512-555-6233",
            3,
            1,
        ],
        [
            "Allison",
            "Gill",
            "Kirk",
            "13800 Skyline Road",
            "",
            "Austin",
            "Texas",
            "78730",
            "01/22/1981",
            "512-555-0480",
            6,
            1,
        ],
        [
            "Alvina",
            "Alexis",
            "Bailey",
            "5107 Concho Creek Drive",
            "",
            "Austin",
            "Texas",
            "78029",
            "03/23/1987",
            "512-555-1098",
            6,
            1,
        ],
    ]
    print(len(data))
    for dat in data:
        print(len(dat))
        sql1 = """INSERT INTO "Employees" (FirstName,MiddleName,LastName,Address1,Address2,City,State,PostalCode,DateOfBirth,PhoneNumber,DepartmentID,Active) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
        info = (
            dat[0],
            dat[1],
            dat[2],
            dat[3],
            dat[4],
            dat[5],
            dat[6],
            dat[7],
            dat[8],
            dat[9],
            dat[10],
            dat[11],
        )
        cursor.execute(sql1, info)
    connection.commit()


def fill_company():
    sql = """INSERT INTO 'Company' (CompanyName,CompanyAddress1,CompanyAddress2,CompanyCity,CompanyState,CompanyPostalCode,CompanyPhone) VALUES ('Farkel and Associates','123 Main Street','','Austin','Texas','78491','515-555-2222')"""
    cursor.execute(sql)
    connection.commit()


def fill_departments():
    deptinfo = [
        ["Human Resources", "512-555-2229", "1"],
        ["Research And Development", "512-555-2228", "1"],
        ["Shipping and Receiving", "512-555-2227", "1"],
        ["Production", "512-555-2226", "1"],
        ["Stock", "512-555-2225", "1"],
        ["Management", "512-555-2224", "1"],
    ]
    sql = """INSERT INTO 'Department' (DeptName,DeptPhone,DeptBuilding) VALUES (?,?,?)
    """
    for dept in deptinfo:
        datavalues = (dept[0], dept[1], dept[2])
        cursor.execute(sql, datavalues)
    # cursor.execute(sql)
    connection.commit()


if __name__ == "__main__":
    startup()
