# This Python file uses the following encoding: utf-8
#####################################################
#                  __       __   _      __   __
#   ___ ___  ___ _/ /_____ / /  (_)__ _/ /  / /____
#  (_-</ _ \/ _ `/  '_/ -_) /__/ / _ `/ _ \/ __(_-<
# /___/_//_/\_,_/_/\_\\__/____/_/\_, /_//_/\__/___/
#                               /___/
#####################################################
# Title:        snakeLights
# Version:      1.0
# Description:  Provides timed lighting for snake encloure
# Author:       Jonas Werner
#####################################################
import math
import time
import colorsys
import datetime

from luma.led_matrix.device import neopixel
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, TINY_FONT

# create matrix device
device = neopixel(width=152, height=1)
device.contrast(64)


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def morningStageA():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0xf4, 0xa0, 0x29, 0x80))

def morningStageB():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0xff, 0xfc, 0xaa, 0x80))

def daytimeStageA():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0xff, 0xfc, 0xaa, 0x80))

def eveningStageA():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0xff, 0xfc, 0xaa, 0x80))

def blackout():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0x00, 0x00, 0x00, 0x80))

def initTest():
    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0x00, 0x00, 0xff, 0x80))
    time.sleep(1)

    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0x00, 0xff, 0x00, 0x80))
    time.sleep(1)

    with canvas(device) as draw:
        draw.line((0, 0, 152, device.height), fill=(0xff, 0x00, 0x00, 0x80))
    time.sleep(1)


def main():

    while True:
        now     = datetime.datetime.now()
        hour    = now.hour
        minute  = now.minute
        second  = now.second

        morningStageAstatus = time_in_range(datetime.time(7, 30, 0), datetime.time(8, 30, 0), datetime.time(hour, minute, second))
        morningStageBstatus = time_in_range(datetime.time(8, 30, 1), datetime.time(9, 0, 0), datetime.time(hour, minute, second))
        daytimeStageAstatus = time_in_range(datetime.time(9, 0, 1), datetime.time(18, 0, 0), datetime.time(hour, minute, second))
        eveningStageAstatus = time_in_range(datetime.time(18, 0, 1), datetime.time(22, 30, 0), datetime.time(hour, minute, second))
        eveningStageBstatus = time_in_range(datetime.time(22, 40, 0), datetime.time(22, 50, 0), datetime.time(hour, minute, second))

        if morningStageAstatus:
            morningStageA()
        elif morningStageBstatus:
            morningStageB()
        elif daytimeStageAstatus:
            daytimeStageA()
        elif eveningStageAstatus:
            eveningStageA()
        elif eveningStageBstatus:
            eveningStageA()
        else:
            blackout()

        time.sleep(10)


if __name__ == "__main__":
    initTest()
    try:
        main()
    except KeyboardInterrupt:
        pass
