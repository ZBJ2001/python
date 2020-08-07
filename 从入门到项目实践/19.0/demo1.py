# _*_ coding: UTF-8 _*_
# 开发团队 ：万宝软件部
# 开发人员 ：Administrator
# 开发时间 : 2020-7-25 22:01
# 文件名称 : demo1.py
# 开发工具 : PyCharm
# 任    务 ：
# 知 识 点 ：

import wx
import wx.xrc
# app = wx.App(False) #创建1个APP，禁用stdout/stderr重定向
# frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")  #这是一个顶层的window
# frame.Show(True)    #显示这个frame
# app.MainLoop()


class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( 100,200 ), wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


def main():
    app = wx.App(False)
    frame = MyFrame2(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()
