#!/usr/bin/env python3

import wx

class MyCanvas(wx.ScrolledCanvas):
    def __init__(self, parent, id=wx.ID_ANY):
        super().__init__(parent, id)

        # attempting to avoid Windows flicker
        # THIS IS WHAT CAUSES THE SCROLLBAR ARTIFACT
        #   if this line is absent, scrollbar corner is erased fine
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        # x smaller than MainWindow, y larger than MainWindow
        self.SetVirtualSize(600, 1000)
        self.SetScrollRate(10,10)

        # scroll so vert. scrollbar is at bottom
        self.Scroll(0, 2000)

        wx.CallLater(
                1000,
                self.zoom_scroll,
                )
    def zoom_scroll(self):
        # x larger than MainWindow, y larger than MainWindow
        self.SetVirtualSize(1000, 1200)
        # scroll so vert. scrollbar is at bottom
        self.Scroll(0, 2000)

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_canvas = MyCanvas(self)
        self.SetSize((800, 600))
        self.Show(True)

def main():
    my_app = wx.App()
    main_win = MainWindow(None)
    my_app.MainLoop()

if __name__ == '__main__':
    main()
