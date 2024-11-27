# Sample Python script for automating Power BI tasks using TMDL format

# This script demonstrates how to automate the export of a Power BI report to a PDF file.

import requests

# Replace with your Power BI workspace and report details
workspace_id = 'your_workspace_id'
report_id = 'your_report_id'
access_token = 'your_access_token'

# Define the export URL
export_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}/ExportTo'

# Define the export parameters
export_params = {
    'format': 'PDF'
}

# Set the headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

# Send the export request
response = requests.post(export_url, headers=headers, json=export_params)

# Check if the request was successful
if response.status_code == 202:
    print('Export request submitted successfully.')
else:
    print(f'Failed to submit export request. Status code: {response.status_code}')
    print(f'Response: {response.text}')
