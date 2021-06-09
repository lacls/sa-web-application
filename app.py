import dash
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import urllib
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import re
import urllib.request
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException,InvalidArgumentException,ElementClickInterceptedException,WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle5 as pickle

# source venv/bin/activate
data = pd.read_csv("avocado.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "//db.onlinewebfonts.com/c/7e0f75fa1eb5ee523ae2961d4e7a11a6?family=Noway"
        "family=text/css",
        "rel": "stylesheet",
    },
    
    dbc.themes.BOOTSTRAP
]

external_scripts = [
    {'src': 'assets/custom.js'},
 
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts,)
server = app.server

app.title = "LTRACK2.0 Analytics: Understand Your Sells!"
context_module=html.Div(children=[
                        #Header
                        html.H1(children="Natural Language AI",
                                style={'font-size':'100',}),
                        
                        html.H4(children="Derive insights from unstructured text using LTRACK2.0",
                                style={'font-weight':'200','font-size':'65'}),
                        html.Div( dbc.Button("Try it for free",disabled=True, className="custom_button",href="#nlp_demo",),
                                 style={"padding-top":"20px","padding-bottom":"20px"},
                                 className="wrap"),
                        ##Introduction
                        html.Section(
                            id="introduction",
                            children=[
                                html.H2(children="Insightful text analysis",
                                        style={'font-weight':'400'}),
                                dbc.Row([
                                dbc.Col(html.P(children="Natural Language uses machine learning to reveal the structure and meaning of text. You can extract \
                                information about people, places, and events, and better understand social media sentiment and customer conversations. \
                                Natural Language AI enables you to analyze text and also integrate it with your document storage on Cloud Storage.",
                                style={'line-height':'28px','font-weight':'400','color':'#5f6368'}),),
                                dbc.Col(
                                    html.Img(src="assets/Pic1.png",
                                                 style={"width":'450px','height':'350px','padding-right':'100px','padding-bottom':'100px'}),
                                                 style={"width":'500px','height':'400px'}),
                                ],
                                style={'display':'flex',"justify-content": "space-evenly"}
                                )
                            ],
                            style={"padding-top":"50px"}
                        ),
                        ##DELIDER
                        html.Div(
                         style={"width":"60px","height":"3px","display":"block","background":"#d183a5"}
                        ),
                        ##Overview
                        html.Section(
                            id="request-response",
                            children=[
                                dbc.Row([
                                        dbc.Col([
                                        html.H3(children="AutoML"),
                                        
                                        html.P(children="Train your own high-quality machine learning custom models to classify, extract, and detect sentiment with minimum effort and machine learning expertise using Vertex AI for natural language, powered by AutoML. You can use the AutoML UI to upload your training data and test your custom model without a single line of code.",
                                        style={'line-height':'28px','font-weight':'400','color':'#5f6368'}),
                                        ],),
                        
                                        dbc.Col([
                                        html.H3(children="Natural Language API"),
                                        
                                        html.P(children="The powerful pre-trained models of the Natural Language API empowers developers to easily apply natural language understanding (NLU) to their applications with features including sentiment analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis.",
                                        style={'line-height':'28px','font-weight':'400','color':'#5f6368'}),
                                        ],),

                                        dbc.Col([
                                        html.H3(children="Insights from customers"),
                                        
                                        html.P(children="Use entity analysis to find and label fields within a document — including emails, chat, and social media — and then sentiment analysis to understand customer opinions to find actionable product and UX insights.",
                                        style={'line-height':'28px','font-weight':'400','color':'#5f6368'}),
                                        ],),
                                        ],
                                    className="horizontal")
                                ],
                                style={"padding-top":"30px"}
                        ),

                        ##Demo
                        html.Section(
                            id="nlp_demo",
                            children=[
                                html.H2(children="Natural Language API demo",
                                        style={"text-align":"center","font-size":"40px"}),
                                dbc.InputGroup(
                                    [dbc.InputGroupAddon("Try the API", addon_type="prepend", style={"text-align":"center","font-weight":"50px"}), 
                                    dbc.Input(id="input",placeholder="Enter text to be analyzed...",type="text")],
                                    size="lg",
                                    style={"padding-top":"50px"}),
                                html.Br(),
                                html.Div(dbc.Button("Analyse", id="summit_button",outline=True, className="simple_button",n_clicks=0),
                                 style={"padding-top":"20px","padding-bottom":"20px","text-align":"center"}),  
                                ##place to generate output
                                html.Div(id='container-button-basic'),
                                html.Div(
                                            dbc.Spinner(color="primary", type="grow",children=[html.Div(id="loading-output")]),
                                ),
                                html.Div([
                                    dbc.Button(
                                        "*Support Language",
                                        id="collapse-button",
                                        outline=True, 
                                        color="primary", 
                                        className="mr-1",
                                       
                                    ),
                                    dbc.Collapse(
                                        dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                                        id="collapse",
                                    ),
                                ],
                                    style={"padding-top":"30px"})
                            ]
                        ),


                        # html.Section(
                        #     id="endpoints",
                        #     children=[
                        #         html.H2(children="Authentication"),
                        #         html.Section(
                        #         id="endpoints--root",
                        #         children=[
                        #             html.H2(children="Root"),
                        #             html.P(children="..."),
                        #             ],
                        #         ),
                        #         html.Section(
                        #         id="endpoints--city-detail",
                        #         children=[
                        #             html.H2(children="City Detail"),
                        #             html.P(children="..."),
                                
                        #         ],
                        #         ),
                        #     ]
                        # ),
                        # html.Section(
                        #     id="links",
                        #     children=[
                        #         html.H2(children="Links"),
                        #         html.P(children="..."),
                        #     ]
                        # ),
                        # html.Section(
                        #     id="expanders",
                        #     children=[
                        #         html.H2(children="Expanders"),
                        #         html.P(children="..."),
                        #     ]
                        # ),
                    ],
                    ),

scrolling_bar= html.Nav(
                    className="section-nav",
                    children=[
                        html.Listing(
                            children="NATURAL LANGUAGE API",
                            style={'font-family':"'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"}
                        ),
                        html.Ol(
                            children=[
                                
                                html.Listing(
                                    html.A(href="#introduction",
                                        children="Introduction")
                                ),
                                html.Listing(
                                    html.A(href="#request-response",
                                        children="Benefits")
                                ),
                                html.Listing(
                                    html.A(href="#nlp_demo",
                                        children="Natural Language API demo")
                                ),
                                # html.Listing(
                                #     children=[
                                #     html.A(href="#endpoints",
                                #         children="Endpoints"),
                                #     html.Ul(
                                #         children=[
                                #         html.Listing(
                                #                 html.A(href="#endpoints--city-detail",
                                #                 children="City Detail",
                                #                 className="")
                                #                 ),
                                #         ]
                                #     ),
                                #     ]
                                # ),
                            html.Listing(
                                    html.A(href="#links",
                                    children="Links",
                                    className="")
                                    ),
                                html.Listing(
                                    html.A(href="#expanders",
                                    children="Expanders",
                                    className="")
                                    ),
                            ],
                        ),
                    ],
                    style={"padding-left":'80px','position':'sticky'})
                
horizontal_display=html.Div(
    dbc.Row([
        dbc.Col(scrolling_bar,width=3),
        dbc.Col(context_module)
       ],
        className="horizontal"
    )
)

app.layout = html.Div(
    children=[
        html.Div([
            dbc.Row([
                dbc.Col(html.H2(children="LTrack2.0",style={"padding-left":"95px"}),md=8),
                dbc.Col(dbc.Nav(
                    [
                        dbc.NavLink("Contact", disabled=True, href="#",style={"font-family":"sans-serif","font-size":"18px",}),
                        dbc.NavLink("About",disabled=True, href="#",style={"font-family":"sans-serif","font-size":"18px"}),
                        dbc.NavLink("Terms",disabled=True,href="#",style={"font-family":"sans-serif","font-size":"18px"}),
                    ]),style={"justify-content": "space-evenly"},
                    )
                ],
                justify="between",),],
            className="header",
           ),

        # html.Div(
        #     children=[
        #         html.Div(
        #             children=[
        #                 html.Div(children="Region", className="menu-title"),
        #                 dcc.Dropdown(
        #                     id="region-filter",
        #                     options=[
        #                         {"label": region, "value": region}
        #                         for region in np.sort(data.region.unique())
        #                     ],
        #                     value="Albany",
        #                     clearable=False,
        #                     className="dropdown",
        #                 ),
        #             ]
        #         ),
        #         html.Div(
        #             children=[
        #                 html.Div(children="Type", className="menu-title"),
        #                 dcc.Dropdown(
        #                     id="type-filter",
        #                     options=[
        #                         {"label": avocado_type, "value": avocado_type}
        #                         for avocado_type in data.type.unique()
        #                     ],
        #                     value="organic",
        #                     clearable=False,
        #                     searchable=False,
        #                     className="dropdown",
        #                 ),
        #             ],
        #         ),
        #         html.Div(
        #             children=[
        #                 html.Div(
        #                     children="Date Range",
        #                     className="menu-title"
        #                     ),
        #                 dcc.DatePickerRange(
        #                     id="date-range",
        #                     min_date_allowed=data.Date.min().date(),
        #                     max_date_allowed=data.Date.max().date(),
        #                     start_date=data.Date.min().date(),
        #                     end_date=data.Date.max().date(),
        #                 ),
        #             ]
        #         ),
        #     ],
        #     className="menu",
        # ),
        
        # html.Div(
        #     children=[
        #         html.Div(
        #             children=dcc.Graph(
        #                 id="price-chart", config={"displayModeBar": False},
        #             ),
        #             className="card",
        #         ),
        #         html.Div(
        #             children=dcc.Graph(
        #                 id="volume-chart", config={"displayModeBar": False},
        #             ),
        #             className="card",
        #         ),
        #     ],
        #     className="wrapper",
        # ),
        html.Div(
            horizontal_display,
        )
    ]
)

# ##outside_Variable
# previous_click=0

# @app.callback(
#     [Output("price-chart", "figure"), Output("volume-chart", "figure")],
#     [
#         Input("region-filter", "value"),
#         Input("type-filter", "value"),
#         Input("date-range", "start_date"),
#         Input("date-range", "end_date"),
#     ],
# )

# def update_charts(region, avocado_type, start_date, end_date):
#     mask = (
#         (data.region == region)
#         & (data.type == avocado_type)
#         & (data.Date >= start_date)
#         & (data.Date <= end_date)
#     )
#     filtered_data = data.loc[mask, :]
#     price_chart_figure = {
#         "data": [
#             {
#                 "x": filtered_data["Date"],
#                 "y": filtered_data["AveragePrice"],
#                 "type": "lines",
#                 "hovertemplate": "$%{y:.2f}<extra></extra>",
#             },
#         ],
#         "layout": {
#             "title": {
#                 "text": "Average Price of Avocados",
#                 "x": 0.05,
#                 "xanchor": "left",
#             },
#             "xaxis": {"fixedrange": True},
#             "yaxis": {"tickprefix": "$", "fixedrange": True},
#             "colorway": ["#17B897"],
#         },
#     }

#     volume_chart_figure = {
#         "data": [
#             {
#                 "x": filtered_data["Date"],
#                 "y": filtered_data["Total Volume"],
#                 "type": "lines",
#             },
#         ],
#         "layout": {
#             "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
#             "xaxis": {"fixedrange": True},
#             "yaxis": {"fixedrange": True},
#             "colorway": ["#E12D39"],
#         },
#     }
#     return price_chart_figure, volume_chart_figure
@app.callback(
    Output("loading-output", "children"), [Input("summit_button", "n_clicks")])
def load_output(n):
    if n:
        time.sleep(1)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"
    
# @app.callback(
#     dash.dependencies.Output('container-button-basic', 'children'),
#     [dash.dependencies.Input('input', 'value'),
#      dash.dependencies.Input('summit_button', 'n_clicks')])
# def update_output(value,click_Value):

#     if click_Value:
#         # print(previous_click,click_Value)
#         return 'The input value was "{}" and the button has been clicked {} times'.format(
#             value,
#             click_Value
#         )
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [dash.dependencies.State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

previous_click=0

@app.callback(
    Output('container-button-basic', 'children'),
    [Input("input",'value'),
    Input('summit_button', 'n_clicks')]   
)

def take_string(text_string,click):
    global previous_click
    if text_string:
        if previous_click!=click:
            previous_click=click
            if "shopee" not in text_string or "official_store" not in text_string:
                return   dbc.Alert(
                        [
                            "Please only input the link from the store in Shopee Mall with the following pattern link: https://shopee.vn/{store_name}_official_store.",
                            html.A(" Find here", href="https://shopee.vn/mall/brands/2365", target="_blank",rel="noopener noreferrer",className="alert-link"),
                        ],
                        color="primary",
                    ),
            else:
                return 'The input_String {}'.format(text_string)
##Get_link_download
  
if __name__ == "__main__":
    app.run_server(debug=True)