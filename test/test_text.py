import unittest
import pandas as pd
import numpy as np
import path
import sys
directory = path.Path(__file__).abspath
sys.path.append(str(directory.parent.parent.parent))

from src.text import TextColumn

test_csv = "C:/Users/Declan/Downloads/food-consumption.csv"
df = pd.read_csv(test_csv)
ds = data.Dataset(test_csv,df)

class TextColumn(unittest.TestCase):

     def test_get_name(self):
         """
         test get name returns expected value
         """

         result = ds.get_name()
         expected = df.col_name

         self.assertEqual(result, expected)


     def test_get_unique(self):
         """
         test get unqiue returns expected value
         """
         result = ds.get_unique()
         expected = df.serie.nunique()

         self.assertEqual(result, expected)

     def test_get_missing(self):
         """
         test get missing returns expected value
         """
         result = ds.get_missing()
         expected = df.isna().sum()

         self.assertEqual(result, expected)

     def test_get_empty(self):
         """
         test get empty returns expected value
         """
         result = ds.get_empty()
         expected = df.isnull().sum()

         self.assertEqual(result, expected)

     def test_get_whitespace(self):
         """
         test get whitespace returns expected value
         """
         result = ds.get_whitespace()
         expected = df.str.isspace().sum()

         self.assertEqual(result, expected)

     def test_get_lowercase(self):
         """
         test get lowecase returns expected value
         """
         result = ds.get_lowercaase()
         expected = df.str.islower().sum()

         self.assertEqual(result, expected)

     def test_get_uppercase(self):
         """
         test get uppercase returns expected value
         """
         result = ds.get_uppercase()
         expected = df.str.isupper().sum()

         self.assertEqual(result, expected)

     def test_get_alphabet(self):
         """
         test get alphabet returns expected value
         """
         result = ds.get_alphabet()
         expected = df.str.isalpha().sum()

         self.assertEqual(result, expected)

     def test_get_digit(self):
         """
         test get digit returns expected value
         """
         result = ds.get_digit()
         expected = df.str.isdigit().sum()

         self.assertEqual(result, expected)


     def test_get_mode(self):
         """
         test get mode returns a mode
         """
         result = df.get_mode()
         expected = ds.mode()

         self.assertEqual(result, expected)


     def test_get_barchart(self, col_name):
         """
         testin bar chart returns object with string matching expected
         """
         result = str(type(get_barchart()))
         expected = str("<class 'altair.vegalite.v4.api.Chart'>")

         self.assertEqual(result, expected)

     def test_get_frequent(self):
         """
         test head values are the same
         """
        self.assertEqual(ds.get_head(), df.head())


if __name__ == '__main__':
    unittest.main()
