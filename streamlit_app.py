import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import streamlit as st

from data_overview import Dataset
from datetime_data_type import DateColumn
from numeric_data_type import NumericColumn
from text_data_type import TextColumn

#Function for adding the uploaded dataset to the webpage cache
@st.cache(allow_output_mutation=True)
def load_csv(csv_file):
    ds = Dataset(csv_file.name, pd.read_csv(csv_file))
    return ds

def launchApp():

    #Initialising containers
    header = st.container()
    data = st.container()
    numeric = st.container()
    text = st.container()
    date = st.container()

    #Page title Container
    with header:
        st.title('Data Explorer Web Application')
        st.write('This web app is designed to perform exploratory data analysis on a dataset (CSV files only) provided by the user. The analyses produce information in four key sections; the overall dataset, numeric data, text data and datetime data.')
        st.write(' ')

        #File uploader widget which is restricted to csv filetypes
        csv_file = st.file_uploader("Choose a CSV file", type=['csv'])

        #displaying uploaded file information
        if csv_file is not None:
            ds = load_csv(csv_file)


            with data:

                #Overall Information Header
                st.header('Summary Information')

                #Page display elements when a CSV file has been uploaded and is accessible

                #Displays the corresponding answers in standard text format through calls to dataclass elements.
                st.markdown('**Name of Table:** ' + ds.get_name())
                st.markdown('**Number of Rows:** ' + str(ds.get_n_rows()))
                st.markdown('**Number of Columns:** ' + str(ds.get_n_cols()))
                st.markdown('**Number of Duplicated Rows:** ' + str(ds.get_n_duplicates()))
                st.markdown('**Number of Rows with Missing Values:** ' + str(ds.get_n_missing()))

                st.markdown('**List of Columns:** ')

                column_names = list(ds.get_cols_list())

                bracketless_column_names = (', '.join(repr(e) for e in column_names))
                column_names_clean = bracketless_column_names.replace("'", "")
                st.text(column_names_clean)

                #Denotes the column types and displays the relevant information in a dataframe visual element
                st.markdown('**Type of Columns:** ')
                st.dataframe(ds.get_cols_dtype().astype(str), 400, 500)

                #Displays Row samples taken from the beginning, end and randomly from each respective visual element.
                #Implements a slider to determine how many dataframe rows should be displayed in each element.
                rowNumberSlider = st.slider('Select the number of rows to be displayed', value=5)
                st.markdown('**Top Rows of Table**')
                st.dataframe(ds.get_head(rowNumberSlider))
                st.markdown('**Bottom rows of Table**')
                st.dataframe(ds.get_tail(rowNumberSlider))
                st.markdown('**Random Sample Rows of Table**')
                st.dataframe(ds.get_sample(rowNumberSlider))

                #Implements a streamlit selectbox to select a column to be converted into datetime format
                #Utilises a button element to confirm conversion, followed an element rerun to display the converted elements.
                conversionSelect = st.selectbox('Which columns do you want to convert to dates', ds.get_cols_list())
                st.write('Current selection: ' + conversionSelect)
                convertButton = st.button('Convert Selected Column')
                if convertButton:
                    ds.df[conversionSelect] = pd.to_datetime(ds.df[conversionSelect].astype(str), infer_datetime_format=True)
                    st.experimental_rerun()


            with numeric:
                st.header('Information on each numeric column')


                num_select = st.selectbox('Select a numeric column to explore:', ds.get_numeric_columns())

                if num_select is not None:
                    st.markdown('')
                    st.markdown('**Field Name: *' + num_select + '* **')

                    num_serie = NumericColumn(num_select, ds.get_series(num_select))
                    text_col1, text_col2 = st.columns(2)

                    with text_col1:
                        st.write('Number of Unique Values:')
                        st.write('Number of Rows with Missing Values:')
                        st.write('Number of Rows with 0 Value:')
                        st.write('Number of Rows with Negative Value:')
                        st.write('Average Value:')
                        st.write('Std. Dev. Value:')
                        st.write('Minimum Value:')
                        st.write('Maximum Value:')

                    with text_col2:
                        st.write(num_serie.get_unique())
                        st.write(num_serie.get_missing())
                        st.write(num_serie.get_zeros())
                        st.write(num_serie.get_negatives())
                        st.write(num_serie.get_mean())
                        st.write(num_serie.get_std())
                        st.write(num_serie.get_min())
                        st.write(num_serie.get_max())

                    st.markdown('')
                    st.markdown('**Histogram: **')
                    num_serie.get_histogram()

                    st.markdown('')
                    st.markdown('**Top 20 Frequent Values**')
                    st.table(num_serie.get_frequent())


            with text:
                st.header('Text Column Information')

                '''
                Section allows for conversion of non string/text/object datatypes to string

                conversionSelect = st.selectbox('Which columns do you want to convert to text',ds.get_not_text_columns())
                st.write('Current selection: ' + conversionSelect)
                convertButton = st.button('Convert Selected Column to string')
                if convertButton:
                    ds.df[conversionSelect] = ds.df[conversionSelect].apply(str)
                    st.experimental_rerun()
                '''

                #i = 0
                #for col_name in ds.get_text_columns():
                    #st.markdown('')
                    #subheader_str = (f"3.{i} Field Name: _{col_name}_")
                    #st.subheader(subheader_str)
                text_select = st.selectbox('Select a text column to explore:', ds.get_text_columns())

                if text_select is not None:
                    st.markdown('')
                    st.markdown('**Field Name: *' + text_select + '* **')
                    #create the data series from the selected option

                    txt_serie = TextColumn(text_select, ds.get_series(text_select))

                    text_col1, text_col2 = st.columns(2)


                    with text_col1:

                        st.write('Number of Unique Values')
                        st.write('Number of Rows with Missing Values')
                        st.write('Number of Empty rows')
                        st.write('Number of Rows with only whitespaces')
                        st.write('Number of Rows with only lower case characters')
                        st.write('Number of Rows with only upper case characters')
                        st.write('Number of Rows with only alphabet characters')
                        st.write('Number of rows with only numbers as characters')
                        st.write('Mode value')

                    with text_col2:

                        st.write(txt_serie.get_unique())
                        st.write(txt_serie.get_missing())
                        st.write(txt_serie.get_empty())
                        st.write(txt_serie.get_whitespace())
                        st.write(txt_serie.get_lowercase())
                        st.write(txt_serie.get_uppercase())
                        st.write(txt_serie.get_alphabet())
                        st.write(txt_serie.get_digit())
                        st.write(txt_serie.get_mode()[0])

                    st.markdown('')
                    st.markdown('**Bar Chart**')
                    txt_serie.get_barchart(text_select)

                    st.markdown('')
                    st.markdown('**Most Frequent Values**')
                    st.table(txt_serie.get_frequent())

                    #i = i+1

            with date:
                st.header('Information on each datetime column')

                #check if csv has been loaded. Only display this section if csv_file is not None.


                option = st.selectbox('Select a <Datetime> column to explore:', ds.get_date_columns())

                #check if a datetime colum has been selected
                if option is not None:
                    st.markdown('')
                    st.markdown('**Field Name: *' + option + '* **')
                    #create the data series from the selected option
                    date_serie = DateColumn(option, ds.get_series(option))


                    #print table of basic information for this column
                    date_col1, date_col2 = st.columns(2)

                    with date_col1:
                        st.write('Number of Unique Values:')
                        st.write('Number of Rows with Missing Values:')
                        st.write('Number of Weekend Dates:')
                        st.write('Number of Weekday Dates:')
                        st.write('Number of Dates in Future:')
                        st.write('Number of Rows with 1900-01-01:')
                        st.write('Number of Rows with 1970-01-01:')
                        st.write('Minimum Value:')
                        st.write('Maximum Value:')

                    #call datetime information from datetime functions
                    with date_col2:
                        st.write(date_serie.get_unique())
                        st.write(date_serie.get_missing())
                        st.write(date_serie.get_weekend())
                        st.write(date_serie.get_weekday())
                        st.write(date_serie.get_future())
                        st.write(date_serie.get_empty_1900())
                        st.write(date_serie.get_empty_1970())
                        st.write(date_serie.get_min())
                        st.write(date_serie.get_max())

                    st.markdown('')
                    st.markdown('**Bar Chart**')
                    date_serie.get_barchart()


                    st.markdown('')
                    st.markdown('**Most Frequent Values**')
                    st.table(date_serie.get_frequent())


    return


if __name__ == '__main__':
    launchApp()
