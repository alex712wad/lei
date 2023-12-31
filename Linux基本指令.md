# Linux基本指令

#### 对文件目录进行操作（cd）

1. cd ... 返回上一级目录
2. cd .../... 返回上两级目录
3. cd /home 进入“/home”目录
4. cd 进入个人的主目录
5. cd ~user1 进入个人的主目录
6. cd - 返回上次所在的目录
7. pwd 显示当前路径

#### 对文件进行操作（ls）

1. ls 查看当前目录中所有的文件

2. ls -F 查看目录中的文件并且会将文件分类是目录文件会在末尾加“ / ”是可执行文件会在末尾加“ * ”是链接文件会加“ @ ”

   ![image-20230410210719689](C:\Users\12868\AppData\Roaming\Typora\typora-user-images\image-20230410210719689.png)

3. ls -a 显示隐藏文件

4. ls -F 查看没当前目录中的文件

5. ls -l 显示文件和目录的详细资料

6. ls [0-9] 显示包含对应数字的文件夹名和目录名

#### 对文件夹进行操作如增加删除等（dir）

1. tree 显示文件和目录由根目录开始的树形结构
2. lstree 显示文件和目录由根目录开始的树形结构
3. mkdir  XXX 创建一个叫XXX的文件夹
4. mkdir XXX   XXX  创建两个文件夹
5. mkdir -p /tmp/dir1/dir2  创建对应的目录
6. rm -f XXX 删除一个叫XXX的文件
7. rmdir XXX 删除一个叫XXX的目录
8. rm -rf XXX 删除XXX的目录和内容
9. rm -rf XXX  XXX  删除XXX和XXX 的目录和内容
10. mv aaa vvv 重命名/移动一个目录（将aaa改为vvv）
11. cp -a dir1 dir2 复制一个目录

