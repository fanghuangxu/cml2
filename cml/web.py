def show_url(url):
    import wx
    import wx.html2

    class MyFrame(wx.Frame):
        def __init__(self, parent, title ,url):
            super().__init__(parent, title=title)

            # 创建 WebView 控件
            self.webview = wx.html2.WebView.New(self)

            # 设置 WebView 控件的大小
            self.webview.SetSize((800, 600))

            # 加载 www.baidu.com 页面
            self.webview.LoadURL(url)

            # 创建一个 Sizer 来布局控件
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self.webview, 1, wx.EXPAND, 5)

            # 设置 Sizer 为当前 Frame 的默认 Sizer
            self.SetSizer(sizer)

            # 设置 Frame 的大小
            self.SetSize((800, 600))

            # 设置 Frame 居中显示
            self.Centre()

    # 创建应用程序
    app = wx.App()

    # 创建主窗口
    frame = MyFrame(None, "sb world wids web ",url=url)

    # 显示主窗口
    frame.Show()

    # 启动应用程序事件循环
    app.MainLoop()
