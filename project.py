str_file = "cities.txt"

def save_cities(city, county, population):
    file = open(str_file, "a")
    file.write("%16s%16s%16f\n"%(city, county, population))
    file.close()

def read_cities():
    file = open(str_file, "r")
    for line in file:
        (city, county, population) = line.split()
        print("%s"%(city)+" "+"%s"%(county)+" "+"%f"%float(population))

print("Data of Kenyan Cities")
print(">>>>>>>>>>>>>>>>>>>>>")
print("1. Add a City")
print("2. View the Cities")
print("3. Most and Least Populated Cities")
print("4. Top 5 most Populated")
str_choice = input("Choose an Option from the above Menu: ")
choice = int(str_choice)

if(choice == 1):
    city = input("Enter city: ")
    county = input("Enter county: ")
    population_str = input("Enter population: ")
    population_str = float(population_str)
    save_cities(city,county,population_str)
elif(choice ==2):
    read_cities()
elif(choice ==3):
    def conversion(num):
        try:
            num=float(num)
            return True
        except Exception:
            return False
    with open('cities.txt', 'r') as f:
       numbers=[float(num) for line in f for num in line.split() if conversion(num)]
    minim = 99999999999999
    maximum= -99999999999999
    if numbers:
        if max(numbers)>maximum:
            maximum=max(numbers)
        if min(numbers)<minim:
           minim=min(numbers)
           print("Most Populated City:" + str(maximum))
           print ("Least Populated City:" + str(minim))
elif(choice == 4):
    print("The Top 5 Most Populated Cities")




