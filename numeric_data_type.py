# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series


  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isnull().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    return (self.serie == 0).sum()

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return (self.serie < 0).sum()

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.serie.mean()

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.serie.std()

  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.serie.max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.serie.median()

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """

    freq = self.serie.value_counts().reset_index()
    freq.columns = ['Values', 'Occurance']

    histogram = alt.Chart(freq).mark_bar().encode(
      x=alt.X('Values', title=self.col_name),
      y='Occurance')

    return st.altair_chart(histogram, use_container_width=True)

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    freq = self.serie.value_counts().reset_index()
    freq.columns = ['Values', 'Occurance']
    freq['Percentage'] = (freq['Occurance'] / freq['Occurance'].sum()) * 100

    return freq.head(20)
