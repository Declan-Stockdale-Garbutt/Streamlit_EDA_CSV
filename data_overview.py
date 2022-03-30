# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
  name: str
  df: pd.DataFrame

  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return self.df.shape[0]

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return self.df.shape[1]

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return list(self.df.columns)

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return self.df.dtypes

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return len(self.df[self.df.duplicated() == True])

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return self.df.isnull().any(axis=1).sum()

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.head(n)

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.tail(n)

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    return self.df.select_dtypes(include='number').columns.to_list()

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return self.df.select_dtypes(include='object').columns.to_list()

  def get_not_text_columns(self): # used to only display non text types to convert to text
    """
      Return list column names of everything else but object/text type from loaded dataset
    """
    return self.df.select_dtypes(exclude='object').columns.to_list()

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return self.df.select_dtypes(include='datetime').columns.to_list()

  def get_series(self, col_name):
    return self.df[col_name].squeeze()
