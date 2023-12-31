class Truck2:
    def __init__(self, truck_id, capacity):
        self.truck_id = truck_id
        self.truckPackages = []
        self.capacity = capacity
        self.truckDistanceMatrix = []  # For the distance matrix specific to this truck's route
        self.truckDistanceAddresses = []  # For addresses corresponding to the packages on this truck
        self.truckPackagesBestTour = []  # For the best delivery order after optimization
        # self.driver = driver
        # self.current_load = 0
        # self.current_route = []

    def load_package(self, package_id):
        if self.current_load < self.capacity:
            self.current_route.append(package_id)
            self.current_load += 1
        else:
            print(f"Truck {self.truck_id} is full. Cannot load more packages.")

    def unload_package(self, package_id):
        if package_id in self.current_route:
            self.current_route.remove(package_id)
            self.current_load -= 1

    def assign_route(self, route):
        if len(route) <= self.capacity:
            self.current_route = route
            self.current_load = len(route)
        else:
            print(f"Route exceeds capacity of Truck {self.truck_id}. Cannot assign route.")

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return (f"Truck ID: {self.truck_id}, Capacity: {self.capacity}, "
                f"Current Load: {self.current_load}, Status: {self.status}, "
                f"Driver: {self.driver}, Route: {self.current_route}")