import math
import numpy as np
import pandas
import sqlite3
import os
import os.path


def convert_insight_to_fedex(file_name, csv_file):
    # list the columns in the array below that you would like to keep in the file
    # list_of_columns = ["V3", "V4", "V10", "V13", "V15", "V16", "V17", "V21", "V26", "V27", "V28"]
    #file_name = csv_file[list_of_columns]
    file_name = csv_file
    fedex.append(file_name)

def convert_newgistics_to_newgistics(file_name, csv_file):
    # list the columns in the array below that you would like to keep in the file
    # list_of_columns = ["V3", "V4", "V10", "V13", "V15", "V16", "V17", "V21", "V26", "V27", "V28"]
    #file_name = csv_file[list_of_columns]
    file_name = csv_file
    newgistics.append(file_name)

def convert_outbound_to_ups(file_name, csv_file):
    # list the columns in the array below that you would like to keep in the file
    # list_of_columns = ["V3", "V4", "V10", "V13", "V15", "V16", "V17", "V21", "V26", "V27", "V28"]
    #file_name = csv_file[list_of_columns]
    file_name = csv_file
    ups.append(file_name)

def create_connection (db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close


if __name__ == "__main__":
    conn = sqlite3.connect("Canals.db")
    c = conn.cursor()

    # comment
    c.execute('''DROP TABLE IF EXISTS results ''')
    # comment these: creates columns with column names col1, col2, col3, colEtc in DB "SanchitsDatabaseOfShippingData.db"
    c.execute('''CREATE TABLE results (TrackingNumber real, RefNumber char, ServiceType text, DeliveryDate text,
                DeliveryTime text, DestinationCity text, DestinationState text, DestinationZip text,
                DestinationCountry text, ShipperCity text, ShipperStateProvince text, ShipperPostal text,
                ShipperCountry text)''')

    TrackingNumber=[]
    RefNumber=[]
    ServiceType=[]
    DeliveryDate=[]
    DeliveryTime=[]
    DestinationCity=[]
    DestinationState=[]
    DestinationZip=[]
    DestinationCountry=[]
    ShipperCity=[]
    ShipperStateProvince=[]
    ShipperPostal=[]
    ShipperCountry=[]

    # comment
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".csv"):
        rawdata = pandas.read_csv(filename, dtype={'Tracking.Number': np.str,'Reference.Number': np.str,
                                        'DeliveryDate': np.str,'Origin Address': np.str,'Origin.City': np.str,
                                    'Recipient.City': np.str, 'Recipient.State': np.str, 'Recipient.Zip': np.str,
                                 'ShipperCity': np.str,'ShipperStateProvince': np.str,'ShipperPostal': np.str,
                                'ShipperCountry': np.str,})
     #   print(rawdata.columns.tolist())


# the following lines just connect to the directory that holds the csv's
desktop = os.path.join(os.path.expanduser("~"), "Documents", "canal_routes", "canal_route_times", "csv")
os.chdir(desktop)

csv_files = os.listdir(desktop)
number_of_csvs = len(csv_files)
# print(csv_files)


# if title has "insight" --> fedex
# if title has "Newgistics" --> newgistics
# if title has "outbound" --> ups

x1 = 0
x2 = 0
x3 = 0
string1 = "InSight"
string2 = "Newgistics"
string3 = "Outbound"

# initialize arrays to hold csv names for later use
fedex_names = []
newgistics_names = []
ups_names = []

# initialize arrays to hold combined csvs (as dataframes)
fedex = []
newgistics = []
ups = []




for i in range(number_of_csvs):
    if "InSight" in csv_files[i]:
        x1 +=1
        name = string1 + str(x1)
        fedex_names.append(name)
        convert_insight_to_fedex(name, pandas.read_csv(csv_files[i]))

    elif "Newgistics" in csv_files[i]:
        x2 += 1
        name = string2 + str(x2)
        newgistics_names.append(name)
        convert_newgistics_to_newgistics(name, pandas.read_csv(csv_files[i]))

    elif "outbound" in csv_files[i]:
        x3 += 1
        name = string3 + str(x3)
        ups_names.append(name)
        convert_outbound_to_ups(name, pandas.read_csv(csv_files[i]))




