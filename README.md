# learn python3
# ... ssh go

0.  添加本地git库

    $ git init 

    $ git add .

    $ git commit -m ""

    $ git remote add origin git@xxx.git or git remote add https:...

    第一次

    $ git push -u origin master

    以后不用加 -u

1.  在本地git中添加user.name & user.email

    $ git config --global user.name ""

    $ git config --global user.email ""

2.  github上有两种协议 https & ssh

    git@xxx.git = 选择ssh并cp

3.  在本地ssh中添加密钥对

    $ ssh-keygen -t rsa

    $ cd ~/.ssh

    分别为id_rsa和id_rsa.pub

4.  将id_rsa.pub里边是内容cp到github中

5.  测试 ssh -T git@github.com

6.  查看本地git远程url并修改为ssh

    $ git remote -v

    $ git remote set-url origin git@xxx.git
    
