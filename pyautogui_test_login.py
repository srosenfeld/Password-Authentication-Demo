import pyautogui
import sqlite3

conn = sqlite3.connect('pg_example.db', timeout=10)
c = conn.cursor()

#Reset username and password
user=''
currentuser = ''
pw = ''

#Use the pyautogui prompt and password to store those as variables
user = pyautogui.prompt(text='Enter your username here', title='Username', default='')
pw = pyautogui.password(text='Enter your password below', title='Password', default='', mask='*')

#Execute SQL statement to search DB for user + pw match
t = (user, pw)
c.execute('SELECT * FROM pg_table1 WHERE user = ? AND pw = ?', t)
print(c.fetchone())
conn.close()

#If there is a match, set currentuser to user
currentuser = user

#At termination of program, reset username, currentuser, and password
user=''
currentuser=''
pw = ''
conn.close()
