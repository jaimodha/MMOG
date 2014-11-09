import random, math

msg = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(7))
print "sent", msg

msg = int(100 * random.random()) - 50
print "sent", msg

msg = int(100 * random.random())
print "sent", msg

msg = 100 * random.random()
print "sent", msg