import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = './Assets/Appeals_Filed_In_2017.csv'
version = '1.0.1'
print(version)


def generate(df=pd.read_csv(file)):
    """Generates a manipulated dataframe from the appeals file in assets"""
    sns.set()
    # Filling null values for date columns before changing dtypes
    df['Date Closed'] = df['Date Closed'].fillna('2099/12/31')
    df['Expiration'] = df['Expiration'].fillna('2099/12/31')
    # Changing appropriate column dtypes
    df['Date Filed'] = pd.to_datetime(df['Date Filed'])
    df['Date Closed'] = pd.to_datetime(df['Date Closed'])
    df['Expiration'] = pd.to_datetime(df['Expiration'])
    # Filling null values for the appropriate columns
    df['Appeal Subtype'] = df['Appeal Subtype'].fillna('No Subtype')
    df['Exam No.'] = df['Exam No.'].fillna(9999)
    df['Title'] = df['Title'].fillna('No Title')
    # Dropping columns of interest
    df = df.drop(columns=['Extension'])
    # After manipulation of appropriate columns, further manipulation to get rid of null values
    df['Exam No.'] = df['Exam No.'].astype('int64')
    # Adding a numerical column for made appeals
    return df


def top_n(n=5, column="Agency"):
    """Returns the dataframe for the n largest values of the interested column"""
    df = generate()
    interested_values = df[column].value_counts()
    interested_values = list(interested_values.head(n).index)
    interested_df = df[df[column].isin(interested_values)]
    return interested_df
