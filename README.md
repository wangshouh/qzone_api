## Qzone API的Python实现

本项目致力于为Qzone中的信息使用Python抓取提供开箱可用的代码模块。

### Qzone Login / QQ空间登录

`qzone_login.py`提供QQ空间二维码登录功能。

调用`get_sessions()`函数后会判断当前目录中是否存在`session.pickle`。如果没有在项目目录下生成`qr.png`登录二维码文件，使用手机扫描后即可登录。该函数返回`requests.session`对象，并在当前目录下生成`session.pickle`保存`Session`对象。如果存在`session.pickle`文件则直接读取其中的内容。

> QQ空间的登陆状态保持时间较短，如果需要重新登录，请手动删除`session.pickle`文件。

### Get active feeds / QQ空间最新说说获取

`qzone_api_spider.py`中的`get_active_feeds(s, qzonetoken, gtk_num, n=1)`函数用来获取QQ空间中的最新说说。

该函数所需的参数分别为：
- s request.Session对象，可以通过`get_sessions()`获取
- qzonetoken 通过调用`get_qzonetoken(s)`函数获取
- gtk_num 通过调用`get_gtk(s)`函数获取
- n 获取说说循环次数。单次循环会获得9或10条说说，默认为1，可根据需求自行修改

该函数返回由说说组成的`list`对象，可通过遍历获取每一条的详细信息。

