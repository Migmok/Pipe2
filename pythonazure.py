import requests
import json
import xml.etree.ElementTree as ET

def create_azure_devops_test_run():
    # Azure DevOps organization URL
    organization_url = 'https://dev.azure.com/miguelmduarte'

    # Personal access token (PAT) with appropriate permissions
    personal_access_token = 'fa6karjl6lufcj6ovtkvubjkif4rwpqyxofegqsdadadu76wggnma'

    # Azure DevOps project name
    project = 'Testezao'

    # Test plan ID
    test_plan_id = '6'

    # Test suite ID
    test_suite_id = '8'

    # API endpoint for creating a test run
    url = f'{organization_url}/{project}/_apis/test/runs?api-version=7.0'

    # Parse the Robot Framework test results from the output XML file
    tree = ET.parse('output.xml')
    root = tree.getroot()
    test_cases = root.findall('.//test')

    # Determine the outcome of each test case
    total_tests = len(test_cases)
    passed_tests = sum(1 for tc in test_cases if tc.find('.//status').attrib['status'] == 'PASS')

    # Calculate the overall outcome of the test run
    if passed_tests == total_tests:
        outcome = 'Passed'
    elif passed_tests == 0:
        outcome = 'Failed'
    else:
        outcome = 'PartiallyPassed'

    # Create the request payload
    payload = {
        'name': 'Robot Framework Test Run',
        'plan': {
            'id': test_plan_id
        },
        'pointIds': [test_suite_id],
        'automated': True,
        'state': 'Completed',
        'outcome': outcome,
        'resultFiles': [
            {
                'filePath': 'output.xml',
                'fileType': 'TestResults'
            }
        ]
    }

    # Send the API request to create/update the test run
    response = requests.post(url, json=payload, auth=('', personal_access_token))
    response.raise_for_status()

    print('Azure DevOps test run created/updated successfully!')
    print('Passed tests:', passed_tests)
    print('Total Tests:', total_tests)
    print('API Response:', response.status_code)

# Call the function to create/update the Azure DevOps test run
create_azure_devops_test_run()