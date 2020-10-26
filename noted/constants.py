import os
import re

class Constants:
	"""Regular expressions and common file paths used by Noted.

	"""
	# regex pattern for validating command line arguments
	master_pattern = re.compile(r"(new|read|del)\s?(-a)?\s?(-v)?\s([a-zA-Z0-9._-]+)\s?([a-zA-Z0-9/._-]+)?")

	# regex pattern for extracting relative file path
	# e.g. Notes/foo/bar.txt --> /foo/bar.txt
	relative_file_path = re.compile(r"Notes\/[a-zA-Z0-9/._-]+")

	# Notes directory (directory all entries are stored)
	notes_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Notes'))

	# the directory audio responses are stored
	response_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'noted', 'response'))
