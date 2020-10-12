import os
import re

### Regular Expressions

# validate command line arguments
master_pattern = re.compile(r"(new|read|del)\s?(-a)?\s?(-v)?\s([a-zA-Z0-9._-]+)\s?([a-zA-Z0-9/._-]+)?")

# relative file paths
regex_rel_path = re.compile(r"Notes\/[a-zA-Z0-9/._-]+")


### Frequently used paths

# notes directory
notes_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Notes'))

# audio response directory
response_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'noted', 'response'))
