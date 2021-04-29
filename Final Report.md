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
https://www.kaggle.com/gpreda/covid-world-vaccination-progress
We have fields like country, country code, date, daily vaccinations, vaccination type, total vaccinations, etc.
You’ll notice that “total vaccinations” doesn’t necessarily align with the cumulative “daily vaccinations”
You’ll also notice “partial vaccinations” are not given, but can be inferred via the given columns

## COVID Case Data
https://ourworldindata.org/covid-cases?country=IND~USA~GBR~CAN~DEU~FRA
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
