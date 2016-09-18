#Defining the main menu
def main():
    try:
        print("Choose Between Kenya and USA")
        print(">>>>>>>>>>>>>>>>>>>>>")
        print("1. Kenya")
        print("2. USA")
        print("3. Exit")
        str_choice = input("1 FOR KENYA AND 2 FOR USA: ")
        choice = int(str_choice)
        # Handling Kenyan Cities
        # Writing to Kenya File
        if (choice == 1):
            str_file = "nairobi.txt"

            def save_nairobi(city, county, population):
                try:
                    file = open(str_file, "a")
                    file.write("%16s%16s%16f\n" % (city, county, population))
                    file.close()
                except Exception:
                    print("Error")

                # Reading from the Kenya file

            def read_nairobi():
                file = open(str_file, "r")
                for line in file:
                    (city, county, population) = line.split()
                    print("%s" % (city) + " " + "%s" % (county) + " " + "%f" % float(population))

                    # Menu Options for Kenya Cities

            another = "Y"
            while another == "Y" or another == "y":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Kenya's Data Of Cities.")
                print("Choose an option Below")
                print("1. Add a City")
                print("2. View the Cities")
                print("3. Most and Least Populated Cities")
                print("4. With over 300,000 People")
                str_choose = input("Choose an Option from the above Menu: ")
                chosen = int(str_choose)

                # Users adding cities into Kenya Data
                if (chosen == 1):
                    city = input("Enter city: ")
                    county = input("Enter county: ")
                    population_str = input("Enter population: ")
                    population_str = float(population_str)
                    save_nairobi(city, county, population_str)

                    # Reading the List of Kenyan Data
                elif (chosen == 2):
                    read_nairobi()

                    # Finding the Most and least populatd cities
                elif (chosen == 3):
                    def conversion(num):
                        try:
                            num = float(num)
                            return True
                        except Exception:
                            return False

                    with open('nairobi.txt', 'r') as f:
                        numbers = [float(num) for line in f for num in line.split() if conversion(num)]
                    minim = 99999999999999
                    maximum = -99999999999999
                    if numbers:
                        if max(numbers) > maximum:
                            maximum = max(numbers)
                        if min(numbers) < minim:
                            minim = min(numbers)
                            print("Most Populated City:" + str(maximum))
                            print("Least Populated City:" + str(minim))

                            # finding cities in Kenya with more than 300,000 in Population
                elif (chosen == 4):
                    with open("nairobi.txt", "r") as n:
                        try:
                            for line in n:
                                row = line.split()
                                population = row[2]
                                city = row[0]
                                if float(population) >= 300000:
                                    print(city, population)
                        except Exception:
                            print("There was an error handling your request")


                                # Prompting the user for further action
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                another = input("Perform another task? Y/N: ")
                if another == "N" or another == "n":
                    return main()

                    # Handling Data in the USA Cities
        elif (choice == 2):
            str_files = "newyork.txt"
            def save_newyork(city, county, population):
                try:
                    file = open(str_files, "a")
                    file.write("%16s%16s%16f\n" % (city, county, population))
                    file.close()
                except Exception:
                    print("There was an error handling your request")

            def read_newyork():
                file = open(str_files, "r")
                for line in file:
                    (city, county, population) = line.split()
                    print("%s" % (city) + " " + "%s" % (county) + " " + "%f" % float(population))

            next = "Y"
            while next == "Y" or next == "y":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("USA Data of Cities.")
                print("Choose an option Below")
                print("1. Add a City")
                print("2. View the Cities")
                print("3. Most and Least Populated Cities")
                print("4. Cities with More that One Million Population")
                print("5. Within 30000 of each other")
                str_selct = input("Choose an Option from the above Menu: ")
                slctd = int(str_selct)

                if (slctd == 1):
                    city = input("Enter city: ")
                    county = input("Enter county: ")
                    population_str = input("Enter population: ")
                    population_str = float(population_str)
                    save_newyork(city, county, population_str)
                elif (slctd == 2):
                    read_newyork()
                elif (slctd == 3):
                    def conversion(num):
                        try:
                            num = float(num)
                            return True
                        except Exception:
                            return False

                    with open('newyork.txt', 'r') as f:
                        numbers = [float(num) for line in f for num in line.split() if conversion(num)]
                        minim = 99999999999999
                        maximum = -99999999999999
                        if numbers:
                            if max(numbers) > maximum:
                                maximum = max(numbers)
                                if min(numbers) < minim:
                                    minim = min(numbers)
                                    print("Most Populated City:" + str(maximum))
                                    print("Least Populated City:" + str(minim))
                elif (slctd == 4):
                    with open("newyork.txt", "r") as n:
                        try:
                            for line in n:
                                row = line.split()
                                population = row[3]
                                city = row[0]
                                if float(population) >= 1000000:
                                    print(city, population)
                        except Exception:
                            print("There was an error handling your request")

                elif (slctd == 5):
                    with open("newyork.txt", "r") as n:
                        try:
                            for line in n:
                                row = line.split()
                                city = row[0]
                                population = row[2]
                                # if float(population) in range(1000000, 2000000):
                                if float(population) <= 1000000:
                                    print(city, population)
                        except Exception:
                            print("There was an error handling your request")

                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                next = input("Perform another task? Y for Yes or N for No: ")
                if next == "N" or next == "n":
                    return main()

                    # Closing the Program
        elif (choice == 3):
            print("Thank you for Passing by.\n Goodbye!")
            exit()
    except Exception:
        print("Error")
main()

