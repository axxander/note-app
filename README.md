# Noted
Noted automates notes. It allows both written and dictated notes. Furthermore, it allows *Alexa-style* verbalisation of exisiting notes.

## Motivation
The initial motivation was to manage my notes and project ideas. However, it became an exercise for learning/practising skills, such as:
- Regular expressions
- Command line interfaces with optional arguments using regular expressions
- Google Speech Recognition library
- Google Text-to-speech library
- Unit testing

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python project dependencies.

```bash
pip install -r requirements.txt
```

Create the alias command "noted" to launch the Noted App from anywhere. On Linux OS, change from `.bash_profile` to `.bashrc`.
```bash
source noted/alias.sh
```

This project is setup to use [Sublime](https://www.sublimetext.com/) with the [command line interface](https://www.sublimetext.com/docs/command_line.html), i.e. `subl` launches the Sublime text editor.

## Usage
The general syntax is

```bash
noted action [-a] [-v] filename.ext [directory]
```

where `action` is either `new`, `read` or `del`, which correspond to creating a new note, reading an existing note or deleting a note respectively. `-a` is the "audio flag", `-v` is the "verbose flag", `filename.ext` is the name of the note and its format and `directory` is the note location.

The audio and verbose flags are only relevant with regards to actions `new` and `read`. Furthermore, if no `directory` is specified, the note will be stored in the `Notes/General` directory.

### Action: new
Create a new note `list.txt` within the `Notes/Shopping` directory by **writing** in the text editor.
```bash
noted new list.txt Shopping
```
Create a new note `list.txt` within the `Notes/Shopping` directory by **dictating**.
```bash
noted new -a list.txt Shopping
```
Create a new note `list.txt` within the `Notes/Shopping` directory by **dictating** *and* opening the text editor to view the dictated note.
```bash
noted new -a -v list.txt Shopping
```

### Action: read
Read existing note `list.txt` within the `Notes/Shopping` in the text editor.
```bash
noted read list.txt Shopping
```
Read existing note `list.txt` within the `Notes/Shopping` directory by **verbalising** the note (Alexa-style audio response).
```bash
noted read -a list.txt Shopping
```
Read existing note `list.txt` within the `Notes/Shopping` directory by **verbalising** *and* opening the text editor to view the note.
```bash
noted read -a -v list.txt Shopping
```

### Action: del
Delete existing note `foo.txt` within the `Notes/General` directory.
```bash
noted del foo.txt
```
Delete existing note `list.txt` within the `Notes/Shopping` directory.
```bash
noted del list.txt Shopping
```
Delete the existing directory `Notes/Shopping`.
```bash
noted del . Shopping
```

## Tests
The unit tests currently only cover the regular expression for handling the command line interface.

## Roadmap
There is currently no plan for additional features.

## License
[MIT](https://choosealicense.com/licenses/mit/)



