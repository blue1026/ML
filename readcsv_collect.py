import pandas as pd

file_path = "C:\\Users\\bluew\\OneDrive\\桌面\\data_with_classes.csv"
df = pd.read_csv(file_path)

# Separate data into three different DataFrames based on the 'Class' column
df_class1 = df[df['Class'] == 1].drop(columns=['Class'])
df_class2 = df[df['Class'] == 2].drop(columns=['Class'])
df_class3 = df[df['Class'] == 3].drop(columns=['Class'])

# Display the dataframes
print("Class 1:")
print(df_class1)
print("\nClass 2:")
print(df_class2)
print("\nClass 3:")
print(df_class3)
