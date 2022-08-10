import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('hypotest.db')
cur = conn.cursor()

st.write('Table: overall_data')
overall_data = cur.execute('select * from overall_data;')
df = pd.DataFrame(overall_data.fetchall(), columns=['ID', 'Submission datetime', 'SEA count', 'JobTech count'])
st.dataframe(df)

st.write('Table: form_data')
form_data = cur.execute('select * from form_data;')
df = pd.DataFrame(form_data.fetchall(), columns=['ID', 'Job ID', 'is sea', 'is jt'])
st.dataframe(df)

st.write('Table: overall_data_course')
overall_data_course = cur.execute('select * from overall_data_course;')
df = pd.DataFrame(overall_data_course.fetchall(), columns=['ID', 'Submission datetime', 'SEA count', 'Thirdparty count'])
st.dataframe(df)

st.write('Table: form_data_course')
form_data_course = cur.execute('select * from form_data_course;')
df = pd.DataFrame(form_data_course.fetchall(), columns=['ID', 'Job ID', 'is sea', 'is tp'])
st.dataframe(df)