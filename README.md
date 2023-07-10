###AirBnB Clone

##Description of the project: 
This project is an implementation of an AirBnB clone. It consists of a command-line interface (CLI) that allows users to interact with the application and perform various operations such as creating, updating, and deleting instances of different classes.

###Description og the command interpreter:
##How to start it:
##Usage:
To start the console, run the following command:
./console.py

##How to use it:
Once the console is running, you can enter commands to interact with the application:
For example:

##Commands:
The console supports the following commands:

1. `create` - Create a new instance of a class and save it to the JSON file. Usage: `create <class name>`.
2. `show` - Display the string representation of an instance based on the class name and ID. Usage: `show <class name> <id>`.
3. `destroy` - Delete an instance based on the class name and ID. Usage: `destroy <class name> <id>`.
4. `all` - Display the string representation of all instances or all instances of a specific class. Usage: `all` or `all <class name>`.
5. `update` - Update an instance based on the class name, ID, attribute name, and attribute value. Usage: `update <class name> <id> <attribute name> "<attribute value>"`.

###Available Classes:
##The project includes the following classes:

1. BaseModel - the base class for all other classes.
2. User - represents a user.
   Public class attributes:
   - email: string (empty string)
   - password: string (empty string)
   - first_name: string (empty string)
   - last_name: string (empty string)

3. State - represents a state.
   Public class attributes:
   - name: string (empty string)

4. City - represents a city.
   Public class attributes:
   - state_id: string (empty string) - the ID of the associated state
   - name: string (empty string)

5. Amenity - represents an amenity.
   Public class attributes:
   - name: string (empty string)

6. Place - represents a place.
   Public class attributes:
   - city_id: string (empty string) - the ID of the associated city
   - user_id: string (empty string) - the ID of the user who owns the place
   - name: string (empty string)
   - description: string (empty string)
   - number_rooms: integer (0)
   - number_bathrooms: integer (0)
   - max_guest: integer (0)
   - price_by_night: integer (0)
   - latitude: float (0.0)
   - longitude: float (0.0)
   - amenity_ids: list of strings (empty list) - list of amenity IDs

7. Review - represents a review.
   Public class attributes:
   - place_id: string (empty string) - the ID of the associated place
   - user_id: string (empty string) - the ID of the user who wrote the review
   - text: string (empty string)

###Authors:
- Glamour Maphanga <glamour.maphangat@gmail.com>
- Samuel Okoh <samokoh40@gmail.com> 
