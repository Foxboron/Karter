# -*- coding: utf-8 -*-
import os
import random
import string
import re

from subprocess import Popen, PIPE


def getuser(ircmsg):
    return ircmsg.split(":")[1].split('!')[0]


def getargs(ircmsg):
    # return ircmsg.split(":")[2].split('!')[0]
    args = parsemsg(ircmsg)[2][1:]
    args = args[len(args)-1].strip("\r\n")
    args = " ".join(str(args).split(" ")[1:])
    return args


_command_dict = {}


def command(name):
    # The decorator appending all fn's to a dict
    def _(fn):
        # Decorators return an inner function whom we
        # pass the function.
        _command_dict[name] = fn
    return _


def nothing(args):
    return ""


def get_command(name):
    # Explicity over implicity?
    # Fuck that

    # We just lower the string.
    # and check later its upper cased
    if name.lower() in _command_dict:
        return _command_dict[name.lower()]
    else:
        return nothing


from subprocess import Popen, PIPE


class KartRunner(object):
    ps = None
    KART_PATH = "/home/fox/Github/kart"

    def check_ps(self):
        if "Finished" in self.ps.stdout.read():
            return True
        return False

    def start_ps(self,args):
        if self.check_ps():
            self.ps = Popen(['./run.zsh', args[0], args[1]], stdout=PIPE, cwd=self.KART_PATH)
            return "Started running process! Look at twitch"
        else:
            return "Still running!"


kr = KartRunner()

@command("start")
def cute(args):
    return kr.start_ps(args)






