#Create class
class Vechile:

    #Create init methood
    def __init__(self,max_speed,mileage):

        #Bind the arguments
        self.max_speed=max_speed
        self.mileage=mileage

#Object creation
modelX= Vechile(240,18)

#Access the variables inside init methood
print("Model Max Speed: ",modelX.max_speed)
print("Model Mileage: ",modelX.mileage)