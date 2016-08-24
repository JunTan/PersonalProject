import Schedule
import Util

if __name__ == '__main__':
	schedule = Schedule.WeekSchedule()
	file = "schedule.csv"
	print "Please enter event detail, type Done if you are done"
	eventDetail = raw_input("--->")
	while "done" not in eventDetail.lower():
		event, startTime, endTime, eventDays = Util.parseEvent(eventDetail)
		for eventDay in eventDays:
		    eventObj = Schedule.Event(event, eventDay)
		    print "eventObj---", eventObj
		    schedule.addSlot(startTime, endTime, eventObj)
		    print event, startTime, endTime, eventDay
		eventDetail = raw_input("--->")
	print "Done"
	Util.outputSchedule(schedule, file)

