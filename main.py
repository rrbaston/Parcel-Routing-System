from hash_table import HashTable
from package import Package
from truck import Truck
from data_loader import (
    loadDistanceData,
    loadAddressData, 
    loadPackageData, 
    get_distance_between, 
    displayDistanceData,
    displayAddressData
)


hash_table = HashTable(size=10)  # Create a HashTable instance
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv') # Load HashTable with package data
# hash_table.display()

distanceData = loadDistanceData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-distance-matrix.csv') # Load distance matrix data
# displayDistanceData(distanceData)
addressData, address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv') # Load address data
# displayAddressData(addressData)

#Test
address1 = "1060 Dalton Ave S"  # Replace with the actual address
address2 = "195 W Oakland Ave"  # Replace with the actual address
distance = get_distance_between(address1, address2, address_to_index, distanceData)
print(f"The distance between {address1} and {address2} is {distance} miles.")


