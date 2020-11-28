# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:51:17 2020

@author: cttc
"""

import sqlite3 as sql
import io
import numpy as np


"""
Student Details Table creation
"""
con = sql.connect('attendance_sys.db')
query = """CREATE TABLE student_details(Sid TEXT PRIMARY KEY,
                                         Sname TEXT,
                                         Sclass_id TEXT,
                                         Sphone_no INTEGER,
                                         Spassword TEXT)"""
con.execute(query)
con.commit()
con.close()




"""
configuring database to store arrays

"""
def adapt_array(arr):
    """
    
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sql.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)
  
# Converts np.array to TEXT when inserting
sql.register_adapter(np.ndarray, adapt_array)

# Converts TEXT to np.array when selecting
sql.register_converter("array", convert_array)
"""
creating student_face data table
"""
con = sql.connect('attendance_sys.db',detect_types = sql.PARSE_DECLTYPES)

query = """CREATE TABLE student_face_data(Sid TEXT,
                                          arr array,
                                          FOREIGN KEY(Sid)
                                          REFERENCES student_details(Sid)
                                          ON DELETE CASCADE
                                          ON UPDATE CASCADE)"""
con.execute(query)
con.commit()
con.close()
"""Student attendance
"""
con = sql.connect('attendance_sys.db',detect_types = sql.PARSE_DECLTYPES)

query = """CREATE TABLE student_attendence(Sid TEXT,
                                          date TEXT,
                                          attendance TEXT DEFAULT'A',
                                          FOREIGN KEY(Sid)
                                          REFERENCES student_details(Sid)
                                          ON DELETE CASCADE
                                          ON UPDATE CASCADE)"""
con.execute(query)
con.commit()
con.close()