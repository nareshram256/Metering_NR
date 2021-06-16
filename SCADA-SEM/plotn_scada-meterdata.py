

def runplotn_scadasem():
    import io
    from glob import glob
    import time
    import os.path
    import os
    import pandas as pd
    from openpyxl import load_workbook
    import matplotlib.pyplot as plt
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

    def plotly_gropplot (df,s):
        import random
    
        clr=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure','beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue','chartreuse', 'chocolate', 'coral', 'cornflowerblue','cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
    'darkgoldenrod', 'darkgray','darkgreen','darkolivegreen', 'darkorange','darkorchid', 'darkred', 'darksalmon', 'darkseagreen','darkslateblue', 'darkslategray', 
    'darkslategrey','darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue','dimgray', 'dodgerblue', 'firebrick','floralwhite', 'forestgreen', 'fuchsia', 
    'gray','green','greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo','ivory', 'khaki', 'lavender', 
    'orange', 'orangered','powderblue', 'purple', 'red', 'rosybrown','royalblue']
        print(df.columns[2*s],s)
        trace1 = go.Scatter(
        x=df['BLOCK'],
        y=df[df.columns[2*s]],
        name = df.columns[2*s],
        line = dict(color = 'Red'),
        yaxis='y1',
        opacity = 0.8)

        trace2 = go.Scatter(
        x=df['BLOCK'],
        y=df[df.columns[2*s+1]],
        name = df.columns[2*s+1],
        line = dict(color = 'Blue'),
        yaxis='y1',
        opacity = 0.8)

        trace3 = go.Scatter(
        x=df['BLOCK'],
        y=df[df.columns[2*s]]-df[df.columns[2*s+1]],
        name = 'error',
        line = dict(color = 'black'),
        yaxis='y2',
        opacity = 0.8)
        data=[trace1,trace2,trace3]
            
        layout = dict(
            title= 'PLOT'+" " +df.columns[2*s],
            xaxis=dict(
                rangeselector=dict(
                buttons=list([
                    dict(step='all')
                ])
            ),
            rangeslider=dict( visible=True),
            type='date'
            
            ),yaxis=dict(title='MW'),yaxis2=dict(title='Error MW',
                                overlaying='y',
                                side='right')
            )
        fig = dict(data=data, layout=layout)
        return(fig)


    #filee=input("Enter xlsx file name for plot: ")

    pathh="./" # where schvsactaul data created

    df1=pd.read_excel(pathh+'SEM-SCADA.xlsx',sheet_name='SCADA')
    df2=pd.read_excel(pathh+'SEM-SCADA.xlsx',sheet_name='meter')
    #print(df1.columns)    
    '''
    A=    ['!Companies!PGCIL!NRLDC_PG!LINE!UPCL_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!UTR_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!RVPN_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!DTL_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!JKS_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!HPSB_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!CHND_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!HVPN_DRL!P.MvMoment',
        '!Companies!PGCIL!NRLDC_PG!LINE!PSEB_DRL!P.MvMoment',]
    '''

    A=[ '!COMPANIES!PGCIL!NRLDC_PG!LINE!PSEB_DRL!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!HVPN_DRL!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!RVPN_DRL!P.MvMoment',
'!COMPANIES!DTL!REPO3_DV!LINE!DV_DRWS!P.MvMoment',
'!COMPANIES!UPPTCL!NH_US_UP!LINE!SEML_TT!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!UTR_DRL!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!HPSB_DRL!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!JKS_DRL!P.MvMoment',
'!COMPANIES!PGCIL!NRLDC_PG!LINE!CHND_DRL!P.MvMoment']

    #B=['date','BLOCK','US-01','UA-91','RN-01','DL-91','JK-91','HP-91','CH-91','HR-91','PB-01']
    B=['date','BLOCK' ,'PB-01','HR-91','RN-01','DL-91','US-01','UA-91','HP-91','JK-91','CH-91']
    #df2.columns=B
    nn=[]
    dff=pd.DataFrame(nn)
    ss=['date','BLOCK']
    for i in range (len(df2.columns)):
        dff[df1.columns[i][30:40]]=df1[df1.columns[i]]
        dff[df2.columns[i][0:5]]=df2[df2.columns[i]]
        #dff['diff'+df2.columns[i]]=df1[df1.columns[i]]-df2[df2.columns[i]]
        
    dff=dff.drop(dff.columns[0],axis=1)   
    print(dff.columns)    
    dff.to_excel('output.xlsx',index=True)
    #print(np.round((len(df.columns)-2)/2,0))    
    srch=[{'label':str(B[i+2]),'value':int(i+1)} for i in range (len(A)) ]
    print(srch)
    app = dash.Dash()
    app.layout =html.Div([
                html.Div([
                html.H1("Northern Region pair plot analysis"),html.P("Built by N.Ram") ],
                style = {'text-align': 'center',"margin-left": "auto", "margin-right": "auto",'padding' : '20px' , 'backgroundColor' : '#1f77b4'}),

                html.Div([
                    dcc.Dropdown(
                                id = 'search',
                                options=srch,value=srch[0]['value'],
                                placeholder="Select one",
                                style={"display": "block", "margin-left": "auto", 
                                        "margin-right": "auto", "width": "30%"}
                            ),                   


            dcc.Graph(id ='plot')])

                ])

    @app.callback(dash.dependencies.Output('plot', 'figure'),[dash.dependencies.Input('search', 'value')])
    def multi_output(search):
        #df1=pd.read_excel('output.xlsx')
        return plotly_gropplot(dff,search)

    app.run_server(debug=True, port=8945, use_reloader=False)  

    return   
runplotn_scadasem()    