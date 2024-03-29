import requests
import json 

# Webex Teams API base URL
api_url = "https://api.ciscospark.com/v1"

# Your Webex Teams API token
api_token = "NTMyOWJmNmEtNDczZC00NzBmLTgxOGEtNDAyMDMxNDViYmQxZjE3Y2I4YjEtMjQy_PE93_b6f7ca7f-55ce-4df9-855a-8cfebcad253f"

# Members' email addresses
your_email = "yanis.sebagh@student.odisee.be"
yvan_email = "yvan.rooseleer@biasc.be"

# Webex Teams space name
space_name = "devasc_skills_YanisSebagh"

# Function to create a Webex Teams space
def create_space(api_url, api_token, space_name):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {"title": space_name}
    response = requests.post(f"{api_url}/rooms", headers=headers, json=payload)
    return response.json()["id"]

# Function to invite members to a Webex Teams space
def invite_members(api_url, api_token, space_id, email_list):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    for email in email_list:
        payload = {"roomId": space_id, "personEmail": email}
        requests.post(f"{api_url}/memberships", headers=headers, json=payload)
# Function to send a message to a Webex Teams space
def send_message(api_url, api_token, space_id, message):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {"roomId": space_id, "text": message}
    requests.post(f"{api_url}/messages", headers=headers, json=payload)
    # Create Webex Teams space
space_id = create_space(api_url, api_token, space_name)

# Invite members to the space
invite_members(api_url, api_token, space_id, [your_email, yvan_email])

# Publish GitHub repository URL in the space
github_repo_url = "https://github.com/Yanis9k/Devasc_Skills.git"
send_message(api_url, api_token, space_id, f"Check out my GitHub repository: {github_repo_url}")

# Send a message to the space
send_message(api_url, api_token, space_id, "Here are my screenshots of devasc skills-based exam")

