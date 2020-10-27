import sys
import re
from typing import Optional, List
import speech_recognition as sr
import new
import delete
import read
from constants import Constants


def arg_parser(user_input: List[str]) -> None:
    """Formats command line arguments and calls required method.
       Can either create a new note (text or audio), read a not (text or audio) and
       delete a note.

    Args:
        user_input: action, audio flag, verbose flag, file name, directory name.

    Returns:
        None
    
    """
    user_input = ''.join(arg.strip() + ' ' for arg in user_input)  # list -> str

    # check valid input with regex
    match = re.search(Constants.master_pattern, user_input)
    if not match:
        sys.exit("Command arguments are invalid.")

    # args are subgroups of regex
    args = match.groups()
    action = args[0]

    # controller
    if action == "new":  # new note
        new._new_helper(*args[1:])
    elif action == "read":  # read note
        read._read_helper(*args[1:])
        pass
    elif action == "del":  # delete note
        delete._del_helper(*args[3:])


if __name__ == "__main__":

    # pass command line arguments to argument parser
    arg_parser(sys.argv[1:])
