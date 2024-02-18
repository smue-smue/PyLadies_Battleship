import sys
import os

# Constructs an absolute path to the 'src' directory.
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Inserts the 'src' directory at the start of the Python path list.
sys.path.insert(0, src_dir)
