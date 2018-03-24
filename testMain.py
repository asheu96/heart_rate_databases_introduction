import pytest
import models
import datetime

def test_findAvg():

        """ Function that tests the findAvg function in main.py
        """
        from main import findAvg
        data1 = [100, 200, 120, 30, 50, 60, 80]
        data2 = [200, 134, 12, 234, 25]
        data3 = [82, 62, 67, 72, 88]
        averages = [91.43, 121, 74.2]
        assert findAvg(data1) == pytest.approx(91.43)
        assert findAvg(data2) == pytest.approx(121)
        assert findAvg(data3) == pytest.approx(74.2)

        data4 = ['a', 'b', 'c']
        assert findAvg(data4) == None

def test_tachycardia():

        """ Function that tests the tachycardia function in main.py
        """
        from main import tachycardia
        assert tachycardia(120.022, 25) == True
        assert tachycardia(80.452, 21) == False
        assert tachycardia(200.123, 15) == False

        assert tachycardia('hello', 'hi') == None
        assert tachycardia(120.452, 'fail') == None


def test_createUser():

        """ Function that tests whether createUser function from main is working properly
        """

        from main import create_user
        email = 'myname@duke.edu'
        age = 21
        heart_rate = 75
        time = datetime.datetime(2018, 3, 23, 19, 0, 0, 000000)
        create_user(email, age, heart_rate, time)
        user = models.User.objects.raw({"_id": "myname@duke.edu"}).first()
        assert user.email == 'myname@duke.edu'
        assert user.age == 21
        assert user.time = [time]
        assert user.heart_rate = [75]
 

def test_addHR():

        """ Function that tests whether add heart rate is functioning properly
        """

        from main import create_user, add_heart_rate
        email = 'test2@duke.edu'
        age = 21
        heart_rate = 75
        time = datetime.datetime(2018, 3, 23, 19, 0, 0, 000000)
        create_user(email, age, heart_rate, time)
        HR2 = 72
        time2 = datetime.datetime(2018, 3, 23, 20, 0, 0, 000000)
        add_heart_rate(email, HR2, time2)

        user = models.User.objects.raw({"_id": email}).first()
        assert user.email == 'test2@duke.edu'
        assert user.age == 21
        assert user.time = [time, time2]
        assert user.heart_rate = [heart_rate, HR2]




