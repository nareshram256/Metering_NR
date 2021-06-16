

def runplotn_meterdata():
    from glob import glob
    import time
    import os.path
    import os
    import pandas as pd
    from openpyxl import load_workbook

    import csv
    from os import path
    import xlsxwriter 
    from datetime import datetime,timedelta, date
    import numpy as np


    import plotly
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    import plotly.graph_objs as go
    import dash
    import dash_core_components as dcc
    import dash_html_components as html

    def plotly_gropplot (df,s,n):
        import random
    
        clr=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure','beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue','chartreuse', 'chocolate', 'coral', 'cornflowerblue','cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
    'darkgoldenrod', 'darkgray','darkgreen','darkolivegreen', 'darkorange','darkorchid', 'darkred', 'darksalmon', 'darkseagreen','darkslateblue', 'darkslategray', 
    'darkslategrey','darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue','dimgray', 'dodgerblue', 'firebrick','floralwhite', 'forestgreen', 'fuchsia', 
    'gray','green','greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo','ivory', 'khaki', 'lavender', 
    'orange', 'orangered','powderblue', 'purple', 'red', 'rosybrown','royalblue']
            
        trace1 = go.Scatter(
        x=df['BLOCK'],
        y=df[df.columns[s]],
        name = df.columns[s][0:5],
        line = dict(color = 'Red'),
        yaxis='y1',
        opacity = 0.8)

        trace2 = go.Scatter(
        x=df['BLOCK'],
        y=df[df.columns[n]],
        name = df.columns[n][0:5],
        line = dict(color = 'Blue'),
        yaxis='y2',
        opacity = 0.8)

        
        data=[trace1,trace2]
            
        layout = dict(
            title= 'PLOT'+" " +df.columns[s][0:5]+" VS " +df.columns[n][0:5],
            xaxis=dict(
                rangeselector=dict(
                buttons=list([
                    dict(step='all')
                ])
            ),
            rangeslider=dict( visible=True),
            type='date'
            
            ),yaxis=dict(title=df.columns[s][0:5]+' MW'),yaxis2=dict(title=df.columns[n][0:5]+' MW',
                                overlaying='y',
                                side='right')
            )
        fig = dict(data=data, layout=layout)
        return(fig)


    filee=input("Enter xlsx file name for plot: ")

    pathh="./" # where schvsactaul data created

    df=pd.read_excel(pathh+filee+'.xlsx')
        
    srch=[{'label':str(df.columns[i]),'value':int(i)} for i in range (2,len(df.columns))]
    app = dash.Dash()
    app.layout =html.Div([
                html.Div([
                html.H1("Northern Region pair plot analysis"),html.P("Built by N.Ram") ],
                style = {'text-align': 'center',"margin-left": "auto", "margin-right": "auto",'padding' : '20px' , 'backgroundColor' : '#1f77b4'}),

                html.Div([
                    dcc.Dropdown(
                                id = 'search',
                                options=srch,value=srch[0]['value'],
                                #multi=True,
                                style={"display": "block", "margin-right": "auto", 
                                         "width": "30%" , }
                            ),   
                    dcc.Dropdown(
                                id = 'search2',
                                options=srch,value=srch[0]['value'],
                                #multi=True,
                                style={"display": "block", "margin-left": "auto", 
                                         "width": "30%" , }
                            ),                                           
                dcc.Graph(id ='plot')]),


                ])

    @app.callback(dash.dependencies.Output('plot', 'figure'),[dash.dependencies.Input('search', 'value'),dash.dependencies.Input('search2', 'value')])
    def multi_output(search,search2):
        df1=pd.read_excel(pathh+filee+'.xlsx')
        return plotly_gropplot(df1,search,search2)

    app.run_server(debug=True, port=8945, use_reloader=False)  

    return
runplotn_meterdata()