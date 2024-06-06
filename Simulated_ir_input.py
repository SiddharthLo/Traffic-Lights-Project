""" A simulation script which simulates input from the ir sensors """

import random

lane_dict = {
    "SouthLeft": 0,
    "SouthStraight": 0,
    "SouthRight": 0,
    "EastLeft": 0,
    "EastStraight": 0,
    "EastRight": 0,
    "NorthLeft": 0,
    "NorthStraight": 0,
    "NorthRight": 0,
    "WestLeft": 0,
    "WestStraight": 0,
    "WestRight": 0
}

gpio_dict = {
    "gpio1": "SouthLeft",
    "gpio2": "SouthStraight",
    "gpio3": "SouthRight",
    "gpio4": "EastLeft",
    "gpio5": "EastStraight",
    "gpio6": "EastRight",
    "gpio7": "NorthLeft",
    "gpio8": "NorthStraight",
    "gpio9": "NorthRight",
    "gpio10": "WestLeft",
    "gpio11": "WestStraight",
    "gpio12": "WestRight"
}


def simulation_ir_counter():
    for i in range(50):
        rnd = random.randint(1, 12)
        gpio_id = "gpio" + str(rnd)
        lane = gpio_dict[gpio_id]
        lane_dict[lane] += 1
    print(lane_dict)


simulation_ir_counter()
