## Qzone API的Python实现

本项目致力于为Qzone中的信息使用Python抓取提供开箱可用的代码模块。

### Qzone Login / QQ空间登录

`qzone_login.py`提供QQ空间二维码登录功能。

调用`get_sessions()`函数后会判断当前目录中是否存在`session.pickle`。如果没有在项目目录下生成`qr.png`登录二维码文件，使用手机扫描后即可登录。该函数返回`requests.session`对象，并在当前目录下生成`session.pickle`保存`Session`对象。如果存在`session.pickle`文件则直接读取其中的内容。

> QQ空间的登陆状态保持时间较短，如果需要重新登录，请手动删除`session.pickle`文件。