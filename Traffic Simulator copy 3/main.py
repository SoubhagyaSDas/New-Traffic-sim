import os
import platform
import time
from map import Map
from gui import MetricGUI
from traffic import TrafficLight
from dynamic_road_item import TrafficLight as TL
from sui import *
from super import *





def main():
    sim_input = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()
    cm = CharMatrix()

    uptown = sim_input.create_road("Uptown", 0, -0.09, 0.180, Heading.North)
    map_obj.add_road(uptown)

    traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=1, green_duration=3)
    traffic_light2 = TrafficLight(mile_marker=80, green_duration=5, yellow_duration=2, red_duration=3)
    uptown.add_road_item(traffic_light1)
    uptown.add_road_item(traffic_light2)
    traffic_lights = [traffic_light1, traffic_light2]

    timer = Timer(1)
    timer.start(traffic_lights,map_obj,cm,cp)

if __name__ == "__main__":
    main()