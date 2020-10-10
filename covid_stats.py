import requests , json
from flask import jsonify , make_response ,Flask, request
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

# our 3 functions

def convert_to_list_diff(lst): #get a list of diffrences
    lst2=[]
    for i in range(1,len(lst)): 
         lst2.append(lst[i]-lst[i-1])
    return lst2 

def dict_key_to_list(dict): #method to convert dictionary to list of its keys
   temp = dict. keys()
   keys_list = list(temp)
   return keys_list

def dict_val_to_list(dict): #method to convert dictionary to list of its values
   temp = dict. values()
   values_list = list(temp)
   return values_list

#end functions

@app.errorhandler(HTTPException) #an error handler for a users wrong input
def handle_exception(e):
    response=e.get_response()
    response.data = json.dumps({

    })
    response.content_type="application/json"
    return response


@app.route('/quit') #method to stop the service
def quit():
    shutdown_hook = request.environ.get('werkzeug.server.shutdown')
    if shutdown_hook is not None:
        shutdown_hook()
        return "Bye"
    return "No shutdown hook"


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

    lst=[] #make a list in order to copy all the values of Recovered
    lst2=[] #make a new list to store the differences
    lst3=[] #list to store the dates

    lst = dict_val_to_list(json_data["timeline"]["recovered"])
    lst3 = dict_key_to_list(json_data["timeline"]["recovered"])
    
    lst2=convert_to_list_diff(lst)

    return jsonify({'country' : country , 'method' : 'newCasesPeak' , 'date' : str(lst3[lst2.index(max(lst2))+1]) , 'value' : max(lst2)}) #return a json format with the details requested

@app.route("/recoveredPeak") # our 2nd ,method.
def recoveredpeak():
    country=request.args.get("country") #let the user pick a country
    parameters={'lastdays' : '31'}
    r=requests.get('https://disease.sh/v3/covid-19/historical/{}'.format(country), params=parameters)
    json_data=r.json()

    lst=[] #make a list in order to copy all the values of Recovered
    lst2=[] #make a new list to store the differences
    lst3=[] #list to store the dates

    lst = dict_val_to_list(json_data["timeline"]["recovered"])
    lst3 = dict_key_to_list(json_data["timeline"]["recovered"])
    
    lst2=convert_to_list_diff(lst)

    return jsonify({'country' : country , 'method' : 'recoveredPeak' , 'date' : str(lst3[lst2.index(max(lst2))+1]) , 'value' : max(lst2)}) #return a json format with the details requested

@app.route("/deathsPeak") # our 3rd ,method.
def deathspeak():
    country=request.args.get("country") #let the user pick a country
    parameters={'lastdays' : '31'}
    r=requests.get('https://disease.sh/v3/covid-19/historical/{}'.format(country), params=parameters)
    json_data=r.json() #parse the data into a json

    lst=[] #make a list in order to copy all the values of Recovered
    lst2=[] #make a new list to store the differences
    lst3=[] #list to store the dates

    lst = dict_val_to_list(json_data["timeline"]["recovered"])
    lst3 = dict_key_to_list(json_data["timeline"]["recovered"])
    
    lst2=convert_to_list_diff(lst)

    return jsonify({'country' : country , 'method' : 'deathsPeak' , 'date' : str(lst3[lst2.index(max(lst2))+1]) , 'value' : max(lst2)}) #return a json format with the details requested
    
if __name__== "__main__" : 
    app.run()