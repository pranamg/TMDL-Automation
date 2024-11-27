# Sample PowerShell script for automating Power BI tasks using TMDL format

# This script demonstrates how to automate the export of a Power BI report to a PDF file.

# Replace with your Power BI workspace and report details
$workspaceId = 'your_workspace_id'
$reportId = 'your_report_id'
$accessToken = 'your_access_token'

# Define the export URL
$exportUrl = "https://api.powerbi.com/v1.0/myorg/groups/$workspaceId/reports/$reportId/ExportTo"

# Define the export parameters
$exportParams = @{
    format = 'PDF'
}

# Set the headers for the request
$headers = @{
    'Content-Type' = 'application/json'
    'Authorization' = "Bearer $accessToken"
}

# Send the export request
$response = Invoke-RestMethod -Uri $exportUrl -Headers $headers -Method Post -Body ($exportParams | ConvertTo-Json)

# Check if the request was successful
if ($response.StatusCode -eq 202) {
    Write-Output 'Export request submitted successfully.'
} else {
    Write-Output "Failed to submit export request. Status code: $($response.StatusCode)"
    Write-Output "Response: $($response | ConvertTo-Json)"
}
