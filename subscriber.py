#pub sub topic
import sys

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



class Subscriber:
	
	def __init__(self, name):
		self.name = name
		self.topicsList = []
		
	def subscribe(self, topic):
		if topic not in self.topicsList:
			self.topicsList.append(topic)
			topic.addSubscriber(self)
			
	def receive(self, message):
		sys.stdout.write(self.name + " received : " + message)
		sys.stdout.write("\n")
        
		
        
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
#		sys.stdout.write(message)
#		self.sendMessages()
			
	def sendMessages(self):
		for msg in self.messages:
			for sub in self.subscribers:
				sub.receive(msg)
