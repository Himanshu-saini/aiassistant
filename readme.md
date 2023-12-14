### AI Assistant
-------------------

# Problem:
There is a excel template where 1st sheet contains list of all tables with some description and next sheets contains information about table columns, data types and its description. Create a API to convert the column into sementic names (human readable) without any other humna interaction.

# Approach:
Create 2 GPT agents. Agent 1 is responsible to convert these column name to sementic name and agent 2 is responsible to verify whether these column names are sementic or not and will provide its input to further correct the data.

# Topics:
- function calling (get json output)
- OpenAI apis

