import Util

class WeekSchedule(object):
        def __init__(self):
		self.timeEvent = Util.Counter()

	def addSlot(self, startTime, endTime, event):
		self.timeEvent["{0}/{1}".format(startTime, endTime)] = event

	def getTimeEvent(self):
		return self.timeEvent

	def printSchedule(self):
		print self.timeEvent

	def getEvent(self, time, day):
		result = []
		for eventTime in self.timeEvent:
			startTime = eventTime.split("/")[0]
			endTime = eventTime.split("/")[1]
			if Util.timeLEG(startTime, time) >= 0 and Util.timeLEG(startTime, Util.updateTime(time)) < 0:
				events = self.timeEvent[eventTime]
				for event in events:
					if event.getEventDay().lower() in day:
						self.timeEvent[eventTime].remove(event)
						result += [event.getEvent() + " " + endTime]
		return result


class Event(object):
	def __init__(self, event, day):
		self.event = event
		self.day = day

	def getEvent(self):
		return self.event

	def getEventDay(self):
		return self.day

	def __str__(self):
		return str(self.event) + str(self.day)
