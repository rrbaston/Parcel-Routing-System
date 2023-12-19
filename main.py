import csv
from hash_table import HashTable
from package import Package
from truck import Truck

def loadPackageData(hash_table, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                # Assuming the CSV columns are in the order:
                # PackageID, Address, Deadline, City, Zip Code, Weight, Status
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                deadline = row[5]
                weight = row[6]
                status = row[7]
                delivery_time = None  # No delivery time in csv

                # Create a Package object
                package = Package(package_id, address, city, state, zip, deadline, weight, status, delivery_time)

                # Insert the Package object into the HashTable
                hash_table.insert(package)

hash_table = HashTable(size=10)  # Create a HashTable instance
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-package-v2.csv')
hash_table.display()


