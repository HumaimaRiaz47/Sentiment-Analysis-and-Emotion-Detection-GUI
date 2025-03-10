import json  # Import the JSON module to handle JSON data


class Database:  # Define a class named Database to manage data in a JSON file

    def add_data(self, name, email, password):  # Method to add a new user's data to the database

        # Open the "db.json" file in read mode and load its contents into the database dictionary
        with open("db.json", "r") as rf:
            database = json.load(rf)  # Load the existing data from the JSON file

        # Check if the email already exists in the database
        if email in database:
            return 0  # If the email already exists, return 0 (indicating failure)
        else:
            # If the email does not exist, add the new user to the database
            database[email] = [name, password]  # Use the email as the key and store the name and password as a list

            # Open the "db.json" file in write mode to save the updated database back to the file
            with open("db.json", "w") as wf:
                json.dump(database, wf)  # Write the updated database to the JSON file

            return 1  # Return 1 to indicate the new data was successfully added


    def search(self, email, password):

        with open("db.json", "r") as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
