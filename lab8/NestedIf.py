#!/usr/bin/env python2

fav_color = raw_input('What is your favorit color? ')

if fav_color == 'blue':
	quest = raw_input('What is your quest? ')
	if quest == 'The Grail':
		print 'Right, off you go!'
	else:	
		print 'Arrrghhh!'
else:
	print 'Arrrghhh!'
