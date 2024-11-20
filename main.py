import tkintertools as tkt
import pywinstyles
import sys


def uistyles(num):
    if num >= 11 or num < 0 :
        sys.exit()
        return
    else :
        styles = ["dark", "mica", "aero", "transparent", "acrylic", "win7","inverse", "popup", "native", "optimised", "light"]
        pywinstyles.apply_style(root,styles[num])
        return

size = size = 500, 300
root = tkt.Tk(title="test",size=size)
root.center()
uistyles(7)    #更改这里的数字来改变窗口风格   Change the numbers here to change the window style.
root.mainloop()