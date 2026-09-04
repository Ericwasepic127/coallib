#!/usr/bin/env python3
# Made by @Ericwasepic127

from datetime import datetime as dt
from shutil import get_terminal_size as gt
from ..itertool import get_last_index as i
from ..pager import get_pager as gp, set_fallback as sf
import argparse, os, sys, getpass, json, sys

set_unable_pager = False
def previewer(text="", title=""):
    global set_unable_pager
    set_unable_pager = True
    show_split()
    print(text)
    show_split("_")

def preview(text):
    in_use = gp()
    in_use(text)
    if not set_unable_pager:
        previewer(text)

sf(previewer)
current = dt.now()
length = gt().columns
save = os.getcwd()
cur = os.path.dirname(__file__)
if not cur and sys.platform == "win32":
    x = __file__.split("\\")
    x.remove(x[i(x)])
    cur = "\\".join(x)
    del x
elif not cur:
    cur = os.path.join(save, __name__)
os.chdir(save)
del save
del i

with open(os.path.join(cur, "use.json")) as x:
    setup = json.load(x)

def show_split(icon="="):
    print(icon*length)

def parse(rhytm: str) -> list:
    return [int(x) for x in rhytm.split("-")]

def get_year() -> int:
    year = current.year
    print("Current year: %d" % year)
    change = input("Would you rather change (type year to change if want to)? ")
    if change:
        if change.isdigit():
            return int(change)
        else:
            print("Gave non-integer!")
    return year

def get_name() -> str:
    try:
        name = getpass.getuser()
        print(f"Found name: {name}")
        change = input("Would you rather change name (type name to change if want to)? ").strip().rstrip()
        if change:
            name = change
    except OSError:
        name = ""
        while not name:
            name = input("Please set name! ").strip().rstrip()
    email = input("Would you rather add email (type email to add if want to)? ").strip().rstrip()
    if email:
        name += f"<{email}>"
    return name

def gather_licenses() -> dict:
    lics = [os.path.join(cur, x) for x in os.listdir(cur) if x.endswith(".license")]
    files = []
    for lic in lics:
        with open(lic) as y:
            files.append(y.read())
    t = ([os.path.basename(z)[:-8] for z in lics], files)
    templates = {}
    for d in range(0, len(t[0])):
       templates[t[0][d]] = t[1][d]
    return templates

templates = gather_licenses()
names = list(templates.keys())

def handle_algo(year: int, name: str, licname: str) -> str:
    templ = templates.get(licname)
    algorhytm = parse(setup.get(licname))
    send = []
    for detect in algorhytm:
        if detect:
            send.append(year)
        else:
            send.append(name)
    return templ.format(*send)

def save_to(location: str, lic: str):
    try:
        with open(location, "w") as file:
            file.write(lic)
    except (BaseException, Exception) as e:
        print("FAILED:", e)

def generate(year, name, nameto, filepath=None):
        licenser = handle_algo(year, name, nameto)
        if filepath:
            save_to(filepath, licenser)
        else:
            preview(licenser)

def greet():
    show_split()
    print("Welcome to License generator")

def get_license(mode=False) -> str:
    print("Please select type of your license:")
    c = 1
    for name in names:
        print(f"{c}. {name}")
        c += 1
    select = input(f"Select (1~{c-1}): ")
    if select == "quit" and mode:
        raise KeyboardInterrupt
    if select and select.isdigit():
        return names[int(select) - 1]
    else:
        print("Not number")
        show_split("-")
        return 1 / 0 if mode else 0

def loop():
    show_split("-")
    nameto = get_license(mode=True)
    year = get_year()
    name = get_name()
    filepath = input("Enter filepath to save (or nothing to preview only): ").rstrip().strip()
    generate(year, name, nameto, filepath)

if __name__ == '__main__':
    greet()
    parser = argparse.ArgumentParser(description="A program to generate Licenses easily")
    parser.add_argument("-n", "--name", help="Name input")
    parser.add_argument("-y", "--year", help="Year input")
    parser.add_argument("-l", "--license", help="License type")
    parser.add_argument("-o", "--output", help="File to write output")
    args = parser.parse_args()
    if args.name or args.year or args.license or args.output:
        if args.year and not args.year.isdigit():
            parser.error("Failed to parse argument of year: Not integer")
            parser.exit(1)
        if args.license and not (args.license in names):
            parser.error(f"No license named {args.license}")
            parser.exit(1)
        name = args.name or get_name()
        year = int(args.year or get_year())
        nameto = args.license or get_license() or sys.exit(1)
        filepath = args.output or input("Enter filepath to save (or nothing to preview only): ").rstrip().strip()
        generate(year, name, nameto, filepath)
    else:
        print("Press Ctrl-C or type 'quit' to exit!")
        while 1:
            try:
                loop()
            except KeyboardInterrupt:
                print("Interrupted, exiting ...")
                break
            except ZeroDivisionError:
                pass
print("Bye!")
