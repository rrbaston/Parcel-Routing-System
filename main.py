import csv
from hash_table import HashTable
from package import Package
from truck import Truck

def loadPackageData(hash_table, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                # Assuming the CSV columns are in the order:
                # PackageID, Address, Deadline, City, Zip Code, Weight, Status
                package_id = row[0]
                address = row[1]
                city = row[2]
                zip_code = row[3]
                deadline = row[4]
                weight = row[5]
                status = row[6]
                delivery_time = None  # No delivery time in csv

                # Create a Package object
                package = Package(package_id, address, city, zip_code, deadline, weight, status, delivery_time)

                # Insert the Package object into the HashTable
                hash_table.insert(package)



hash_table = HashTable(size=10)  # Create a HashTable instance
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/Parcel-Routing-System/WGUPS-address.csv')



