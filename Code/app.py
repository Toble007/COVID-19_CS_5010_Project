# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:03:24 2021

@author: msachs
"""

import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import os
import dash_table as dt
import plotly.express as px

#os.chdir('C:/Users/MSachs.MSACHS-DELL/Documents/UVA MSDS/CS 5010/Semester Project/Dashboard')

country_df = pd.read_csv('Country Lookup.csv', 
            header=0,na_values=('#NULL!',''))
country_df = country_df.iloc[:,[0,4]]

daily_case = pd.read_csv('Daily COVID Case Data.csv', 
            header=0,na_values=('#NULL!',''))
daily_case = pd.merge(daily_case, country_df,left_on = 'location',right_on = 'TableName', how = 'left')
daily_case = daily_case.drop(columns = 'TableName')

daily_vacc = pd.read_csv('Daily COVID Vaccine Data.csv', 
            header=0,na_values=('#NULL!',''))

daily_case.iloc[:,3:11] = daily_case.iloc[:,3:11].fillna(0)
daily_case['date_x'] = pd.to_datetime(daily_case['date_x'])
daily_vacc['date'] = pd.to_datetime(daily_vacc['date'])
daily_case = daily_case.rename({"location":"Country"}, axis='columns') 
daily_vacc = daily_vacc.rename({"country":"Country"}, axis='columns') 
#daily_case = daily_case[daily_case['location'] == 'Albania']
#daily_vacc = daily_vacc[daily_vacc['country'] == 'Albania']

combined_df = pd.merge(daily_case, daily_vacc, left_on = ("Country","date_x"), right_on = ("Country","date"), how = "left" , suffixes = ("_1", "_2"))
np.where(combined_df.columns.isin(["date_x"]) == True)
np.where(combined_df.columns.isin(["Country"]) == True)
###combined_df = combined_df.drop(combined_df.columns[23], axis=1)

###bring in cleaned weekly data
cov_df = pd.read_csv('Cleaned COVID Data.csv', 
            header=0,na_values=('#NULL!',''))
###correlation
cov_con_df = cov_df
cov_con_df.columns = ['continent',
'location',
'population',
'population_density',
'median_age',
'aged_65_older',
'cardiovasc_death_rate',
'diabetes_prevalence',
'handwashing_facilities',
'life_expectancy',
'human_development_index',
'Case Week',
'new_tests',
'new_cases',
'new_deaths',
'total_tests',
'total_cases',
'total_deaths',
'Vaccines',
'Vaccine Week',
'Weekly Vaccines Given',
'Total People Vaccinated',
'Total People Fully Vaccinated',
'Adjusted savings',
'FDI (%)',
'FDI ($)',
'GDP per capita',
'Manufacturing (%)',
'Services (%)',
'pdi',
'idv',
'mas',
'uai',
'ltowvs',
'ivr',
'Region',
'IncomeGroup',
'Case Week Max'
]
cov_con_df = cov_con_df.loc[cov_con_df.groupby(['location'])['Case Week'].idxmax()]

###add additional metrics
cov_con_df["COVID_infection_rate"] = (cov_con_df["total_cases"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_positivity_rate"] =(cov_con_df["total_cases"]/cov_con_df["total_tests"]).round(2)
cov_con_df["COVID_mortality_rate"] = (cov_con_df["total_deaths"]/cov_con_df["total_cases"]).round(2)
cov_con_df['Total People Fully Vaccinated'] = cov_con_df['Total People Fully Vaccinated'].fillna(0)
cov_con_df['People Part Vac'] = cov_con_df['Total People Vaccinated'] - cov_con_df['Total People Fully Vaccinated']
cov_con_df["COVID_p_vac_rate"] = (cov_con_df["People Part Vac"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_f_vac_rate"] = (cov_con_df["Total People Fully Vaccinated"]/cov_con_df["population"]).round(2)
cov_con_df["COVID_s_vac_rate"] = (cov_con_df["Total People Vaccinated"]/cov_con_df["population"]).round(2)

###final calculation
cor_df = cov_con_df[cov_con_df.columns[~cov_con_df.columns.isin(["continent","location","Vaccines","Region","IncomeGroup","Case Week Max"])]]
corr_p = cor_df.corr()
#corr_p.reset_index(inplace = True)

###calculate vaccination rates, infection rates, etc
cov_df["Infection Rate"] = (cov_df["total_cases"]/cov_df["population"]).round(2)
cov_df["Positivity Rate"] =(cov_df["total_cases"]/cov_df["total_tests"]).round(2)
cov_df["Mortality Rate"] = (cov_df["total_deaths"]/cov_df["total_cases"]).round(2)
cov_df['Total People Fully Vaccinated'] = cov_df['Total People Fully Vaccinated'].fillna(0)
cov_df['People Part Vac'] = cov_df['Total People Vaccinated'] - cov_df['Total People Fully Vaccinated']
cov_df["Partial Vaccination Rate"] = (cov_df["People Part Vac"]/cov_df["population"]).round(2)
cov_df["Full Vaccination Rate"] = (cov_df["Total People Fully Vaccinated"]/cov_df["population"]).round(2)
cov_df["Overall Vaccination Rate"] = (cov_df["Total People Vaccinated"]/cov_df["population"]).round(2)


###isolate unique vaccines
vaccine_list = cov_df.Vaccines.dropna().unique()
new_v_list = np.array([])
for v in vaccine_list:
    iterator = v.split(", ")
    for i in iterator:
        new_v_list = np.append(new_v_list,i)

new_v_list = np.unique(new_v_list)


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "COVID Analytics: An International View"

app.layout = html.Div(
    children=[
    html.Div(
    children=[
        html.H1(children="COVID Analytics",className = "header-description",),
        html.P(
            children="Analyze the spread of Covid"
            " and the vaccination efforts"
            " by country",className="header-description",
        ),
            ],
            className="header",
        ),
 html.Div(
            children=[
               html.Div(
                   children = [
                       html.Div(children = "Map View", className = "menu-title"),
                       dcc.Dropdown(
                           id="view-filter",
                           options=[
                               {"label": View, "value": View}
                               for View in ['Cases','Vaccines']
                               ],
                               value = "Cases",
                               clearable=False,
                               className="dropdown",
                               ),
                       ]
                   )
            ],
            className="menu",
        ),
 html.Div(
    children=[
        html.Div(
            children=dcc.Graph(id = 'heat_map',
            ),
            className="card",
        ),
     ],
    className="wrapper",
   ),
  html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Country", className="menu-title"),
                        dcc.Dropdown(
                            id="country-filter",
                            options=[
                                {"label": Country, "value": Country}
                                for Country in np.sort(daily_case.Country.unique())
                            ],
                            value="United States",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu2",
        ),
html.Div(
    children=[
        html.Div(
            children=dcc.Graph(id = 'case_chart',
            config={"displayModeBar": False},
            ),
            className="card",
        ),
     ],
    className="wrapper2",
   ),
  html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="COVID Metric", className="menu-title2"),
                        dcc.Dropdown(
                            id="cov-filter",
                            options=[
                                {"label": Metric, "value": Metric}
                                for Metric in ["Infection Rate","Positivity Rate",
                                                "Mortality Rate","Partial Vaccination Rate","Full Vaccination Rate","Overall Vaccination Rate"]
                            ],
                            value="Overall Vaccination Rate",
                            clearable=False,
                            className="dropdown", 
                        ),],),
                html.Div(
                    children=[
                        html.Div(children="Country Grouping", className="menu-title2"),
                        dcc.Dropdown(
                            id="group-filter",
                            options=[
                                {"label": Group, "value": Group}
                                for Group in ["continent","Region","IncomeGroup","Vaccines"]
                            ],
                            value="IncomeGroup",
                            clearable=False,
                            className="dropdown", 
                        ),],),
                html.Div(
                    children=[
                        html.Div(children="Filter Selection", className="menu-title2"),
                        dcc.Dropdown(
                            id="filt-filter",
                            clearable=False,
                            className="dropdown", 
                        )
                    ]
                ),
            ],
            className="menu3", 
        ),
html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
            id = 'vacc_chart',
            config={"displayModeBar": False},
        ),
        className="card", 
       ),
     ],
    className="wrapper3",
   ),
html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
            id = 'corr_chart',
            config={"displayModeBar": False},
        ),
        className="card", 
       ),
     ],
    className="wrapper4",
   ),

# html.Div([
#     html.Div(id="table1"),
#     ])
 ]
)


@app.callback(
    [Output('filt-filter', 'options'),Output('filt-filter', 'value')],
    [Input('group-filter', 'value')]
)

def update_date_dropdown(name):
    if name != "Vaccines":
        return [{'label': Filter, 'value': Filter} for Filter in np.sort(cov_df[cov_df.columns[cov_df.columns.isin([name])]].fillna("Unknown").squeeze().unique())], np.sort(cov_df[cov_df.columns[cov_df.columns.isin([name])]].fillna("Unknown").squeeze().unique())[0]
    else:
        return[{'label': Filter, 'value': Filter} for Filter in new_v_list], new_v_list[0]


@app.callback(
    [Output("heat_map","figure"),Output("case_chart", "figure"), Output("vacc_chart", "figure"),Output("corr_chart", "figure")],
    [
        Input("country-filter", "value"), Input("view-filter","value"), Input("cov-filter","value"), Input("group-filter","value"), Input("filt-filter","value")
    ],
)
def update_charts(Country,View,Metric,Group,Filter):
    mask = (
        (combined_df.Country == Country)
    )
    if Group != "Vaccines":
        mask2 = (
            (cov_df[cov_df.columns[cov_df.columns.isin([Group])]].fillna("Unknown").squeeze() == Filter)
        )
    else:
         mask2 = (
            (cov_df[cov_df.columns[cov_df.columns.isin([Group])]].fillna("Unknown").squeeze().str.contains(Filter))
        )
    filtered_data = combined_df.loc[mask, :]
    filtered_data2 = cov_df.loc[mask2, :]
    
    case_chart_figure = {
                "data": [
                    {
                        "x": filtered_data["date_x"],
                        "y": filtered_data["new_tests"],
                        "type": "lines",
                        'name': 'New Tests',
                    },
                    {
                        "x": filtered_data["date_x"],
                        "y": filtered_data["new_cases"],
                        "type": "lines",
                        'name': 'New Cases',
                    }, {
                        "x": filtered_data["date_x"],
                        "y": filtered_data["new_deaths"],
                        "type": "lines",
                        'name': 'New Deaths',
                    },
                        {
                        "x": filtered_data["date_x"],
                        "y": filtered_data["Daily Change"],
                        "type": "lines",
                        'name': 'New Vaccines',
                    },
                ],
                "layout": {"title": {"text" : "Daily COVID Cases Reported",
                            "x": 0.05,
                            "xanchor": "left",},
                        "xaxis": {"fixedrange": True},
                        "yaxis": {
                            "title": "Total Occurences",
                            "fixedrange": True,
                        },
                        "colorway": ["#800080","#ffa500","#FF0000","#17B897"],
        },
    }
    if Metric in ["Infection Rate","Positivity Rate","Mortality Rate"]:
        # vacc_chart_figure = {
        #     "data": [
        #                 {
        #                     "x": filtered_data2["Case Week"],
        #                     "y": filtered_data2[filtered_data2.columns[filtered_data2.columns.isin([Metric])]].squeeze(),
        #                     "type": "lines",
        #                     "color" : filtered_data2["location"],
        #                 },
        #             ],
        #             "layout": {"title": {"text" : "Weekly COVID Metrics Reported",
        #                         "x": 0.05,
        #                         "xanchor": "left",},
        #                     "xaxis": {"fixedrange": True},
        #                     "yaxis": {
        #                         "title": "% Of Population",
        #                         "fixedrange": True,},
        #                     "showlegend": True,
        #                     # "colorway": ["#17B897"],
        #             },
        # }
        vacc_chart_figure = px.scatter(filtered_data2, x="Case Week", y=Metric, color= "location")
        vacc_chart_figure.update_traces(mode='lines')
    else:
        # vacc_chart_figure = {
        #     "data": [
        #                 {
        #                     "x": filtered_data2["Vaccine Week"],
        #                     "y": filtered_data2[filtered_data2.columns[filtered_data2.columns.isin([Metric])]].squeeze(),
        #                     "type": "lines",
        #                     "color" : filtered_data2["location"],
        #                 },
        #             ],
        #             "layout": {"title": {"text" : "Weekly COVID Vaccines Administered",
        #                         "x": 0.05,
        #                         "xanchor": "left",},
        #                     "xaxis": {"fixedrange": True},
        #                     "yaxis": {
        #                         "title": "% Of Population",
        #                         "fixedrange": True,},
        #                     "showlegend": True,
        #                     # "colorway": ["#17B897"],
        #             },
        vacc_chart_figure = px.scatter(filtered_data2, x="Vaccine Week", y=Metric, color= "location")
        vacc_chart_figure.update_traces(mode='lines')
        # }

    
    if View == 'Cases':
        daily_case2 = daily_case.groupby(['Country'])["date_x"].idxmax()
        daily_case2 = daily_case.loc[daily_case2]
        daily_case2["COVID_infection_rate"] = (daily_case2["total_cases"]/daily_case2["population"]*100).round(2)
        daily_case2["COVID_positivity_rate"] =(daily_case2["total_cases"]/daily_case2["total_tests"]*100).round(2)
        daily_case2["COVID_mortality_rate"] = (daily_case2["total_deaths"]/daily_case2["total_cases"]*100).round(2)
        daily_case2['hover_text'] = daily_case2["Country"] + " <br>COVID Infection Rate:" + daily_case2["COVID_infection_rate"].apply(str) + "% " +'<br>COVID Positivity Rate: ' + daily_case2["COVID_positivity_rate"].apply(str) + '% <br>COVID Mortality Rate: ' + daily_case2["COVID_mortality_rate"].apply(str) + '%'
        trace = go.Choropleth(locations=daily_case2['Country Code'],z=daily_case2['COVID_infection_rate'],
                              text=daily_case2['hover_text'],
                              hoverinfo="text",
                              marker_line_color='white',
                              autocolorscale=False,
                              reversescale=True,
                              colorscale="RdBu",marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                              colorbar={"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                        'title': {"text": 'Infection Risk Scale', "side": "top"},
                                        'tickvals': [ 0, 50],
                                        'ticktext': ['0', '50']})  
        heat_map_figure = {"data": [trace],
                           "layout": go.Layout(height=800,geo={'showframe': True,'showcoastlines': True,
                                                               'projection': {'type': "miller"}})}

    else:
        daily_case3 = daily_case.iloc[:,[1,11]]
        daily_case2 = daily_vacc.groupby(['Country'])["date"].idxmax()
        daily_case2 = daily_vacc.loc[daily_case2]
        daily_case2 = pd.merge(daily_case2,daily_case3, on = "Country", how = "left")
        daily_case2['people_fully_vaccinated'] = daily_case2['people_fully_vaccinated'].fillna(0)
        daily_case2['people_part_vac'] = daily_case2['people_vaccinated'] - daily_case2['people_fully_vaccinated']
        daily_case2["COVID_p_vac_rate"] = (daily_case2["people_part_vac"]/daily_case2["population"]*100).round(2)
        daily_case2["COVID_f_vac_rate"] = (daily_case2["people_fully_vaccinated"]/daily_case2["population"]*100).round(2)
        daily_case2['hover_text'] = daily_case2["Country"] + " <br>COVID Partial Vaccination Rate:" + daily_case2["COVID_p_vac_rate"].apply(str) + "% " +'<br>COVID Full Vaccination Rate: ' + daily_case2["COVID_f_vac_rate"].apply(str) + '%'
        trace = go.Choropleth(locations=daily_case2['iso_code'],z=daily_case2['COVID_p_vac_rate'],
                              text=daily_case2['hover_text'],
                              hoverinfo="text",
                              marker_line_color='white',
                              autocolorscale=False,
                              reversescale=True,
                              colorscale="RdBu",marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                              colorbar={"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                        'title': {"text": 'Vaccination Rate Scale', "side": "top"},
                                        'tickvals': [ 0, 75],
                                        'ticktext': ['0', '75']})   
    
        heat_map_figure = {"data": [trace],
        "layout": go.Layout(height=800,geo={'showframe': True,'showcoastlines': True,
        'projection': {'type': "miller"}})}
    
    # data = filtered_data2[filtered_data2.columns[filtered_data2.columns.isin([Metric,"location",Group])]].to_dict('rows')
    # columns =  [{"name": i, "id": i,} for i in (filtered_data2[filtered_data2.columns[filtered_data2.columns.isin([Metric,"location",Group])]].columns)]

    corr_chart_figure = go.Figure(data=go.Heatmap(z= corr_p.values.tolist(),
            x = corr_p.columns.tolist(),
            y = corr_p.index.tolist()
               ))
    corr_chart_figure.update_xaxes(side="top")
    
    return heat_map_figure,case_chart_figure, vacc_chart_figure, corr_chart_figure
    # dt.DataTable(data=data, columns=columns)

        

if __name__ == "__main__":
    app.run_server(debug=True)