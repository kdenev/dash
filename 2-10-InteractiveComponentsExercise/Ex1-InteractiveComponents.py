#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
from turtle import width
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd



# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(
        min=-5
        , max = 5
        , step = .25
        , count=1
        , value=[-1, 1]
        , id='range-output'
    ),

    html.Hr(),  # add a horizontal rule

    html.Div(id='multi-output', style={'fontFamily':'helvetica', 'fontSize':40, 'font-weight': 'bold'})

], style={'fontFamily':'helvetica', 'fontSize':18})



# Create a Dash callback:
@app.callback(
    Output('multi-output', 'children'),
    [Input('range-output', 'value')])
def mult_two(value):
    return f'You have selected {value[0]} and {value[1]}. Product is {value[0] * value[1]}.'





# Add the server clause:

if __name__ == '__main__':
    app.run_server()
