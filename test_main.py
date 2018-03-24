import pytest
import models
import datetime
from pymodm import connect

connect("mongodb://vcm-3579.vm.duke.edu:27017/heart_rate_app")

def test_findAvg():

        """ Function that tests the findAvg function in main.py
        """
        from main import findAvg
        data1 = [100, 200, 120, 30, 50, 60, 80]
        data2 = [200, 134, 12, 234, 25]
        data3 = [82, 62, 67, 72, 88]
        assert findAvg(data1) == pytest.approx(91.42857)
        assert findAvg(data2) == pytest.approx(121)
        assert findAvg(data3) == pytest.approx(74.2)

        data4 = ['a', 'b', 'c']
        with pytest.raises(TypeError):
            findAvg(data4)

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
        create_user(email, age, heart_rate)
        user = models.User.objects.raw({"_id": "myname@duke.edu"}).first()
        assert user.email == 'myname@duke.edu'
        assert user.age == 21
        assert user.heart_rate == [75]
 

def test_addHR():

        """ Function that tests whether add heart rate is functioning properly
        """

        from main import create_user, add_heart_rate
        email = 'test2@duke.edu'
        age = 21
        heart_rate = 75
        create_user(email, age, heart_rate)
        HR2 = 72
        time2 = datetime.datetime(2018, 3, 23, 20, 0, 0, 000000)
        add_heart_rate(email, HR2, time2)

        user = models.User.objects.raw({"_id": email}).first()
        assert user.email == 'test2@duke.edu'
        assert user.age == 21
        assert user.heart_rate == [heart_rate, HR2]




