import streamlit as st
import pandas as pd
import random
import re
from create_db import *

form = st.form('experiment', clear_on_submit=False)

filename = r'first500.csv'
num_qns = 5  # number of questions in survey

# file in the format of jobid, sea_skills, jt_skills
data = pd.read_csv(filename)
desc = data.jobId
jt = data.jt_skills
sea = data.sea_skills

def format_skills(txt):
    '''
    Converts string of text into a sorted list in title case.
    '''
    txt = txt.title()
    txt = txt.strip('[]')
    txt = re.sub("['']", '', txt)
    txt = txt.split(',')
    txt = [i.strip(' ') for i in txt]
    return sorted(txt)

def append_results(jt, sea):
    '''
    Appends 1 or 0 into is_sea and is_jt list to represent whether user picked sea or jt for question.
    '''
    is_jt.append(jt)
    is_sea.append(sea)

with form:
    st.write('## Jobs questionnaire')
    st.caption(' ### Instructions: There will be a total of 5 randomly generated questions. Please select the option which you feel better describes the skills mentioned in the description. For instance, if a skill appears in the option but does not accurately reflect the job description, it may not be a good match. ')

    # variables to store current form data
    job_qn_asked = list()
    is_sea = list()
    is_jt = list()

    for i in range(num_qns):
        qn_index = random.randrange(0, len(desc)+1)
        
        if qn_index not in job_qn_asked:

            job_qn_asked.append(desc[qn_index]) # stores the qn picked
            sea_skills = format_skills(sea[qn_index])
            jt_skills = format_skills(jt[qn_index])
            choice = random.randrange(1,3) # shuffles order of sea and jt options
            
            st.write("Job ID: " + desc[qn_index])

            if choice == 1:
                df1 = pd.DataFrame(sea_skills, columns=['A'])
                df2 = pd.DataFrame(jt_skills, columns=['B'])
                st.table(pd.concat([df1, df2], axis=1).fillna('-'))
                radio = st.radio(f'Question {i+1}', ('A', 'B'))
                if radio == 'A':
                    append_results(0, 1)
                else:
                    append_results(1, 0)

            else:
                df1 = pd.DataFrame(jt_skills, columns=['A'])
                df2 = pd.DataFrame(sea_skills, columns=['B'])
                st.table(pd.concat([df1, df2], axis=1).fillna('-'))
                radio = st.radio(f'Question {i+1}', ('A', 'B'))
                if radio == 'A':
                    append_results(1, 0)
                else:
                    append_results(0, 1)


submit = form.form_submit_button()
if submit == True:
    overall_data(sum(is_sea), sum(is_jt))
    for result in range(5):
        form_data(fetch_id(), job_qn_asked[result], is_sea[result], is_jt[result])
    st.balloons()
    st.success('Successfully submitted!')
    st.stop()


# bold words that are similar for both skills?
# insert the actual jd