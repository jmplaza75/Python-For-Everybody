import sqlite3

def process_email_file(filename):
    # Connect to the SQLite database
    with sqlite3.connect('emaildb.sqlite') as conn:
        cur = conn.cursor()

        # Drop the Counts table if it exists and create a new one
        cur.execute('DROP TABLE IF EXISTS Counts')
        cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

        # Open the file and process it line by line
        with open(filename) as fh:
            for line in fh:
                if line.startswith('From: '):
                    pieces = line.split()
                    email = pieces[1]
                    org = email.split('@')[-1]

                    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
                    row = cur.fetchone()

                    if row is None:
                        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
                    else:
                        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org,))

        # Commit the transaction once after processing the file
        conn.commit()

        # Retrieve and display the top 10 organizations by count
        sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
        print("Counts:")
        for row in cur.execute(sqlstr):
            print(f"{row[0]}: {row[1]}")

def main():
    # Get the filename from the user or use 'mbox.txt' as the default
    fname = input('Enter file name: ')
    if not fname:
        fname = 'mbox.txt'

    # Process the email file
    process_email_file(fname)

if __name__ == '__main__':
    main()
