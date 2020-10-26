import constants
import sys
import os
from typing import Optional
import re
import shutil


def _del_helper(filename: str, directory: Optional[str]) -> None:
	"""Controls deletion of either directory or file within directory with parent Notes.

	Args:
		filename: Note file name to be deleted within given directory.
		directory: Directory within Notes directory to be deleted.
		
	Returns:
		None

	"""
	if filename == ".":  # delete directory
		if not directory:  # delete General directory
			delete_directory()
		else:  # delete specific directory
			delete_directory(directory)
	else:  # delete file
		if not directory:  # delete file in General directory
			delete_file(filename)
		else:  # delete file in specific directory
			delete_file(filename, directory)


def delete_file(filename: str, directory: str = "General") -> None:
	"""Deletes file in specified directory.

	Args:
		filename: Note file name to be deleted within given directory.
		directory: Directory within Notes directory to be deleted.

	Returns:
		None

	"""
	file_path = os.path.join(constants.notes_dir, directory, filename)  # absolute path to note file
	rel_file_path =  re.search(constants.regex_rel_path, file_path).group()  # relative path to not file

	try:  # file exists
		os.remove(file_path)
		print(f"Note '{rel_file_path}' deleted.")
	except FileNotFoundError:  # file does not exist
		sys.exit(f"Note '{rel_file_path}' does not exist.")


def delete_directory(directory: str = "General") -> None:
	"""Deletes empty or non-empty directory in Notes directory.

	Args:
		directory: Directory within Notes directory to be deleted.

	Returns:
		None

	"""
	dir_path = os.path.join(constants.notes_dir, directory)  # absolute path to note dir
	rel_dir_path =  re.search(constants.regex_rel_path, dir_path).group()  # relative path to note dir

	query = f"Are you sure you want to delete '{rel_dir_path}' directory? (y/n) "  # user confirmation
	q = input(query)
	if q.lower() == 'y':  # delete dir
		try:  # dir exists
			shutil.rmtree(dir_path)
			print(f"Directory '{rel_dir_path}' deleted.")
		except:  # dir does not exist
			sys.exit(f"Directory '{rel_dir_path}' does not exist.")
	else:  # cancel dir deletion
		sys.exit("No deletion.")


