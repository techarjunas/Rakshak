from firebase import firebase
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from twilio.rest import Client
import requests
import heatmapgenerated
from heatmapgenerated import *
from flask import send_file


firebase = firebase.FirebaseApplication("https://rakshaksih.firebaseio.com/", None)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




 





@app.route('/hello',methods=['POST'])
@cross_origin()
def hello():
   
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    # Category = request.form.get('location_victim')
    info = request.form.to_dict()
    print(info)

    c = info['location']
    d = "https://www.google.com/maps/search/?api=1&query="+c
    a= info['username'] + " needs help and is currently present  at " + d
    b = info['emergency1']
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"jPCJ9YOmIHtgKFAc4kBilbXUSe8WDrsM31yfRVnp2QaqZLxT0EN4c2X6BpWGmjAbualF9Pq3JigkYrw1","sender_id":"FSTSMS","message":a,"language":"english","route":"p","numbers":b}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    {
        "request_id": "vrc5yp9k4sfze6t",
        "message": [
            "Message sent successfully"
        ]
    }
    return ("successful")








@app.route('/hellowithoutsignin',methods=['POST'])
@cross_origin()
def hellow():
   
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    # Category = request.form.get('location_victim')
    info = request.form.to_dict()
    print(info)

    c = info['location']
    d = "https://www.google.com/maps/search/?api=1&query="+c
    a= "Someone" + " needs help and is present  at " + d
    b = "7014020949"
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"jPCJ9YOmIHtgKFAc4kBilbXUSe8WDrsM31yfRVnp2QaqZLxT0EN4c2X6BpWGmjAbualF9Pq3JigkYrw1","sender_id":"FSTSMS","message":a,"language":"english","route":"p","numbers":b}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    {
        "request_id": "vrc5yp9k4sfze6t",
        "message": [
            "Message sent successfully"
        ]
    }
    return ("successful")


# send alert to all registered users


@app.route('/SendAlert_ToAll',methods=['POST'])
@cross_origin()
def send():
   
    def msg(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    # Category = request.form.get('alertflask')
    info = request.form.to_dict('alerttobesent')
    print(info['alerttobesent'])

    data = firebase.get('users','')
    registered_users = ""
    for i in data:
    # for y in data[i] :
        z = str(data[i]['regnumber'] +',') 
        registered_users = registered_users + z
    print (registered_users)

    # sending alert msg requested from admin

    a= info['alerttobesent']
    b = str(registered_users)
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"jPCJ9YOmIHtgKFAc4kBilbXUSe8WDrsM31yfRVnp2QaqZLxT0EN4c2X6BpWGmjAbualF9Pq3JigkYrw1","sender_id":"FSTSMS","message":a,"language":"english","route":"p","numbers":b}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    {
    # "return": true,
        "request_id": "vrc5yp9k4sfze6t",
        "message": [
            "Message sent successfully"
        ]
    }

    return ("sent messages")



@app.route('/generateheatmap',methods=['GET'])
@cross_origin()
def mapgenerate():
   
    def generate_map(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


    generate_heat_map()
    


    safe_path = "myplot.png"
        
    # Category = request.form.get('location_victim')
    # return ("successful")
    return send_file(safe_path, as_attachment=True)








if __name__ == '__main__':
 
    app.run(host='0.0.0.0', port=8000)