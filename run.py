from datetime import datetime # imports the datetime package (standard library)

import dash_bootstrap_components as dbc # bootstrap support
import dash_core_components as dcc # dash core components support
from dash.dependencies import Input, Output # I/O support
import dash_html_components as html # html support
import dash_table # dash table support
import dash # package used to deploy app locally

import pandas as pd # common package used in financial applications to work with data frames

import plotly.express as px # packages used to create the graphs: 'express',...
import plotly.graph_objects as go # and 'graph_objects' for the candlestick chart

import extract # imports the functions created in the 'extract.py' file
from extract import Wallet # imports the wallet class defined in 'extract.py'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# instantiates the dash package to create a flask server, using bootstrap

eth_date, openPrice, closePrice, dailyHigh, dailyLow, volume = extract.getEthereum()
btc_date, btc_price = extract.getBitcoin()
pick, symbol, cost, day_change, multiple, mcap = extract.cmcScreen()
# making calls to the functions created in 'extract.py' and storing their return values in new variables...

myPortfolio = Wallet()
# instantiates the wallet class as myPortfolio
myPortfolio.setEtherAmount(7.48)
# put 5 ether in the 'wallet'
myPortfolio.setBitcoinAmount(0.15)
# put 0.15 bitcoin in the 'wallet'

multiplierEth = myPortfolio.getEtherAmount()
# created a variable to hold myPortfolio object's Ethereum Balance
multiplierBtc = myPortfolio.getBitcoinAmount()
# created a variable to hold myPortfolio object's Bitcoin Balance
ether_value, bitcoin_value, wallet_value = [], [], []
# creates a series of empty list to hold the newly calculated values

for price in closePrice:
# using a for loop to iterate through the ethereum prices
    ether_value += [multiplierEth * price]
    # and filling the ether_value list with the wallet amount * respective price
for price in btc_price:
# using a for loop to iterate through the bitcoin prices
    bitcoin_value += [multiplierBtc * price]
    # and filling the bitcoin_value list with the wallet amount * respective price
for date in range(len(eth_date)):
# for the dates in bitcoin/ether timeseries data...
    wallet_value += [bitcoin_value[date] + ether_value[date]]
    # fill the wallet_value list with the combined bitcoin and ethereum values (based on myPortfolio)

df = pd.DataFrame(list(zip(eth_date, closePrice, openPrice, dailyHigh, dailyLow, volume)),
columns=['Date', 'Price', 'Open', 'dailyHigh', 'dailyLow', 'Volume'])
# uses the pandas package to create a data frame named df from the 'extract.getEthereum()' values
df2 = pd.DataFrame(list(zip(pick, symbol, cost, day_change, multiple, mcap)),
columns=['Token', 'Symbol', 'Cost (USD)', '7d Percent Change', '7d Multiple', 'Market Cap (USD)'])
# uses the pandas package to create a data frame named df2 from the 'extract.cmcScreen()' values
df3 = pd.DataFrame(list(zip(eth_date, wallet_value)),
columns=['Date', 'Wallet'])
# uses the pandas package to create a data frame named df3 based on myPortfolio 'wallet_value'

fig = px.line(df3, x='Date', y='Wallet').update_layout(height=500)

now = datetime.now()
# using the datetime package, creates a variable now to grab current time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# formats the now variable into a hours:minutes:seconds and stores in current_time

sidebar = html.Div(
# creates the 'sidebar' part of the web application using the dash_html_components package
    [
        html.P(date_time),
        # creates <p>date_time</p>
        html.H2('ALLOTROPE LLC', className='display-7'),
        # creates <h2>CS521</h2>
        html.Hr(),
        # creates <hr> or horizontal rule
        html.H2('Momentum Report', className='display-6'),
        # creates <h2>Cryptocurrency Monitor Project</h2>
        html.P('by Devin Dyson', className='lead'),
        # creates <p>by Devin Dyson</p>
        html.Hr(),
        # creates <hr> or horizontal rule
        dbc.Nav(
        # creates the navigation section
            [
                dbc.NavLink('Table', href='/table', active='exact'), # /table
                dbc.NavLink('Ideas', href='/ideas', active='exact'), # /ideas
                dbc.NavLink('Portfolio', href='/portfolio', active='exact'), # /portfolio
            ],
            vertical=True, # elements aligned vertically 'vertical stacking'
            pills=True, # indicate active state with pills
        ),
    ],
    style={
    # adds some css style to the sidebar
        'position': 'fixed',
        'top': 0, 'left': 0, 'bottom': 0,
        'width': '18rem',
        'padding': '2rem 1rem',
        'background-color': '#f8f9fa',
    }
)

content = html.Div(
# creates the main section of the page
    id='page-content',
    style={'margin-left': '20rem', 'margin-right': '2rem', 'padding': '2rem 1rem'}
    # adding some css style to the content section
    )

app.layout = html.Div([dcc.Location(id='url'), sidebar, content])
# sets the layout for the app... comprised of sidebar and content

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
# necessary to interact with the navlinks, input and output are specified

def render_page_content(pathname):
# function to render the page content depending on which navlink is active
    if pathname == '/ideas':
    # if the navlink selected is Table = /table
        return dash_table.DataTable(
        # renders the table from 'df'
            id='ideas',
            columns=[{'name': i, 'id': i} for i in df.columns],
            # using list comprehension to set key:value pairs for df.columns
            data=df.to_dict('records')
            # identifies the data to be displayed in dash_table
        )
    elif pathname == '/table'  or pathname == '/':
    # if the navlink selected is Ideas = /ideas
        return html.Div([
        # renders html <div>contents</div> with the following contents:
            html.H1('MOMENTUM TRADES'),
            # <h1>MOMENTUM TRADES</h1>
            html.P('if cmc_data[\'data\'][i][\'quote\'][\'USD\'][\'market_cap\'] != 0 and \
                    cmc_data[\'data\'][i][\'quote\'][\'USD\'][\'percent_change_7d\'] > 20:'),
            # <p>if cmc_data[\'data\'][i][\'quote\'][\'USD\'][\'market_cap\'] != 0 and
            # cmc_data[\'data\'][i][\'quote\'][\'USD\'][\'percent_change_7d\'] > 20:</p>
            dash_table.DataTable(
            # creates a dash table from 'df2'
                id='table',
                columns=[{'name': i, 'id': i} for i in df2.columns],
                # using list comprehension to set key:value pairs for df2.columns
                data=df2.to_dict('records')
                # identifies the data to be displayed in dash_table
            )
        ])
    elif pathname == '/portfolio':
    # this represents the home/default page also the portfolio page
        return html.Div([
        # renders html <div>contents</div> with the following contents:
            dcc.Graph(figure=fig),
            # renders the content from 'fig'
            html.H6('Amount of Ethereum in wallet: '),
            # <h6>'Amount of Ethereum in wallet: '</h6>
            html.P(myPortfolio.getEtherAmount()),
            # <p>myPortfolio.getEtherAmount()</p>
            html.H6('Amount of Bitcoin in wallet: '),
            # <h6>'Amount of Bitcoin in wallet: '</h6>
            html.P(myPortfolio.getBitcoinAmount()),
            # <p>myPortfolio.getBitcoinAmount()</p>
            html.H6('Amount of Ethereum in wallet (USD): '),
            # <h6>'Amount of Ethereum in wallet (USD): '</h6>
            html.P(myPortfolio.getEtherBalance()),
            # <p>myPortfolio.getEthereumAmount()</p>
            html.H6('Amount of Bitcoin in wallet (USD): '),
            # <h6>'Amount of Bitcoin in wallet (USD): '</h6>
            html.P(myPortfolio.getBitcoinBalance()),
            # <p>myPortfolio.getBitcoinBalance()</p>
            html.H6('Total wallet balance (USD): '),
            # <p>myPortfolio.getEtherBalance()</p>
            html.P(myPortfolio.getTotalBalance()),
            # <p>myPortfolio.getTotalBalance()</p>
        ])

    return dbc.Jumbotron(
    # component for showcasing key content and messages
        [
            html.H1('404: Not found', className='text-danger'),
            # if the user tries to reach a different page, return a 404 message
            html.Hr(),
            # <hr> horizontal rule
            html.P(f'The pathname {pathname} was not recognised...'),
            # <p>The pathname {pathname} was not recognised...</p>
        ]
    )

if __name__ == '__main__':
# protects users from accidentally invoking the script
    app.run_server(debug=True,port=8000)
    # boots up the local server on port 8000, debug mode is active
