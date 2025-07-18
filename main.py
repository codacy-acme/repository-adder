import requests
import argparse

def add_repository(baseurl, provider, organization, repo, token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'api-token': token,
        'caller': 'codacy-integration-helper'
    }
    data = {
        "provider": provider,
        "repositoryFullPath": f'{organization}/{repo}'
    }
    url = f'{baseurl}/api/v3/repositories'
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return True, f"Successfully added {repo}: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Failed to add {repo}: {e.response.status_code if e.response else 'N/A'}, Response: {e.response.text if e.response else 'N/A'}"
    updateRepositoryIntegrationsSettings()
    return


# PATCH /organizations/{provider}/{remoteOrganizationName}/repositories/{repositoryName}/integrations/providerSettings
def update_repository_integrations_settings(baseurl, provider, remoteOrganizationName, repositoryName, token):
    data = {
        "commitStatus": False,
        "pullRequestComment": False,
        "pullRequestSummary": False,
        "coverageSummary": False,
        "suggestions": False,
        "aiEnhancedComments": False
        }
    url = f'{baseurl}/api/v3/organizations/{provider}/{remoteOrganizationName}/repositories/{repositoryName}/integrations/providerSettings'
    try:
        response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return True, f"Successfully updated integration settings {repo}: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Failed to update integrations settings {repo}: {e.response.status_code if e.response else 'N/A'}, Response: {e.response.text if e.response else 'N/A'}"
    return

def process_files(file_path, baseurl, provider, organization, token):
    with open(file_path, 'r') as file:
        for line in file:
            repo = line.strip()
            if repo:
                success, message = add_repository(baseurl, provider, organization, repo, token)
                print(message)

def main():
    print('\nWelcome to Codacy Integration Helper - A solution to Add Repositories\n')
    parser = argparse.ArgumentParser(description='Codacy Integration Helper')
    parser.add_argument('--token', dest='token', required=True,
                        help='the api-token to be used on the REST API')
    parser.add_argument('--file', dest='file', required=True,
                        help='path to the txt file containing repository names')
    parser.add_argument('--provider', dest='provider', required=True,
                        help='git provider (gh|ghe)')
    parser.add_argument('--organization', dest='organization', required=True,
                        help='organization name')
    parser.add_argument('--baseurl', dest='baseurl', default='https://app.codacy.com',
                        help='codacy server address (ignore if cloud)')
    args = parser.parse_args()
    process_files(args.file, args.baseurl, args.provider, args.organization, args.token)
    return

if __name__ == '__main__':
    main()