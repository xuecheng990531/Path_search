import xml.etree.ElementTree as ET
import csv
import unicodedata

tree = ET.parse('file/test.kml')
root = tree.getroot()

placeDict = dict.fromkeys(["name","lat","lng"],"")

outputFileName = "test.csv"
f = open(outputFileName, "w")
w = csv.DictWriter(f, placeDict.keys())
w.writeheader()

for line in root.iter('*'):

    #name
    if line.tag == '{http://www.opengis.net/kml/2.2}name':
        nameArray = line.text.split("-")
        if len(nameArray) == 2:
            if unicodedata.east_asian_width(nameArray[0][0]) != "Na":
                placeDict["name_jp"] = nameArray[0]
                placeDict["name_en"] = nameArray[1]
            else:
                placeDict["name_en"] = nameArray[0]
                placeDict["name_jp"] = nameArray[1]
        else:
            if unicodedata.east_asian_width(nameArray[0][0]) != "Na":
                placeDict["name_jp"] = line.text
                placeDict["name_en"] = ""
            else:
                placeDict["name_en"] = line.text
                placeDict["name_jp"] = ""

    #description
    if line.tag == '{http://www.opengis.net/kml/2.2}description':
        placeDict["description"] = line.text

    #coordinates
    if line.tag == '{http://www.opengis.net/kml/2.2}coordinates':
        coordArray = line.text.split(",")
        placeDict["lng"] = coordArray[0]
        placeDict["lat"] = coordArray[1]

        w.writerow(placeDict)
        placeDict["description"] = ""

f.close()