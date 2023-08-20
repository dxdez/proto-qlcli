# Quick List CLI

Quick List is a command-line interface (CLI) tool that allows users to manage and interact with a to-do list. It uses the Typer library for creating the CLI interface. Here's an overview of the basic commands and functionality of the application:

#### init:
Command: 
```
qklist init
```
Purpose: Initializes the configuration and database for the quicklist.<br/>
Parameters: `--db-path`; Specifies the database file path.<br/>
Functionality: Creates a configuration file and initializes a database for the quicklist.

&nbsp;
#### add:
Command: 
```
qklist add "Description of the task"
```
Purpose: Adds a new item to the to-do list.<br/>
Parameters: `--priority`; Specifies the priority level of the task (1 to 3).<br/>
Functionality: Adds a new item to the to-do list with the specified description and priority.

&nbsp;
#### list:
Command: 
```
qklist list
```
Purpose: Lists all items in the to-do list.<br/>
Functionality: Retrieves all items from the to-do list and displays them with their IDs, priorities, completion status, and descriptions.

&nbsp;
#### complete:
Command: 
```
qklist mark <item_id>
```
Purpose: Marks a specific item as completed.<br/>
Functionality: Sets the completion status of the specified item to "done."

&nbsp;
#### remove:
Command: 
```
qklist pull <item_id>
```
Purpose: Removes a specific item from the to-do list.<br/>
Parameters: `--force`; Forces deletion without confirmation.<br/>
Functionality: Removes the specified item from the to-do list. If not forced, asks for confirmation.

&nbsp;
#### clear:
Command: 
```
qklist empty
```
Purpose: Removes all items from the to-do list.<br/>
Parameters: `--force `- Forces deletion without confirmation.<br/>
Functionality: Clears all items from the to-do list. If not forced, asks for confirmation.

&nbsp;
#### --version:
Option: 
```
--version
```
Note: you can also use `-v` as an alternative.<br/>
Purpose: Shows the version of the application and exits.<br/>
Functionality: Prints the version information for the application.

&nbsp;<br/>
Each command corresponds to a specific action that can be performed on the to-do list. Users interact with the CLI by typing these commands along with their respective parameters. The application initializes its configuration and database, adds, lists, completes, removes, and clears items in the to-do list. It also provides a version option for users to check the application version.

To use this application, users would run the script with the appropriate commands and parameters in their terminal. For example:

- `qklist init`
- `qklist add "Buy groceries" --priority 2`
- `qklist list`
- `qklist mark 1`
- `qklist pull 2 --force`
- `qklist empty`
- `qklist --version`

Ensure that you have the necessary imports and dependencies installed to use this application successfully. You can extend and customize the functionality of your CLI tool further based on your requirements.


