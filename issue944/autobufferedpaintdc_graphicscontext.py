#!/usr/bin/env python3
  
import wx

class TestPanel(wx.Window):
    def __init__(self, parent, paintdc_type, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.Bind(wx.EVT_PAINT, self.on_paint)

        if paintdc_type == 1:
            self.use_paintdc = True
            self.use_bufferedpaintdc = False
            self.use_autobufferedpaintdc = False
        elif paintdc_type == 2:
            self.use_paintdc = False
            self.use_bufferedpaintdc = True
            self.use_autobufferedpaintdc = False
        else:
            self.use_paintdc = False
            self.use_bufferedpaintdc = False
            self.use_autobufferedpaintdc = True

        if self.use_autobufferedpaintdc:
            self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

    def on_paint(self, _evt):
        if self.use_paintdc:
            paint_dc = wx.PaintDC(self)
        if self.use_bufferedpaintdc:
            paint_dc = wx.BufferedPaintDC(self)
        if self.use_autobufferedpaintdc:
            paint_dc = wx.AutoBufferedPaintDC(self)

        graphics_dc = wx.GraphicsContext.Create(paint_dc)

        pen_color = wx.Colour(255, 0, 0, 255)
        brush_color = wx.Colour(255, 0, 0, 128)

        graphics_dc.SetPen(
                wx.Pen(colour=pen_color, width=1, style=wx.SOLID)
                )
        graphics_dc.SetBrush(
                wx.Brush(colour=brush_color, style=wx.BRUSHSTYLE_SOLID)
                )
        graphics_dc.DrawRectangle(
                100, 100,
                200, 200,
                )

class MyFrame(wx.Frame):
    def __init__(self, parent, paintdc_type, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize((800, 600))

        self.test_panel = TestPanel(self, paintdc_type)
        if paintdc_type==1:
            self.SetTitle('PaintDC')
        elif paintdc_type==2:
            self.SetTitle('BufferedPaintDC')
        else:
            self.SetTitle('AutoBufferedPaintDC')

        self.Show(True)

def main():
    my_app = wx.App()

    paintdc_win = MyFrame(None, 1)
    bufferedpaintdc_win = MyFrame(None, 2)
    autobufferedpaintdc_win = MyFrame(None, 3)

    my_app.MainLoop()

if __name__ == '__main__':
    main()
