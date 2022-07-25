# 哔哩哔哩Windows版网课批量解密和重命名
> [哔哩哔哩Windows版](https://app.bilibili.com/?spm_id_from=333.880.b_696e7465726e6174696f6e616c486561646572.9)：v1.3.1
## 代码功能
将哔哩哔哩哔哩哔哩Windows版中下载的网课批量**解密**和**更名**，视频输出结果保留在**本项目的根目录**/***.exe文件的根目录**下。

> 注：本代码仅用于学习。

## 实现逻辑
根据MP4目录下的.info文件命名标题。

## 使用方法
~~根据自己哔哩哔哩中设置的下载目录，**需更改第8行的download_dir**后，即可运行。~~

~~例如：download_dir = "D:/download/"~~

~~又例如：download_dir = "D:/download/255067124/"~~

不想了解代码的童鞋，**仅需下载BilibiliDeNamer_win.exe文件**（19MB）。

将BilibiliDeNamer_win.exe拷贝到视频下载的位置，该位置（包括子文件夹）中的**所有**.m4s文件都将被合并和重命名。

如需将所有视频打包，生成的视频文件在**本项目的根目录**/***.exe文件的根目录**下，全选后复制到其他路径即可。

操作完成后，哔哩哔哩缓存文件不会进行任何更改，还可在哔哩哔哩软件中播放。

## TODO
- 有的标题带有文件名的非法符号，需替换。
- 有的同一标题带有多个视频，若用相同标题命名，导出时会有问题。