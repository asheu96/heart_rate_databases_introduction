import pytest

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

def test_tachycardia

        """ Function that tests the tachycardia function in main.py
        """
        from main import tachycardia
        assert tachycardia(120.022, 25) == True
        assert tachycardia(80.452, 21) == False
        assert tachycardia(200.123, 15) == False

        assert tachycardia('hello', 'hi') == None
        assert tachycardia(120.452, 'fail') == None





