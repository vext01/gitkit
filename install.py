#!/usr/bin/env python3
import os
import sys

HOME = os.environ["HOME"]
DIR = os.path.abspath(os.path.dirname(__file__))
GITCONFIG_SRC = os.path.join(DIR, ".gitconfig")
GITCONFIG_DEST = os.path.join(HOME, ".gitconfig")
LOCAL_GITCONFIG_DEST = os.path.join(HOME, ".gitconfig-local")

TEMPLATE = """[user]
	name = %s
	email = %s
	signingKey = %s
"""


def prompt(msg):
    sys.stdout.write(msg + ": ")
    sys.stdout.flush()
    return input()


def bail(msg):
    print(msg)
    sys.exit(1)


def main():
    if os.path.exists(GITCONFIG_DEST):
        bail("%s already exists" % GITCONFIG_DEST)

    if os.path.exists(LOCAL_GITCONFIG_DEST):
        bail("%s already exists" % LOCAL_GITCONFIG_DEST)

    name = prompt("Full name")
    email = prompt("Email")
    pub_key = prompt("SSH public key")

    with open(LOCAL_GITCONFIG_DEST, "w") as fh:
        fh.write(TEMPLATE % (name, email, pub_key))
    os.symlink(GITCONFIG_SRC, GITCONFIG_DEST)

main()
