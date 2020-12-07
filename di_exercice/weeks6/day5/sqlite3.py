# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")