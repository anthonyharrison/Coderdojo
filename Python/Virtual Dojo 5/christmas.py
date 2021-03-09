import random

MAX_DAYS=12

word = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Nineth', 'Tenth', 'Eleventh', 'Twelfth']
number = ['A', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
gifts = ['Plump Partridge', 'Turtle Dove', 'French Hen', 'Calling Bird', 'Golden Ring', 'Mooing Cow', 'Swimming Swan', 'Milking Maid', 'Dancing Donkey', 'Leaping Lord', 'Piping Piper', 'Drumming Drummer']

gift_order = []
#gift_order = range(0,MAX_DAYS)
for i in range(MAX_DAYS):
    gift_added = False
    while not gift_added:
        n = random.randint(0,MAX_DAYS-1)
        if n not in gift_order:
            gift_order.append(n)
            gift_added = True

#print (gift_order)

gift_count = 0 
for day in range(MAX_DAYS):
    #print (day)
    print ("On the", word[day], "day of Christmas my true love gave to me:")
    for gift in range(day,-1,-1):
        #print (gift)
        if gift == 0:
            if day != 0:
                print ("And ", end='')
            extra = " in a Pear Tree"
        else:
            extra = "s"
        print (number[gift],gifts[gift_order[gift]]+extra)
        gift_count = gift_count + gift + 1
    print ()

print ("Gifts delivered", gift_count)
