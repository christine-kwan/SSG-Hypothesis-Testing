import sqlite3
import streamlit as st

def commit_query(con, cur):
    con.commit()
    con.close()

# for job survey
def overall_data(sea_cnt, jt_cnt):
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()
    # parent table: overall_data
    cur.execute('CREATE TABLE IF NOT EXISTS overall_data(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SUBMIT_DATE DATETIME, SEA_COUNT INT, JT_COUNT INT);')
    # insert values into overall_data
    cur.execute('INSERT INTO overall_data VALUES(null, current_timestamp, ?, ?);', (sea_cnt, jt_cnt))
    # saving row
    commit_query(con, cur)

def form_data(id, job_id, is_sea, is_jt):
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()

    # child table: form_data
    cur.execute('CREATE TABLE IF NOT EXISTS form_data(ID int, JOB_ID varchar(70), IS_SEA TINYINT, IS_JT TINYINT, FOREIGN KEY (ID) REFERENCES OVERALL_DATA(ID));')

    # insert values into form_data
    cur.execute('INSERT INTO form_data VALUES(?, ?, ?, ?);', (id, job_id, is_sea, is_jt))
    commit_query(con, cur)

def fetch_id():
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()
    fk_id = cur.execute('select id from overall_data order by id desc limit 1;')
    return fk_id.fetchall()[0][0]

# for course survey

def overall_data_course(sea_cnt, tp_cnt):
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()
    # parent table: overall_data
    cur.execute('CREATE TABLE IF NOT EXISTS overall_data_course(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SUBMIT_DATE DATETIME, SEA_COUNT INT, TP_COUNT INT);')
    # insert values into overall_data
    cur.execute('INSERT INTO overall_data_course VALUES(null, current_timestamp, ?, ?);', (sea_cnt, tp_cnt))
    # saving row
    commit_query(con, cur)

def form_data_course(id, job_id, is_sea, is_tp):
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()

    # child table: form_data
    cur.execute('CREATE TABLE IF NOT EXISTS form_data_course(ID int, JOB_ID varchar(70), IS_SEA TINYINT, IS_TP TINYINT, FOREIGN KEY (ID) REFERENCES OVERALL_DATA(ID));')

    # insert values into form_data
    cur.execute('INSERT INTO form_data_course VALUES(?, ?, ?, ?);', (id, job_id, is_sea, is_tp))
    commit_query(con, cur)

def fetch_id_course():
    con = sqlite3.connect('hypotest.db')
    cur = con.cursor()
    fk_id = cur.execute('select id from overall_data_course order by id desc limit 1;')
    return fk_id.fetchall()[0][0]