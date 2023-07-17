import unittest
import Main_Script
class Testadd(unittest.TestCase):
    def test_value(self):
        from Main_Script import get_user_value
        assert get_user_value()

    def test_result(self):
        import class_ILS
        a = class_ILS.ILS.calculate(5)
        assert a == 1.4000000000000001

    def test_file(self):
        lise_result = Main_Script.third_screen(5)
        results_file = open('/Users/kfirzand/PycharmProjects/First_Project/results_list.txt', 'r')
        content = results_file.read()
        assert content == str(lise_result)
        results_file.close()
