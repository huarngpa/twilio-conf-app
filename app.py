import os
from flask import Flask, flash, redirect, render_template, request, session, abort
from twilio.rest import Client
import re

app = Flask(__name__)

# Better security practices, making env variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route("/")
def index():
    return render_template('index.html'), 200

@app.route("/service", methods=['POST'])
def receive_order():
    event_json = request.get_json()
    # print(event_json)
    to_number = event_json['to_number']
    conf_num = event_json['conf_num']
    passcode_1 = event_json['passcode_1']
    passcode_2 = event_json['passcode_2']
    body_msg = ''
    if re.search(r"^\+1[0-9]{10}", to_number) == None:
        return '', 500
    if re.search(r"^\+1[0-9]{10}", conf_num) == None:
        return '', 500
    else:
        body_msg += conf_num
    if len(passcode_1) > 0:
        body_msg += ',,'+passcode_1+'#'
    if len(passcode_2) > 0:
        body_msg += ',,'+passcode_2+'#'
    message = client.messages.create(
        to=to_number,
        from_=os.environ['TWILIO_NUMBER'],
        body='Join the conference: '+body_msg
    )
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
