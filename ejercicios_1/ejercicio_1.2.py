#This code calculate how much time will take to say a phrase calculating an average of 2 words per second
phrase = input("Tell me a sentence and I'll calculate how long it would take you to say it: ")

#Create a list with all the words of the phrase (it separates when its a space)
separated_words = phrase.split(" ")

#Use len() to see how much elements are in the list
words_quantity = len(separated_words)

#In the case that it will take more than a minute, we say to calm down
if words_quantity > 120:
    print("Calm down, i didnt ask you for a bible either")

#Calculate how much time it will take to say the words and show it in the screen (Dalto speaks 30% faster than the average)
print(f"You said {words_quantity} words and it will take {words_quantity/2} seconds to say it")
print(f"Dalto will say it in {words_quantity / 2 - words_quantity * 100 // 2 * 0.3 / 100 }")
