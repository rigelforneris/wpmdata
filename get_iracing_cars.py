import wpmdata,sys,re

find = 0

username = ''
password = ''

year = sys.argv[1]
season = sys.argv[2]

#year = input("Digite o ano")
#season = input("Digite a temporada")

#car_list = open("data/car_list", "r")
car_list = open("data/car_list", "r")
driver_list = open("data/driver_list", "r")

cars_array=[]

for drivers in driver_list:
    driver = drivers.strip()
    wpmdata.GetCars(username,password,driver,season,year)
    for car in wpmdata.GetCars.cars: 
        cars_array.append(car)
cars_array = list(dict.fromkeys(cars_array))

for car in car_list:
    car=car.rstrip('\n')
    for car_verify in cars_array:
        car_find=re.match(car,car_verify)
        if car_find:
            find+=1
    if find == 0:
        print("WARNING: Car "+car+" DOES NOT RACING IN THIS SEASON!!!")
    elif find > 0:
        print("OK, car "+car+" Racing.")
    find=0
