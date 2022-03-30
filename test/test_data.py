# To be filled by students
import unittest

from pandas.core.frame import DataFrame
from .. import data
import pandas as pd

df = pd.read_csv('Test_Dataset.csv')
ds = data.Dataset('Test_Dataset.csv', df)
class TestData(unittest.TestCase):



    def test_get_name(self):

        result = ds.get_name()
        expected = df.name


        self.assertEqual(result, expected)

    def test_get_n_rows(self):

        result = ds.get_n_rows()
        expected = df.shape[0]

        self.assertEqual(result, expected)


    def test_get_n_cols(self):

        result = ds.get_n_cols()
        expected = df.shape[1]

        self.assertEqual(result, expected)


    def test_get_cols_list(self):

        result = ds.get_cols_list()
        expected = list(df.columns)

        self.assertEqual(result, expected)


    def test_get_cols_dtype(self):

        result = ds.get_cols_dtype()
        expected = df.dtypes

        self.assertEqual(result, expected)


    def test_get_n_duplicates(self):

        result = ds.get_n_duplicates()
        expected = len(df[df.duplicated() == True])

        self.assertEqual(result, expected)


    def test_get_n_missing(self):

        result = ds.get_n_missing()
        expected = df.isnull().any(axis=1).sum()

        self.assertEqual(result, expected)


    def test_get_head(self):

        self.assertEqual(ds.get_head(0), df.head(0))
        self.assertEqual(ds.get_head(), df.head())
        self.assertEqual(ds.get_head(10), df.head(10))


    def test_get_tail(self):

        self.assertEqual(ds.get_tail(0), df.tail(0))
        self.assertEqual(ds.get_tail(), df.tail())
        self.assertEqual(ds.get_tail(10), df.tail(10))


    def test_get_sample(self):

        self.assertEqual(ds.get_sample(0), df.sample(0))
        self.assertEqual(ds.get_sample(), df.sample())
        self.assertEqual(ds.get_sample(10), df.sample(10))


    def test_get_numeric_columns(self):

        result = ds.get_numeric_columns()
        expected = self.df.select_dtypes(include='number').columns.to_list()

        self.assertEqual(result, expected)


    def test_get_text_columns(self):

        result = ds.get_text_columns()
        expected = self.df.select_dtypes(include='object').columns.to_list()

        self.assertEqual(result, expected)


    def test_get_date_columns(self):

        result = ds.get_date_columns()
        expected = self.df.select_dtypes(include='datetime').columns.to_list()

        self.assertEqual(result, expected)
