# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    Return the name of the selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return the number of  the unique values for a selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return the number of missing values for a selected column
    """
    return self.serie.isna().sum()

  def get_empty(self):
    """
    Return the number of rows with an empty string for a selected column
    Uses isnull() but might be better to sum over cells with length == 0 
    """
    return self.serie.isnull().sum()

  def get_whitespace(self):
    """
    Return the number of rows with only whitespaces for selected column
    """
    return self.serie.str.isspace().sum()

  def get_lowercase(self):
    """
    Return the number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    """
    Return the number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper().sum()

  def get_alphabet(self):
    """
    Return the number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha().sum()

  def get_digit(self):
    """
    Return the number of rows with only numbers as characters for selected column
    """
    return self.serie.str.isdigit().sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    If multiple modes occur, first value alphabetically is shown in app
    """
    return self.serie.mode()


  def get_barchart(self, col_name):
    """
    Return the generated bar chart for selected column  - bar chart is sorted

    Bar chart generated using altair
    Index is reset after counting in descending order
    Column names changed to required convention
    """

    df = self.serie.value_counts().reset_index()
    col_name = str(col_name)
    df.columns = [col_name, 'Count of Records']

    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X(col_name, sort=alt.EncodingSortField(field="Number of Occurances", op="count", order='ascending')),#'Value'
        y = alt.Y('Count of Records',axis=alt.Axis(tickMinStep=1)) # added tick
        )

    return st.altair_chart(chart, use_container_width=True)



  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    Table is descending by %
    """
    n = 20
    df = self.serie.value_counts().reset_index()
    df.columns = ['Value', 'Occurance']

    df['Percentage %'] = (df['Occurance'] / df['Occurance'].sum()) * 100

    return df.head(n)
