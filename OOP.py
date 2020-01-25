# # creating a class
#
# class Car:
#     # class atribute
#     make = "Toyota"


class Laptop():
    model = "HP"

    # switch on
    def switch(self):
        print("=====loading========")


    # switch off
    def switch_off(self):
        print("-------switching off-------------")


    # display wallpaper
    def play_music(self):
        print("Picture")





hp_elite = Laptop()
hp_elite.RAM = "2GB"
hp_elite.HDD = "500 GB"
hp_elite.Screen_size = "11 inch"

hp_pavilion = Laptop()
hp_pavilion.RAM = "2GB"
hp_pavilion.HDD = "250 GB"
hp_pavilion.Screen_size = "10 inch"

hp_envy = Laptop()
hp_envy.RAM = "2GB"
hp_envy.HDD = "1 TB"
hp_envy.Screen_size = "10 inch"

hp_probook = Laptop()
hp_probook.RAM = "2GB"
hp_probook.HDD = "750 GB"
hp_probook.Screen_size = "15 inch"

hp_elite.switch()
hp_elite.switch_off()



class Person:

    def __init__(self, name, age, weight):  # constructor is a function that calls itself the minute you call and instance.
        self.theName = name
        self.theAge = age
        self.theWeight = weight

    #update age
    def update_age(self,newAge):
        self.theAge = newAge

    def update_name(self,newName):
        self.theName = newName


Paul = Person("Kanyi", 20, 45)

print("initial age:", Paul.theAge)
Paul.update_age(40)
print("Current age:", Paul.theAge)

print("initial name:", Paul.theName)
Paul.update_name("Mark")
print("The current name:", Paul.theName)


# inheritance abstruction polymophysm and encapsulation
