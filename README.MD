### zfun

  > 个人常用函数库。**Z**henghy **Fun**tion

### Install:

    pip3 install -U zfun

### Log

  - Version 1.1.6

    Modify `BIO.humanChrName`, 默认为1-22,X,Y,M. 输入参数`cl`可选。

  - Version 1.1.5

    Modify `mkdirf`, 接受一个路径，如果前面目录存在则创建。否则返回异常，退出程序。

  - Version 1.1.4
  
    Modify `MYSQL.ExecQuery`. 修改数据库查询返回值，`res[0]`为列名。不兼容以前的版本。

    Add Class `BIO`. 增加生物信息学常用内容。增加静态方法`BIO.humanChrName`，返回人类染色体名称的字典。

  - Version 1.1.0
  
    精简了常用函数：nowf(), mkdirf(),MYSQL(), mkscript()