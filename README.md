# Okta-CreateGroupRule

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/365e9646bdbb4f3b8d6c04060f0ce676)](https://www.codacy.com/manual/cloudkevin_2/Okta-CreateGroupRule?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cloudkevin/Okta-CreateGroupRule&amp;utm_campaign=Badge_Grade)

When the 'Enhance Group Push' feature is enabled with Active Directory and Okta, all AD groups dissappear from the GUI. This means that you have no visibility into preexisting AD group membership. Unfortunately even making an API call does not uncover these groups, however Okta Support does have visibility into these. If you contact Okta Support you can get the IDs for each AD group that is now hidden, and from there can use this script to create Group Rules based off of those groups.

## Example
Group A (AD Group) has 5 members. Group B is created as an Okta group and linked with Group A. Once this happens Group B will be the only group visible in the GUI but will have 0 members. To get proper visibility back you can create Group C and use a Group Rule to pull the members of Group A (hidden in the GUI) into your Okta Group C. When viewing the group members you can differentiate between the two by looking at their group assignment reason.

## Script Requirements
HOST = 'YOUR_DOMAIN.okta.com'  
APITOKEN = 'YOUR_TOKEN'
