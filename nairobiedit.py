print("Choose Between Kenya and USA")
print(">>>>>>>>>>>>>>>>>>>>>")
print("1. Kenya")
print("2. USA")
str_choice = input("1 FOR KENYA AND 2 FOR USA: ")
choice = int(str_choice)

if(choice == 1):
    str_file = "nairobi.txt"
    def save_nairobi(city, county, population):
        file = open(str_file, "a")
        file.write("%16s%16s%16f\n" % (city, county, population))
        file.close()

    def read_nairobi():
        file = open(str_file, "r")
        for line in file:
            (city, county, population) = line.split()
            print("%s" % (city) + " " + "%s" % (county) + " " + "%f" % float(population))

    another = "Y"
    while another == "Y" or another == "y":
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Kenya's Data Of Cities.")
        print("Choose an option Below")
        print("1. Add a City")
        print("2. View the Cities")
        print("3. Most and Least Populated Cities")
        print("4. Top 5 most Populated")
        str_choose = input("Choose an Option from the above Menu: ")
        chosen = int(str_choose)
        if (chosen == 1):
            city = input("Enter city: ")
            county = input("Enter county: ")
            population_str = input("Enter population: ")
            population_str = float(population_str)
            save_nairobi(city, county, population_str)
        elif (chosen == 2):
            read_nairobi()
        elif (chosen == 3):
            """textFile = open('nairobi.txt', 'r')
            numberList = []
            for line in textFile:
                numberList.append(line.split())
            #for e in numberList:
                #print(e)
            #textFile.close()

            def minimum(min):
                minimum = min(numberList)
                return minimum
            def maximum(max):
                maximum = max(numberList)
                return maximum #in range(300000)

            print ("The Least Populated City is", min(numberList))
            print ("The Most Populated City is", max(numberList))"""
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
        elif (chosen == 4):
            overthree = open("nairobi.txt", "r")
            overthree in range(4000000)
            print(overthree)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        another = input("Perform another task? Y/N: ")
        if another == "N" or another == "n":
            exit()


elif (choice == 2):
    str_files = "newyork.txt"
    def save_newyork(city, county, population):
        file = open(str_files, "a")
        file.write("%16s%16s%16f\n" % (city, county, population))
        file.close()

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
        print("4. Top 5 most Populated")
        str_selct = input("Choose an Option from the above Menu: ")
        slctd = int(str_selct)

        if (slctd == 1):
            city = input("Enter city: ")
            county = input("Enter county: ")
            population_str = input("Enter population: ")
            population_str = float(population_str)
            save_newyork(city,county,population_str)
        elif(slctd == 2):
            read_newyork()
        elif(slctd == 3):
            """textFile = open('newyork.txt', 'r')
            numberList = []
            for line in textFile:
                numberList.append(line.split())
                for e in numberList:
                    print(e)
            textFile.close()
            def minimum(min):
                minimum = min(numberList)
                return minimum
            def maximum(max):
                maximum = max(numberList)
                return maximum


            print("The Most Populated City is", min(numberList))
            print("The Least Populated City is", max(numberList))
            """
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
            #abvslct = input("Enter range of polpulation: ")
            with open("newyork.txt", "r") as n:
                for line in n:
                    row = line.split()
                    population = row[2]
                    print (population in range(300000))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        next = input("Perform another task? Y for Yes or N for No: ")
        if next == "N" or next == "n":
            exit()

