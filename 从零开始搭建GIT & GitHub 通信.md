从零开始搭建GIT & GitHub 通信

1.安装git，下载地址：[https://git-scm.com/download/win](https://link.jianshu.com/?t=https://git-scm.com/download/win)

2.文件夹里面右键 Git Bash Here

3.全局设置输入

```csharp
git config --global user.name "your name" 
git config --global user.email "your@email.com"
```

4.输入创建SSH KEY 点3次回车，建议在默认目录生成.ssh

```
ssh-keygen -t rsa -C "your@email.com"
```

5.前往GitHub 保存Key，Key目录再用户名-.ssh文件夹 id_rsa.pub

6.继续输入，输入yes

```
ssh -T git@github.com
```

7.GitHub上选择Clone with ssh，在git代码框输入ssh地址，就可以从github仓库复制到本地，例子：

```
git clone git@github.com:lixuanye1994/PythonTest.git
```

-------------------------------------------------------------------------------------

8.Push 到 github (上传到git仓库)

```
git init
git add README.md (目录里面创建一个readme.md)
git commit -m "first commit"
git remote add origin git@github.com:lixuanye1994/PythonTest.git
git push -u origin master
```

9.之后

```
git add XXXX(添加修改后的文件)
git commit -m "first commit" (添加备份说明)
git remote add origin git@github.com:lixuanye1994/PythonTest.git (连接远程仓库)
git push -u origin master (推送到master分支)
```

