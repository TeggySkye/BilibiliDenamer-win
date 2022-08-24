import os
import sys
from pathlib import Path
'''解密'''
from numpy import fromfile, uint8   # pip install numpy
# mp4合并代码：
# file1 = "video.mp4"  # 可换成绝对路径
# file2 = "audio1.mp4"  # 可换成绝对路径
# result = "output.mp4"  # 可换成绝对路径
# os.system(f"ffmpeg.exe -i {file1} -i {file2} -acodec copy -vcodec copy {result}")

'''----------------若下载路径发生变化，更改此处----------------'''
# download_dir = "D:/0bilibili-downloadReserve/download"
download_dir = Path(sys.argv[0]).resolve().parent  # 脚本文件的父文件夹的绝对路径

'''----------------若前缀所在位置发生变化，更改此处----------------'''
start_sequence_of_title = '"PartNo":'
end_sequence_of_title = '","PartName"'

'''----------------若标题所在位置发生变化，更改此处----------------'''
start_label_of_title = '"title":'
end_label_of_title = '","duration"'

'''os.walk遍历该路径下所有路径和文件'''
cnt = 0
for f_path, dir_name, f_names in os.walk(download_dir):
    print("当前路径:", end='')
    print(f_path)  # 当前路径
    # print(dir_name)    #
    print("当前路径下的文件:", end='')  # 当前扫描的文件
    print(f_names)  # 当前扫描的文件
    # 状态变量，0表示未生成，1表示已生成
    sta_Video=0
    sta_Audio=0
    dir_out=0 # 1表示当前目录下的视频已经合并
    '''在当前目录下寻找MP4文件'''
    for f_name in f_names:
        if 'm4s' in f_name:
            mp4_name = f_name
            cnt = cnt+1
            '''保存M4S绝对路径'''
            mp4_path = f_path + '/' + mp4_name
            print('found one mp4 in:  ' + mp4_path)

            '''解密操作'''
            read = fromfile(mp4_path, dtype=uint8)
            if all(read[0:9] == [48, 48, 48, 48, 48, 48, 48, 48, 48]):
                if all(read[317:318] == [2]):
                    new_name = "video.mp4"
                    # 新文件的文件名
                    new_name_path = f_path + '/' + new_name
                    # 保存解密后的文件
                    read[9:].tofile(new_name_path)
                    file1 = new_name_path
                    sta_Video=1
                elif all(read[317:318] == [1]):
                    new_name = "audio.mp4"
                    # 新文件的文件名
                    new_name_path = f_path + '/' + new_name
                    # 保存解密后的文件
                    read[9:].tofile(new_name_path)
                    file2 = new_name_path
                    sta_Audio=1
                '''根据.info文件，找到标题内容'''
        if (sta_Audio == sta_Video == 1):
            # ('videoInfo' in f_name) and
            for f_inpath, dir_inname, f_innames in os.walk(f_path):
                if dir_out == 1:
                    break
                for f_inname in f_innames:
                    if 'videoInfo' in f_inname:
                        info_path = f_path + '/' + f_inname
                        print('found one info:  ' + info_path)

                        '''打开.info文件,编码方式可在VS code中打开查看'''
                        with open(info_path, encoding='utf-8') as f:
                            '''读取.info文件中所有内容'''
                            text_content = f.read()
                            # print(text_content)

                            # '''找到sequence位置'''
                            # sequence_start = text_content.find(start_sequence_of_title) + len(start_sequence_of_title)
                            # sequence_end = text_content.find(end_sequence_of_title, sequence_start)  # 字符结束的位置

                            '''找到标题位置'''
                            '''find:在字符串中查找指定子串，返回标题第一个字符的位置（0，1，2...）'''
                            title_numb_start = text_content.find(start_label_of_title) + len(
                                start_label_of_title)  # + len(start_label_of_title)为标题第一个字符的位置
                            title_numb_end = text_content.find(end_label_of_title, title_numb_start)  # 字符结束的位置
                            # print( str(title_numb_start) + "  " + str(title_numb_end) )

                            # '''new_name = P + sequence + title'''
                            # new_name = "P" + text_content[sequence_start + 1:sequence_end] + " " + text_content[title_numb_start + 1:title_numb_end] + ".mp4"
                            '''new_name = title'''
                            new_name = text_content[title_numb_start + 1:title_numb_end] + ".mp4"
                            new_name = new_name.replace('\\', '')  # \\表示\
                            new_name = new_name.replace(' ', '_')
                            new_name = new_name.replace('/', '')
                            new_name = new_name.replace(':', '')
                            new_name = new_name.replace('*', '')
                            new_name = new_name.replace('?', '')
                            new_name = new_name.replace('<', '')
                            new_name = new_name.replace('>', '')
                            new_name = new_name.replace('|', '')
                            print(new_name, end='')
                            f.close()
                            new_name_path = f_path + '/' + new_name

                            '''try以避免报错'''
                            try:
                                '''重命名'''
                                os.system(f"ffmpeg.exe -i {file1} -i {file2} -vcodec copy -acodec copy {new_name}")
                                # os.rename(mp4_path, new_name_path)
                                dir_out = 1
                                print(' successfully renamed and deleted')
                            except:
                                print(' failed')
                            try:
                                print("removing files...")
                                os.remove(file1)
                                os.remove(file2)
                                print(' success')
                            except:
                                print(' failed')

        else:
            pass
            # print('not mp4 file,continuing...')

    print('\n')
