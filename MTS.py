import pandas as pd

#Program to help analyze US Treasury Monthly Treasury Statement MTS_OutlyAgcy_20190501_20240430 2.csv
# Load the CSV file
file_path = 'MTS_OutlyAgcy_20190501_20240430 2.csv'
data = pd.read_csv(file_path)

# Filter data for the fiscal year 2023 and for the "Coronavirus Relief Fund" classification description, excluding 'total'
coronavirus_relief_fund_data = data[
    (data['Fiscal Year'] == 2023) & 
    (data['Classification Description'].str.contains('peace corps', case=False)) & 
    (~data['Classification Description'].str.contains('Total', case=False))
]

# Calculate the sum of the 'Current Month Net Outlays Amount' for the "Coronavirus Relief Fund"
coronavirus_relief_fund_sum = coronavirus_relief_fund_data['Current Month Net Outlays Amount'].sum()
coronavirus_relief_fund_std = coronavirus_relief_fund_data['Current Month Net Outlays Amount'].std()
percent_reduct = (coronavirus_relief_fund_std / coronavirus_relief_fund_sum) * 100

print(f'sum data: {coronavirus_relief_fund_sum}')
print(f'std data: {coronavirus_relief_fund_std}')
print(f'percent: {percent_reduct}')
