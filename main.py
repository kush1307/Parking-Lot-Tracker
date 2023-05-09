class ParkingLotTracker:

    def __init__(self, data={}):
        self.data = data
        self.spot_n = 1

    def assign_parking_spot(self, vehicle_num):
        """
        Function to assign latest parking spot to the vehicle coming in.
        """

        if self.data.get("available_spot")[0] > self.data.get("levels") - 1:
            return "Parking is FULL."

        if self.data.get("vehicle_spot").get(vehicle_num):
            return "Vehicle with this number already parked in the parking."

        self.data.get("parking_data")[self.data.get("available_spot")[0]][
            self.data.get("available_spot")[1]] = vehicle_num
        self.data.get("vehicle_spot")[vehicle_num] = {"level": self.data.get(
            "parking_level_names")[self.data.get("available_spot")[0]], "spot": self.spot_n}
        self.spot_n += 1

        if self.data.get("available_spot")[1] < self.data.get("size") - 1:
            self.data.get("available_spot")[1] += 1

        else:
            self.data["available_spot"][0] += 1
            self.data["available_spot"][1] = 0

        return "Added!"

    def get_vehicle_parking_spot_number(self, vehicle_num):
        """
        Function to get vehicle level and spot number.
        """

        return self.data.get("vehicle_spot").get(vehicle_num, "No vehicle parked with this number.")

    def print_parking(self):
        for level in self.data.get("parking_data"):
            print(level)

data = {
    "levels": 2,
    "size": 3,
    "parking_data": [[""] * 3, [""] * 3],
    "parking_level_names": {0: "A", 1: "B"},
    "parking_level_size": {},
    "available_spot": [0, 0],
    "emptied_spot": [],
    "vehicle_spot": {}
}

park = ParkingLotTracker(data=data)

while True:
    park_choice = int(input(
        "1. Please Assign me a parking slot.\n2. Please tell me where my vehicle is located.\n3. Show Parking\n4. Exit\n\n=> "))

    if park_choice == 1:
        vehicle_num = input("Enter your vehicle number: ")
        print(park.assign_parking_spot(vehicle_num=vehicle_num))

    elif park_choice == 2:
        vehicle_num = input("Enter your vehicle number: ")
        print(park.get_vehicle_parking_spot_number(vehicle_num=vehicle_num))

    elif park_choice == 3:
        park.print_parking()

    elif park_choice == 4:
        print("Exit")
        break

    else:
        print("Please enter a valid choice.")
    print("\n\n")
