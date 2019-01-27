import sys
import csv
import os
import io


def startwriting(fjson, country, city, lat, lon, code):

    try:
        print(pop)
        fjson.write('{"ccode":')
        fjson.write('"')
        fjson.write(country)
        fjson.write('"')
        fjson.write(',')

        fjson.write('"city":')
        fjson.write('"')
        fjson.write(city)
        fjson.write('"')
        fjson.write(',')

        fjson.write('"lat":')
        fjson.write('"')
        fjson.write(lat)
        fjson.write('"')
        fjson.write(',')

        fjson.write('"long":')
        fjson.write('"')
        fjson.write(lon)
        fjson.write('"')
        fjson.write(',')

        fjson.write('"code":')
        fjson.write('"')
        fjson.write(code)
        fjson.write('"')
        fjson.write('},')
        fjson.write('\n')
        fjson.close()
    except UnicodeEncodeError:
        print('passing')


maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

locationBuffer = open('x:\\geolocation\\worldcitiespop.csv', 'r', encoding='utf-8')
#locationBuffer = open('e:\\worldcitiespopNEW.txt', 'r', encoding='utf-16')
extractor = csv.reader(locationBuffer)
header = next(extractor)
countryIndex = header.index('Country')
cityIndex = header.index('City')
codeIndex = header.index('Region')
popIndex = header.index('Population')
latIndex = header.index('Latitude')
longIndex = header.index('Longitude')
print('countryIndex ', countryIndex)

fjson: io.TextIOWrapper

fjson = open('z:\\geolocation\\a.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\b.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\c.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\d.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\e.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\f.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\g.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\h.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\i.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\j.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\k.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\l.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\m.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\n.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\o.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\p.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\q.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\r.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\s.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\t.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\u.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\v.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\w.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\x.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\y.json', 'w+')
fjson.write('[')
fjson.close()

fjson = open('z:\\geolocation\\z.json', 'w+')
fjson.write('[')
fjson.close()
for row in extractor:

    country = row[countryIndex]
    city = row[cityIndex]
    code = row[codeIndex]
    lat = row[latIndex]
    lon = row[longIndex]
    pop = row[popIndex]

    if city.find('a') == 0:
        fjson = open('z:\\geolocation\\a.json', 'a', newline="")
        # print(fjson.__class__.__name__)

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('b') == 0:
        fjson = open('z:\\geolocation\\b.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('c') == 0:
        fjson = open('z:\\geolocation\\c.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('d') == 0:

        fjson = open('z:\\geolocation\\d.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('e') == 0:
        fjson = open('z:\\geolocation\\e.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('f') == 0:
        fjson = open('z:\\geolocation\\f.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('g') == 0:
        fjson = open('z:\\geolocation\\g.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('h') == 0:
        fjson = open('z:\\geolocation\\h.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('i') == 0:
        fjson = open('z:\\geolocation\\i.json', 'a', newline="")
        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('j') == 0:
        fjson = open('z:\\geolocation\\j.json', 'a', newline="")
        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('k') == 0:
        fjson = open('z:\\geolocation\\k.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('l') == 0:
        fjson = open('z:\\geolocation\\l.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('m') == 0:
        fjson = open('z:\\geolocation\\m.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('n') == 0:
        fjson = open('z:\\geolocation\\n.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('o') == 0:
        fjson = open('z:\\geolocation\\o.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('p') == 0:
        fjson = open('z:\\geolocation\\p.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('q') == 0:
        fjson = open('z:\\geolocation\\q.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)

    elif city.find('r') == 0:
        fjson = open('z:\\geolocation\\r.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('s') == 0:
        fjson = open('z:\\geolocation\\s.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('t') == 0:
        fjson = open('z:\\geolocation\\t.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('u') == 0:
        fjson = open('z:\\geolocation\\u.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('v') == 0:
        fjson = open('z:\\geolocation\\v.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)
    elif city.find('x') == 0:
        fjson = open('z:\\geolocation\\x.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)

    elif city.find('y') == 0:
        fjson = open('z:\\geolocation\\y.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)

    elif city.find('w') == 0:
        fjson = open('z:\\geolocation\\w.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)

    elif city.find('z') == 0:
        fjson = open('z:\\geolocation\\z.json', 'a', newline="")

        if len(pop) > 2:
            startwriting(fjson, country, city, lat, lon, code)

fjson = open('z:\\geolocation\\a.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\b.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\c.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\d.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\e.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\f.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\g.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\h.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\i.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\j.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\k.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\l.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\m.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\n.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\o.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\p.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\q.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\r.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\s.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\t.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\u.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\v.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\w.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\x.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\y.json', 'a', newline="")
fjson.write(']')
fjson.close()

fjson = open('z:\\geolocation\\z.json', 'a', newline="")
fjson.write(']')
fjson.close()
locationBuffer.close()





