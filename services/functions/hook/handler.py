import io
import os
import contextlib
import json
import subprocess
import shutil
import sys

from git import Repo


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def get_stdin():
    pass

def main():
    payload = json.loads(get_stdin())


if __name__ == '__main__':
    main()
