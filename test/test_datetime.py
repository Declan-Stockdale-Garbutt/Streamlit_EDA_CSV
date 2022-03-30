import unittest
import pandas as pd
import numpy as np

#import path and sys to link the parent 'src' directory to the PYTHONPATH. This allows the import of datetime.py
import path
import sys
directory = path.Path(__file__).abspath()
#note: path has to go up one further level, as datetime.py is a standard py library. To avoid importing the wrong library, need to reference 'src.datetime'
sys.path.append(str(directory.parent.parent.parent))
# ---

from src.datetime import DateColumn

class TestDateTime(unittest.TestCase):
	def test_get_name(self):
		name = 'Date'
		series = pd.Series(pd.date_range("1/1/2021", freq="D", periods=3))
		dc = DateColumn(name, series)

		self.assertEqual('Date', dc.get_name())


	def test_get_unique(self):
		name = 'Date'
		expected_unique = 4
		s1 = pd.Series(pd.date_range("1/1/2021", freq="D", periods=3))
		s2 = pd.Series(pd.date_range("1/2/2021", freq="D", periods=3))
		s3 = pd.concat([s1, s2])
		dc = DateColumn(name, s3)

		self.assertEqual(expected_unique,dc.get_unique())


	def test_get_missing(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("1/1/2021", freq="D", periods=3))
		s2 = pd.Series([np.NaN, np.NaN])
		s3 = pd.Series(pd.date_range("1/4/2021", freq="D", periods=3))
		s4 = pd.concat([s1, s2, s3])
		dc = DateColumn(name, s4)
		expected = 2

		self.assertEqual(expected, dc.get_missing())


	def test_get_weekend_present(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("11/1/2021", freq="D", periods=22))
		dc = DateColumn(name, s1)
		expected = 6

		self.assertEqual(expected, dc.get_weekend())

	def test_get_weekend_na(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("11/1/2021", freq="D", periods=3))
		dc = DateColumn(name, s1)
		expected = 0

		self.assertEqual(expected, dc.get_weekend())

	def test_get_weekday(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("11/1/2021", freq="D", periods=22))
		dc = DateColumn(name, s1)
		expected = 16

		self.assertEqual(expected, dc.get_weekday())

	def test_get_future_present(self):
		name = 'Date'
		today = pd.to_datetime("today")
		s1 = pd.Series(pd.date_range(today, freq="D", periods=5))
		dc = DateColumn(name, s1)
		expected = 4

		self.assertEqual(expected, dc.get_future())

	def test_get_future_na(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("1/1/2011", freq="D", periods=5))
		dc = DateColumn(name, s1)
		expected = 0

		self.assertEqual(expected, dc.get_future())

	def test_get_empty_1900(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("1/1/2021", freq="D", periods=3))
		s2 = pd.Series(pd.date_range("1/1/1900", freq="D", periods=1))
		s3 = pd.Series(pd.date_range("1/4/2021", freq="D", periods=3))
		s4 = pd.concat([s1, s2, s3, s2, s2])
		dc = DateColumn(name, s4)
		expected = 3

		self.assertEqual(expected, dc.get_empty_1900())

	def test_get_empty_1970(self):
		name = 'Date'
		s1 = pd.Series(pd.date_range("1/1/2021", freq="D", periods=3))
		s2 = pd.Series(pd.date_range("1/1/1900", freq="D", periods=1))
		s3 = pd.Series(pd.date_range("1/4/2021", freq="D", periods=3))
		s4 = pd.Series(pd.date_range("1/1/1970", freq="D", periods=1))
		s5 = pd.concat([s1, s2, s4, s2, s4, s3])
		dc = DateColumn(name, s5)
		expected = 2

		self.assertEqual(expected, dc.get_empty_1900())


if __name__ == '__main__':
    unittest.main()
