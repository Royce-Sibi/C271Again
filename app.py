from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC0e99256697bbcea8c4a142f9bab25523'
    TWILIO_SYNC_SERVICE_SID = 'ISa109dd2c9e372aefa8f92b7d4a5c5997'
    TWILIO_API_KEY = 'SKed9389b1aa6180e3708381275dbfb6f9'
    TWILIO_API_SECRET = '8ioBl5lAE4QCYRA8svC0kkhwUJKPfWM2'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(host='0.0.0.0')

