import flask_task.process as process
import json
import flask_task.mnk as mnk
def form_data(n, pol):
    res=process.Processor.process(n,pol)
    n=int(n)
    pol=int(pol)
    r=[]
    for i in res:
        
        data={}
        data['bank']=i[3]
        data['labels']=i[0]
        data['options']={}
        data['datasets']=[]
        d1={}
        dar=[]
        for j in range(0, len(i[1])):
            temp={}
            temp['x']=i[1][j]
            temp['y']=i[0][j]
            dar.append((temp))
        d1['label']=i[4]+"_buy"
        d1['data']=dar
        d1['backgroundColor']='rgba(255,255,255,0)'
        d1['borderColor']='rgb(255, 99, 132)'
        data['datasets'].append(d1)
        d2={}
        dar=[]
        for j in range(0, len(i[2])):
            temp={}
            temp['x']=i[2][j]
            temp['y']=i[0][j]
            dar.append((temp))
        d2['label']=i[4]+"_sell"
        d2['data']=dar
        d2['backgroundColor']='rgba(255,255,255,0)'
        d2['borderColor']='rgb(200, 135, 232)'
        data['datasets'].append(d2)
        x_, y_,ineg=mnk.predict(i[1][-n:],i[0][-n:],pol)
        
        dar=[]
        for j in range(0, len(x_)):
            temp={}
            temp['x']=x_[j]
            temp['y']=y_[j]
            dar.append((temp))
        d3={}
        d3['label']=i[4]+"_buy_pred"
        d3['data']= dar
        d3['backgroundColor']='rgba(255, 99, 132, 0.5)'
        d3['borderColor']='rgba(255,255,255,0)'
        data['datasets'].append(d3)

        x_, y_,ineg=mnk.predict(i[2][-n:],i[0][-n:],pol)
        
        dar=[]
        for j in range(0, len(x_)):
            temp={}
            temp['x']=x_[j]
            temp['y']=y_[j]
            dar.append((temp))
        d4={}
        d4['label']=i[4]+"_sell_pred"
        d4['data']= dar
        d4['backgroundColor']='rgba(200, 135, 232, 0.5)'
        d4['borderColor']='rgba(255,255,255,0)'
        data['datasets'].append(d4)
        data['labels'].append(y_[-1])
        r.append(data)
    return r

