#!/usr/bin/env python3

import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Create tables with appropriate columns
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
	id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name   TEXT UNIQUE
);

CREATE TABLE Course (
	id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title  TEXT UNIQUE
);

CREATE TABLE Member (
	user_id     INTEGER,
	course_id   INTEGER,
	role        INTEGER,
	PRIMARY KEY (user_id, course_id)
)
''')

# Load JSON data
fname = input('Enter file name: ')
if len(fname) < 1:
	fname = 'roster_data.json'
	
str_data = open(fname).read()
json_data = json.loads(str_data)

# Parse JSON and insert into database
for entry in json_data:
	name = entry[0]
	title = entry[1]
	role = entry[2]
	
	# Insert or ignore if the user already exists
	cur.execute('''INSERT OR IGNORE INTO User (name) 
		VALUES ( ? )''', (name, ))
	cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
	user_id = cur.fetchone()[0]
	
	# Insert or ignore if the course already exists
	cur.execute('''INSERT OR IGNORE INTO Course (title) 
		VALUES ( ? )''', (title, ))
	cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
	course_id = cur.fetchone()[0]
	
	# Insert into Member with role
	cur.execute('''INSERT OR REPLACE INTO Member
		(user_id, course_id, role) VALUES ( ?, ?, ? )''',
		(user_id, course_id, role))
	
	# Commit the transaction
	conn.commit()
	
# Close the connection
cur.close()
