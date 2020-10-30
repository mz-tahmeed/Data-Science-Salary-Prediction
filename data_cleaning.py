# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:44:28 2020

@author: tahmeed
"""
import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#Salary Parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0 )

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K', '').replace('CA$', ''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#State Field
#df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.Location.value_counts()

df['same_state'] =df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#Age of company
df['age'] =df.Founded.apply(lambda x: x if x<1 else 2020 -x)
df.columns


#Persing of job description (Python, etc.)
df['Job Description'][0]

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#R Studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studion' in x.lower() or 'r-studio' in x.lower() else 0)
df.r_yn.value_counts()

#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

#AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

df.columns

#df_out = df.drop(['Unnamed: 0'], axis =1)

df.to_csv('salary_data_cleaned.csv',index = False)

pd.read_csv('salary_data_cleaned.csv')