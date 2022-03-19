import asyncio
import dotenv
import logging
import os
import sys
from pyracing_wpm.response_objects import career_stats, chart_data, iracing_data,upcoming_events, historical_data, session_data
import unittest
import datetime
from pyracing_wpm.client import Client
from pyracing_wpm import constants
import asyncio
import json

        
def GetCars(username, password, driver, quarter, year):
    ir = Client(username, password)
    global car
    async def main():              
        result_list = await ir.event_results(driver,quarter,year=year,data_format='json',category=constants.Category.road.value,sort=constants.Sort.start_time.value,show_races=1,show_tts=1,show_ops=1)
        cars=[]
        for result in result_list:
            subsession_id=str(result.subsession_id)
            car=str(result.car_id)
            car_class_id=str(result.car_class_id)

            car_class = await ir.car_class(car_class_id)
            car = car_class.cars[0].name
            cars.append(car)
        cars = list(dict.fromkeys(cars))
        GetCars.cars = cars
    asyncio.run(main())

def test():    
    global x
    test.x=1