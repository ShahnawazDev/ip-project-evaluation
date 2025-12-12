# Basic fixed values for metro system
timePerStation = 3
interchangeTime = 10
metroStart = 6 * 60
metroEnd = 23 * 60
ratePerStation = 10
ratePerLine = 30

# Reading metro file
def metroFile(fileName):
    metroData = {}
    currentLine = None

    with open(fileName, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue

            if line.startswith("[") and line.endswith("]"):
                currentLine = line[1:-1]
                metroData[currentLine] = {"stations": []}
            else:
                if currentLine is not None:
                    metroData[currentLine]["stations"].append(line)

    return metroData


# Convert names to simple format
def normalizeName(name):
    name = name.lower()
    name = name.replace("-", " ")
    name = name.replace("_", " ")
    name = name.replace("  ", " ")
    return name.strip()


# Find line and station matching
def findLineAndStation(metroInfo, userLine, userStation):
    lineName = normalizeName(userLine)
    stationName = normalizeName(userStation)

    possibleLines = []
    for line in metroInfo:
        if lineName in normalizeName(line):
            possibleLines.append(line)

    if len(possibleLines) == 0:
        for line in metroInfo:
            for st in metroInfo[line]["stations"]:
                if stationName in normalizeName(st):
                    possibleLines.append(line)
                    break

        if len(possibleLines) == 0:
            return None, None

    finalLine = possibleLines[0]

    for realStation in metroInfo[finalLine]["stations"]:
        if stationName in normalizeName(realStation):
            return finalLine, realStation

    return finalLine, None


# Convert HH:MM to minutes
def convertTime(timeString):
    hours, mins = timeString.split(":")
    return int(hours) * 60 + int(mins)


# Convert minutes to HH:MM
def convertMin(mins):
    h = mins // 60
    m = mins % 60
    return f"{h:02d}:{m:02d}"


# Find next metro time
def nextMetro(curr):
    if curr < metroStart or curr > metroEnd:
        return None

    if (8*60 <= curr <= 10*60) or (17*60 <= curr <= 19*60):
        freq = 4
    else:
        freq = 8

    first = metroStart

    if curr <= first:
        return first

    diff = curr - first
    wait = diff % freq

    if wait == 0:
        return curr
    else:
        return curr + (freq - wait)


# Decide interchange time based on rush hour
def interchangeTimeMinutes(currTime):
    if (8*60 <= currTime <= 10*60) or (17*60 <= currTime <= 19*60):
        return 12
    return 8


# Find next N metros for a station
def upcomingMetros(metroInfo, lineIn, stationIn, timeGiven, n=10):
    line, station = findLineAndStation(metroInfo, lineIn, stationIn)

    if line is None:
        return "Line not found."

    if station is None:
        return f"Station '{stationIn}' not found on line '{line}'."

    timeInMin = convertTime(timeGiven)

    if timeInMin < metroStart or timeInMin > metroEnd:
        return "No service available at this time."

    allTrains = []
    for i in range(n):
        nxt = nextMetro(timeInMin)
        if nxt is None:
            break

        allTrains.append(convertMin(nxt))
        timeInMin = nxt + 1

    return allTrains


# Time between stations on same line
def sameLineTime(lineInfo, s1, s2):
    stations = lineInfo["stations"]
    i = stations.index(s1)
    j = stations.index(s2)
    return abs(j - i) * timePerStation

#Journey planner
def journeyPlan(metro, srcStationInput, dstStationInput, startTime):
    srcLine, srcStation = findLineAndStation(metro, srcStationInput, srcStationInput)
    dstLine, dstStation = findLineAndStation(metro, dstStationInput, dstStationInput)
    if srcLine is None or dstLine is None or srcStation is None or dstStation is None:
        return "Station not found."

    startMin = convertTime(startTime)
    nextTrain = nextMetro(startMin)
    if nextTrain is None:
        return "No service available at this time."

    if srcLine == dstLine:
        t = sameLineTime(metro[srcLine], srcStation, dstStation)
        arrival = nextTrain + t
        fare = ratePerStation + ratePerStation
    if srcStation == dstStation:
        return f"Please enter 2 different stations"

        return (
            f"Journey Plan:\n"
            f"Start at {srcStation} ({srcLine})\n"
            f"Next metro at {convertMin(nextTrain)}\n"
            f"Arrive at {dstStation} at {convertMin(arrival)}\n"
            f"Total travel time: {arrival - startMin} minutes\n"
            f"Estimated Fare: {fare} rupees"
        )
    return interchange(metro, srcStationInput, dstStationInput, startTime)

#If journey has interchanges
def interchange(metro, srcStationInput, dstStationInput, startTime):
    srcLine, srcStation = findLineAndStation(metro, srcStationInput, srcStationInput)
    dstLine, dstStation = findLineAndStation(metro, dstStationInput, dstStationInput)
    if srcLine is None or dstLine is None or srcStation is None or dstStation is None:
        return "Invalid stations or lines."

    bestStation = None
    bestTime = 10**9

    for st in metro[srcLine]["stations"]:
        if st in metro[dstLine]["stations"]:
            t1 = sameLineTime(metro[srcLine], srcStation, st)
            t2 = sameLineTime(metro[dstLine], st, dstStation)
            total = t1 + interchangeTime + t2
            if total < bestTime:
                bestTime = total
                bestStation = st
                bestT1 = t1
                bestT2 = t2

    startMin = convertTime(startTime)
    nextSrc = nextMetro(startMin)
    if nextSrc is None:
        return "No service available at this time."

    arrivalInterchange = nextSrc + bestT1
    interDelay = interchangeTimeMinutes(arrivalInterchange)
    nextDstLine = nextMetro(arrivalInterchange + interDelay)
    if nextDstLine is None:
        return "No service available at this time."

    finalArrival = nextDstLine + bestT2
    fare = ratePerStation + ratePerStation + ratePerLine

    return (
        f"Journey Plan:\n"
        f"Start at {srcStation} ({srcLine})\n"
        f"Next metro at {convertMin(nextSrc)}\n"
        f"Arrive at {bestStation} at {convertMin(arrivalInterchange)}\n"
        f"Transfer to {dstLine} (Interchange time: {interDelay} min)\n"
        f"Next {dstLine} metro departs at {convertMin(nextDstLine)}\n"
        f"Arrive at {dstStation} at {convertMin(finalArrival)}\n"
        f"Total travel time: {finalArrival - startMin} minutes\n"
        f"Estimated Fare: {fare} rupees"
    )


metro = metroFile("metro_data1.txt")

print("PART A: Next Metros at a Station:-")
lineInput = input("Enter Line: ")
stationInput = input("Enter Station: ")
startTimeA = input("Time of Travel: ")

trains = upcomingMetros(metro, lineInput, stationInput, startTimeA)

if isinstance(trains, list) and len(trains) > 0 and ":" in trains[0]:
    print("\nNext metro at", trains[0])
    if len(trains) > 1:
        print("Subsequent metros at", ", ".join(trains[1:]))
else:
    print(trains)

print("\nPART B: Journey Planner:-")
source = input("Source Station: ")
destination = input("Destination Station: ")
startTimeB = input("Time of Travel: ")

print()
print(journeyPlan(metro, source, destination, startTimeB))



    
