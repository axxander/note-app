import speech_recognition as sr
from typing import Optional
import os
from constants import Constants
import sys
import re


def _new_helper(audio_flag: Optional[str], verbose_flag: Optional[str], filename: str, directory: Optional[str]) -> None:
	"""Records microphone audio and returns transcription.
	   Utilises Google Speech Recognition.

	Args:
		audio_flag: Dictate the note using machine microphone.
		verbose_flag: Auto opens dictated note in Sublime after recording.
		filename: Note file name (include extension).
		directory: Directory to store note.

	Returns:
		None

	"""
	# default directory if directory not givrn
	if not directory:
		directory = "General"

	# make directory if it does not exist
	dir_path = os.path.join(Constants.notes_dir, directory)
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)

	# make file if it already exists, else return already exists error
	file_path = os.path.join(dir_path, filename)
	if not os.path.isfile(file_path):
		if not audio_flag:  # typed note
			os.system("subl " + file_path)
		else:  # dictate note
			text = dictate()
			with open(file_path, 'w') as f:
					f.write(text)
			if verbose_flag:  # view transciption in subl
				os.system("subl " + file_path)	
	else:  # overwriting not allowed
		print(file_path)
		rel_file_path =  re.search(Constants.relative_file_path, file_path).group()
		sys.exit(f"Note '{rel_file_path}' already exists.")


def dictate() -> Optional[str]:
	"""Records microphone audio and returns transcription.
	   Utilises Google Speech Recognition.

	Args:
		None

	Returns:
		text: Audio note tanscription.

	"""
	r = sr.Recognizer()
	with sr.Microphone() as source:  # use machine microphone
		print('recording audio...')
		audio = r.listen(source)

	try:  # recognise dictation
		text = r.recognize_google(audio)
	except sr.UnknownValueError:  # unintelligible dictation
		sys.exit("Google Speech Recognition could not understand note.")
	except sr.RequestError as e:  # concerns API
		sys.exit(f"Could not request results from Google Speech Recognition service; {e:0}")

	return text



