import requests
import json

# Define the API endpoint and parameters
url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_5"
params = {
    "filter": "record_fiscal_year:eq:2023,classification_desc:eq:Peace Corps",
    "fields": "record_date,classification_desc,current_month_net_outly_amt",
    "format": "json"
}

# Make the API request
response = requests.get(url, params=params)

print(f"Response: {response}")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

        # Extract elements named 'current_month_net_outly_amt'
    net_outlays = [
        float(item['current_month_net_outly_amt'])
        for item in data.get('data', [])
        if 'current_month_net_outly_amt' in item
    ]


  # Calculate the sum of the extracted values
    total_net_outlays = sum(net_outlays)

    # Print the extracted elements
    print("Total Net Outlays:", total_net_outlays)


        # Save the response data to a file
    with open('r-2.json', 'w') as file:
        json.dump(data, file, indent=4)


else:
    print(f"Failed to fetch data: {response.status_code}")
