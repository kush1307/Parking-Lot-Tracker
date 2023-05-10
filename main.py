import constants


class ParkingLotTracker:
    """
    ParkingLotTracker application that assigns parking spot to incoming vehicle and
    retrieves level and spot number based on vehicle number.
    """

    def __init__(self, data={}):
        self.data = data
        self.spot_n = 1

    def assign_parking_spot(self, vehicle_num):
        """
        Function to assign latest parking spot to the vehicle coming in.
        """

        if self.data.get("available_spot")[0] > self.data.get("levels") - 1:
            return constants.PARKING_FULL

        if self.data.get("vehicle_spot").get(vehicle_num.strip().lower()):
            return constants.ALREADY_EXISTS

        self.data.get("parking_data")[self.data.get("available_spot")[0]][
            self.data.get("available_spot")[1]] = vehicle_num.strip().lower()
        self.data.get("vehicle_spot")[vehicle_num.strip().lower()] = {"level": self.data.get(
            "parking_level_names")[self.data.get("available_spot")[0]], "spot": self.spot_n}
        self.spot_n += 1

        if self.data.get("available_spot")[1] < self.data.get("size") - 1:
            self.data.get("available_spot")[1] += 1

        else:
            self.data["available_spot"][0] += 1
            self.data["available_spot"][1] = 0

        return constants.SUCCESS

    def get_vehicle_parking_spot_number(self, vehicle_num):
        """
        Function to get vehicle level and spot number.
        """

        return self.data.get("vehicle_spot").get(vehicle_num, constants.NO_VEHICLE)

    def print_parking(self):
        """
        Function to print parking level stats.
        """

        for level in self.data.get("parking_data"):
            print(level)


n = 20 # Number of parking spots on each level.
data = {
    "levels": 2,
    "size": n,
    "parking_data": [[""] * n, [""] * n],
    "parking_level_names": {0: "A", 1: "B"},
    "available_spot": [0, 0],
    "vehicle_spot": {}
}

park = ParkingLotTracker(data=data)

while True:
    try:
        park_choice = int(input(constants.PARK_CHOICE))
    except ValueError as e:
        print(constants.INVALID_INPUT)
        continue

    if park_choice == 1:
        vehicle_num = input(constants.VEHICLE_NUM_INPUT)
        print(park.assign_parking_spot(vehicle_num=vehicle_num))

    elif park_choice == 2:
        vehicle_num = input(constants.VEHICLE_NUM_INPUT)
        print(park.get_vehicle_parking_spot_number(vehicle_num=vehicle_num))

    elif park_choice == 3:
        park.print_parking()

    elif park_choice == 4:
        print(constants.EXIT)
        break

    else:
        print(constants.INVALID_CHOICE)
    print("\n\n")
