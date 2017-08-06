import math
import numpy as np
import pandas
import sqlite3
import os
import os.path

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

# current_dir = '~/Desktop/csv'
# print(len([name for name in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, name))]))

# the following lines just connect to the directory that holds the csv's
desktop = os.path.join(os.path.expanduser("~"), "Desktop", "csv")
os.chdir(desktop)
print(os.getcwd())


csv_files = os.listdir()
number_of_csvs = len(csv_files)
print(csv_files)

fedex = []
newgistics = []
ups = []
# if title has "insight" --> fedex
# if title has "Newgistics" --> newgistics
# if title has "outbound" --> ups
x = 0
for i in range(number_of_csvs):
    x += 1
    if "InSight" in csv_files[i]:
        print(csv_files[i])
    elif "Newgistics" in csv_files[i]:
        print("nuge")
    else:
        print("ups")
print(x)



# print(csv_files[i])


# everything up to this point creates a sqlite database called "Canals" --> in local /Users/kishorprasain/PycharmProjects/












###########################################################################################################

        # for i in range(0, 1000000):
        #     TrackingNumber.append(rawdata['Tracking.Number'][i])
        #     RefNumber.append(rawdata['Ref.Number'][i])
        #     # lookup in rawdata for the columne 'Charge_Amount'
        #     ServiceType.append(rawdata('Newgistics')[i])
        #     DeliveryTime.append(rawdata('Not Applicable')[i])
        #     DeliveryDate.append(rawdata('Delivery Date')[i])
        #     DestinationCity.append(rawdata['Recipient City'][i])
        #     DestinationState.append(rawdata['Recipient State'][i])
        #     DestinationZip.append(rawdata['Recipient Zip'][i])
        #     DestinationCountry.append(rawdata['United States '][i])
        #     ShipperCity.append(rawdata['Origin City'][i])
        #     ShipperStateProvince.append(rawdata['OriginState'][i])
        #     ShipperPostal.append(rawdata['Newgistics'][i])
        #     ShipperCountry.append(rawdata['United States'][i])
        #     #print(TrackingNumber)
        #
        #
        #
        #
        #     try:
        #        c.execute("insert into results values ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %
        #         (TrackingNumber[i], RefNumber[i], ServiceType[i],
        #         DeliveryDate[i], DeliveryTime[i], DestinationCity[i],DestinationState[i], DestinationZip[i], DestinationCountry[i],
        #         ShipperCity[i], ShipperStateProvince[i],ShipperPostal[i],ShipperCountry[i]))
        #
        #     except:
        #         c.execute("insert into results values (?, '%s', '%s', '%s','%s,'%s','%s','%s','%s','%s','%s','%s','%s')"
        #                   % (0, "N/A", "N/A", "N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A","N/A"))

# # c.execute("""INSERT INTO results (trackingid,proposedcost)VALUES(?, ?) """, (trackingid, proposedcost))
# # c.executemany("""INSERT INTO results ('proposedcost')VALUES(?) """, (proposedcost))
#
# conn.commit()
# conn.close()