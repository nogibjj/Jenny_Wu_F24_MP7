[![Python Application Test with Github Actions](https://github.com/nogibjj/Jenny_Wu_F24_MP7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jenny_Wu_F24_MP7/actions/workflows/cicd.yml)

# Jenny_Wu_F24_MP7
## Package a Python Script into a Command-Line Tool 

### Requirements 
Package a Python script with setuptools or a similar tool
Include a user guide on how to install and use the tool
Include communication with an external or internal database (NoSQL, SQL, etc) [If you use Rust you can skip the DB part]

### CLI Explainations 
In this CLI command, we are extracting data from a URL and creating a .csv into the "data" folder. To call the CLI, type in "python cli.py extract ["URL HERE"] ["FILE PATH"]"
![alt text](<cli pass/Extract CLI.png>)


In this CLI command, we are creating a database and a table from the previously extracted .csv file with the preprocessed table values. To call the CLI, type in "python cli.py transform ["Location of the previously saved .csv file"] ["name of db file"] ["desired table name"]"
![alt text](<cli pass/Create_DB CLI.png>)

In this CLI command, from the table we previously created, we are querying the first 10 Incidents Against a F/BLK Victim in the Streets of the Bronx. To call the CLI, type in "python cli.py query_1 ["database name"] ["table name"]
![alt text](<cli pass/Query_1 CLI.png>)

In this CLI command, from the table we previously created, we are querying all incidents that happen on 2023-12-29. To call the CLI, type in "python cli.py query_1 ["database name"] ["table name"]
![alt text](<cli pass/Query_2 CLI.png>)
