


def runplot_loss():

    import pandas as pd 
    import numpy as np 
    import time
    from datetime import datetime,timedelta, date
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



    ddd=input("how many excels: ")
    for run in range (int(ddd)):

        excel=input("Enter name of Excel ")
        data=pd.read_excel(excel+".xlsx")

        zer_1=np.zeros(96)
        dff = pd.DataFrame(zer_1, columns = ['Name']) 
        d   = input('Enter starting date format ddmmyy: ')
        for s in range (len(data.columns[2:])):

            for j in range (7):
                date_1 = datetime.strptime(d, "%d%m%y")
                end_date = date_1 + timedelta(days=j)
                k=end_date.strftime("%d")+end_date.strftime("%m")+end_date.strftime("%y")
                dff[data.columns[2+s]+str(k)]=np.zeros(96)

        for i in range (len(data.columns[2:])):        
            for j in range (7):
                date_1 = datetime.strptime(d, "%d%m%y")
                end_date = date_1 + timedelta(days=j)
                k=end_date.strftime("%d")+end_date.strftime("%m")+end_date.strftime("%y")
                dff[data.columns[2+i]+str(k)]=data[data.columns[2+i]].iloc[96*j:96+96*j].values
            
        lst2=data.columns[2:]
        #print(dff) 
        lst= [lst2[i]+ str((datetime.strptime(d, "%d%m%y")+ timedelta(days=j)).strftime("%d")+(datetime.strptime(d, "%d%m%y")+ timedelta(days=j)).strftime("%m")+(datetime.strptime(d, "%d%m%y")+ timedelta(days=j)).strftime("%y")) for i in range (len(lst2)) for j in range (7)]
        df2=dff[lst]
        writer = pd.ExcelWriter('Naresh_dir'+str(run)+'.xlsx')
        df2.to_excel(writer)
        writer.save()
        print("completed data collection")












    #excel=input("old_Enter name of Excel ")
    #ddd=pd.read_excel(excel+".xlsx")
    #lst2=ddd.columns[2:]

    def plotly_gropplot (df,gpu,typ):
        data=[]
        if(typ=='BAR'):
            choco=['Actual','SCADA']
            for com in range (1): # if you wanna comapre with anaother excel make it 2
                if(com==1):
                    df=pd.read_excel('Naresh_dir1.xlsx')

                w=[]
                v=[]
                for s in range (len(df.columns)):
                    if(gpu in df.columns[s] and (gpu=='Percent loss' or gpu=='FREQ')):
                        w.append(str('d ')+df.columns[s][len(df.columns[s])-6:])
                        v.append(df.mean()[s])
                    elif(gpu in df.columns[s] and (gpu!='Percent loss' or gpu!='FREQ')):
                        w.append(str('d ')+df.columns[s][len(df.columns[s])-6:])
                        v.append(df.sum()[s]/400)     
                trace1 = go.Bar(x=w,y=v,text=np.round(v,1),textposition='auto',textfont=dict(family='sans serif',size=18,color='black'),name = choco[com])
                data.append(trace1)






            layout=dict(
                title="Total LUs "+gpu+" barchart",barmode='group',color='smoker'
            )
            fig = dict(data=data, layout=layout)
            return(fig)


        else:
            import random
        
            clr=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure','beige', 'bisque', 'black', 'blanchedalmond', 'blue',
        'blueviolet', 'brown', 'burlywood', 'cadetblue','chartreuse', 'chocolate', 'coral', 'cornflowerblue','cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
        'darkgoldenrod', 'darkgray','darkgreen','darkolivegreen', 'darkorange','darkorchid', 'darkred', 'darksalmon', 'darkseagreen','darkslateblue', 'darkslategray', 
        'darkslategrey','darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue','dimgray', 'dodgerblue', 'firebrick','floralwhite', 'forestgreen', 'fuchsia', 
        'gray','green','greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo','ivory', 'khaki', 'lavender', 
        'orange', 'orangered','powderblue', 'purple', 'red', 'rosybrown','royalblue']
            
                    
            for j in range (len(lst2)):
                if(gpu==lst2[j]):
                    data=[]
                    for i in (df.columns[1+7*j:8+7*j]):
                        trace = go.Scatter(
                        x=['00:00:00','00:15:00','00:30:00','00:45:00','01:00:00','01:15:00','01:30:00','01:45:00','02:00:00','02:15:00','02:30:00','02:45:00','03:00:00','03:15:00','03:30:00','03:45:00','04:00:00','04:15:00','04:30:00','04:45:00','05:00:00','05:15:00','05:30:00','05:45:00','06:00:00','06:15:00','06:30:00','06:45:00','07:00:00','07:15:00','07:30:00','07:45:00','08:00:00','08:15:00','08:30:00','08:45:00','09:00:00','09:15:00','09:30:00','09:45:00','10:00:00','10:15:00','10:30:00','10:45:00','11:00:00','11:15:00','11:30:00','11:45:00','12:00:00','12:15:00','12:30:00','12:45:00','13:00:00','13:15:00','13:30:00','13:45:00','14:00:00','14:15:00','14:30:00','14:45:00','15:00:00','15:15:00','15:30:00','15:45:00','16:00:00','16:15:00','16:30:00','16:45:00','17:00:00','17:15:00','17:30:00','17:45:00','18:00:00','18:15:00','18:30:00','18:45:00','19:00:00','19:15:00','19:30:00','19:45:00','20:00:00','20:15:00','20:30:00','20:45:00','21:00:00','21:15:00','21:30:00','21:45:00','22:00:00','22:15:00','22:30:00','22:45:00','23:00:00','23:15:00','23:30:00','23:45:00'],
                        y=df[i],
                        name = i,
                        line = dict(color = clr[random.randint(0,len(clr)-1)]),
                        opacity = 0.8)

                        data.append(trace)
                        if(gpu!='NET1' and gpu!= 'NET2'):
                            layout = dict(
                                title= gpu+ '  LOSS PLOT'+" " +'daywise',
                                xaxis=dict(
                                    rangeselector=dict(
                                    buttons=list([
                                        dict(step='all')
                                    ])
                                ),
                                rangeslider=dict( visible=True),
                                
                                ),yaxis=dict(title='MW')
                            )
                        else:
                            layout = dict(
                                title= gpu+ '   PLOT'+" " +'daywise',
                                xaxis=dict(
                                    rangeselector=dict(
                                    buttons=list([
                                        dict(step='all')
                                    ])
                                ),
                                rangeslider=dict( visible=True),
                                
                                ),yaxis=dict(title='MW')
                            )   
                    fig = dict(data=data, layout=layout)
                    return(fig)
            
            
            

    #pathh="C:\\Users\\NARESH RAM\\Desktop\\NARESH_MASTER\\Master_naresh_prog_metering\\group_data or notmal from meter\\" # where schvsactaul data created
     

    srch=[{'label':lst2[i],'value':lst2[i]} for i in range (len(lst2))]
    #srch3=[{'label':'BAR','value':'BAR'},{'label':'PLOT','value':'PLOT'}]
    srch3=[{'label':'BAR','value':'BAR'},{'label':'PLOT','value':'PLOT'}]

    
    pp="" # this is where new excel created_data
    app = dash.Dash()
    app.layout =html.Div([
                html.Div([
                html.H1("Northern Region plot analysis"),html.P("Built for Metering department") ],
                style = {'text-align': 'center',"margin-left": "auto", "margin-right": "auto",'padding' : '20px' , 'backgroundColor' : '#1f77b4'}),

                    
                  
                html.Div([

                    dcc.Dropdown(
                                id = 'search',value=srch[0]['value'],
                                options=srch,
                                placeholder="Select plots",
                                style={"display": "block", "margin-left": "auto", 
                                        "margin-right": "auto", "width": "30%"}
                            ),                       
                    dcc.Dropdown(
                                id = 'search3',
                                options=srch3,value=srch3[0]['value'],
                                placeholder="select TYPE",
                                style={"display": "block", "margin-right": "auto", 
                                 "width": "20%"}
                            ),                 
            
            dcc.Graph(id ='plot',animate=False)])

                ])

    @app.callback(dash.dependencies.Output('plot', 'figure'),[dash.dependencies.Input('search', 'value'),dash.dependencies.Input('search3', 'value')])
    def multi_output(search,typ):
        
        df=pd.read_excel('Naresh_dir0.xlsx')
        
        return plotly_gropplot(df,search,typ)    

    app.run_server(debug=True, port=8945, use_reloader=False)  
    exit()
    return
runplot_loss()


