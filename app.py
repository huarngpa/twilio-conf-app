import os
from flask import Flask, flash, redirect, render_template, request, session, abort
from twilio.rest import Client


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
    to_number = event_json['']
    message = client.messages.create(
        to='+12487198316',
        from_=os.environ['TWILIO_NUMBER'],
        body='hello, world!'
    )
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
