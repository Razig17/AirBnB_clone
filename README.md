## Description
The AirBnB Clone project is a Python-based implementation of a simplified version of the AirBnB website. The project includes a command-line interface (CLI) that allows users to interact with the application using commands.

## Command Interpreter

The ALX Airbnb Console is built on a command interpreter that allows users to interact with the system through a series of commands.

## How to start the console

1. Clone the project repository from GitHub.
2. Run the console application using the command:
   `$ python3 console.py` or
   `$ ./console.py` make sure that console.py have execute permissions.

## Examples

1. `create`: Creates a new instance of a class, saves it (to the JSON file) and prints the `id`.

	Syntax: `create <class name>`

	Ex: `$ create User`
   
2. `show`: Prints the string representation of an instance based on the class name and `id`.

	Syntax: `show <class name> <id>`

	Ex: `$ show User 1234-1234-1234`

3. `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

	Syntax: `update <class name> <id> <attribute name> "<attribute value>"`

	Ex: `$ update User 1234-1234-1234 email "aibnb@mail.com"`.

4. `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file).

	syntax: `destroy <class name> <id>`

	Ex: `$ destroy User 1234-1234-1234`.
   
5. `all`: Prints all string representation of all instances based or not on the class name.

	syntax: `all [class name]` or `[class name].all()`

	Ex: `$ all User` or `$ all` or `$ User.all()`.
