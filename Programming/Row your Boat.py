class Passenger:
    def __init__(self, name):
        self.name = name

class Boat:
    def __init__(self, name, number_of_engine, capacity):
        self.name = name
        self.number_of_engine = number_of_engine
        self.capacity = capacity
        self.people_list = []

        print("Boat name:", self.name)
        print("Number of engines:", self.number_of_engine)
        print("Capacity:", self.capacity)

    def travel(self):
        self.dest = input("Select a destination: ")
        try:
            self.no_of_passengers = int(input("How many passengers? "))
        except ValueError:
            print("Invalid number.")
            exit()

        if self.no_of_passengers <= 0:
            print("Invalid number of passengers.")
            exit()
        elif self.no_of_passengers > self.capacity:
            print("This number exceeds our capacity.")
            exit()

        for i in range(self.no_of_passengers):
            name = input(f"Passenger {i + 1}'s name: ")
            passenger = Passenger(name)
            self.people_list.append(passenger)

        print("Passenger List:")
        for p in self.people_list:
            for i in range(self.no_of_passengers):
                print(f"{i+1}.", p.name)

boat = Boat("Serenity", 2, 30)
boat.travel()