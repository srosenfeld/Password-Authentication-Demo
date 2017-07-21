import pyautogui
import sqlite3

conn = sqlite3.connect('pg_example.db')


#Reset username and password
currentuser = ''
pw = ''

#Use the pyautogui prompt and password to store those as variables
user = pyautogui.prompt(text='Enter your username here', title='Username', default='')
pw = pyautogui.password(text='Enter your password below', title='Password', default='', mask='*')

#Execute SQL statement to search DB for user + pw match

#If there is a match, set currentuser to user

