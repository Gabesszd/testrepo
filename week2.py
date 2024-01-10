import re
hand = open('C:\\Important\\Training\\Coursera\\Python\\numbers.txt')
#print(hand.read())
stuff = list()
stuffint = list()
for line in hand:
    stuff = stuff + re.findall('([0-9]+)',line)
for i in stuff:
    stuffint.append(int(i))
print(stuffint)
print('sum: ', sum(stuffint))

    
