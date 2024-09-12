import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')

# Expected format:
#   Track Title, Artist Name, Album Title, Genre Name, Length, Rating, Count

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7: continue

    track_title = pieces[0]
    artist_name = pieces[1]
    album_title = pieces[2]
    genre_name = pieces[3]
    length = pieces[4]
    rating = pieces[5]
    count = pieces[6]

    print(track_title, artist_name, album_title, genre_name, length, rating, count)

    # Insert or ignore artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist_name, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name, ))
    artist_id = cur.fetchone()[0]

    # Insert or ignore album
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album_title, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album_title, ))
    album_id = cur.fetchone()[0]

    # Insert or ignore genre
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre_name, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre_name, ))
    genre_id = cur.fetchone()[0]

    # Insert or replace track
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( track_title, album_id, genre_id, length, rating, count ) )

    conn.commit()

handle.close()
