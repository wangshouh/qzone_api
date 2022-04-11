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

### Get person feeds / 正序获取说说

`qzone_api_spider.py`中的`get_person_feeds(s, gtk_num, uin, qzonetoken, n=1)`函数用来获取QQ空间中的以时间正序排列说说（即从账号第一条说说开始获取）。

该函数主要用于获取自己的所有说说，也可以获取他人的说说。但后者经常由于QQ空间的权限设置导致失败。故而不建议使用此函数爬取他人说说。

该函数所需的参数分别为：
- s request.Session对象，可以通过`get_sessions()`获取
- qzonetoken 通过调用`get_qzonetoken(s)`函数获取
- gtk_num 通过调用`get_gtk(s)`函数获取
- uin 所需爬取的QQ号
- n 获取说说循环次数。单次循环会获得20条说说，默认为1，可根据需求自行修改

该函数返回由说说组成的`list`对象，可通过遍历获取每一条的详细信息。

> 注意： 该函数可通过更改内部参数实现抓取他人说说，具体实现方式为更改`param`中的`pos`参数，将其设为0，可以获取有权限限制的他人说说。
### Get Feeds / 逆序获得说说

`qzone_api_spider.py`中的`get_feeds(s, qzonetoken, gtk_num, uin, n=1)`函数用来获取QQ空间中的以时间逆序排列说说（即从账号第新说说向前获取）。

该函数主要用于获取可进入空间的最新说说。该函数基本适用于一切有权限访问的QQ空间。你可以使用该函数比较完整的获取特定朋友的最新说说。但该函数也存在一定问题，即如果您对说说展示有限制的好友使用，调整`n`参数也无法获取更多说说，反而会导致多次获取同一说说。在此处举一个例子，如果您的朋友仅展示5条说说，您将`n`设置为2（理论上可以获取12条说说），但实际得到的说说数量为5条说说各重复一次，请在后期数据清洗时注意此重复数据问题。

该函数所需的参数分别为：
- s request.Session对象，可以通过`get_sessions()`获取
- qzonetoken 通过调用`get_qzonetoken(s)`函数获取
- gtk_num 通过调用`get_gtk(s)`函数获取
- uin 所需爬取的QQ号
- n 获取说说循环次数。单次循环会获得6条说说，默认为1，可根据需求自行修改

该函数返回由说说组成的`list`对象，可通过遍历获取每一条的详细信息。

