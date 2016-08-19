"""import csv
import os

mydict = {
    "name2" : "pass2",
    "name3" : "pass3"
#     ...
}

csv_file = 'cities.csv'  # file to be updated
tempfilename = os.path.splitext(csv_file)[0] + '.bak'
try:
    os.remove(tempfilename)  # delete any existing temp file
except OSError:
    pass
os.rename(csv_file, tempfilename)

# create a temporary dictionary from the input file
with open(tempfilename, mode='rb') as infile:
    reader = csv.reader(infile, skipinitialspace=True)
    header = next(reader)  # skip and save header
    temp_dict = {row[0]: row[1] for row in reader}

# only add items from my_dict that weren't already present
temp_dict.update({key: value for (key, value) in mydict.items()
                      if key not in temp_dict})

# create updated version of file
with open(csv_file, mode='wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(temp_dict.items())

os.remove(tempfilename)  # delete backed-up original

import csv

with open('cities.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    populations = []
    cities = []
    for row in readCSV:
        city = row[1]
        population = row[3]

        populations.append(population)
        cities.append(city)

    print("The Following are the available cities")
    print(cities)
print("............................................")
print("Enter a new City")

def csv_writer(data_list, file_path):
    file_p = open(file_path, "r+")
    reader_pattern = csv.reader(file_p, delimiter=",", quotechar="$")
    write_pattern = csv.writer(file_p, delimiter=",", quotechar="$")

    content = list(reader_pattern)

    file_p.seek(1)
    write_pattern.writerow(data_list)
    write_pattern.writerows(content)
    file_p.truncate()
    file_p.close()

data_list = [input("Enter rank: "), input("Enter city: "), input("Enter County/State: "), input("Enter population: ")]

csv_writer(data_list,'cities.csv')
"""
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

