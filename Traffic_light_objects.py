""" A dictionary with the all lanes and lanes they can combine with """

traffic_dict = {
    "SouthLeft": ["SouthStraight", "SouthRight", "EastRight", "NorthLeft", "WestRight"],
    "SouthStraight": ["SouthLeft", "SouthRight", "NorthStraight", "NorthRight", "WestRight"],
    "SouthRight": ["SouthLeft", "SouthStraight", "EastLeft", "EastStraight", "EastRight", "NorthStraight",
                   "NorthRight", "WestLeft", "WestRight"],

    "EastLeft": ["EastStraight", "EastRight", "NorthRight", "WestLeft", "SouthRight"],
    "EastStraight": ["EastLeft", "EastRight", "WestStraight", "WestRight", "SouthRight"],
    "EastRight": ["EastLeft", "EastStraight", "NorthLeft", "NorthStraight", "NorthRight", "WestStraight",
                  "WestRight", "SouthLeft", "SouthRight"],

    "NorthLeft": ["NorthStraight", "NorthRight", "WestRight", "SouthLeft", "EastRight"],
    "NorthStraight": ["NorthLeft", "NorthRight", "SouthStraight", "SouthRight", "EastRight"],
    "NorthRight": ["NorthLeft", "NorthStraight", "WestLeft", "WestStraight", "WestRight", "SouthStraight",
                   "SouthRight", "EastLeft", "EastRight"],

    "WestLeft": ["WestStraight", "WestRight", "SouthRight", "EastLeft", "NorthRight"],
    "WestStraight": ["WestLeft", "WestRight", "EastStraight", "EastRight", "NorthRight"],
    "WestRight": ["WestLeft", "WestStraight", "SouthLeft", "SouthStraight", "SouthRight", "EastStraight",
                  "EastRight", "NorthLeft", "NorthRight"]
}
