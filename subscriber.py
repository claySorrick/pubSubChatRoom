#pub sub topic
import sys


"""
Publisher class
sends messages to topics
"""
class Publisher:
	
	def __init__(self, name):
		self.name = name
		self.topicsList = []
	
	def publish(self, message):
		for t in self.topicsList:
			t.addMessage(message)
	
	def addTopic(self, topic):
		if topic not in self.topicsList:
			self.topicsList.append(topic)


"""
Subscriber class
receives messages from the topics it has subscribed to
"""
class Subscriber:
	
	def __init__(self, name):
		self.name = name
		self.topicsList = []
		
	def subscribe(self, topic):
		if topic not in self.topicsList:
			self.topicsList.append(topic)
			topic.addSubscriber(self)
			
	def receive(self, topic, message):
		sys.stdout.write("Name: " + self.name)
		sys.stdout.write(", Topic: " + topic.name)
		sys.stdout.write(", Message: " + message)
		sys.stdout.write("\n")
        
		
"""
Topic class
delivers messages to subscribers
"""
class Topic:

	def __init__(self, name):
		self.name = name
		self.messages = []
		self.subscribers = []
		
	def addSubscriber(self, subscriber):
		if subscriber not in self.subscribers:
			self.subscribers.append(subscriber)
			
	def addMessage(self, message):
		self.messages.append(message)
#		self.sendMessages()
			
	def sendMessages(self):
		for msg in self.messages:
			for sub in self.subscribers:
				sub.receive(self, msg)
		self.messages = []