# AirBnB Clone Command Interpreter

## Project Description

This project is an AirBnB clone command interpreter built in Python. It provides a command-line interface for managing AirBnB-like objects and interacting with them through various commands. The command interpreter allows you to create, update, delete, and retrieve objects, as well as perform other actions related to your AirBnB clone.

## Command Interpreter Description

The command interpreter is a command-line tool that lets you interact with the AirBnB clone's objects. It uses a simple and intuitive syntax for entering commands and managing data.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the command: `./console.py`

### How to Use the Command Interpreter

Once the command interpreter is running, you can enter various commands to interact with your AirBnB objects. Commands have the format: `command_name class_name [parameters]`.

Here are a few example commands:

- `create User`: Create a new User object.
- `show User 123`: Display information about the User with ID 123.
- `update User 123 email "new_email@example.com"`: Update the email of User 123.
- `all State`: List all State objects.
- `destroy City 456`: Delete the City object with ID 456.

### Examples

Here are some examples of using the command interpreter:

1. Creating a new User:

(hbnb) create User

2. Displaying information about a User:

(hbnb) show User 123

3. Updating a User's email:

(hbnb) update User 123 email "new_email@example.com"

4. Listing all State objects:

(hbnb) all State

5. Deleting a City object:

(hbnb) destroy City 456
