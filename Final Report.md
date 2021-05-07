# Introduction
Our group started out with a interest in COVID Data and how different factors effected this. We hoped to determine which socioeconomic factors effected COVID outcomes and general information on COVID vaccines, testing and cases worldwide and per country. We knew this was too large and would have to decrease the scope of the project but we would proceed and get as much as we could done.

## Project Scope
Our group was interested in COVID-19 data and understanding COVID trends on an international level. As such, we had a few precursory questions that drove our data selection:

The relationship between vaccination and covid case growth

The relationship between testing and covid case growth

What factors, if any, are leading indicators of higher COVID rates?

Which countries are able to ramp up their vaccination efforts the fastest? What factors contribute to a country’s vaccine implementation?

Are certain vaccines more effective in curbing COVID spread? On a more general level, does vaccination rate impact COVID infection rate? What is the respective time lag?

## Scrum Roles
Project Manager - Matthew Sachs

Software Architect - Thomas Butler

Quality Assurance Manager - Karan Manwani

User Interface Designer - Matthew Sachs

A Project Manager makes sure every aspect of the design will fit into our primary goal. Matthew's job was to keep us on track and make sure we weren't straying from our project scope.

A Software Architect makes sure the idea we think of is actually possible to code. Thomas's job was to make sure everything was possible to code and help those who were having trouble or come up with the code framework for the problem if they were off course.

A Quality Assurance Manager makes sure the code is robust, there job is to make sure all potential aspects of the code will not cause errors for our intended use case. Karan ensured we had unit testing and helped us understand if a particular part of our code wasn't coded in a proper manner.

A User Interface Designer makes sure the results we come to is shown in a easy to understand way for our client. This role makes it possible for other people to understand our work without looking through our code and allows those without the required background knowledge to understand what we did. Matthew's job was to make sure all our results were presented in a understandable way for our client.

Even though each of the group members were assigned or fell into these roles, every scrum role was filled by every group member at some time during the project.

## Project Workflow
![Project Flow](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Project%20Flow.png)

Our project workflow was very consistent. We broke everything up into pieces. Our first meeting was determining what we had to do to finish the project and dividing the work as evenly as possible for the rest of our project. Every meeting we used our plan from the first meeting and determined more details who would work on what so we could show what we did for that week. An example of this is the first meeting we decided on our main topic and our job was to find datasets and go think about what questions we wanted answered on those datasets. We should post what we find on slack and then we would discuss which datasets we wanted to use and which questions we wanted to answer the next week.

## Project Management
Our project management was all over the place. We started out with a google document detailing our ideas and the datasets we were using. Eventually we moved over to exclusively a group chat in Slack where we would post our code various ideas and talk about our meetings. Right at the end of our project we set up a Github project. The way Github tracks changes would have been very useful to share code and see various changes in our code. If I was going to redo this project right now I would set up a Github project for all of our work to go on and use Slack for communication through the team. This would make us much more efficient.

# The Data
*Describe your data set and its significance. Where did you obtain this data set from? Why did you choose the data set that you did? Indicate if you carried out any preprocessing/data cleaning/outlier removal, and so on to sanitize your data.*

## Vaccine Data

The crux of our project resides with accurate COVID-19 vaccine data. While it is difficult to believe in the veracity of data reported by countries with low transparency scores (see https://www.transparency.org/en/cpi/2020/index/nzl), we arrived at the conclusion that we could only do so much to clean up the data; the majority of reported data needs to be taken at face value. For this reason, further analysis likely warrants grouping customers by transparency score (ie: high trapnsparency, average transparency, and low transparency) and evaluating COVID-related numbers through this lens.

We gathered our vaccine data from Kaggle, https://www.kaggle.com/gpreda/covid-world-vaccination-progress. The dataset is updated daily with the latest reported numbers and contains 15 fields, largely representing one of four categories: country level, vaccine level, date level, and source-related information. The country level data encompasses the country name and country code, which are of important note because these fields serve as the connective tissue between our datasets. Vaccine data includes the raw number of vaccines given on a particular day, the raw number of vaccinated people on a particular day, smoothed vaccination numbers, adjusted vaccination numbers, and vaccine types. There are two glaring omissions from these fields: partial vaccinations given and vaccination rate. Both of these metrics can be calculated after bringing in population data, but we still need to account for missing data and incorrectly calculated rolling sum columns.

161 countries are represented in the data, and the date ranges (from when we downloaded the data) are from 12/13/2020, which is the earliest vaccination implementation for any country, to 3/30/2020. This gives us a best-case scenario of 3.5 months of vaccination data. The daily numbers fluctuate wildly from country to country, and the standard deviation of daily vaccinations across all the countries is 244,102. This is a strong indicator of a) the inherent reporting inconsistencies and b) the disparity in vaccination implementations between countries.

## COVID Case Data

To supplement our vaccine data, we needed the actual COVID-19 case data as well; this is updated daily and can be downloaded from https://ourworldindata.org/covid-cases?country=IND~USA~GBR~CAN~DEU~FRA. Spanning 59 fields and 215 countries, a couple take-aways are immediately apparent: there are quite a few countries which have reported COVID 19 cases and are yet to implement a vaccine program, and the breadth of data here indicates the likelihood of non-COVID fields. Sure enough, there are a number of potential infection predictors, including but not limited to: population size, median age, and average life expectancy. Predictors that are directly related to COVID's spread and potency, like cardiovascular deaths, handwashing facilities, and prevalence of diabetes, complement our COVID-specific metrics like daily cases reported, daily deaths reported, and daily tests conducted. Unfortunantely, a number of fields, like patients in ICU, number of smokers, etc, have a paucity of countries represented and, as a result, can only be effectively modeled for a subset of countries.

The data has observations from as early as 1/1/2020, which is nearly a full year's worth of data more than our vaccine data. Assuming the dataset's reported numbers are roughly as accurate as our vaccine numbers, we would assume that the increased number of observations would help us to train our models more effectively

We have fields like country, country code, date, daily cases, daily deaths, total cases, etc.
We also have some boiler-plate demographic data
You’ll notice that some countries are missing quite a bit of data in some fields

## Cultural Dimension Data
https://geerthofstede.com/research-and-vsm/dimension-data-matrix/
Geert Hofstede is a social scientist who rates countries on 0-100 scale on 6 dimensions: power distance, individualism, masculinity, uncertainty avoidance, long-term orientation, and indulgence
There are some regional entries here, and a lot of missing data
The country codes here do not necessarily align with the country codes in our other datasets

## Economic Indicator Data
https://data.worldbank.org/topic/economy-and-growth
There are quite a few economic indicators (245) included here, complemented with country and country code designations
The data is an odd wide-long mesh; note that the indicators are consolidated to a single column, whereas the years each have their very own
The data format presented a challenging reconfiguration

# Experimental Design
*Describe briefly your process, starting from where you obtained your data all the way to means of obtaining results/output.* 

## Vaccine Clean-Up


## COVID Case Clean-Up


## Cultural Dimension Clean-Up


## Economic Indicator Clean-Up


## Merging Datasets

## Testing

# Beyond the original specifications
*Highlight clearly what things you did that went beyond the original specifications. That is, discuss what you implemented that would count toward the extra-credit portion of this project (see section below).*

## User Stories

## Requirements

## COVID Dashboard

## Testing

# Results
*Display and discuss the results. Describe what you have learned and mention the relevance/significance of the results you have obtained.*

## Hypothesis 1: COVID Vaccinations vs. Lagged COVID Cases
This model intents to answer the relationship between COVID Case growth and COVID vaccination worldwide. Code for model can be found https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Code/Covid_Vaccines_Tests_Cases_Regression_Code_and_Unit_Testing.py in the 'Vaccine v cases regression cell', testing is found inside the 'testing' cell and the data is loaded in inside the 'data load in and test v cases regression' cell.

### Model Preparation
The COVID Cases and COVID Vaccines datasets were used in this model. All data points that did not have Vaccine happening during that week were removed. All zero value data points for Weekly Vaccines Given and new COVID cases were removed. Any country that was vaccinating but not reporting any covid cases were removed. Any country that didn't have at least 3 weeks of vaccine data was removed. The reason why any country that didn't have at least 3 weeks of vaccine data were removed was because they were not actively vaccinating. Alot of countries had vaccines donated to them from various sources and either can't afford and/or get access to more vaccines.

![Weekly Vaccines vs New Cases](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Given%20vs%20New%20Cases%20data%20clean.png)

![Zoomed in](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Given%20vs%20New%20Cases%20data%20clean%20zoomed%20in.png)

Above is the graph for the linear relationshp between COVID Vaccines and COVID Cases. The data is not a linear function so a log-log transformation was applied to the data.

![Log transformed data](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Given%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean.png)

The transformed data looks more linear now so proceeded to model fitting.

### Model Description
Weekly Vaccines vs New COVID Cases were fitted with a simple linear regression model. Output and graphs are below.

![Simple model regression output](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20regression%20output.png)

![Residual Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Residual%20Plot%20Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean.png)

![QQ Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/QQ%20Plot%20Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean.png)

![Autocorrelation Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Autocorrelation%20Plot%20New%20Cases%20Transformed%20data%20clean.png)

There are some issues with the model. The residual plot shows a nonconstant variance and non-zero mean. The QQ Plot has a light-tailed distribution. The Autocorrelation plot shows that an autocorrelation issue exists. The nonconstant variance and non-zero mean means that there is probably a issue with my model. When I made these models I didn't know how to fix these issues. So I tried fitting more variables to the model in hopes it would solve some of the issues.

![Multi-Regression Model](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean%20weekly%20regression%20output.png)

Ran this and check for significant terms and then interactive terms. All the additional terms are already log transformed.

![Interative termed model](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean%20weekly%20interactive%20term%20regression%20output.png)

![Residual Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Residual%20Plot%20Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean%20weekly%20interactive%20term.png)

![QQ Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/QQ%20Plot%20Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean%20weekly%20interactive%20term.png)

This is the model I ended up with. My issues from before are still there but the residual plot looks better and the autocorrelation issue might have been fixed, I just had no clue how to check. From here I didn't know how to improve the model further.

### Model Interpretation
![Interative termed model](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Weekly%20Vaccines%20Transformed%20vs%20New%20Cases%20Transformed%20data%20clean%20weekly%20interactive%20term%20regression%20output.png)

A 10% increase in new cases for current week leads to a 2.1% increase in Vaccines for the current week.

The Week 1 coefficient is negative but it has a interactive term and the break even point which causes more vaccines is at least 303 cases on new cases. To come to this number take the absolute value of the coefficient Week_1 / the interactive term (new cases transformed:Week 1) and set that equal to ln(new cases). Solve that equation. Math is shown below.

![Math](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Math%20on%20interative%20equation.png)

A 10% increase in cases from 3 weeks ago leads to a 1% increase in Vaccines for the current week.

### Testing
All columns used in this model were tested to ensure there were no NA values in them and that all the values inside the columns were greater than zero. All countries were tested to ensure they held at least 3 weeks of vaccine data. Created columns for Week 1 to Week 9 were tested to insure they held the correct values.

### Improvements
Starting out our group asked this question in a way that we didn't know how to answer. The question was reworded a few times but we never got a perfect answer. If we had more time we would have figured out how to create an ARIMA (auto regressive integrated moving average) model to answer this question. Originally we didn't know what a autoregressive model was and would now use that to sovle the time lag issue present in the model.

## Hypothesis 2: COVID Testing Rates vs COVID Cases
This model intents to answer what the relationship between COVID Case growth and COIVD Testing is worldwide. Code for model and data load in can be found https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Code/Covid_Vaccines_Tests_Cases_Regression_Code_and_Unit_Testing.py in the 'data load in and test v cases regression' cell and testing is found inside the 'testing' cell.

### Model Preparation
The COVID Cases dataset was used in this model. All zero value data points for new COVID tests and new COVID cases were removed. 

![New Test vs New Cases](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/New%20Tests%20vs%20New%20Cases.png)

As shown above the data was not a linear function. So a log-log transformation was tried on the data. 

![Transformed data](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/New%20Tests%20Transformed%20vs%20New%20Cases%20Transformed.png)

This somewhat solved the linearity problem so proceed to model fitting.

### Model Description
New COVID Tests vs New COVID Cases were fitted with a simple linear regression model. Output and graphs are below.

![Regression output](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/New%20Tests%20Transformed%20vs%20New%20Cases%20Transformed%20regression%20output.png)

![Residual Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Residual%20Plot%20New%20Tests%20Transformed%20vs%20New%20Cases%20Transformed.png)

![QQ PLot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/QQ%20Plot%20New%20Tests%20Transformed%20vs%20New%20Cases%20Transformed.png)

![Autocorrelation Plot](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Autocorrelation%20Plot%20New%20Cases%20Transformed%20data%20clean.png)

There are some issues with the model. The residual plot shows a nonconstant variance and non-zero mean. The QQ Plot has a slight downward skew. The Autocorrelation plot shows that an autocorrelation issue exists. The nonconstant variance and non-zero mean means that there is probably a issue with my model. When I made these models I didn't know how to fix these issues.

### Model Interpretation
![Regression output](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/New%20Tests%20Transformed%20vs%20New%20Cases%20Transformed%20regression%20output.png)

Overall, this model states that a 10% increase in cases leads to a 1.1^Bcase or 1.1^0.5970 = 1.0586 or 5.86% increase in testing.

### Testing
All columns used in this model were tested to ensure there were no NA values in them and that all the values inside the columns were greater than zero.

### Improvements
Starting out our group asked this question in a way that we didn't know how to answer. The question was reworded a few times but we never got a perfect answer. If we had more time we would have figured out how to create an ARIMA (auto regressive integrated moving average) model to answer this question. Originally we didn't know what a autoregressive model was and would now use that to sovle the time lag issue present in the model.

## Hypothesis 3: A Country's Ability To Scale Vaccination Efforts Is Related To HDI
The hypothesis of this model is: The more advanced a country based on the Human Development Index (HDI), the higher their abiltiy to scale vaccination efforts, which is measured by vaccination rates.

### Model Preparation
The Vaccination, Worldbank, and Covid cases datasets were used for this model. Human Development Index is a calculated index using life expectancy, education, and per capita income indicators. It is compliled by the United Nations Development Programme (UNDP). Below is the scale and categories of the index
- Score of 0.8 and above considered as very high.
- 0.7 to 0.799 is high.
- 0.550 to 0.699 considered medium.
- Below 0.550 is low

Vaccination rates were calculated for each country using the vaccination data and demographics data i.e. Total People Vaccinated/population.
The final percentage of the population vaccinated was taken by finding the highest percentage of vaccination rates per country, which in theory should be the latest day of vaccinations. The dataframe was then grouped by country to produce one datapoint for each country showing their percentage of population vaccinated against their human development index.
Countries without a human development index score were dropped from the analysis. This resulted in 15 countries being dropped and the analysis had a total of 100 countries.

### Model Description
A scatter plot and fitted plot of the Human Development Index against Vaccination rate was produced to perform initial exploratory data analysis. The HDI is the predictor variable and Vaccination rate is the response variable.
Below are the two plots:

![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/ScatterPlot_HumanDevIndex_VaccinationRates.png)
![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/FittedPlot_HDI_VaccinationRates.PNG)

As can be seen from the plots, it appears that there could be a linear relationship between HDI and Vaccination rates. There are also some points which are on the top right side of the plots that apprear to be leverage points given their much higher vaccination rates versus most other countries.

Below is the top 10 countries based on vaccination rates along with their corresponding HDI and GDP Per capita numbers (in current $).

![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Top10_VaccinationRates.PNG)

This does show that most of these countries have an HDI above 0.8. It also shows Seychelles and Israel appeart to be the leverage points, given their signficantly higher vaccination rates. 

The next step was to proceed with building a simple linear regression model. 
![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/Regression_HumanDev_VaccinatioRates.PNG)

### Model Interpretation
The results show that the HDI (predictor variable) coefficient has a value of 23.7212 and a t-statistic of 2.702. This means it is statistically signficant within a 95% confidence interval. This can be interpreted as for a unit change in the Human development index, the vaccination rate of a country increases by 23.7%.
However, this model had a low R-Square value of 0.069, which meant that 7% of the variance of Vaccination rates is explained by HDI in this model.

### Testing
Unit testing was done to ensure there were no negative values for HDI and Vaccination Rates. Testing was also done to ensure vaccination rates were equal to or lower than 100, given that this was a calculated number in percentage terms.

### Improvements
Further improvements would be focused on improving the model to better explain the variance. This could be done by trying models outside of linear regression or finding the appropriate transformation.
The data also showed a positive skewness as illustrated by the QQ plot below. So perhaps dealing with the outliers would not only correct for the skewness, but also produce a better R-squared and hence a better explanation of the variance.

![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/QQPLOT_HDI_VaccinationRates.PNG)
## Hypothesis 4: Cultural Dimensions Play A Role In COVID Infection Rates
The hypothesis of this model is: Countries with high individualism & uncertainty avoidance had higher covid cases.

### Model Preparation
The Covid cases was sourced from Ourworld dataset on Covid cases. Geert Hofstede cultural dimensions data set was our other data source for this model.

Two cultural dimensions were selected from Hofstede Cultural dimensions : individualism and uncertainty avoidance.

Individualism index measures the ties people have to their society.
- The scores demonstrate loosely Knit vs. tightly knit social framework within a country.
- High value indicates weak interpersonal connection to people outside their core family.

Uncertainty avoidance measures the society’s tolerance for uncertainty. Countries will high scores tend to be more uncomfortable with uncertainty.

The below bar plot shows an example of two countries with different Individualism and Uncertainty avoidance scores. These are also two countries which had different responses to the Covid 19 pandemic.

![](https://github.com/Toble007/COVID-19_CS_5010_Project/blob/main/Visualizations/USA_vs_Singapore_idv%26uai.PNG)

Covid positive rates  were calculated for each country using the covid cases data and demographics data i.e. Total population tested positive for Covid/population. The final percentage of covid positive cases was taken by finding the highest percentage of covid rates per country, which in theory should be the latest day of cases.
Data was grouped by country to produce one datapoint for each country showing their percentage of covid cases  against their individualism and uncertainty avoidance measures.Countries without cultural dimension scores were dropped from the analysis. This resulted in a  total of 67 countries for the analysis.


### Model Description

### Model Interpretation

### Testing

### Improvements

# Conclusions

## Key Takeaways

## Opportunities For Further Investigation
