# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:26:44 2021

@author: Thomas Butler, vra2cf
"""

'''
As covid cases increase and vaccinations increase, how does this effect covid case growth?
As covid cases increase and testing increases or decreases, how does this effect covid case growth?

change in covid cases week by week, "new_cases" y
change in testing week by week, "new_tests"
change in vaccination week by week, "Weekly Vaccines Given"
as change in vaccinations increase is there a decrease in change in covid case growth?
as change in testing increases/decreases is there a decrease/increase in change in covid case growth?
want to see a negative b1 on both regressions.
check to see if covid vaccines are effected x weeks down the line by viewing covid cases
'''
#%% packages
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import scipy.stats as stats
import unittest
import math
#%% data load in and test v cases regression
df = pd.read_csv("Cleaned COVID Data.csv")

#df["location"].unique()
'''
['Algeria', 'Egypt', 'Mauritius', 'Morocco', 'Rwanda', 'Senegal',
       'Seychelles', 'South Africa', 'Zimbabwe', 'Azerbaijan', 'Bahrain',
       'Bangladesh', 'Cambodia', 'China', 'Hong Kong', 'India',
       'Indonesia', 'Iran', 'Israel', 'Japan', 'Jordan', 'Kazakhstan',
       'Kuwait', 'Lebanon', 'Macao', 'Malaysia', 'Maldives', 'Myanmar',
       'Nepal', 'Oman', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Singapore',
       'South Korea', 'Sri Lanka', 'Turkey', 'United Arab Emirates',
       'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bulgaria',
       'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia',
       'Faeroe Islands', 'Finland', 'France', 'Germany', 'Gibraltar',
       'Greece', 'Guernsey', 'Hungary', 'Iceland', 'Ireland',
       'Isle of Man', 'Italy', 'Jersey', 'Latvia', 'Liechtenstein',
       'Lithuania', 'Luxembourg', 'Malta', 'Monaco', 'Montenegro',
       'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia',
       'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
       'Switzerland', 'Ukraine', 'United Kingdom', 'Anguilla', 'Barbados',
       'Bermuda', 'Canada', 'Cayman Islands', 'Costa Rica', 'Dominica',
       'Dominican Republic', 'El Salvador', 'Greenland', 'Mexico',
       'Montserrat', 'Panama', 'Saint Lucia', 'Trinidad and Tobago',
       'Turks and Caicos Islands', 'United States', 'Australia',
       'New Zealand', 'Argentina', 'Bolivia', 'Brazil', 'Chile',
       'Colombia', 'Ecuador', 'Falkland Islands', 'Guyana', 'Paraguay',
       'Peru', 'Uruguay', 'Venezuela']
'''
#df.isna().sum()
'''
continent                                                       0
location                                                        0
population                                                      0
population_density                                             17
median_age                                                    310
aged_65_older                                                 310
cardiovasc_death_rate                                         212
diabetes_prevalence                                            41
handwashing_facilities                                       3871
life_expectancy                                                10
human_development_index                                       160
Case Week                                                       0
new_tests                                                       0
new_cases                                                       0
new_deaths                                                      0
total_tests                                                     0
total_cases                                                     0
total_deaths                                                    0
Vaccines                                                     4745
Vaccine Week                                                 4745
Weekly Vaccines Given                                        4745
Total People Vaccinated                                      4745
Total People Fully Vaccinated                                4745
Adjusted savings: education expenditure (% of GNI)            587
Foreign direct investment, net inflows (% of GDP)             620
Foreign direct investment, net inflows (BoP, current US$)     612
GDP per capita (current US$)                                  461
Manufacturing, value added (% of GDP)                         608
Services, value added (% of GDP)                              565
pdi_x                                                        1827
idv_x                                                        1827
mas_x                                                        1827
uai_x                                                        1827
ltowvs_x                                                     1673
ivr_x                                                        1673
Region                                                       1673
IncomeGroup                                                  1673
Case Week Max                                                   0
'''

#df["Count"] = 1
#df[["Vaccine Week","Count"]].groupby(by=["Vaccine Week"]).sum()
'''
              Count
Vaccine Week       
1.0             115
2.0             102
3.0              84
4.0              75
5.0              70
6.0              62
7.0              56
8.0              46
9.0              36
10.0             21
11.0              5
12.0              2
'''
#remove any cases with < 0
df["not 0 case"] = True
for num in range(len(df)):
    if df["new_cases"][num] < 0:
        df.loc[num,'not 0 case'] = False
df = df[df["not 0 case"]]
df = df.reset_index(drop=True)

sns.regplot(x="new_cases",y="new_tests", data= df)
plt.title("New Tests vs New Cases")
plt.savefig('New Tests vs New Cases.png')
plt.show()
plt.close('all')

#remove any data point that has 0 new cases.
case = df.copy()
case["not 0 case"] = True
for num in range(len(case)):
    if case["new_cases"][num] == 0:
        case.loc[num,'not 0 case'] = False
case = case[case["not 0 case"]]
case = case.reset_index(drop=True)

#remove any data point that has <=0 new tests.
case["not 0 test"] = True
for num in range(len(case)):
    if case["new_tests"][num] <= 0:
        case.loc[num,'not 0 test'] = False
case = case[case["not 0 test"]]
case = case.reset_index(drop=True)

#transform new cases
case["new_cases_transformed"] = case["new_cases"].apply(lambda x: math.log(x))
#case["new_cases_transformed"] = stats.boxcox(case["new_cases"])[0]

sns.regplot(x="new_cases_transformed",y="new_tests", data= case)
plt.title("New Tests vs New Cases Transformed")
plt.savefig('New Tests vs New Cases Transformed.png')
plt.show()
plt.close('all')

#transform new_tests
case["new_tests_transformed"] = case["new_tests"].apply(lambda x: math.log(x))
#case["new_tests_transformed"] = stats.boxcox(case["new_tests"])[0]

sns.regplot(x="new_cases_transformed",y="new_tests_transformed", data= case)
plt.title("New Tests Transformed vs New Cases Transformed")
plt.savefig('New Tests Transformed vs New Cases Transformed.png')
plt.show()
plt.close('all')
test = case[['new_cases_transformed','new_tests_transformed']]
x = test['new_cases_transformed']
x = sm.add_constant(x)
y = test['new_tests_transformed']
reduced = sm.OLS(y,x).fit()
#print(reduced.summary())
"""
                              OLS Regression Results                             
=================================================================================
Dep. Variable:     new_tests_transformed   R-squared:                       0.607
Model:                               OLS   Adj. R-squared:                  0.607
Method:                    Least Squares   F-statistic:                     5681.
Date:                   Mon, 19 Apr 2021   Prob (F-statistic):               0.00
Time:                           18:23:21   Log-Likelihood:                -5991.8
No. Observations:                   3682   AIC:                         1.199e+04
Df Residuals:                       3680   BIC:                         1.200e+04
Df Model:                              1                                         
Covariance Type:               nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                     6.2261      0.064     96.792      0.000       6.100       6.352
new_cases_transformed     0.5970      0.008     75.371      0.000       0.581       0.613
==============================================================================
Omnibus:                        3.143   Durbin-Watson:                   0.226
Prob(Omnibus):                  0.208   Jarque-Bera (JB):                3.147
Skew:                          -0.047   Prob(JB):                        0.207
Kurtosis:                       3.107   Cond. No.                         26.1
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
#residual plot
r_student = reduced.outlier_test()["student_resid"]
sns.regplot(x=r_student,y=reduced.fittedvalues)
plt.title("Residual Plot New Tests Transformed vs New Cases Transformed")
plt.savefig('Residual Plot New Tests Transformed vs New Cases Transformed.png')
plt.show()
plt.close('all')

#qq plot
fig, ax = plt.subplots()
_, (__, ___, r) = stats.probplot(reduced.resid, plot=ax, fit=True)
plt.title("QQ Plot New Tests Transformed vs New Cases Transformed")
plt.savefig('QQ Plot New Tests Transformed vs New Cases Transformed.png')
plt.show()
plt.close('all')

#autocorrelation plot
x = pd.plotting.autocorrelation_plot(case["new_cases_transformed"])
plt.title("Autocorrelation Plot New Cases Transformed")
# ploting the Curve
x.plot()
plt.savefig('Autocorrelation Plot New Cases Transformed.png')
# Display
plt.show()
plt.close('all')
#https://www.geeksforgeeks.org/python-pandas-plotting-the-autocorrelation-plot/

#ok have a increasing variance and a non-zero mean. I don't know how to fix both of these. 
#I would guess I am missing predictors but I am not sure which those are.

#%% Vaccine v cases regression
#print(len(df))
#5410
df = df[-df['Vaccine Week'].isna()]
df = df.reset_index(drop=True)
#print(len(df))
#674

#df.isna().sum()
'''
continent                                                      0
location                                                       0
population                                                     0
population_density                                            17
median_age                                                    74
aged_65_older                                                 74
cardiovasc_death_rate                                         59
diabetes_prevalence                                           41
handwashing_facilities                                       561
life_expectancy                                               10
human_development_index                                       65
Case Week                                                      0
new_tests                                                      0
new_cases                                                      0
new_deaths                                                     0
total_tests                                                    0
total_cases                                                    0
total_deaths                                                   0
Vaccines                                                       0
Vaccine Week                                                   0
Weekly Vaccines Given                                          0
Total People Vaccinated                                        0
Total People Fully Vaccinated                                  0
Adjusted savings: education expenditure (% of GNI)            98
Foreign direct investment, net inflows (% of GDP)             85
Foreign direct investment, net inflows (BoP, current US$)     77
GDP per capita (current US$)                                  68
Manufacturing, value added (% of GDP)                         83
Services, value added (% of GDP)                              73
pdi_x                                                        202
idv_x                                                        202
mas_x                                                        202
uai_x                                                        202
ltowvs_x                                                     196
ivr_x                                                        196
Region                                                       196
IncomeGroup                                                  196
Case Week Max                                                  0
'''
sns.regplot(y="Weekly Vaccines Given",x="new_cases", data= df)
plt.title("Weekly Vaccines Given vs New Cases")
plt.savefig('Weekly Vaccines Given vs New Cases.png')
plt.show()
plt.close('all')

test = df[['new_cases','Weekly Vaccines Given']]
x = test['new_cases']
x = sm.add_constant(x)
y = test['Weekly Vaccines Given']
reduced = sm.OLS(y,x).fit()
#print(reduced.summary())
'''
                              OLS Regression Results                             
=================================================================================
Dep. Variable:     Weekly Vaccines Given   R-squared:                       0.228
Model:                               OLS   Adj. R-squared:                  0.227
Method:                    Least Squares   F-statistic:                     199.0
Date:                   Mon, 19 Apr 2021   Prob (F-statistic):           9.03e-40
Time:                           18:27:57   Log-Likelihood:                -10389.
No. Observations:                    674   AIC:                         2.078e+04
Df Residuals:                        672   BIC:                         2.079e+04
Df Model:                              1                                         
Covariance Type:               nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        1.72e+05   4.82e+04      3.569      0.000    7.74e+04    2.67e+05
new_cases      4.1931      0.297     14.107      0.000       3.610       4.777
==============================================================================
Omnibus:                      923.559   Durbin-Watson:                   0.719
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           180801.196
Skew:                           7.203   Prob(JB):                         0.00
Kurtosis:                      81.933   Cond. No.                     1.69e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.69e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
'''
#residual plot
r_student = reduced.outlier_test()["student_resid"]
sns.regplot(x=r_student,y=reduced.fittedvalues)
plt.title("Residual Plot Weekly Vaccines vs New Cases")
plt.savefig('Residual Plot Weekly Vaccines vs New Cases.png')
plt.show()
plt.close('all')

#qq plot
fig, ax = plt.subplots()
_, (__, ___, r) = stats.probplot(reduced.resid, plot=ax, fit=True)
plt.title("QQ Plot Weekly Vaccines vs New Cases")
plt.savefig('QQ Plot Weekly Vaccines vs New Cases.png')
plt.show()
plt.close('all')

#autocorrelation plot
x = pd.plotting.autocorrelation_plot(df["new_cases"])
plt.title("Autocorrelation Plot New Cases")
# ploting the Curve
x.plot()
plt.savefig('Autocorrelation Plot New Cases.png')
# Display
plt.show()
plt.close('all')

#remove any country that doesn't have covid cases but are vaccinating anyways.
df["not 0 cases"] = True
count = 0
for num in range(len(df)):
    if num == len(df)-1:
        if df["total_cases"][num] == 0:
            for x in range(count+1):
                df.loc[num-x-1,'not 0 cases'] = False
    elif df['location'][num+1] == df['location'][num]:
        count += 1
    else:
        if df["total_cases"][num] == 0:
            for x in range(count+1):
                df.loc[num-x,'not 0 cases'] = False
        count = 0

df = df[df["not 0 cases"]]
df = df.reset_index(drop=True)

#print(len(df))
#1042

#remove all datapoints that have either 0 new cases and/or 0 Weekly Vaccines Given
df["not 0 new cases or Weekly Vaccines Given"] = True
for num in range(len(df)):
    if df["new_cases"][num] <= 0:
        df.loc[num,'not 0 new cases or Weekly Vaccines Given'] = False
    elif df["Weekly Vaccines Given"][num] <= 0:
        df.loc[num,'not 0 new cases or Weekly Vaccines Given'] = False
df = df[df["not 0 new cases or Weekly Vaccines Given"]]
df = df.reset_index(drop=True)

#print(len(df))
#849

#checking which countries have at least 3 weeks of vaccine data
df['At least 3 weeks of vaccine data'] = False
for num in range(len(df)):
    if num == 0:
        count = 0
        vac_count = 0
    elif df['location'][num] == df['location'][num-1]:
        count += 1
        if df["Weekly Vaccines Given"][num] != 0:
            vac_count += 1
    else:
        if vac_count >= 3:
            for x in range(count+1):
                df.loc[num-x-1,'At least 3 weeks of vaccine data'] = True
        count = 0
        vac_count = 0

#removing any country that doesn't have 3 weeks of vaccine data.
df = df[df["At least 3 weeks of vaccine data"]]
df = df.reset_index(drop=True)

df = df.rename(columns={"Weekly Vaccines Given": "Weekly_Vaccines_Given"})

#print(len(df))
#778

#regraph to see if anything else should be changed.
sns.regplot(y="Weekly_Vaccines_Given",x="new_cases", data= df)
plt.title("Weekly Vaccines Given vs New Cases data clean")
plt.savefig('Weekly Vaccines Given vs New Cases data clean.png')
plt.show()
plt.close('all')

#zoom in a bit
ax = sns.regplot(y="Weekly_Vaccines_Given",x="new_cases", data= df)
plt.title("Weekly Vaccines Given vs New Cases data clean zoomed in")
ax.set(ylim=(0, 500000), xlim=(0, 50000))
plt.savefig('Weekly Vaccines Given vs New Cases data clean zoomed in.png')
plt.show(ax)
plt.close('all')
#so either I need a transformation and/or influential point removal from this.
#lets try transforming
df["new_cases_transformed"] = df["new_cases"].apply(lambda x: math.log(x))
'''
box = stats.boxcox(df["new_cases"])[0]
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.boxcox.html
df['new_cases_transformed']=pd.Series(box)
#https://stackoverflow.com/questions/44424594/converting-numpy-array-into-dataframe-column
'''

sns.regplot(y="Weekly_Vaccines_Given",x="new_cases_transformed", data= df)
plt.title("Weekly Vaccines Given vs New Cases Transformed data clean")
plt.savefig('Weekly Vaccines Given vs New Cases Transformed data clean.png')
plt.show()
plt.close('all')

df["Weekly_Vaccines_Given_transformed"] = df["Weekly_Vaccines_Given"].apply(lambda x: math.log(x))
'''
box = stats.boxcox(df["Weekly_Vaccines_Given"])[0]
df['Weekly_Vaccines_Given_transformed']=pd.Series(box)
'''

sns.regplot(y="Weekly_Vaccines_Given_transformed",x="new_cases_transformed", data= df)
plt.title("Weekly Vaccines Given Transformed vs New Cases Transformed data clean")
plt.savefig('Weekly Vaccines Given Transformed vs New Cases Transformed data clean.png')
plt.show()
plt.close('all')

#fit a model
test = df[['new_cases_transformed','Weekly_Vaccines_Given_transformed']]
x = test['new_cases_transformed']
x = sm.add_constant(x)
y = test['Weekly_Vaccines_Given_transformed']
reduced = sm.OLS(y,x).fit()
#print(reduced.summary())
'''
                                    OLS Regression Results                                   
=============================================================================================
Dep. Variable:     Weekly_Vaccines_Given_transformed   R-squared:                       0.326
Model:                                           OLS   Adj. R-squared:                  0.325
Method:                                Least Squares   F-statistic:                     221.7
Date:                               Mon, 19 Apr 2021   Prob (F-statistic):           3.56e-41
Time:                                       18:15:19   Log-Likelihood:                -935.98
No. Observations:                                460   AIC:                             1876.
Df Residuals:                                    458   BIC:                             1884.
Df Model:                                          1                                         
Covariance Type:                           nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                     5.1999      0.406     12.798      0.000       4.401       5.998
new_cases_transformed     0.6312      0.042     14.889      0.000       0.548       0.715
==============================================================================
Omnibus:                       63.340   Durbin-Watson:                   0.805
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              308.655
Skew:                          -0.467   Prob(JB):                     9.47e-68
Kurtosis:                       6.903   Cond. No.                         45.5
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
#residual plot
r_student = reduced.outlier_test()["student_resid"]
sns.regplot(x=r_student,y=reduced.fittedvalues)
plt.title("Residual Plot Weekly Vaccines Transformed vs New Cases Transformed data clean")
plt.savefig('Residual Plot Weekly Vaccines Transformed vs New Cases Transformed data clean.png')
plt.show()
plt.close('all')

#qq plot
fig, ax = plt.subplots()
_, (__, ___, r) = stats.probplot(reduced.resid, plot=ax, fit=True)
plt.title("QQ Plot Weekly Vaccines Transformed vs New Cases Transformed data clean")
plt.savefig('QQ Plot Weekly Vaccines Transformed vs New Cases Transformed data clean.png')
plt.show()
plt.close('all')

#autocorrelation plot
x = pd.plotting.autocorrelation_plot(df["new_cases_transformed"])
plt.title("Autocorrelation Plot New Cases Transformed data clean")
# ploting the Curve
x.plot()
plt.savefig('Autocorrelation Plot New Cases Transformed data clean.png')
# Display
plt.show()
plt.close('all')

#ok looks like the log transformations solved the problem, but created a problem with a non-zero mean this might be fixed by putting in more regressors. 
#It also still looks like i have 1 to a few influential points lets look at that after we have the full model.

#check to see if covid vaccines are effected x weeks down the line by viewing covid cases
df["Week_1"] = 0
df["Week_2"] = 0
df["Week_3"] = 0
df["Week_4"] = 0
df["Week_5"] = 0
df["Week_6"] = 0
df["Week_7"] = 0
df["Week_8"] = 0
df["Week_9"] = 0

for num in range(len(df)):
    count = 0
    if df["new_cases_transformed"][num] != 0:
        while df["location"][num] == df["location"][num+count]:
            count +=1
            if num + count == len(df):
                break
    if count != 0:
        count -=1
        if count >= 1:
            df.loc[num+1,"Week_1"] = df.loc[num,"new_cases_transformed"]
        if count >= 2:
            df.loc[num+2,"Week_2"] = df.loc[num,"new_cases_transformed"]
        if count >= 3:
            df.loc[num+3,"Week_3"] = df.loc[num,"new_cases_transformed"]
        if count >= 4:
            df.loc[num+4,"Week_4"] = df.loc[num,"new_cases_transformed"]
        if count >= 5:
            df.loc[num+5,"Week_5"] = df.loc[num,"new_cases_transformed"]
        if count >= 6:
            df.loc[num+6,"Week_6"] = df.loc[num,"new_cases_transformed"]
        if count >= 7:
            df.loc[num+7,"Week_7"] = df.loc[num,"new_cases_transformed"]
        if count >= 8:
            df.loc[num+8,"Week_8"] = df.loc[num,"new_cases_transformed"]
        if count >= 9:
            df.loc[num+9,"Week_9"] = df.loc[num,"new_cases_transformed"]


test = df[['new_cases_transformed','Weekly_Vaccines_Given_transformed',"Week_1","Week_2","Week_3","Week_4","Week_5","Week_6","Week_7","Week_8","Week_9"]]
x = test[test.columns[~test.columns.isin(["Weekly_Vaccines_Given_transformed"])]]
x = sm.add_constant(x)
y = test['Weekly_Vaccines_Given_transformed']
result = sm.OLS(y,x).fit()
#print(result.summary())
'''
                                    OLS Regression Results                                   
=============================================================================================
Dep. Variable:     Weekly_Vaccines_Given_transformed   R-squared:                       0.477
Model:                                           OLS   Adj. R-squared:                  0.465
Method:                                Least Squares   F-statistic:                     40.87
Date:                               Mon, 19 Apr 2021   Prob (F-statistic):           4.57e-57
Time:                                       18:38:22   Log-Likelihood:                -877.91
No. Observations:                                460   AIC:                             1778.
Df Residuals:                                    449   BIC:                             1823.
Df Model:                                         10                                         
Covariance Type:                           nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                     5.3965      0.363     14.864      0.000       4.683       6.110
new_cases_transformed     0.4208      0.043      9.681      0.000       0.335       0.506
Week_1                    0.1237      0.031      3.931      0.000       0.062       0.185
Week_2                    0.0403      0.031      1.280      0.201      -0.022       0.102
Week_3                    0.0494      0.032      1.562      0.119      -0.013       0.112
Week_4                    0.0159      0.032      0.489      0.625      -0.048       0.080
Week_5                    0.0173      0.034      0.503      0.615      -0.050       0.085
Week_6                    0.0055      0.036      0.152      0.879      -0.065       0.076
Week_7                    0.0036      0.039      0.094      0.925      -0.072       0.079
Week_8                    0.0383      0.045      0.849      0.396      -0.050       0.127
Week_9                    0.0277      0.049      0.564      0.573      -0.069       0.124
==============================================================================
Omnibus:                       66.303   Durbin-Watson:                   0.552
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              675.834
Skew:                           0.004   Prob(JB):                    1.76e-147
Kurtosis:                       8.938   Cond. No.                         88.2
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''

#anova to compare models
anovaResults = anova_lm(reduced, result)
#https://stackoverflow.com/questions/45243802/how-do-i-do-an-f-test-to-compare-nested-linear-models-in-python
#print(anovaResults)
'''
   df_resid          ssr  df_diff     ss_diff          F        Pr(>F)
0     458.0  1576.290273      0.0         NaN        NaN           NaN
1     449.0  1224.594770      9.0  351.695503  14.327758  2.029158e-20
'''
#We can see that according to the ANOVA output at least 1 of the weekly terms are significant.

test = df[['new_cases_transformed','Weekly_Vaccines_Given_transformed',"Week_1","Week_3","Week_6"]]
x = test[test.columns[~test.columns.isin(["Weekly_Vaccines_Given_transformed"])]]
x = sm.add_constant(x)
y = test['Weekly_Vaccines_Given_transformed']
reduced = sm.OLS(y,x).fit()
#print(reduced.summary())

'''
                                    OLS Regression Results                                   
=============================================================================================
Dep. Variable:     Weekly_Vaccines_Given_transformed   R-squared:                       0.466
Model:                                           OLS   Adj. R-squared:                  0.463
Method:                                Least Squares   F-statistic:                     168.6
Date:                               Sat, 08 May 2021   Prob (F-statistic):          9.72e-104
Time:                                       17:44:25   Log-Likelihood:                -1479.2
No. Observations:                                778   AIC:                             2968.
Df Residuals:                                    773   BIC:                             2992.
Df Model:                                          4                                         
Covariance Type:                           nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                     6.2495      0.258     24.233      0.000       5.743       6.756
new_cases_transformed     0.3326      0.034      9.867      0.000       0.266       0.399
Week_1                    0.1411      0.024      5.923      0.000       0.094       0.188
Week_3                    0.0884      0.018      4.928      0.000       0.053       0.124
Week_6                    0.0696      0.015      4.645      0.000       0.040       0.099
==============================================================================
Omnibus:                       82.798   Durbin-Watson:                   0.528
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              564.271
Skew:                           0.135   Prob(JB):                    2.95e-123
Kurtosis:                       7.163   Cond. No.                         67.7
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''

anovaResults = anova_lm(reduced, result)
#print(anovaResults)
'''
   df_resid          ssr  df_diff    ss_diff         F    Pr(>F)
0     773.0  2041.214830      0.0        NaN       NaN       NaN
1     767.0  2008.598419      6.0  32.616412  2.075808  0.053873
'''
#keep reduced model.

test = df[['new_cases_transformed','Weekly_Vaccines_Given_transformed',"Week_1","Week_3","Week_6"]]
result = smf.ols(formula="Weekly_Vaccines_Given_transformed~new_cases_transformed*Week_1+new_cases_transformed*Week_3+new_cases_transformed*Week_6",data=test).fit()
#print(result.summary())
'''
                                    OLS Regression Results                                   
=============================================================================================
Dep. Variable:     Weekly_Vaccines_Given_transformed   R-squared:                       0.485
Model:                                           OLS   Adj. R-squared:                  0.480
Method:                                Least Squares   F-statistic:                     103.4
Date:                               Sat, 08 May 2021   Prob (F-statistic):          2.18e-106
Time:                                       17:44:25   Log-Likelihood:                -1465.3
No. Observations:                                778   AIC:                             2947.
Df Residuals:                                    770   BIC:                             2984.
Df Model:                                          7                                         
Covariance Type:                           nonrobust                                         
================================================================================================
                                   coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------
Intercept                        8.2690      0.468     17.686      0.000       7.351       9.187
new_cases_transformed            0.1162      0.054      2.168      0.030       0.011       0.221
Week_1                          -0.2065      0.095     -2.184      0.029      -0.392      -0.021
new_cases_transformed:Week_1     0.0355      0.009      3.795      0.000       0.017       0.054
Week_3                           0.1279      0.094      1.365      0.173      -0.056       0.312
new_cases_transformed:Week_3    -0.0040      0.009     -0.429      0.668      -0.022       0.014
Week_6                           0.0012      0.085      0.014      0.989      -0.165       0.168
new_cases_transformed:Week_6     0.0068      0.008      0.810      0.418      -0.010       0.023
==============================================================================
Omnibus:                       90.869   Durbin-Watson:                   0.579
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              650.971
Skew:                           0.211   Prob(JB):                    4.40e-142
Kurtosis:                       7.461   Cond. No.                     1.05e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.05e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
'''
anovaResults = anova_lm(reduced, result)
#print(anovaResults)
'''
   df_resid          ssr  df_diff    ss_diff         F    Pr(>F)
0     773.0  2041.214830      0.0        NaN       NaN       NaN
1     770.0  1969.697671      3.0  71.517159  9.319233  0.000005
'''
#At least 1 of the weekly interactive terms are significant.

test = df[['new_cases_transformed','Weekly_Vaccines_Given_transformed',"Week_1","Week_3","Week_6"]]
reduced = smf.ols(formula="Weekly_Vaccines_Given_transformed~new_cases_transformed*Week_1+Week_3+Week_6",data=test).fit()
#print(reduced.summary())
'''
                                    OLS Regression Results                                   
=============================================================================================
Dep. Variable:     Weekly_Vaccines_Given_transformed   R-squared:                       0.484
Model:                                           OLS   Adj. R-squared:                  0.481
Method:                                Least Squares   F-statistic:                     144.9
Date:                               Sat, 08 May 2021   Prob (F-statistic):          2.08e-108
Time:                                       17:44:25   Log-Likelihood:                -1465.6
No. Observations:                                778   AIC:                             2943.
Df Residuals:                                    772   BIC:                             2971.
Df Model:                                          5                                         
Covariance Type:                           nonrobust                                         
================================================================================================
                                   coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------
Intercept                        8.2904      0.465     17.812      0.000       7.377       9.204
new_cases_transformed            0.1139      0.053      2.133      0.033       0.009       0.219
Week_1                          -0.2062      0.070     -2.928      0.004      -0.344      -0.068
new_cases_transformed:Week_1     0.0355      0.007      5.229      0.000       0.022       0.049
Week_3                           0.0884      0.018      5.014      0.000       0.054       0.123
Week_6                           0.0688      0.015      4.667      0.000       0.040       0.098
==============================================================================
Omnibus:                       90.372   Durbin-Watson:                   0.576
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              641.355
Skew:                           0.211   Prob(JB):                    5.39e-140
Kurtosis:                       7.428   Cond. No.                         749.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''

anovaResults = anova_lm(reduced, result)
#print(anovaResults)
'''
   df_resid          ssr  df_diff   ss_diff       F    Pr(>F)
0     772.0  1971.383935      0.0       NaN     NaN       NaN
1     770.0  1969.697671      2.0  1.686264  0.3296  0.719313
'''
# keep reduced model

#residual plot
r_student = reduced.outlier_test()["student_resid"]
sns.regplot(x=r_student,y=reduced.fittedvalues)
plt.title("Residual Plot Weekly Vaccines Transformed vs New Cases Transformed data clean weekly interactive term")
plt.savefig('Residual Plot Weekly Vaccines Transformed vs New Cases Transformed data clean weekly interactive term.png')
plt.show()
plt.close('all')

#qq plot
fig, ax = plt.subplots()
_, (__, ___, r) = stats.probplot(reduced.resid, plot=ax, fit=True)
plt.title("QQ Plot Weekly Vaccines Transformed vs New Cases Transformed data clean weekly interactive term")
plt.savefig('QQ Plot Weekly Vaccines Transformed vs New Cases Transformed data clean weekly interactive term.png')
plt.show()
plt.close('all')


'''
outliers
'''

#%% testing
'''
#testing on df
is there a way to test regression models/should we test them?
'''
class df_testcase(unittest.TestCase):
    
    def test_no_na_in_important_columns(self):
        #check to make sure no na's are in used columns
        for name in ['continent','location','Case Week','new_tests','new_cases','new_deaths',
                     'total_tests','total_cases','total_deaths','Vaccine Week','Weekly_Vaccines_Given']:
            for bol in df[name].isna():
                self.assertTrue(bol == False)
        
    def test_Week_1_to_9_calculating_correctly(self):
        #test Week 1-9 to make sure calculation is correct, checking 1 country.
        lis = df["Weekly_Vaccines_Given_transformed"][20:29].values.tolist()
        count = 0
        for num in range(9,0,-1):
            count += 1
            if count == 1:
                self.assertTrue(lis[0:num], df["Week_1"][4+count:12].values.tolist())
            elif count == 2:
                self.assertTrue(lis[0:num], df["Week_2"][4+count:12].values.tolist())
            elif count == 3:
                self.assertTrue(lis[0:num], df["Week_3"][4+count:12].values.tolist())
            elif count == 4:
                self.assertTrue(lis[0:num], df["Week_4"][4+count:12].values.tolist())
            elif count == 5:
                self.assertTrue(lis[0:num], df["Week_5"][4+count:12].values.tolist())
            elif count == 6:
                self.assertTrue(lis[0:num], df["Week_6"][4+count:12].values.tolist())
            elif count == 7:
                self.assertTrue(lis[0:num], df["Week_7"][4+count:12].values.tolist())
            elif count == 8:
                self.assertTrue(lis[0:num], df["Week_8"][4+count:12].values.tolist())
            elif count == 9:
                self.assertTrue(lis[0:num], df["Week_9"][4+count:12].values.tolist())
                
    def test_not_0_cases_is_calculated_correctly(self):
        #check that 'not 0 cases' is calculated correctly
        for case in df[['location','total_cases']].groupby(by=["location"]).max()['total_cases']:
            self.assertNotEqual(case, 0)
        
    def test_At_least_3_weeks_of_vaccine_data_is_True(self):
        #check that there are at least 3 weeks of vaccine data
        for x in df[['location','Weekly_Vaccines_Given']].groupby(by=["location"]):
            count = 0
            for val in x[1]["Weekly_Vaccines_Given"]:
                if val != 0:
                    count += 1
                    if count >= 3:
                        break
            self.assertTrue(count >= 3, msg = x[0])
    
    def test_all_positive_values_in_relevant_columns(self):
        #make sure df["Weekly_Vaccines_Given"], df["new_cases"], case["new_tests"], case["new_cases"] all have <0 values.
        for x in df["Weekly_Vaccines_Given"]:
            self.assertTrue(x > 0)
        for x in df["new_cases"]:
            self.assertTrue(x > 0)
        for x in case["new_tests"]:
            self.assertTrue(x > 0)
        for x in case["new_cases"]:
            self.assertTrue(x > 0)

if __name__ == '__main__':
    unittest.main()  
    
