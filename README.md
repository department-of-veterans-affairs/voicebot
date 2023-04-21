# voicebot

## Ticketing System Jira: https://vajira.max.gov/secure/RapidBoard.jspa?rapidView=9147&projectKey=VOIC&quickFilter=36252

Confluence: https://confluence.boozallencsn.com/display/VOICEBOT/VOICEBOT+Home

## Data Sources
There are multiple APIs that are being looked at for potential consumption by the voicebot that contain information on the veterans claim status, personal information, and content from the va.gov website. We have spreadsheets which detail what APIs we have access to, how to get access and where to find documentation as well as what fields can be found in these APIs that could be relevant to the use cases outlined in our flows.

### API field documentation
This spreadsheet has all the APIs that have been discovered and documents the relevant endpoints and fields possible for use with the voicebot. This is not an exhaustive list and there are still some caveats to their use/integration. 

https://dvagov.sharepoint.com/:x:/s/VoiceBot/ERt9wFuq7U1KiWdXCiy2XH4BKjRaw0iZw-dHdvi3qrnbSQ?e=iLsGuz

### Data Access and Location
This spreadsheet contains links to API documentation and environments and how to access links/accounts. 

https://dvagov.sharepoint.com/:x:/r/sites/VoiceBot/Shared%20Documents/General/Data%20and%20Access/Data%20Status.xlsx?d=w96bb66c677de4a628e1bea78b50b3ace&csf=1&web=1&e=f93eu0

### Other Github Repos

There are a few different repos in the VA Github which are being used. The first is for the [WebHook](https://github.com/department-of-veterans-affairs/voicebot-webhooks), this is used to perform logical functions and executions for DialogFlow. The second is for the [Intent Designer](https://github.com/department-of-veterans-affairs/voicebot-intent-designer) which is used as a CRM to manage the linkages between intents and training phrases and help search. Each repo has its own documentation on how to setup and utilize the applications.

### DialogFlow & WebHook

The DialogFlow system allows for flows and matching of training phrases to intents. It allows simple movement around in flows; however, introducing dynamic content is imperative whereby veterans can authenticate or select claims and even find out if they might qualify based on certain qualifications they have. In this instance we use we WebHook.
The [WebHook](https://github.com/department-of-veterans-affairs/voicebot-webhooks) contains a set of mock data at this time but is designed to be able to authenticate a user and then go through a list of claims for that user. If a claim has been selected, the user can also ask certain questions surrounding their claim. All of this is considered dynamic content and resides in the WebHook.

### Intent Designer

Although the end system DialogFlow is where the intents and their corresponding training phrases will live, it is important to be able to manage and determine whether potential duplicates exist. This is where [Intent Designer](https://github.com/department-of-veterans-affairs/voicebot-intent-designer) comes in. It contains mappings of all intents and their corresponding training phrases as well as being able to do "potential duplicate checks" which allows the users creating intents to know whether there are potential collisions.
The Intent Designer currently runs independently of DialogFlow as well as the WebHook. After a user enters new training phrases (or creates a new intent) they can export the file as a CSV and then import it directly into DialogFlow making the Intent Designer the system of record. There are many more features which have been identified which will help give a broader understanding to the users of DialogFlow.
