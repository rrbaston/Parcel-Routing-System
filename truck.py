from data_loader import (
    loadDistanceData,
    loadAddressData, 
    loadPackageData,
    displayDistanceData,
    displayAddressData
)
from hash_table import HashTable
import datetime

class Truck:
    def __init__(self, truck_id, capacity, start_time):
        self.truck_id = truck_id
        self.capacity = capacity
        self.truckPackages = []  # Holds package IDs or package objects
        self.truckDistanceMatrix = []  # For the distance matrix specific to this truck's route
        self.truckDistanceAddresses = []  # For addresses corresponding to the packages on this truck
        self.truckPackagesBestTour = []  # For the best delivery order after optimization
        self.current_time = start_time # This assumes start_time is a datetime object

    def load_package(self, package):
        if len(self.truckPackages) < self.capacity: # If truck has space, add more packages to truck
            self.truckPackages.append(package)
        else:
            print(f"Truck {self.truck_id} is full. Cannot load more packages.")

    def unload_package(self, package_id):
        # This is a conditional clause that includes p in the new list 
        # only if the package_id of p is not equal to the package_id we want to remove.
        # It creates a new list without the removed item.
        self.truckPackages = [p for p in self.truckPackages if p.package_id != package_id]

    def truckAddressListAndDistanceMatrix(self, address_to_index, distanceData):
        # Assuming truckPackages contains package objects with an 'address' attribute
        self.truckDistanceAddresses = [pkg.address for pkg in self.truckPackages] # Load truckDistanceAddress
        self.truckDistanceMatrix = [                                              # Load truckDistanceMatrix
            [
                distanceData[address_to_index[addr1]][address_to_index[addr2]] 
                for addr2 in self.truckDistanceAddresses
            ] 
            for addr1 in self.truckDistanceAddresses
        ]
        self.truckPackagesBestTour = list(self.truckPackages)  # Initial best tour is the order of loading

    def display_truck_info(self):
        print(f"Truck ID: {self.truck_id}")
        print(f"Capacity: {self.capacity}")
        print("Packages on truck:")
        for pkg in self.truckPackages:
            print(f"  Package ID: {pkg.package_id}, Address: {pkg.address}")
        print("Current Best Tour:")
        for pkg in self.truckPackagesBestTour:
            print(f"  Package ID: {pkg.package_id}, Address: {pkg.address}")

    def load_truck_with_priorities(self, package_list):
        # Sort the package list based on the delivery deadline
        package_list.sort(key=lambda pkg: datetime.datetime.strptime(pkg.deadline, '%I:%M %p') if pkg.deadline != 'EOD' else datetime.datetime.max)

        # Filter and load packages that can only be on this truck
        truck_specific_packages = [pkg for pkg in package_list if f'Can only be on truck {self.truck_id}' in pkg.special_notes]
        for pkg in truck_specific_packages:
            if len(self.truckPackages) < self.capacity:
                self.truckPackages.append(pkg)

        # Filter and load packages that must be delivered together
        # Here we would need more logic to handle groups, this is a placeholder
        grouped_packages = [pkg for pkg in package_list if 'Must be delivered with' in pkg.special_notes]
        for pkg in grouped_packages:
            if len(self.truckPackages) < self.capacity:
                self.truckPackages.append(pkg)

        # Filter and load packages with earliest deadlines not in the special categories
        early_deadline_packages = [pkg for pkg in package_list if pkg.deadline != 'EOD' and pkg not in truck_specific_packages and pkg not in grouped_packages]
        for pkg in early_deadline_packages:
            if len(self.truckPackages) < self.capacity:
                self.truckPackages.append(pkg)

        # Filter and load delayed packages based on current time
        delayed_packages = [pkg for pkg in package_list if 'Delayed' in pkg.special_notes]
        for pkg in delayed_packages:
            delay_time_str = pkg.special_notes.split('---will not arrive to depot until ')[-1]
            delay_time = datetime.datetime.strptime(delay_time_str, '%I:%M %p').time()
            if self.current_time >= delay_time:
                if len(self.truckPackages) < self.capacity:
                    self.truckPackages.append(pkg)

        # Load EOD packages last if there's still capacity
        eod_packages = [pkg for pkg in package_list if pkg.deadline == 'EOD' and pkg not in truck_specific_packages and pkg not in grouped_packages and pkg not in delayed_packages]
        for pkg in eod_packages:
            if len(self.truckPackages) < self.capacity:
                self.truckPackages.append(pkg)


# hash_table = HashTable(size=10)  # Create a HashTable instance
# loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv') # Load HashTable with package data
# # hash_table.display()
# # Assuming 'address_to_index' is a dictionary mapping addresses to indices in 'distanceData'
# distanceData = loadDistanceData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-distance-matrix.csv') # Load distance matrix data
# # displayDistanceData(distanceData)
# addressData, address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv') # Load address data
# # displayAddressData(addressData)

# # Retrieve all packages
# all_packages = hash_table.get_all_packages()

# # Example usage of the Truck class:
# truck2 = Truck(2, 100)

# # Manually load packages based on assumptions:
# # Assuming 'package_list' is a list of package objects available for loading
# # package_list = [1, 2, 3]  # Define or load your list of packages
# # mandatory_packages = [9, 18, 27]  # Example package IDs that must go on truck 2

# # Manually load mandatory packages and other packages as needed
# for pkg in all_packages:
#     # if pkg.package_id in mandatory_packages or other_heuristic_conditions:
#         truck2.load_package(pkg)



# # Once all packages are loaded, generate the address list and distance matrix for truck 2
# truck2.truckAddressListAndDistanceMatrix(address_to_index, distanceData)

# # Display truck information
# truck2.display_truck_info()
