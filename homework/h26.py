class Dog:

    def __init__(self, name, breed):
        # Instance variables: Unique to each instance of the class
        self.name = name
        self.breed = breed

    def display_details(self):
        """Method to display the details of the dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        

# Create an instance of the Dog class for the first dog
dog1 = Dog("Buddy", "Golden Retriever")

# Create an instance of the Dog class for the second dog
dog2 = Dog("Max", "German Shepherd")

# Display details for both dogs using the display_details method
print("Details of the first dog:")
dog1.display_details()

print("Details of the second dog:")
dog2.display_details()