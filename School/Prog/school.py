
if __name__ == "__main__":
    secs = int(input("Insert time in seconds"))
    mins = int(input("Insert time in minutes"))
    hours = 0

    totalseconds = secs + (mins * 60)
    remainingsec = totalseconds % 60
    mins = totalseconds // 60
    hours = mins // 60
    remainingmin = mins % 60

    print(f"The total seconds are {totalseconds}, The seconds are {remainingsec}, The minutes are {remainingmin}, The hours are {hours}\n")