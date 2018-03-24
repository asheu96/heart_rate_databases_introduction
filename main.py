from pymodm import connect
import models
import datetime
import numpy

def add_heart_rate(email, heart_rate, time):

    """
    Adds heart rate data on to existing user
    :param email: str type parameter of specified user
    :param heart_rate: int type parameter of specified user
    :param time: 
    """
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user(email, age, heart_rate):

    """
    Creates user with email, age and heart_rate parameters and saves it within the database
    :param email: str type parameter of specified user, contains email address
    :param heart_rate: int type parameter of the heart rate of the specified user at a particular time
    :param age: int type parameter of the age of the specified user
    """
    u = models.User(email, age, [], []) # create a new User instance
    u.heart_rate.append(heart_rate) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database

def print_user(email):
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)

def findAvg(heartrate):

    """ Function that takes in an heartrate list as the input and computes the average HR of the heart_rate measurements
    :param heartrate: User list of heartrates under question
    :returns: average value of the heartrate measurements
    :raises TypeError: if given list of heartrates cannot be averaged (i.e. is not of the correct type)
    """

    try:
        average = numpy.mean(heartrate)
        return average
    except TypeError:
        print('given heartrate list contains elements that cannot be averaged')
        raise TypeError
        return None


def tachycardia(intervalAvg, age):

    """ Simple function that returns whether a patient will be diagnosed with tachcardia or not.
    The measure is as defined in https://books.google.com/books?id=s3UBLYEWUxwC&pg=PA93#v=onepage&q&f=false with
    the cut off being ab0ve 100 bpm for adults 
    :param intervalAvg: Average heart rate of a patient given the starting time to look at
    :param age: Age of the patient under question
    :returns: True if user is diagnosed with tachycardia
    :returns: False if user heart rate is in normal conditions
    :returns: None if intervalAvg is not float type of if age is not int type
    """

    if not isinstance(intervalAvg, float):
        print('Input interval average is not of float type')
        return None

    if not isinstance(age, int):
        print('Input age is not of int type')
        return None


    if intervalAvg > 100 and age >= 21:
        return True
    else:
        return False

