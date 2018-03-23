from flask import Flask, jsonify, request
from pymodm import connect, MongoModel, fields
from models import *
from main import *
import datetime, numpy

app = Flask(__name__)
connect("mongodb://vcm-3579.vm.duke.edu:27017/heart_rate_app")

@app.route('/api/heart_rate/<email>', methods=['GET'])
def userHR(email):

        """ Function is a GET request that allows us to access the heartrate of the requested email address if it exists
        :param email: Email address of the person whose heart rate we want to obtain
        :returns: jsonified data that contains the heart rate of user if user exists - else, tells user that specified user does not exist
        """
        
        mail = "{0}".format(email)
        print(mail)
        try:
                u = models.User.objects.raw({"_id": mail}).first()
                data = {"Heart Rate": str(u.heart_rate)}
        except:
                print('User does not exist')
                data = {"Heart Rate": 'User does not exist'}
                return jsonify(data), 404

        # if user tries to access a user that does not exist, returns a page that tells them the user doesn't exist
        return jsonify(data), 200

@app.route('/api/heart_rate/average/<email>', methods=['GET'])
def avgUserHR(email):

        """ Function is a GET request that allows us to access the average heart rate of the requested email address if it exists
        :param email: Email address of the person whose heart rate we want to obtain
        :returns: HTTP code 404 if user cannot be found within the database
        :returns: HTTP code 200 and jsonified average heart rate if average specified user HR is successfully calculated/obtains
        """
        mail = "{0}".format(email)
        try:
                user = models.User.objects.raw({"_id": email}).first()
                avgHR = findAvg(user.heart_rate)
                data = {"Avg Heart Rate": avgHR}
        except:
                print('User does not exist')
                data = {"Avg Heart Rate": 'User does not exist'}
                return jsonify(data), 404

        return jsonify(data), 200

@app.route('/api/heart_rate', methods=['POST'])
def postHR():

        """ Function is a POST method that allows us to add heart_rate measurements to selected user. If user does not exist, creates the new user
        :returns: HTTP code 400 if inputs are not of the correct types or if input fields are generally incorrect
        :returns: HTTP code 200 if a new user has been successfully created or if a heartrate has been appended to existing user
        """
        r = request.get_json()
        try:
                email = r['user_email']
                age = r['user_age']
                HR = r['heart_rate']

        except:
                return 'Input fields are incorrect, double check before re-requesting', 400

        if not isinstance(email, str):
                return 'Email input must be a string, please reinput', 400

        if not isinstance(age, int):
                return 'Age must be an int (in years), please reinput', 400

        if not isinstance(HR, int):
                return 'Heartrate must be an int, please reinput', 400


        time = datetime.datetime.now()

        try:
                add_heart_rate(email, HR, time)
                return 'Heartrate has been successfully added', 200
                
        except:
                print('User not found, creating new user')
                create_user(email, age, HR)
                return 'User has been created', 200


@app.route('/api/heart_rate/interval_average', methods=['POST'])
def postAvg():

        """ Function is a POST method that allows us to post an email and a timeSince parameter. Calculates the average
        heart rate since the given input time.
        :returns: 
        """

        r = request.get_json()

        try:
                email = r['user_email']
                timeSince = r['heart_rate_average_since']
                

        except:
                return 'Input fields are incorrect, double check before re-requesting', 400

        if not isinstance(email, str):
                return 'Email input must be a string, please reinput', 400

        try:
                timeStrip = datetime.datetime.strptime(timeSince, "%Y-%m-%d %H:%M:%S.%f")
        except:
                'Input time not of correct format', 400

        
                      
        try:
                u = models.User.objects.raw({'_id': email}).first()
                for count, elem in enumerate(u.heart_rate_times):
                        if elem > timeStrip:
                                break
                # goes up until the last time that is less than the given time
                avgHR = numpy.mean(u.heart_rate[count::])
                tac = tachycardia(avgHR, u.age)
                data = {"user_email": email, "heart_rate_average_since": timeSince, 'heart_rate_average': avgHR,'tachycardia': tac}
                return jsonify(data), 200

        except:
                return 'User not found', 404

