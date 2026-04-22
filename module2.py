# # Leave the following code, it will import pandas and create a sample dataframe. To play with this exercise in VS code, this is the section you should copy/paste into your notebook first.
# import pandas as pd
# # Sample DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['NYC', 'LA', 'Chicago', 'Miami'],
#     'Email': ['a@example.com', 'b@example.com', 'c@example.com', 'd@example.com']
# }
# df = pd.DataFrame(data)


# # --- EXERCISE STARTS HERE!!=== #

# # 1. Drop the Email column and store in new variable
# # df_no_email = df.drop('Email', axis=1)#YOUR CODE HERE
# # print(df_no_email)

# # # 2. Drop row with index 2 in place
# # df.drop(2, inplace=True)
# # print(df)

# # # Re-create DataFrame for next steps- just leave this alone, continue to # 3
# # df = pd.DataFrame(data)

# # # # 3. Drop City and Email columns, assign back to df
# # df = df.drop(['City','Email'], axis=1)# YOUR CODE HERE
# # print(df)

# # # Re-create again for next step
# df = pd.DataFrame(data)

# # # 4. Drop first and last row, store in df_trimmed
# # df_trimmed = df.drop([0, 2])
# # # YOUR CODE HERE
# # print(df_trimmed)

# # Leave this code alone
# import pandas as pd
# import numpy as np

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, np.nan, 35, 40, None],
#     'City': ['NYC', 'LA', None, 'Miami', 'Boston']
# }
# df = pd.DataFrame(data)

# # --- EXERCISE STARTS HERE!! --- #

# Answer the questions below INSIDE the print statements
# 1. View the first 5 rows of the DataFrame
# print(df.head())# YOUR CODE HERE!!)

# # 2. Show where values are missing
# print(df.isnull())

# # 3. Count of missing values by column
# print(df.isnull().sum())

# # 4. Drop rows with missing data
# print(df.dropna())

# # 5. Re-create original - leave this part alone and move to # 6
#df = pd.DataFrame(data)

# # 6. Drop columns with missing data
# print(df.dropna(axis=1))

# # # 7. Re-create again - Leave this alone again and move to # 7
# df = pd.DataFrame(data)

# # # 8. Fill missing Age with mean
# # df= df.fillna(df['Age'].mean())
# # print(df)

# # # 9. Fill missing City with "Unknown"
# df= df.fillna('unknown')
# print(df)


# # LEAVE THIS CODE ALONE
# import pandas as pd
# # Load sample data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Diana'],
#     'Age': [25, 30, 35, 25, 30, 40],
#     'City': ['NYC', 'LA', 'SF', 'NYC', 'LA', 'NYC']
# }
# df = pd.DataFrame(data)

# --- EXERCISE STARTS HERE!! --- #
# Write your answers INSIDE the print statements

# 1. Find which rows are duplicates (across all columns)
# print("\nDuplicated rows (True if row is a duplicate of an earlier one):")
# print(df.duplicated())

# 2. Drop duplicate rows (keeping the first occurrence)
# print("\nDataFrame with duplicates dropped (keep='first'):")
# print(df.drop_duplicates())

# 3. Drop duplicate rows (keeping only the last occurrence)
# print("\nDataFrame with duplicates dropped (keep='last'):")
# print(df.drop_duplicates(keep='last'))

# # 4. Drop ALL duplicates (remove both original and duplicate)
# print("\nDataFrame with ALL duplicates removed (keep=False):")
# print(df.drop_duplicates(keep=False))

# import pandas as pd

# # Original DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Dept': ['HR', 'Finance', 'IT'],
#     'Sal': [60000, 70000, 80000]
# }
# df = pd.DataFrame(data)


# # ANSWER THE QUESTIONS BELOW
# # 1. Rename 'Dept' to 'Department'and 'Sal' to 'Salary'
# df.rename(columns= {
#     'Dept': 'Department',
#     'Sal': 'Salary'
# }, inplace=True)

# # 2. Reorder columns so 'Salary' appears first, followed by 'Name' and 'Department'
# df=df[['Salary', 'Name', 'Department']]

# # 4. Print the updated DataFrame
# print(df)


# LEAVE THIS PART ALONE
# import pandas as pd

# # Sample Data
# data = {
#     'Store': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
#     'Product': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Bananas', 'Oranges', 'Apples', 'Bananas', 'Bananas'],
#     'Sales': [100, 80, 90, 120, 110, 60, 95, 85, 75],
#     'Profit': [30, 25, 20, 40, 35, 15, 32, 22, 18]
# }
# df = pd.DataFrame(data)
# # View the first few rows
# print(df.head())

# ----- EXERCISE STARTS HERE ---- #

# ANSWER THE FOLLOWING QUESTIONS INSIDE THE PRINT STATEMENTS

# 1. Group the data by Store and use .agg() to find the average Sales and average Profit for each store
#print(df.groupby('Store').agg(Avg_Sales=('Sales', 'mean'),Avg_Profit=('Profit', 'mean')))

# 2. Group by Product and get the maximum Sales and minimum Profit
#print(df.groupby('Product').agg(Max_Sales=('Sales', 'max'), Min_Profit=('Profit', 'min')))

# 3. Group by Store and return both the average Sales and maximum Profit, but name the columns 'Avg_Sales' and 'Max_Profit'
# print(df.groupby('Store').agg(Avg_Sales=('Sales', 'mean'), Max_Profit=('Profit', 'max')))

# 4. BONUS: Group by both Store and Product, and find the total Sales using .agg()
#print(df.groupby(['Store', 'Product']).agg(Total_Sales=('Sales', 'sum')))


# # DO NOT CHANGE THIS CODE
# import pandas as pd

# # Set up the first DataFrame
# df_customers = pd.DataFrame({
#     'CustomerName': ['Alice', 'Bob', 'Charlie']
# }, index=[101, 102, 103])

# # Set up the second DataFrame
# df_orders = pd.DataFrame({
#     'OrderTotal': [250, 300, 400]
# }, index=[101, 102, 103])

# ANSWER THE QUESTIONS BELOW!

# 1. Join df_orders to df_customers on the index
#print(df_customers.join(df_orders, how='left'))

# # 2. Add a new column to df_customers with city data
# df_cities = pd.DataFrame({
#      'City': ['NYC', 'LA', 'Chicago']
#  }, index=[101, 102, 103])
# print(df_customers.join(df_cities, how='left'))

# import pandas as pd

# def clean_data(df):
#     return df.dropna()
    

# # Testing mechanism - do not modify!
# data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]}
# df = pd.DataFrame(data)
# print(clean_data(df))


#marimo week 1

# import pandas as pd

# data = {
# "Name": [
#     "Alice", "Bob", "Charlie", "David", "Evelyn",
#     "Frank", "Grace", "Henry", "Isla", "Jack",
#     "Karen", "Leo", "Mia", "Noah", "Olivia",
#     "Paul", "Quinn", "Ruby", "Sam", "Tina"
# ],
# "Age": [25, 32, 37, 29, 41, 28, 34, 45, 26, 31, 39, 27, 33, 36, 30, 42, 24, 38, 35, 29],
# "Department": [
#     "HR", "Engineering", "Sales", "Marketing", "Engineering",
#     "Finance", "Support", "Operations", "HR", "Sales",
#     "Engineering", "Support", "Marketing", "Finance", "Operations",
#     "Engineering", "HR", "Sales", "Support", "Marketing"
# ],
# "Salary": [
#     50000, 75000, 62000, 58000, 80000,
#     54000, 52000, 70000, 51000, 64000,
#     82000, 53000, 60000, 56000, 68000,
#     79000, 49500, 65500, 54500, 61000
# ],
# }

# df = pd.DataFrame(data)

#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.shape)

# import pandas as pd

# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# df = pd.read_csv(url)

#print(df.head())

#print(df.loc[12,["Name", "Age"]])
#print(df.iloc[0:5, 0:3])
#print(df.loc[(df['Pclass'] == 1) & (df['Sex'] == "female")])
#print(df.iloc[9, df.columns.get_loc("Age")])
#print(df.loc[100:105, ["Fare", "Survived"]])

# import pandas as pd

# url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
# df = pd.read_csv(url)

#print(df.head())

# print(df.describe())
#print(df.value_counts("Embarked"))
# print(df.value_counts("Pclass"))
# print(df["Age"].mean())
#print(df['Fare'].max())
#print(df["Name"].nunique())
#print(df.value_counts("Sex"))
#print(df.nunique())


# import pandas as pd

# data = {
# "Name": ["Alice", "Bob", "Charlie", "David"],
# "Age": [25, 30, 35, 40],
# "City": ["NYC", "LA", "Chicago", "Miami"],
# "Email": ["a@example.com", "b@example.com", "c@example.com", "d@example.com"],
# }

# df = pd.DataFrame(data)
#print(df.head())
#print(df.drop('Email', axis = 1))
#print(df.drop(2))
#print(df.drop('City', axis=1)&('Email', axis=1))
#df_trimmed=df.iloc[1:-1]


# import pandas as pd
# import numpy as np

# data = {
# "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
# "Age": [25, np.nan, 35, 40, None],
# "City": ["NYC", "LA", None, "Miami", "Boston"],
# }

# df = pd.DataFrame(data)

# print(df.head())
#print(df.isnull())
#print(df.isnull().sum())
#print(df.dropna())
#print(df.dropna(axis=1))
#print(df.fillna(df["Age"].mean()))
#print(df.fillna("unknown"))


# import pandas as pd

# data = {
# "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"],
# "Age": [25, 30, 35, 25, 30, 40],
# "City": ["NYC", "LA", "SF", "NYC", "LA", "NYC"],
# }

# df = pd.DataFrame(data)

# #print(df.duplicated())
# #print(df.drop_duplicates())
# #print(df.drop_duplicates(keep='last'))
# print(df.drop_duplicates(keep=False))


# import pandas as pd

# data = {
# "fname": ["Alice", "Bob", "Charlie"],
# "lname": ["Smith", "Jones", "Brown"],
# "ctry": ["USA", "Canada", "UK"],
# }

# df = pd.DataFrame(data)

#print(df.rename(columns={'fname': 'FirstName','lname':'LastName'}))
#print(df.rename(columns ={'fname': "FirstName", "lname": "LastName", "Ctry": "Country"}))

# import pandas as pd

# data = {
# "Name": ["Alice", "Bob", "Charlie"],
# "Dept": ["HR", "Finance", "IT"],
# "Sal": [60000, 70000, 80000],
# }

# df = pd.DataFrame(data)
# df=df.rename(columns={'Dept': 'Department', 'Sal':"Salary"})
# df = df[["Salary", 'Name', "Department"]]
# print(df)

# import pandas as pd

# data = {
# "Store": ["A", "A", "A", "B", "B", "C", "C", "C", "C"],
# "Product": ["Apples", "Oranges", "Bananas", "Apples", "Bananas", "Oranges", "Apples", "Bananas", "Bananas"],
# "Sales": [100, 80, 90, 120, 110, 60, 95, 85, 75],
# "Profit": [30, 25, 20, 40, 35, 15, 32, 22, 18],
# }

# df = pd.DataFrame(data)
# #print(df.head())

# #(print(df.groupby("Store")[["Sales", "Profit"]].mean()))
# # print(df.groupby("Product").agg({
# #     'Sales': "max",
# #     "Profit": 'min'
# # }))

# print(df.groupby('Store').agg(
#     Avg_Sales =('Sales', 'mean'),
#     Max_Profit=('Profit', 'max')    
# ))

import pandas as pd

df_customers = pd.DataFrame({
"CustomerName": ["Alice", "Bob", "Charlie"]
}, index=[101, 102, 103])

df_orders = pd.DataFrame({
"OrderTotal": [250, 300, 400]
}, index=[101, 102, 103])

#print(df_customers.join(df_orders))
