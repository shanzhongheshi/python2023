import pandas as pd

def read_excel_column(file_path, sheet_name, column_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        column_data = df[column_name].tolist()
        return column_data
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

# Example usage:
file_path = 'C:/Users/86906/Desktop/1.xlsx'
sheet_name = 'Sheet1'  # Replace with your sheet name
column_name = 'id'  # Replace with the name of the column you want to extract

column_list = read_excel_column(file_path, sheet_name, column_name)
print(column_list)
