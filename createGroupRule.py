import requests as r
import logging as l
import settings as s

ruleName = input('Group Rule Name: ')
adGroupId = input('Active Directory (source) Group Id:')
oktaGroupId = input('Okta Group (destination) Id: ')

payload = "{\n  \"type\": \"group_rule\",\n  \"name\": \""+ruleName+"\",\n  \"conditions\": {\n    \"people\": {\n      \"users\": {\n        \"exclude\": []\n      },\n      \"groups\": {\n        \"exclude\": []\n      }\n    },\n    \"expression\": {\n      \"value\": \"isMemberOfAnyGroup(\\\""+adGroupId+"\\\")\",\n      \"type\": \"urn:okta:expression:1.0\"\n    }\n  },\n  \"actions\": {\n    \"assignUserToGroups\": {\n      \"groupIds\": [\n        \""+oktaGroupId+"\"\n      ]\n    }\n  }\n}"

def buildHeader():
	return{
		'Accept': "application/json",
    	'Content-Type': "application/json",
    	'Authorization': 'SSWS ' + s.APITOKEN,
    	'Host': f"{s.HOST}"
		}

def createGroupRule():
	global payload
	l.info("Starting createGroupRule")
	url = f"https://{s.HOST}/api/v1/groups/rules"
	l.debug(url)
	headers = buildHeader()
	result = r.request("POST", url, data=payload, headers=headers)
	print(result)
	print(f"Status Code: {result.status_code}")
	l.debug(headers)
	if result.status_code == 200:
		print("Group Rule Created Successfully")
	if result.status_code != 200:
		l.error(f"API Request Failed")

def main():
	createGroupRule()

if __name__ == '__main__':
	main()