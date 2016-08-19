str_file = "cities.txt"

def save_cities(city, county, population):
    file = open(str_file, "a")
    file.write("%16s%16s%16f\n"%(city,county,population))
    file.close()

def read_cities():
    file = open(str_file, "r")
    for line in file:
        (city,county,population) = line.split()
        print("%s"%(city)+"   "+"%s"%(county)+" "+"%f"%float(population))

"""def most_populated():
    highest_population = 0
    population = open("cities.txt")
    for line in population:
        if float(line) > highest_population:
          highest_population = float(line)
        population.close()
        print("The most populated City is: ")
        print(highest_population)
"""


print("Data of Kenyan Cities")
print(">>>>>>>>>>>>>>>>>>>>>")
print("1. Add a City")
print("2. View the Cities")
print("3. Most Populated City")
print("4. Least Populated City")
str_choice = input("Choose an Option from the above Menu: ")
choice = int(str_choice)

if(choice == 1):
    city = input("Enter city: ")
    county = input("Enter county: ")
    population_str = input("Enter population: ")
    #county = float(county)
    population_str = float(population_str)
    save_cities(city,county,population_str)
elif(choice ==2):
    read_cities()
#else:(choice == 3)
#most_populated()

