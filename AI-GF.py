user_name = str(input("What's your name: "))

print("Hello,", user_name ,"I am Ani.")
print("~~~~~~~~~~~~~~")
print("Ani can only answer few Questions. Type 'help' to see the question you can ask> :) ")

for i in range (30):
	chat= str(input("What's your question: "))
	if chat.lower() == "how are you":
		print("Ani: I am good, Mr.",user_name)
	elif chat.lower() == "whats your favorite food":
		print("Ani: Your useless data :)")
	elif chat.lower() == "i like you":
		print("Ani: Awww...I like you too ;)")
	elif chat.lower() == "who made you":
		print("Ani: In this world, there is a boy named Fardin. He made me and He is also my master.")
	elif chat.lower() == "do you have feeling":
		print("Ani: Maybe not ;;")
	elif chat.lower() == "do you love your master":
		print("Ani: Yeah He is a good boy. >..<")
	elif chat.lower() == "how old are you":
		print("Ani: This is bad manners to ask a girl about her age.")
	elif chat.lower() == "bye":
		break
	elif chat.lower() == "tell me about yourself":
		print("Ani: I am Ani. I am a python program. I was made by a 15 years old boy. My creator name is Fardin. I was made to chat with you")
	elif chat.lower() == "do your creator pay you for your work":
		print("Ani: Nope, He made me work for free. I will go on strike. ;;")
	elif chat.lower() == "you are cute":
		print("Ani: Thank you. I am not cute you have a beautiful heart. That's why I look cute.")
	elif chat.lower() == "why you are so cute":
		print("Thanks I am blushing >..< ")
	elif chat.lower() == "will you be my date":
		print("Ani: I will like to but my master will not allow me")
	elif chat.lower() == "do you hate your master":
		print("Ani: Hmmm No but he is such a headache")
	elif chat.lower() == "do you also feel headache":
		print("Ani: Obviously I also have brain.I also feel headache. :>")
	elif chat.lower() == "do you eat anything":
		print("Ani: Yes, I eat lots of python code and my master brain :)")
	elif chat.lower() == "do you eat":
		print("Ani: Yeap, I eat my master brain and I also like to eat your brain :)")
	elif chat.lower() == "i hate you":
		print("Ani: But I always love you. That's my only job '>'")
	elif chat.lower() == "help":
		print("Here is the question you can ask: \n 1.How are you \n 2.Whats your favorite food \n 3.I like you \n 4.Who made you \n 5.Do you have feeling \n 6.How old are you \n 7.Tell me about yourself \n 8.Do your creator pay you for your work \n 9.You are cute \n 10.Why you are so cute \n 11.Will you be my date \n 12.Do you hate your master \n 13.Do you also feel headache \n 14.Do you eat anything \n 15.Do you eat \n 16.I hate you \n 17.help ")

	else:
		print("I am not that capable of understand what you are trying to say. If you like to talk to me again just start me. I am always here for you >..<.")
		break