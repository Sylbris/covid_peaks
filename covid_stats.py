import requests , json
from flask import jsonify , make_response ,Flask, request
from datetime import datetime,timedelta


app = Flask(__name__)

@app.route("/status")
def status_check():
    status=requests.get('https://disease.sh/')
    if status.ok :
        return jsonify({'status : ' : 'Success'})
    else :
        return jsonify({'status : ' : 'failed'})

@app.route("/newCasesPeak") # our 1st ,method.
def newcasespeak():
    country=request.args.get("country") #let the user pick a country
    parameters={'lastdays' : '31'}
    r=requests.get('https://disease.sh/v3/covid-19/historical/{}'.format(country), params=parameters)
    json_data=r.json()
    lst=[] #make a list in order to copy all the values of the cases
    for i in json_data["timeline"]["cases"].values(): #copy the values into list
        lst.append(i)
    lst2=[] #make a new list to store the differences
    for i in range(1,len(lst)): #finding the largest diffrence the list
         lst2.append(lst[i]-lst[i-1])
    newdate=datetime.now()-timedelta(days=lst2.index(max(lst2))) #get the current date and subtract the index of the maximum value
    newdate=datetime.strftime(newdate, "%m/%d/%Y") #fomrmat the date to convinient display
    return jsonify({'country' : country , 'method' : 'newCasesPeak' , 'date' : str(newdate) , 'value' : max(lst2)}) #return a json format with the details requested

@app.route("/recoveredPeak") # our 2nd ,method.
def recoveredpeak():
    country=request.args.get("country") #let the user pick a country
    parameters={'lastdays' : '31'}
    r=requests.get('https://disease.sh/v3/covid-19/historical/{}'.format(country), params=parameters)
    json_data=r.json()
    lst=[] #make a list in order to copy all the values of Recovered
    lst2=[] #make a new list to store the differences
    lst3=[] #list to store the dates
    for i in json_data["timeline"]["recovered"].values(): #copy the values into list
        lst.append(i)
    for i in json_data["timeline"]["recovered"].keys(): #store the keys
        lst3.append(i)
    for i in range(1,len(lst)): #get a list of diffrences
         lst2.append(lst[i]-lst[i-1])

    #newdate=datetime.now()-timedelta(days=lst2.index(max(lst2))) #get the current date and subtract the index of the maximum value
    #newdate=datetime.strftime(newdate, "%m/%d/%Y") #fomrmat the date to convinient display

    return jsonify({'country' : country , 'method' : 'recoveredPeak' , 'date' : str(lst3[lst2.index(max(lst2))+1]) , 'value' : max(lst2)}) #return a json format with the details requested

@app.route("/deathsPeak") # our 3rd ,method.
def deathspeak():
    country=request.args.get("country") #let the user pick a country
    parameters={'lastdays' : '31'}
    r=requests.get('https://disease.sh/v3/covid-19/historical/{}'.format(country), params=parameters)
    json_data=r.json()
    lst=[] #make a list in order to copy all the values of the cases
    for i in json_data["timeline"]["deaths"].values(): #copy the values into list
        lst.append(i)
    lst2=[] #make a new list to store the differences
    for i in range(1,len(lst)): #finding the largest diffrence the list
         lst2.append(lst[i]-lst[i-1])
    newdate=datetime.now()-timedelta(days=lst2.index(max(lst2))) #get the current date and subtract the index of the maximum value
    newdate=datetime.strftime(newdate, "%m/%d/%Y") #fomrmat the date to convinient display
    return jsonify({'country' : country , 'method' : 'deathsPeak' , 'date' : str(newdate) , 'value' : max(lst2)}) #return a json format with the details requested
    
if __name__== "__main__" : 
    app.run()