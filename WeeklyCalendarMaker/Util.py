import csv

Monday = ["monday", "m", "mon", "mo"]
Tuesday = ["tuesday", "tu", "t", "tue"]
Wednesday = ["wednesday", "we", "w", "wed"]
Thursday = ["thursday", "th"]
Friday = ["friday", "fr", "f", "fri"]
Saturday = ["saturday", "sa"]
Sunday = ["sunday", "s", "su"]
day = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday

class Counter(dict):
    """
    A counter keeps track of counts for a set of keys.

    The counter class is an extension of the standard python
    dictionary type.  It is specialized to have number values
    (integers or floats), and includes a handful of additional
    functions to ease the task of counting data.  In particular,
    all keys are defaulted to have value 0.  Using a dictionary:

    a = {}
    print a['test']

    would give an error, while the Counter class analogue:

    >>> a = Counter()
    >>> print a['test']
    0

    returns the default 0 value. Note that to reference a key
    that you know is contained in the counter,
    you can still use the dictionary syntax:

    >>> a = Counter()
    >>> a['test'] = 2
    >>> print a['test']
    2

    This is very useful for counting things without initializing their counts,
    see for example:

    >>> a['blah'] += 1
    >>> print a['blah']
    1

    The counter also includes additional functionality useful in implementing
    the classifiers for this assignment.  Two counters can be added,
    subtracted or multiplied together.  See below for details.  They can
    also be normalized and their total count and arg max can be extracted.
    """
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def __setitem__(self, key, value):
        if self[key] == 0:
            dict.__setitem__(self, key, [value])
        else:
            dict.__setitem__(self, key, self[key] + [value])

def compareTime(time1, time2):
    time1Hour = int(time1.split(":")[0])
    time1Min = int(time1.split(":")[1])
    time2Hour = int(time2.split(":")[0])
    time2Min = int(time2.split(":")[1])
    if time1Hour < time2Hour:
        return time1, time2
    elif time1Hour == time2Hour:
        if time1Min < time2Min:
            return time1, time2
        else:
            return time2, time1
    else:
        return time2, time1

def parseEvent(eventDetail):
    detailList = eventDetail.split()
    event = ""
    time1 = None
    time2 = None
    eventDays = []
    for item in detailList:
        if item.lower() in day:
            eventDays += [item]
        elif ":" in item:
            if time1 is None:
                time1 = item
            else:
                time2 = item
        else:
            event = event + " " + item
    startTime, endTime = compareTime(time1, time2)
    return event, startTime, endTime, eventDays

def timeLEG(time1, time2):
    time1Hour = int(time1.split(":")[0])
    time1Min = int(time1.split(":")[1])
    time2Hour = int(time2.split(":")[0])
    time2Min = int(time2.split(":")[1])
    if time1Hour < time2Hour:
        return -1
    elif time1Hour == time2Hour:
        if time1Min < time2Min:
            return -1
        elif time1Min > time2Min:
            return 1
        else:
            return 0

    return 1

def updateTime(time, inc = 30):
    timeHour = time.split(":")[0]
    timeMin = time.split(":")[1]
    timeMin = int(timeMin) + inc
    if timeMin == 60:
        timeHour = int(timeHour) + 1
        timeMin = 0
    return "{0}:{1}".format(str(timeHour), str(timeMin))

def outputSchedule(schedule, filename):
    with open(filename, "w") as scheduleFile:
        fileWriter = csv.writer(scheduleFile, lineterminator = "\n")
        #Write the head line
        fileWriter.writerow(['Time'] + ['Mon'] + ['Tue'] + ['Wed'] + ['Th'] + ['Fri'])
        writeTime = "9:00"
        while timeLEG(writeTime, "21:00") == -1:
            monClass = schedule.getEvent(writeTime, Monday)
            tueClass = schedule.getEvent(writeTime, Tuesday)
            wedClass = schedule.getEvent(writeTime, Wednesday)
            thClass = schedule.getEvent(writeTime, Thursday)
            friClass = schedule.getEvent(writeTime, Friday)
            maxLength = max(len(monClass), len(tueClass), len(wedClass), len(thClass), len(friClass))
            monClass += [None] * (maxLength - len(monClass))
            tueClass += [None] * (maxLength - len(tueClass))
            wedClass += [None] * (maxLength - len(wedClass))
            thClass += [None] * (maxLength - len(thClass))
            friClass += [None] * (maxLength - len(friClass))
            for idx in range(maxLength):
                fileWriter.writerow([writeTime] + [monClass[idx]] + [tueClass[idx]] \
                                    + [wedClass[idx]] + [thClass[idx]] + [friClass[idx]] )
            fileWriter.writerow([writeTime] + [None] + [None] + [None] + [None] + [None] )

            writeTime = updateTime(writeTime)
            print "writeTime: ", writeTime









