# Coderdojo Virtual #1

print ("Let’s introduce ourselves.")
print ("My name is Eliza. What is your name?")
name = input()
print ("Hello " + name + ". I am really pleased to meet you.")
# Asking questions
print ("So where are you from?")
place = input()
print ("Wonderful! I have heard that is a great place to live.")
# Being decisive
print ("How are you feeling today?")
feeling = input()
if feeling == "Sad":
  print ("I’m sorry you feel like that.")
else:
  print ("That’s good.")
# Having a conversation
answer = "No"
while answer != "Yes":
  print ("Are we nearly there?")
  answer = input()
print ("Yippee! We are finally here.")
# Goodbye
print ("Thanks for chat, " + name +".")
print ("We will have to do this again soon.")
print ("Goodbye.")