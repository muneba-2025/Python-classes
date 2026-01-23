class Dog:

    def __init__(self, name, breed):
    
        self.name = name
        self.breed = breed

    def display_details(self):
        """Method to display the details of the dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        


dog1 = Dog("Buddy", "Golden Retriever")


dog2 = Dog("Max", "German Shepherd")


print("Details of the first dog:")
dog1.display_details()

print("Details of the second dog:")
dog2.display_details()