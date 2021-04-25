# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:02:00 2021

@author: msachs
"""

import pandas as pd
import numpy as np
import os
import datetime
import scipy.cluster.hierarchy as spc

os.chdir('C:/Users/MSachs.MSACHS-DELL/Documents/UVA MSDS/CS 5010/Semester Project')


###read weekly data into pandas dataframe and pull latest data point per country
cov_df = pd.read_csv('Cleaned COVID Data.csv', 
            header=0,na_values=('#NULL!',''))

cov_con_df = cov_df.loc[cov_df.groupby(['location'])['Case Week'].idxmax()]

###add additional metrics
cov_con_df["COVID_infection_rate"] = (cov_con_df["total_cases"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_positivity_rate"] =(cov_con_df["total_cases"]/cov_con_df["total_tests"]).round(2)
cov_con_df["COVID_mortality_rate"] = (cov_con_df["total_deaths"]/cov_con_df["total_cases"]).round(2)
cov_con_df['Total People Fully Vaccinated'] = cov_con_df['Total People Fully Vaccinated'].fillna(0)
cov_con_df['People Part Vac'] = cov_con_df['Total People Vaccinated'] - cov_con_df['Total People Fully Vaccinated']
cov_con_df["COVID_p_vac_rate"] = (cov_con_df["People Part Vac"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_f_vac_rate"] = (cov_con_df["Total People Fully Vaccinated"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_s_vac_rate"] = (cov_con_df["Total People Vaccinated"]/cov_con_df["population"]).round(2)

###find correlation
cor_df = cov_con_df[cov_con_df.columns[~cov_con_df.columns.isin(["continent","location","Vaccines","Region","IncomeGroup","Case Week Max"])]]
corr_p = cor_df.corr()
corr_p.reset_index(inplace = True)

cov_con_df.plot(x = 'human_development_index',y = 'COVID_s_vac_rate', kind = 'scatter',title = 'Tips By Order Value', marker = '^', color = 'orange')


os.chdir('C:/Users/msachs/Downloads')
k_df = pd.read_csv('human_dev&vaccination.csv', 
            header=0,na_values=('#NULL!',''))
m_df = pd.merge(cov_con_df,k_df,on = "location",how = "inner")
m_df = m_df.loc[m_df["COVID_s_vac_rate"] != m_df["total % population vaccinated"]]