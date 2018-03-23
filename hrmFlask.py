from flask import Flask, jsonify, request
from pymodm import connect
from pymodm import MongoModel, fields
from models import *
from main import *
import datetime
import numpy

app = Flask(__name__)
connect("mongodb://vcm-3579.vm.duke.edu:27017/heart_rate_app")

@app.route('/api/heart_rate/<email>', methods=['GET'])
def userHR(email):

        """ Function is a GET request that allows us to access the heartrate of the requested email address if it exists
        :param email: Email address of the person whose heart rate we want to obtain
        :returns: jsonified data that contains the heart rate of user if user exists - else, tells user that specified user does not exist
        """
        mail = '{0}'.format(email)
        try:
                u = User.objects.raw({'_id': mail}).first()
                data = {"Heart Rate": str(u.heart_rate)}
        except:
                print('User does not exist')
                data = {"Heart Rate": 'User does not exist'}

        # if user tries to access a user that does not exist, returns a page that tells them the user doesn't exist
        
        return jsonify(data)

@app.route('/api/heart_rate/average/<email>', methods=['GET'])
def avgUserHR(email):

        """ Function is a GET request that allows us to access the average heart rate of the requested email address if it exists
        :param email: Email address of the person whose heart rate we want to obtain
        :returns: jsonified data that contains the average heart rate of user if user exists - else, tells user that specified user does not exists
        """
        mail = '{0}'.format(email)
        try:
                u = User.objects.raw({'_id': mail}).first()
                hrData = u.heart_rate
                sum = numpy.sum(hrData)
                # sums the heart rate data
                avgHR = double(sum)/double(hrData)
                # gets the average

                data = {"Avg Heart Rate": avgHR}
        except:
                print('User does not exist')
                data = {"Avg Heart Rate": 'User does not exist'}

        return jsonify(data)

@app.route('/api/heart_rate', methods=['POST'])
def postHR():

        """ Function is a POST method that allows us to add heart_rate measurements to selected user. If user does not exist, creates the new user
        """
        r = request.get_json()
        email = r['user_email']
        age = r['user_age']
        HR = r['heart_rate']
        time = datetime.datetime.now()

        try:
                u = User.objects.raw({'id': email}).first()
                add_heart_rate(email, HR, time)
                data = {'user_email': u.email, 'user_age': u.age, 'heart_rate': u.heart_rate, 'time': time}

        except:
                print('User not found, creating new user')
                create_user(email, age, HR)
                data = {'user_email': email, 'user_age': age, 'heart_rate': HR, 'time': time}

        return jsonify(data)
