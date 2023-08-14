# Quick List CLI

Quick List is a command-line interface (CLI) tool that allows users to manage and interact with a to-do list. It uses the Typer library for creating the CLI interface. Here's an overview of the basic commands and functionality of the application:

#### init:
Command: 
```
quicklist-cli init
```
Purpose: Initializes the configuration and database for the quicklist.
Parameters: --db-path (optional) - Specifies the database file path.
Functionality: Creates a configuration file and initializes a database for the quicklist.

#### add:
Command: 
```
quicklist-cli add "Description of the task"
```
Purpose: Adds a new item to the to-do list.
Parameters: --priority (optional) - Specifies the priority level of the task (1 to 3).
Functionality: Adds a new item to the to-do list with the specified description and priority.

#### list:
Command: 
```
quicklist-cli list
```
Purpose: Lists all items in the to-do list.
Functionality: Retrieves all items from the to-do list and displays them with their IDs, priorities, completion status, and descriptions.

#### complete:
Command: 
```
quicklist-cli complete <item_id>
```
Purpose: Marks a specific item as completed.
Functionality: Sets the completion status of the specified item to "done."

#### remove:
Command: 
```
quicklist-cli remove <item_id>
```
Purpose: Removes a specific item from the to-do list.
Parameters: --force (optional) - Forces deletion without confirmation.
Functionality: Removes the specified item from the to-do list. If not forced, asks for confirmation.

#### clear:
Command: 
```
quicklist-cli clear
```
Purpose: Removes all items from the to-do list.
Parameters: --force - Forces deletion without confirmation.
Functionality: Clears all items from the to-do list. If not forced, asks for confirmation.

#### --version:
Option: 
```
--version
```
Note: you can also use `-v` as an alternative.
Purpose: Shows the version of the application and exits.
Functionality: Prints the version information for the application.

Each command corresponds to a specific action that can be performed on the to-do list. Users interact with the CLI by typing these commands along with their respective parameters. The application initializes its configuration and database, adds, lists, completes, removes, and clears items in the to-do list. It also provides a version option for users to check the application version.

To use this application, users would run the script with the appropriate commands and parameters in their terminal. For example:

- `quicklist-cli init`
- `quicklist-cli add "Buy groceries" --priority 2`
- `quicklist-cli list`
- `quicklist-cli complete 1`
- `quicklist-cli remove 2 --force`
- `quicklist-cli clear`
- `quicklist-cli --version`

Ensure that you have the necessary imports and dependencies installed to use this application successfully. You can extend and customize the functionality of your CLI tool further based on your requirements.

