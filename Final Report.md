# Introduction
*Describe your project scenario. Starting out, what did you hope to accomplish/learn?*

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
Briefly discuss associated responsibilities

## Project Workflow
Show diagram
Discuss weekly cadence
Give example of sprints goals

## Project Management
Discuss original set up without github
Later incorporation of github
Google Slides
Google Docs
Sharing on Slack
How could we have been more efficient?

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

## Hypothesis 1: COVID Vaccinations Impact Lagged COVID Cases
### Model Preparation

### Model Description

### Model Interpretation

### Testing

## Hypothesis 2: COVID Testing Rates Help Set Infection Rate Expectations
### Model Preparation

### Model Description

### Model Interpretation

### Testing

## Hypothesis 3: A Country's Ability To Scale Vaccination Efforts Is Related To HDI
### Model Preparation

### Model Description

### Model Interpretation

### Testing

## Hypothesis 4: Cultural Dimensions Play A Role In COVID Infection Rates
### Model Preparation

### Model Description

### Model Interpretation

### Testing

# Conclusions

## Key Takeaways

## Opportunities For Further Investigation
