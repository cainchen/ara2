#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="ara", user="ara", password="ara", host="192.168.43.17", port="5432")

print ("Opened database successfully")
