# Coderdojo Virtual #4
#
# What time is it?
#

import time

def get_time():
    now = time.localtime()
    hour = now[3]
    minutes = now[4]
    print "The current time is:",hour,minutes
    return [hour,minutes]

def hour_to_words(hour):
    hour_words = ["Twelve","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven"]
    return hour_words[hour % 12]

def minute_to_words(minutes):
    minute_words = ["O'clock exactly", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Quarter", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
                    "Twenty-one", "Twenty-two", "Twenty-three","Twenty-four","Twenty-five", "Twenty-six", "Twenty-seven", "Twenty-eight", "Twenty-nine", "Half"]
    if minutes > len(minute_words):
        return str(minutes)
    else:
        return minute_words[minutes]

the_time = get_time()
if the_time[1] > 30:
    time_string = minute_to_words(60 - the_time[1]) + " minutes to " + hour_to_words(the_time[0]+1)
else:
    time_string = minute_to_words(the_time[1]) + " minutes past " + hour_to_words(the_time[0])
print "It is",time_string
