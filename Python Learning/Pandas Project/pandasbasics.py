import pandas as pd
import numpy as np
# Create a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})
print("Pandas is working!")
print(df)
#working as dictionary
# Create a DataFrame from a dictionary
dict1 = {
    "Name": ['Apon', 'Muhtasim'],
    "Marks": [90, 99],
    "City": ['Dhaka', 'New York']
}
df2=pd.DataFrame(dict1)
print(df2)
# Create a DataFrame from a list of dictionaries
list_of_dicts = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30}
]
df3 = pd.DataFrame(list_of_dicts)
print(df3)
# Create a DataFrame from a list of lists
list_of_lists = [
    ["Alice", 25],
    ["Bob", 30]
]
df4 = pd.DataFrame(list_of_lists, columns=["Name", "Age"])
print(df4)
#exporting to csv(excel file)
df4.to_csv("datasheet.csv")
#not showing index in csv file
df4.to_csv("datasheet.csv", index=False)
#for showing some beginning rows
print(df4.head(1))  # Show the first row
print(df4.head(2))  # Show the first two rows
#for showing some ending rows
print(df4.tail(1))  # Show the last row
print(df4.tail(2))  # Show the last two rows
#for showing some specific rows
print(df4.iloc[0])  # Show the first row
print(df4.iloc[1])  # Show the second row
#for showing some specific columns
print(df4["Name"])  # Show the 'Name' column
print(df4[["Name", "Age"]])  # Show the 'Name' and 'Age
#for describing the data
print(df4.describe())  # Show summary statistics for numerical columns
#for reading a csv file
df5 = pd.read_csv("datasheet.csv")
print(df5)
#for basics of csv file
print(df5.shape)  # Show the shape of the DataFrame (rows, columns)
df5['Age'][0]=35
print(df5)  # Show the updated DataFrame
print(df5.to_csv("datasheet.csv"))  # Save the updated DataFrame to CSV
df5.index=['first', 'second']
print(df5)  # Show the DataFrame with custom index
#to show all the cells
set=pd.Series(np.random.randn())
print(set)  # Show the Series with random numbers
print(type(set))  # Show the type of the Series
set1 = pd.DataFrame(np.random.randn(334,5),index=np.arange(334))# Show the DataFrame with random numbers
print(set1.head())  # Show the first few rows of the DataFrame
print(type(set1))  # Show the type of the DataFrame
print(set1.dtypes)  # Show the data types of each column
set1[0][0]="APON" # Update the first cell of the first column
print(set1.dtypes)  # Show the data types of each column again
print(set1.index)  # Show the index of the DataFrame
print(set1.columns)  # Show the columns of the DataFrame
set1.to_numpy()  # Convert the DataFrame to a NumPy array
print(set1.to_numpy())  # Show the NumPy array representation of the DataFrame
set1[0][0]=0.3 # Update the first cell of the first column again
print(set1.to_numpy())  # Show the updated DataFrame as a NumPy array
print(set1.T)  # Transpose the DataFrame (swap rows and columns)
print(set1.T.to_numpy())  # Show the transposed DataFrame as a NumPy array
print(set1.sort_index(axis=0, ascending=False))  # Sort the DataFrame by index in descending order
print(set1.sort_index(axis=1, ascending=False))  # Sort the DataFrame by columns in descending order
print(set1[0]) # Show the first column of the DataFrame
print(set1[0].sort_values(ascending=False))  # Sort the first column in descending order
print(set1[0].sort_values(ascending=True))  # Sort the first column in ascending order
print(set1[0].sort_values(ascending=True).head())  # Show the first few sorted values of the first column
print(type(set1[0]))  # Show the type of the first column (Series)
print(set1[0].to_numpy())  # Convert the first column to a NumPy array
print(set1[0].to_list())  # Convert the first column to a list
#set2=set1 #this is malpractiseas set2 is a reference to set1, not a copy
set2 = set1.copy()  # Create a copy of set1 to avoid modifying the original DataFrame
print(set2)  # Show the DataFrame set2, which is a copy of set1
set1.loc[0, 0] = 0.5  # Update the first cell of the first column in set1
print(set1)  # Show the updated DataFrame set1
print(set2)  # Show the unchanged DataFrame set2
set1.columns=list("ABCDE")  # Update the column names of set1
print(set1)  # Show the DataFrame set1 with updated column names
print(set1.head(2))  # Show the first two rows of set1
print(set1.tail(2))  # Show the last two rows of set1
set1.loc[0,0]=0.6
print(set1.head(2))  # Show the first two rows of set1 after updating the first cell
set1.drop(0, axis=1, inplace=True)  # Drop the first column of set1
print(set1)  # Show the DataFrame set1 after dropping the first column
print(set1.loc[[1,2], ['C', 'D']]) # Show the value at row index 1 and column index 2, and the columns 'C' and 'D'
print(set1.loc[1:3, ['C', 'D']])  # Show rows 1 to 3 and columns 'C' and 'D'
print(set1.loc[1:3, :])  # Show rows 1 to 3 and all columns
print(set1.loc[(set1['A'] < 0.3) & (set1['C'] > 0.1)])  # Update the 'A' column where the first column is greater than 0.5
print(set1.loc[(set1['A'] < 0.3) & (set1['C'] > 0.1), ['A', 'C']])  # Show columns 'A' and 'C' where the conditions are met
print(set1.iloc[0,4])  # Show the value at the first row and fifth column using integer-location based indexing
print(set1.iloc[0, 4:])  # Show the value at the first row and columns from the fifth column onwards
print(set1.iloc[[0,1], [1,2]])  # Show the values at the first two rows and second and third columns
print(set1.iloc[0:2, 1:3])  # Show the values at the first two rows and second and third columns using slicing
set1.drop(0)  # Drop the first row of set1
print(set1)  # Show the DataFrame set1 after dropping the first row
set1.drop(['A', 'B'], axis=1, inplace=False)  # Drop columns 'A' and 'B' from set1 not modifying the original DataFrame if true, then remove the original DataFrame
print(set1)  # Show the DataFrame set1 after dropping columns 'A' and 'B'
set1=set1.dropna()  # Drop rows with any NaN values from set1
print(set1)  # Show the DataFrame set1 after dropping rows with NaN values
print(set1.reset_index(drop=True))  # Reset the index of set1, dropping the old index
print(set1['B'].isnull())  # Check for NaN values in column 'B'
print(set1['B'].notnull())  # Check for non-NaN values in column 'B'
set1['B']=None  # Set all values in column 'B' to None
print(set1)  # Show the DataFrame set1 after setting column 'B' to None
print(set1['B'].isnull())  # Check for NaN values in column 'B' after setting it to None
set1.loc[:, ['B']]= 7 # Set all values in column 'B' to 7
print(set1)  # Show the DataFrame set1 after setting column 'B' to 7
print(set1.dropna(how='all'))  # Drop rows where all elements are NaN
print(set1.dropna(how='any'))  # Drop rows where any element is NaN
print(set1.drop_duplicates())  # Drop duplicate rows from set1
print(set1.drop_duplicates(subset=['A', 'C']))  # Drop duplicate rows based on columns 'A' and 'C'
print(set1.drop_duplicates(subset=['A', 'C'], keep='last'))  # Drop duplicates based on 'A' and 'C', keeping the last occurrence
print(set1.drop_duplicates(subset=['A', 'C'], keep=False))  # Drop all duplicates based on 'A' and 'C'
print(set1.duplicated())  # Check for duplicate rows in set1
print(set1.drop_duplicates(subset=['A', 'C'], keep='first'))  # Drop duplicates based on 'A' and 'C', keeping the first occurrence
print(set1.info())  # Show information about the DataFrame set1, including data types and non-null counts
print(set1['A'].unique())  # Show unique values in column 'A'
print(set1['A'].nunique())  # Show the number of unique values in column 'A'
#to import data from excel file
datasheet= pd.read_excel("C:\\AI Projects\\Python Learning\\Pandas Project\\student_scores.xlsx")  # Read data from an Excel file
print(datasheet)  # Show the DataFrame read from the Excel file
#to export data to excel file
#datasheet.to_excel("C:\\AI Projects\\Python Learning\\Pandas Project\\student_scores.xlsx", index=False)
print(datasheet.head())  # Show the first few rows of the DataFrame read from the Excel file
print(datasheet.tail())  # Show the last few rows of the DataFrame read from the Excel file
print(datasheet.describe())  # Show summary statistics for numerical columns in the DataFrame
print(datasheet.columns)  # Show the columns of the DataFrame read from the Excel file
print(datasheet.shape)  # Show the shape of the DataFrame (rows, columns)
print(datasheet.dtypes)  # Show the data types of each column in the DataFrame
print(datasheet['Name'])  # Show the 'Name' column of the DataFrame
print(datasheet['Name'].unique())  # Show unique names in the 'Name' column
print(datasheet['Name'].nunique())  # Show the number of unique names in the 'Name' column
print(datasheet['Name'].value_counts())  # Show the count of each unique name in the 'Name' column
print(datasheet['Name'].value_counts().head(2))  # Show the top 2 most frequent names in the 'Name' column
#mathematical operations
print(datasheet['EEE'].mean())  # Show the mean of the 'EEE' column
print(datasheet['EEE'].median())  # Show the median of the 'EEE' column
print(datasheet['EEE'].mode())  # Show the mode of the 'EEE' column
print(datasheet['EEE'].std())  # Show the standard deviation of the 'EEE' column
print(datasheet['EEE'].var())  # Show the variance of the 'EEE' column
print(datasheet['EEE'].min())  # Show the minimum value in the 'EEE' column
print(datasheet['EEE'].max())  # Show the maximum value in the 'EEE' column
print(datasheet['EEE'].sum())  # Show the sum of the 'EEE' column
print(datasheet['EEE'].count())  # Show the count of non-null values in the 'EEE' column
print(datasheet['EEE'].quantile(0.25))  # Show the 25th percentile of the 'EEE' column
print(datasheet['EEE'].quantile(0.75))  # Show the 75th percentile of the 'EEE' column
print(datasheet['EEE'].quantile([0.25, 0.5, 0.75]))  # Show the 25th, 50th, and 75th percentiles of the 'EEE' column
print(datasheet['EEE'].quantile([0.1, 0.9]))  # Show the 10th and 90th percentiles of the 'EEE' column