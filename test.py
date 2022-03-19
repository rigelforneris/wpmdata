import re

find = 0
car_list = open("data/car_list", "r")
filepath = 'data/car_list'
cars_array=['iRacing Formula iR-04', 'Cadillac CTS-V Racecar', 'McLaren MP4-12C GT3', 'Porsche 718 Cayman GT4 Clubsport MR', 'Porsche 911 GT3 Cup (992)','CARRO DO DEMONIO1','12313']

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