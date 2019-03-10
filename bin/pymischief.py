#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style
import time
import argparse
from mischief.pwned import Pwned
try:
    import simplejson as json
except ImportError:
    import json


def handleArgs():
    parser = argparse.ArgumentParser(description='Search haveibeenpwned.com')
    parser.add_argument('file', help='json file with account names')
    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":

    args = handleArgs()

    with open(args['file']) as file:
        data = file.read()

    accounts = json.loads(data)

    p = Pwned()

    for email in accounts:
        d = p.account(email)
        if d is None:
            print(Fore.GREEN + ">> No leaks for", email, Style.RESET_ALL)
            continue
        print("[{}]========================".format(email))
        for b in d:
            print(Fore.MAGENTA + " {} [{} accounts total]".format(b['Title'], p.clean(b['PwnCount'])))
            print(Fore.CYAN + "   Domain: {}".format(b['Domain']))
            print(Fore.CYAN + "   {}".format(b['BreachDate']))

            if b['IsRetired']:
                print(Fore.GREEN + "   Retired")
            else:
                print(Fore.RED + "   Data still on web")

            if b['IsVerified']:
                print(Fore.RED + "   Hack verified by website")
            else:
                print(Fore.YELLOW + "   Hack not verified by website")

            print(Style.RESET_ALL + "   Leaked data:")
            for dd in b['DataClasses']:
                print("     - {}".format(dd))
            # print(Style.RESET_ALL)
        time.sleep(1)

    for acc in accounts:
        # print("Paste:",acc,"==============")
        paste = p.paste(acc)
        if paste is None:
            print(Fore.GREEN + ">> No pastes for", acc, Style.RESET_ALL)
            continue

        print("Paste:", acc, "==============")
        for b in paste:
            s = b['Source']
            if s == "AdHocUrl":
                print("  AdHocUrl: {}".format(b['Id']))
            elif s == "Pastebin":
                print("  Pastebin: https://pastebin.com/{}".format(b['Id']))
            elif s == "QuickLeak":
                print("  QuickLeak: http://quickleak.se/{}".format(b['Id']))
            else:
                print("   {}: {}".format(b['Source'], b['Id']))

        time.sleep(1)

    # num = p.password(pwd)
    # print("Password {} used {} times".format(pwd, num))
