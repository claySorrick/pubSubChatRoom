#pub/sub server
from subscriber import Publisher, Subscriber, Topic


		
class PubSubServer:

	topicsList = []
	
	def forwardMessages(self):
		for t in self.topicsList:
			t.sendMessages()
				
	
	
server = PubSubServer()

kennel = Publisher("kennel")
pound = Publisher("pound")
catPalace = Publisher("catPalace")	
	
dogLover = Subscriber("dogLover")
catLover = Subscriber("catLover")

dog = Topic("dog")
cat = Topic("cat")

kennel.addTopic(dog)
pound.addTopic(cat)
pound.addTopic(dog)
catPalace.addTopic(cat)

dogLover.subscribe(dog)
catLover.subscribe(cat)

server.topicsList.append(dog)
#for t in server.topicsList: print(t.name)
server.topicsList.append(cat)
#for t in server.topicsList: print(t.name)


kennel.publish("Dogs are great!")
pound.publish("We have too many cats and a lot of dogs")
catPalace.publish("Crazy Cat Ladies Unite")

server.forwardMessages()

