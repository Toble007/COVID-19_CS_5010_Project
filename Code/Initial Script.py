# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:03:17 2021

@author: msachs
"""

import pandas
import numpy
import os
import datetime

os.chdir('C:/Users/MSachs.MSACHS-DELL/Documents/UVA MSDS/CS 5010/Semester Project')

###read hofstede data into pandas dataframe
hof_df = pandas.read_csv('Hofstede.csv', 
            header=0,na_values=('#NULL!',''))
hof_df.country[hof_df.ctr == 'USA'] = 'United States'
hof_df.country[hof_df.ctr == 'EGY'] = 'Egypt, Arab Rep.'
hof_df.country[hof_df.ctr == 'GBR'] = 'United Kingdom'
hof_df.country[hof_df.ctr == 'IRA'] = 'Iran, Islamic Rep.'
hof_df.country[hof_df.ctr == 'BOS'] = 'Bosnia and Herzegovina'
hof_df.country[hof_df.ctr == 'CZE'] = 'Czech Republic'
hof_df.country[hof_df.ctr == 'DOM'] = 'Dominican Republic'
hof_df.country[hof_df.ctr == 'HOK'] = 'Hong Kong SAR, China'
hof_df.country[hof_df.ctr == 'KOR'] = 'Korea, Rep.'
hof_df.country[hof_df.ctr == 'KYR'] = 'Kyrgyz Republic'
hof_df.country[hof_df.ctr == 'MAC'] = 'North Macedonia'
hof_df.country[hof_df.ctr == 'RUS'] = 'Russian Federation'
hof_df.country[hof_df.ctr == 'SLK'] = 'Slovak Republic'
hof_df.country[hof_df.ctr == 'TAI'] = 'Bosnia and Herzegovina'
hof_df.country[hof_df.ctr == 'VEN'] = 'Venezuela, RB'
hof_df_comp = hof_df.dropna()
###impute data by region (consider income too)
country_df = pandas.read_csv('Country Lookup.csv', 
            header=0,na_values=('#NULL!',''))
country_df = pandas.concat([country_df.iloc[:,0:3],country_df.iloc[:,4]],axis=1)
hof_df = pandas.merge(hof_df,country_df,left_on = ['country'],right_on = ['TableName'],how = 'left')
hof_df = hof_df.dropna(subset=['Country Code'])
pdi = hof_df.groupby('Region')[['pdi']].median()
idv = hof_df.groupby('Region')[['idv']].median()
mas = hof_df.groupby('Region')[['mas']].median()
uai = hof_df.groupby('Region')[['uai']].median()
ltowvs = hof_df.groupby('Region')[['ltowvs']].median()
ivr = hof_df.groupby('Region')[['ivr']].median()
hof_df = pandas.merge(hof_df,pdi, on = 'Region', how = 'inner')
hof_df.pdi_x = hof_df.pdi_x.fillna(hof_df.pdi_y)
hof_df = pandas.merge(hof_df,idv, on = 'Region', how = 'inner')
hof_df.idv_x = hof_df.idv_x.fillna(hof_df.idv_y)
hof_df = pandas.merge(hof_df,mas, on = 'Region', how = 'inner')
hof_df.mas_x = hof_df.mas_x.fillna(hof_df.mas_y)
hof_df = pandas.merge(hof_df,uai, on = 'Region', how = 'inner')
hof_df.uai_x = hof_df.uai_x.fillna(hof_df.uai_y)
hof_df = pandas.merge(hof_df,ltowvs, on = 'Region', how = 'inner')
hof_df.ltowvs_x = hof_df.ltowvs_x.fillna(hof_df.ltowvs_y)
hof_df = pandas.merge(hof_df,ivr, on = 'Region', how = 'inner')
hof_df.ivr_x = hof_df.ivr_x.fillna(hof_df.ivr_y)
hof_df = hof_df.iloc[:,0:12]

###read vaccination data into pandas dataframe
vac_df = pandas.read_csv('country_vaccinations.csv', 
            header=0,na_values=('#NULL!',''))
vac_df = vac_df.iloc[:,0:13]
vac_df['date'] = pandas.to_datetime(vac_df['date'])
vac_df = vac_df.dropna(subset=['iso_code'])
vac_df = vac_df.sort_values(by = ['country','date'], ascending = True)
vac_df = vac_df.reset_index()
for b in range(3,11):
    for i in range(1,len(vac_df)):
        if vac_df.country[i] != vac_df.country[i-1]:
            continue
        else:
            if pandas.isnull(vac_df.iloc[i,b]) == True:
                vac_df.iloc[i,b] = vac_df.iloc[i-1,b]
            else:
                continue
            
vac_df['Daily Change']=vac_df.groupby('country')['total_vaccinations'].diff().fillna(0)
vac_df['Day Count']= vac_df.groupby('country').cumcount()+1
vac_df['Week'] = vac_df['Day Count'].astype(int) / 7
vac_df['Week'] = vac_df['Week'].apply(numpy.ceil)
###descriptive stats of daily data
vac_summ_stats = vac_df.groupby('country')['Daily Change'].describe()
vac_summ_stats['Weeks For Analysis'] = vac_summ_stats['count'].astype(int) / 7
vac_summ_stats['Weeks For Analysis'] = vac_summ_stats['Weeks For Analysis'].apply(numpy.floor)
vac_summ_stats.reset_index(inplace=True)
###aggregate data by week
new_vac_df = vac_df.groupby(['country','vaccines','Week'])[['Daily Change']].sum()
new_vac_df2 = vac_df.groupby(['country','vaccines','Week'])[['people_vaccinated','people_fully_vaccinated']].max()
new_vac_df = pandas.merge(new_vac_df,new_vac_df2, left_index=True, right_index=True, how = 'inner')
new_vac_df.reset_index(inplace=True)
new_vac_df['Rolling Total']= new_vac_df.groupby('country')['Daily Change'].cumsum()
new_vac_df['people_vaccinated'] = new_vac_df['people_vaccinated'].fillna(new_vac_df['Rolling Total'])
new_vac_df['people_fully_vaccinated'] = new_vac_df['people_fully_vaccinated'].fillna(0)
new_vac_df = new_vac_df.iloc[:,0:6]
new_vac_df.columns = ['Country','Vaccines','Vaccine Week','Weekly Vaccines Given','Total People Vaccinated','Total People Fully Vaccinated']
new_vac_df = pandas.merge(new_vac_df, vac_summ_stats[['country','Weeks For Analysis']], left_on = 'Country',right_on = 'country',how = 'inner')
new_vac_df = new_vac_df[new_vac_df['Vaccine Week'] <= new_vac_df['Weeks For Analysis']]
new_vac_df = new_vac_df.iloc[:,0:6]

###read country case data into pandas dataframe
cases_df = pandas.read_csv('owid-covid-data.csv', 
            header=0,na_values=('#NULL!','','nan'))
cases_df['date'] = pandas.to_datetime(cases_df['date'])
cases_df = cases_df[~cases_df.iso_code.str.contains(r'OWID(?!$)')]
cases_coverage = cases_df.groupby('location').describe()
cases_df = cases_df[['continent','location','date','total_cases','new_cases','total_deaths','new_deaths','icu_patients','hosp_patients','new_tests','total_tests','population','population_density','median_age',
                     'aged_65_older','cardiovasc_death_rate','diabetes_prevalence','handwashing_facilities','life_expectancy','human_development_index']]
cases_df.iloc[:,3:20] = cases_df.iloc[:,3:20].astype(float)
###descriptive stats for daily data
cases_summ_stats = cases_df.groupby('location')['new_cases'].describe()
###make sure last day of covid case data is equal to or less than the last day of vaccine data
max_vac = vac_df.groupby('country')['date','total_vaccinations'].max()
max_vac.reset_index(inplace=True)
max_vac = max_vac.iloc[:,0:2]
cases_df = pandas.merge(cases_df,max_vac,left_on = 'location',right_on = 'country', how = 'left')
cases_df = cases_df[cases_df['date_x'] <= cases_df['date_y']]
###bring in vaccine week
cases_df = pandas.merge(cases_df, vac_df.iloc[:,[1,3,16]], left_on = ['location','date_x'], right_on = ['country','date'], how = 'left')
###create case week
cases_df = cases_df.sort_values(by = ['location','date_x'])
cases_df['Day Count']= cases_df.groupby('location').cumcount()+1
cases_df['Case Week'] = cases_df['Day Count'].astype(int) / 7
cases_df['Case Week'] = cases_df['Case Week'].apply(numpy.ceil)
cases_df['Week'] = cases_df['Week'].fillna(0)
###reset "week"
reset = cases_df[cases_df["Week"]==1].groupby(["location"]).min("Case Week")
reset.reset_index(inplace=True)
reset = reset.iloc[:,[0,20]]
reset["Case Week Adjustment"] = reset["Case Week"] - 1
reset.columns = ["location","Min Case Week","Case Week Adjustment"]
###bring back into dataset
cases_df = pandas.merge(cases_df, reset, on = "location", how = "left")
cases_df["Week"][cases_df["Case Week"] >= cases_df["Min Case Week"]] = cases_df["Case Week"][cases_df["Case Week"] >= cases_df["Min Case Week"]] - cases_df["Case Week Adjustment"][cases_df["Case Week"] >= cases_df["Min Case Week"]]
###bring adjust vaccine week back into vaccine dataset
vac_df = pandas.merge(vac_df,cases_df.iloc[:,[1,2,24]], left_on = ['country','date'],right_on = ['location','date_x'], how = 'left')
vac_df["Week_x"] = vac_df["Week_y"]
vac_df = vac_df.iloc[:,0:17]
vac_df.rename(columns={'Week_x':'Week'}, inplace=True)
###recalculate vac aggregate
new_vac_df = vac_df.groupby(['country','vaccines','Week'])[['Daily Change']].sum()
new_vac_df2 = vac_df.groupby(['country','vaccines','Week'])[['people_vaccinated','people_fully_vaccinated']].max()
new_vac_df = pandas.merge(new_vac_df,new_vac_df2, left_index=True, right_index=True, how = 'inner')
new_vac_df.reset_index(inplace=True)
new_vac_df['Rolling Total']= new_vac_df.groupby('country')['Daily Change'].cumsum()
new_vac_df['people_vaccinated'] = new_vac_df['people_vaccinated'].fillna(new_vac_df['Rolling Total'])
new_vac_df['people_fully_vaccinated'] = new_vac_df['people_fully_vaccinated'].fillna(0)
new_vac_df = new_vac_df.iloc[:,0:6]
new_vac_df.columns = ['Country','Vaccines','Vaccine Week','Weekly Vaccines Given','Total People Vaccinated','Total People Fully Vaccinated']
new_vac_df = pandas.merge(new_vac_df, vac_summ_stats[['country','Weeks For Analysis']], left_on = 'Country',right_on = 'country',how = 'inner')
new_vac_df = new_vac_df[new_vac_df['Vaccine Week'] <= new_vac_df['Weeks For Analysis']]
new_vac_df = new_vac_df.iloc[:,0:6]
###aggregate data by case week
new_cases_df = cases_df.groupby(['continent','location','population','population_density','median_age',
                                 'aged_65_older','cardiovasc_death_rate','diabetes_prevalence','handwashing_facilities',
                                 'life_expectancy','human_development_index','Week','Case Week'],dropna = False)[['new_tests','new_cases','new_deaths']].sum()
new_cases_df2 = cases_df.groupby(['continent','location','population','population_density','median_age',
                                 'aged_65_older','cardiovasc_death_rate','diabetes_prevalence','handwashing_facilities',
                                 'life_expectancy','human_development_index','Week','Case Week'],dropna = False)[['total_tests','total_cases','total_deaths']].max()
new_cases_df = pandas.merge(new_cases_df,new_cases_df2, left_index=True, right_index=True, how = 'inner')
new_cases_df.reset_index(inplace=True)
new_cases_df['total_tests'] = new_cases_df['total_tests'].fillna(0)
new_cases_df['total_cases'] = new_cases_df['total_cases'].fillna(0)
new_cases_df['total_deaths'] = new_cases_df['total_deaths'].fillna(0)
###merge case data with vaccine data
new_cases_df = pandas.merge(new_cases_df,new_vac_df, left_on = ['location','Week'], right_on = ['Country','Vaccine Week'], how = 'left' )
new_cases_df = new_cases_df.drop(columns=['Week','Country'])

###read economic data into pandas dataframe
econ_df = pandas.read_csv('microeconomic.csv', 
            header=2,na_values=('#NULL!',''))
econ_df = pandas.melt(econ_df,id_vars=('Country Name','Country Code','Indicator Name','Indicator Code'))
econ_df = econ_df.rename({"variable":"Year","value":"Metric"}, axis='columns') 
econ_df = econ_df[econ_df.Year != 'Unnamed: 65']
econ_df['Year'] = econ_df['Year'].astype(int)
econ_count = econ_df.groupby(['Country Code','Indicator Code'])[['Year']].count()
econ_max = econ_df[econ_df.Metric.notnull()].groupby(['Country Code','Indicator Code'])[['Year']].max()
econ_max_numc = econ_max.groupby('Indicator Code')[['Year']].count()
econ_max_avg = econ_max.groupby('Indicator Code')[['Year']].mean()
econ_max_min = econ_max.groupby('Indicator Code')[['Year']].min()
econ_var_matrix = pandas.merge(econ_max_numc,econ_max_avg,on = 'Indicator Code',how = 'outer')
econ_var_matrix = pandas.merge(econ_var_matrix,econ_max_min,on = 'Indicator Code',how = 'outer')
econ_var_matrix = econ_var_matrix.rename({'Year_x':'Number Of Countries','Year_y':'Average Last Year','Year':'Most Out Of Date Data'}, axis = 'columns')

del([econ_max_numc,econ_max_avg,econ_max_min])

###read in econ variable explanations
expl = pandas.read_csv('Economic Variable Lookup.csv', 
            header=0,na_values=('#NULL!',''))
expl = expl.iloc[:,0:3]
###merge explanation to variable matrix
econ_var_matrix = pandas.merge(econ_var_matrix,expl,left_on = 'Indicator Code',right_on = 'INDICATOR_CODE',how = 'inner')
###create list of desired variables, from matrix
#var_list = ['NY.GDP.PCAP.CD','NY.GNP.PCAP.CD','BX.KLT.DINV.WD.GD.ZS','NV.IND.MANF.ZS']
var_list = ['NY.GDP.PCAP.CD','NV.IND.MANF.ZS','BX.KLT.DINV.CD.WD','BX.KLT.DINV.WD.GD.ZS','NY.ADJ.AEDU.GN.ZS','NV.SRV.TOTL.ZS']
###apply variable list to matrix, inner join with main df
econ_max.reset_index(inplace=True)
econ_max = econ_max[econ_max["Indicator Code"].isin(var_list)]
econ_df = pandas.merge(econ_df,econ_max,on = ['Country Code','Indicator Code','Year'], how = 'inner')

###join hofstede and economic variable datasets to consolidated case dataset
econ_df2 = econ_df.pivot_table(index=["Country Name", "Country Code"], 
                    columns='Indicator Name', 
                    values='Metric')
new_cases_df = pandas.merge(new_cases_df,econ_df2, left_on = 'location', right_on = 'Country Name', how = 'left')
new_cases_df = pandas.merge(new_cases_df,hof_df, left_on = 'location', right_on = 'country', how = 'left')
new_cases_df = new_cases_df.drop(columns = ['ctr','country','Country Code','TableName'])

###remove all case weeks where the vaccine data is not up to speed
max_case_week = new_cases_df[(new_cases_df.columns[new_cases_df.columns.isin(["location","Case Week","Vaccine Week"])])][pandas.notna(new_cases_df['Vaccine Week'])].groupby('location').max()
max_case_week = max_case_week.iloc[:,0:1]
max_case_week.reset_index(inplace=True)
max_case_week.columns  = ['location','Case Week Max']
new_cases_df = pandas.merge(new_cases_df,max_case_week, on = 'location', how = 'left')
new_cases_df = new_cases_df[new_cases_df["Case Week"] <= new_cases_df["Case Week Max"]]

###backfill daily data
cases_df["new_tests"] = cases_df["new_tests"].fillna(0)
cases_df["new_deaths"] = cases_df["new_deaths"].fillna(0)
cases_df["new_cases"] = cases_df["new_cases"].fillna(0)
cases_df['total_tests']= cases_df.groupby('location')['new_tests'].cumsum()
cases_df['total_deaths']= cases_df.groupby('location')['new_deaths'].cumsum()
cases_df['total_cases']= cases_df.groupby('location')['new_cases'].cumsum()

###write to csv
os.chdir('C:/Users/MSachs.MSACHS-DELL/Documents/UVA MSDS/CS 5010/Semester Project/Dashboard')
cases_df.to_csv('Daily COVID Case Data.csv', index=False)
vac_df.to_csv('Daily COVID Vaccine Data.csv', index=False)
new_cases_df.to_csv('Cleaned COVID Data.csv',index=False)
vac_summ_stats.to_csv('Descriptive Stats Of Vaccines.csv',index=False)
cases_summ_stats.to_csv('Descriptive Stats Of COVID Cases.csv',index=False)