import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("avocado.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

external_scripts = [
    {'src': 'assets/custom.js'},
 
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts,)
server = app.server

app.title = "Avocado Analytics: Understand Your Avocados!"
context_module=html.Div(children=[
                        html.H1(children="Natural Language AI",
                                style={'font-size':'100',}),
                        html.H4(children="Derive insights from unstructured text using Avocado machine learning.",
                                style={'font-weight':'400'}),
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
                                dbc.Col(html.Img(src="assets/Google_photo.png",
                                                 style={"width":'500px','height':'380px','padding-right':'100px','padding-bottom':'100px'}),),
                                ],
                                style={'display':'flex',"justify-content": "space-evenly"}
                                )
                            ]
                        ),
                        html.Section(
                            id="request-response",
                            children=[
                                html.H2(children="Request & Response"),
                                html.P(children="..."),
                            ]
                        ),
                        html.Section(
                            id="authentication",
                            children=[
                                html.H2(children="Authentication"),
                                html.P(children="..."),
                            ]
                        ),
                        html.Section(
                            id="endpoints",
                            children=[
                                html.H2(children="Authentication"),
                                html.Section(
                                id="endpoints--root",
                                children=[
                                    html.H2(children="Root"),
                                    html.P(children="..."),
                                    ],
                                ),
                                html.Section(
                                id="endpoints--city-detail",
                                children=[
                                    html.H2(children="City Detail"),
                                    html.P(children="..."),
                                
                                ],
                                ),
                            ]
                        ),
                        html.Section(
                            id="links",
                            children=[
                                html.H2(children="Links"),
                                html.P(children="..."),
                            ]
                        ),
                        html.Section(
                            id="expanders",
                            children=[
                                html.H2(children="Expanders"),
                                html.P(children="..."),
                            ]
                        ),
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
                                        children="Request")
                                ),
                                html.Listing(
                                    html.A(href="#authentication",
                                        children="Authentication")
                                ),
                                html.Listing(
                                    children=[
                                    html.A(href="#endpoints",
                                        children="Endpoints"),
                                    html.Ul(
                                        children=[
                                        html.Listing(
                                                html.A(href="#endpoints--city-detail",
                                                children="City Detail",
                                                className="")
                                                ),
                                        ]
                                    ),
                                    ]
                                ),
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
                    style={"padding-left":'80px',"padding-right":'100px','position':'sticky','padding-top':'200px'})
                
horizontal_display=html.Div(
    dbc.Row([
        dbc.Col(scrolling_bar),
        dbc.Col(context_module)
       ],
        className="horizontal"
    )
)
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                    " and the number of avocados sold in the US"
                    " between 2015 and 2018",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value="Albany",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
        html.Div(
            horizontal_display,
        )
    ]
)


@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    app.run_server(debug=True)