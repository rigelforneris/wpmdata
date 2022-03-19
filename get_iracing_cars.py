import wpmdata,sys,re

username = 'frost.gurren@gmail.com'
password = 'T9qmZV9fGx3V!vi'

year = sys.argv[1]
season = sys.argv[2]

#year = input("Digite o ano")
#season = input("Digite a temporada")

car_list = open("data/car_list", "r")
driver_list = open("data/driver_list", "r")

cars_array=[]

for drivers in driver_list:
    driver = drivers.strip()
    #print("reading driver "+driver)
    wpmdata.GetCars(username,password,driver,season,year)
    for car in wpmdata.GetCars.cars: 
        cars_array.append(car)
cars_array = list(dict.fromkeys(cars_array))

for car in cars_array:
    for car_compare in car_list:
        car_compare = car_compare.strip()
        carfind=re.search(car_compare,car)
        if carfind:
            print("Car "+car+" found on cars setup base!")
        if not carfind:
            print("Warning: car "+car+" NOT found on cars setup base!")


#print(cars_array)