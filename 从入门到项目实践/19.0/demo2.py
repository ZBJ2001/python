# _*_ coding: UTF-8 _*_
# 开发团队 ：万宝软件部
# 开发人员 ：Administrator
# 开发时间 : 2020-8-3 22:04
# 文件名称 : demo2.py
# 开发工具 : PyCharm
# 任    务 ：练习GUI
# 知 识 点 ：

import wx


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wyPython')
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
