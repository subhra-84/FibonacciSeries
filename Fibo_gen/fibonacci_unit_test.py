import fibonacci_Series
import unittest


class TestFibonacciSeries(unittest.TestCase):
    def Test_1(self):
        expected_result=[0,1,1,2,3]
        test_result=fibonacci_Series.fibonacciSeries(5)

        self.assertEqual(expected_result,test_result)
    def Test_2(self):
        expected_result=[]
        test_result=fibonacci_Series.fibonacciSeries(0)
        self.assertEqual(expected_result,test_result)

    def Test_2(self):
        expected_result=[0]
        test_result=fibonacci_Series.fibonacciSeries(1)
        self.assertEqual(expected_result,test_result)


if __name__== '__main__':
    unittest.main()