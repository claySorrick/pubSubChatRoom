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
mansBestFriend = Subscriber("mansBestFriend")
animalLover = Subscriber("animalLover")

dog = Topic("dog")
cat = Topic("cat")

kennel.addTopic(dog)
pound.addTopic(cat)
pound.addTopic(dog)
catPalace.addTopic(cat)

dogLover.subscribe(dog)
catLover.subscribe(cat)
mansBestFriend.subscribe(dog)
animalLover.subscribe(dog)
animalLover.subscribe(cat)

server.topicsList.append(dog)

server.topicsList.append(cat)



kennel.publish("Dogs are great!")
pound.publish("We have too many cats and a lot of dogs")
catPalace.publish("Crazy Cat Ladies Unite")

server.forwardMessages()
print("")

pound.publish("Stray Black Cat picked up, Albany")
pound.publish("Black Cat owner found")

server.forwardMessages()
print("")

catPalace.publish("New cat Towers available")

server.forwardMessages()
print("")

