import threading
import datetime

x = datetime.datetime.now()
td = x.day
tm = x.month
ty = x.year
date = input("please enter your birth date in the format DD/MM/YYYY ")
bd = int(date[0:2])
bm = int(date[3:5])
by = int(date[6:10])
days = 0
if by % 4 == 0:
    if bm == 1:
        days = 335 + (31 - bd)
    if bm == 2:
        days = 306 + (29 - bd)
    if bm == 3:
        days = 275 + (31 - bd)
    if bm == 4:
        days = 245 + (30 - bd)
    if bm == 5:
        days = 214 + (31 - bd)
    if bm == 6:
        days = 184 + (30 - bd)
    if bm == 7:
        days = 153 + (31 - bd)
    if bm == 8:
        days = 122 + (31 - bd)
    if bm == 9:
        days = 92 + (30 - bd)
    if bm == 10:
        days = 61 + (31 - bd)
    if bm == 11:
        days = 31 + (30 - bd)
    if bm == 12:
        days = (31 - bd)
else:
    if bm == 1:
        days = 334 + (31 - bd)
    if bm == 2:
        days = 305 + (28 - bd)
    if bm == 3:
        days = 274 + (31 - bd)
    if bm == 4:
        days = 244 + (30 - bd)
    if bm == 5:
        days = 213 + (31 - bd)
    if bm == 6:
        days = 183 + (30 - bd)
    if bm == 7:
        days = 152 + (31 - bd)
    if bm == 8:
        days = 121 + (31 - bd)
    if bm == 9:
        days = 91 + (30 - bd)
    if bm == 10:
        days = 60 + (31 - bd)
    if bm == 11:
        days = 30 + (30 - bd)
    if bm == 12:
        days = (31 - bd)
while by < ty - 1:
    by = by + 1
    if by % 4 == 0:
        days = days + 366
    else:
        days = days + 365
if ty % 4 == 0:
    if tm == 1:
        days = days + td
    if tm == 2:
        days = days + 31 + td
    if tm == 3:
        days = days + 60 + td
    if tm == 4:
        days = days + 91 + td
    if tm == 5:
        days = days + 121 + td
    if tm == 6:
        days = days + 152 + td
    if tm == 7:
        days = days + 182 + td
    if tm == 8:
        days = days + 213 + td
    if tm == 9:
        days = days + 244 + td
    if tm == 10:
        days = days + 274 + td
    if tm == 11:
        days = days + 305 + td
    if tm == 12:
        days = days + 335 + td
elif ty % 4 != 0:
    if tm == 1:
        days = days + td
    if tm == 2:
        days = days + 31 + td
    if tm == 3:
        days = days + 59 + td
    if tm == 4:
        days = days + 90 + td
    if tm == 5:
        days = days + 120 + td
    if tm == 6:
        days = days + 151 + td
    if tm == 7:
        days = days + 181 + td
    if tm == 8:
        days = days + 212 + td
    if tm == 9:
        days = days + 242 + td
    if tm == 10:
        days = days + 273 + td
    if tm == 11:
        days = days + 304 + td
    if tm == 12:
        days = days + 334 + td

ya = "you are "
do = " days old"
ho = " hours old"
mo = " minutes old"
so = " seconds old"
moo = " months old"
hr = x.hour
minute = (x.hour * 60) + x.minute
sec = (minute * 60) + x.second
months = int(days / 12)
hours = int((days * 24) + hr)
minutes = int((hours * 60) + minute)
seconds = int((minutes * 60) + sec)
print(ya + str(months) + moo)
print(ya + str(days) + do)
print(ya + str(hours) + ho)
print(ya + str(minutes) + mo)
print(ya + str(seconds) + so)
threading.Event().wait(10)
print("thankyou")
