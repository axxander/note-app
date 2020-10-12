import speech_recognition as sr
import os
import re

def main():
	
	with open('Notes/General/test.txt', 'r') as f:
		s = f.read()

	print(repr(s))

if __name__ == '__main__':
	main()