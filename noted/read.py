import sys
import os
from constants import Constants
from typing import Optional
import re
import playsound
from gtts import gTTS


def _read_helper(audio_flag: Optional[str], verbose_flag: Optional[str], filename: str, directory: Optional[str]) -> None:
	"""Handles read options, i.e. read text or speak.

	Args:
		audio_flag: Dictate the note using machine microphone.
		verbose_flag: Auto opens dictated note in Sublime after recording.
		filename: Note file name (include extension).
		directory: Directory to store note.

	Returns:
		None

	"""
	if not directory:
		directory = "General"

	file_path = os.path.join(Constants.notes_dir, directory, filename)
	rel_file_path =  re.search(Constants.relative_file_path, file_path).group()
	if os.path.isfile(file_path):
		if not audio_flag:
			os.system("subl " + file_path)
		else:
			with open(file_path, 'r') as f:
				text = f.read()
			response(text)
			if verbose_flag:
				os.system("subl " + file_path)
	else:
		sys.exit(f"Note '{rel_file_path}' does not exist.")


def response(text: str) -> None:
	"""Converts text to spoken audio.
	   Utilises Google Text-to-Speech module.

	Args:
		text: Text to speak.

	Returns:
		None

	"""
	try:
		tts = gTTS(text=text, lang="en")  # set text to speech
	except:
		sys.exit("Sorry, my speak function is not currently functioning.")

	f_audio = os.path.join(Constants.response_dir, "response.mp3")
	tts.save(f_audio)  # save audio file

	playsound.playsound(f_audio)  # play sound
	os.remove(f_audio)  # delete response mp3



	