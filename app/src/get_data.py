import urllib3, sys, geojson
from bs4 import BeautifulSoup
from geojson import Point, Feature, FeatureCollection

def main():

    url = "https://wiki.osgeo.org/wiki/Edu_current_initiatives#Current_members_of_the_Geo_for_All_Labs_Network"

    data = []

    print("Downloading web page...")

    beautiful = urllib3.PoolManager().request('GET', url).data

    soup = BeautifulSoup(beautiful, "html.parser")

    print("Scraping data...")

    a = soup.find_all('table')

    table = a[0]

    rows = table.find_all('tr')


    for row in rows:
        cols = row.find_all("td")
        cols = [ele for ele in cols]
        data.append([ele for ele in cols])
    # print(data[1])
    # ----- Format of "data" --------
    # 1 - Laboratory name, 2 - City, 3 - Country, 4 - Continent, 5 - Coordinates(long, lat), 
    # 6 - Application recieved / announced, 7 - Notes(specify category etc), 8 - Contact names, 9 - Contact emails

    records = []

    for record in data:
        if(len(record)>0):
            # Organization
            labname = record[1].text.strip()
            laburl = ''
            try:
                laburl = record[1].find('a').get('href')
            except:
                pass

            print(laburl)
            # City
            city = record[2].text.strip()
            # Country
            country = record[3].text.strip()
            # Continent
            continent = record[4].text.strip()
            # Application status
            applicationstatus = record[6].text.strip()
            # Notes
            notes = record[7].text.strip()
            # Contact names
            names = record[8].text.strip()
            # Contact emails
            emails = record[9].text.strip()

            # Long, lat
            geolocation = record[5].text.strip()
            if(geolocation==u''):
                continue
            longitude = float(geolocation.split(',')[0])
            latitude = float(geolocation.split(',')[1])
            # print(name+" "+latitude+" "+longitude)
            records.append([labname, longitude, latitude, city, country, continent, applicationstatus, notes, names, emails, laburl])

    # print(MultiPoint(geo))

    myFeatures = []

    # ------- Format of "records" ------------
    # 0 - organisation, 1 - long, 2 - lat, 3 - city, 4 - country, 5 - continent, 6 - applicationstatus, 7 - notes,
    # 8 - names, 9 - emails

    for record in records:
        myPoint = Point((record[1], record[2]))
        myFeature = Feature(geometry=myPoint, properties={"Laboratory":record[0], "City":record[3], "Country":record[4], "Continent":record[5], "Application":record[6]
                                                        , "Notes (specify category etc)":record[7], "Contact names":record[8], "Contact emails":record[9], "url":record[10]})
        # myFeature = Feature(geometry=myPoint, properties={"Organisation":record[0]})
        myFeatures.append(myFeature)

    myFeatureCollection = FeatureCollection(myFeatures)
    print("Writing data...")
    with open("data/data.geojson", 'w') as out:
        out.write(geojson.dumps(myFeatureCollection, sort_keys=True))
    print("Done")

if __name__ == '__main__':
    main()