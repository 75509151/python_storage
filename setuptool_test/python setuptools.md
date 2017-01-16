[TOC]

## 问题提出

首先，当我们从公司的代码库checkout一个项目时，执行python setup.py develop,便可开始执行在我们自己的电脑上运行项目。不深究的话，也许就过了。毕竟项目已经运行起来了。可是深究的话，便为你以后自己搭建一个项目开启了一个良好的开始。恰好本人公司的代码重构，可以从０开始接触，便不打算放过这个难逢的机会。

```python setup.py develop```到底做了什么？

##二话不说，先上代码

setup.py

```.py



#!/usr/bin/env python



import sys

from setuptools import setup, find_packages



with open('README.txt') as f:

    long_description = f.read()



with open('CHANGES.txt') as f:

    long_description += "\n\n" + f.read()



with open('requirements.txt') as f:

    requires = f.read()





setup(name='platform', version='1.3',

      long_description=long_description,

      packages=find_packages(),

      include_package_data=True,

      zip_safe=False,

      install_requires=requires,

      description='Cereson Platform.',

      )

```



README.txt

```

# PLATFORM README

-----------------



Apply microservices and TDD makes enterprises more productive.



- Install packages.



./setup.py develop



- Show all callable commands.



fab -l



- Run some services.



fab run:user



- Run unit tests.



fab test



- Run system test.



fab sys



- Create platform documents.



fab doc

```

CHANGE.txt

```

0.1

---



- Platform on RabbitMQ.

-- All services can work in the internal net.



0.2

---



- Support python environment test.

-- Add tox to test various python environments.



0.3

---



- Clear service code.

-- Keep it simple and easy.



0.4

---



- Make setup.py controll all.

-- Now, it's easy to use.

-- It's easy to extend, too.



0.5

---



- Add pydoc.

-- Doc is important!



0.6

---



- Add sphinx.

-- Supply docs.



0.7



- Unify naming.

-- Add module's prefix to it's variables.



0.8



- Add configuration center

-- Any service can store data in it.



0.9



- Add reload



1.0



- It's a tag

-- Now it's time to develop all kinds of services.



1.1



- Add log configuration

-- Remove code dependency.



1.2



- Add fabric

-- Take fabric to manage tasks



1.3



- Extract all tasks arguments

-- Control all tasks from configuration files.

```

requirements.txt

```

alabaster==0.7.9

amqp==2.1.1

Babel==2.3.4

docopt==0.6.2

docutils==0.12

ecdsa==0.13

eventlet==0.19.0

Fabric==1.12.0

funcsigs==1.0.2

greenlet==0.4.10

imagesize==0.7.1

Jinja2==2.8

kombu==4.0.0

MarkupSafe==0.23

mock==2.0.0

mockredispy==2.9.3

mocksqlalchemy==0.1.2

mogo==0.4.0

mongolog==0.1.1

multiprocessing==2.6.2.1

MySQL-python==1.2.5

nameko==2.4.2

nameko-sqlalchemy==0.0.4

paramiko==1.17.2

path.py==9.0

pbr==1.10.0

pluggy==0.4.0

py==1.4.31

pycrypto==2.6.1

Pygments==2.1.3

pymongo==3.3.1

pytest==3.0.4

pytz==2016.7

PyYAML==3.12

redis==2.10.5

requests==2.12.3

six==1.10.0

snowballstemmer==1.2.1

Sphinx==1.5b1

SQLAlchemy==1.1.4

tox==2.5.0

vine==1.1.3

virtualenv==15.1.0

Werkzeug==0.11.11

```

##自己先想想

```python setup.py develop``` 看这句话。python 就是说用python的解释器，setup.py就是setup.py这个py脚本, develop估计是这个脚本文件能够带的参数，具体参数啥含义查资料

## 自己写之前，看看别人怎么说

[别人说](http://www.bjhee.com/setuptools.html)

#python打包分发工具 setuptools

python setuptools是python标准的打包及分发工具，简单易用。随python安装在我们的机器上，我们只需写一个简单的setup.py安装文件，就可以将我们的python应用打包。

##第一个项目实战

假设我们的项目名为setup-demo，包名为myapp　目录结构如下:

```

setup-demo/
  ├ setup.py         # 安装文件
  └ myapp/           # 源代码
      ├ __init__.py    
      ...
```

一个最基本的setup.py:

```

#coding:utf8

from setuptools import setup

 
setup(

    name='MyApp',         # 应用名

    version='1.0',        # 版本号

    packages=['myapp']    # 包括在安装包内的Python包

)

```

有了以上的setup.py文件，我们便可以打包，也可以将应用安装到本地python环境(虽然我们公司的项目比较大，但是实践发现，执行命令一样)。

###创建egg包

``` python setup.py 包名```

执行```python setup.py bdist_egg```

```

├── build

│   ├── bdist.linux-x86_64

│   └── lib.linux-x86_64-2.7

│       └── myapp

├── dist

├── myapp

└── MyApp.egg-info

```

会发现多个dist目录，并有个egg文件，文件格式为"应用名-版本号-python版本.egg"。并且多了个build和MyApp.egg-info来存放打包的中间结果。

###创建tar.gz包

```python setup.py sdist --formats=gztar```

同上一个相同的作用，不过创建的文件类型为tar.gz，看dist目录下多了一个MyApp-1.0.tar.gz

###安装应用

```python setup.py install```

该命令会将当前的Python应用安装到当前Python环境的”site-packages”目录下，这样其他程序就可以像导入标准库一样导入该应用的代码了。

###开发方式安装

```python setup.py develop```

如果应用在开发过程中会频繁变更，每次安装还需要先将原来的版本卸掉，很麻烦。使用”develop”开发方式安装的话，应用代码不会真的被拷贝到本地Python环境的”site-packages”目录下，而是在”site-packages”目录里创建一个指向当前应用位置的链接。这样如果当前位置的源码被改动，就会马上反映到”site-packages”里。

###引入非python文件

上例中，只是将'myapp'包下的源码打包，如果还想打包其他非python 的文件，如果静态文件(js,css,图片)。该如何做呢？

现在我们要在项目目录下添加一个"MANIFEST.in"文件。假设我们把所有的静态文件放在"static"目录下，现在的目录结构为:

```



setup-demo

    ├── MANIFEST.in    #清单文件

    ├── myapp                #源代码

    │   ├── __init__.py　

    │   └── static            #静态文件目录

    └── setup.py            #安装文件

```

MANIFEST.in

在文件中列出想要包内引入的目录路径

```

recursive-include myapp/static *

recursive-include myapp/xxx *

```

“recursive-include”表明包含子目录。别急，还有一件事要做，就是在”setup.py”中将” include_package_data”参数设为True：

```

#coding:utf8

from setuptools import setup

 
setup(

    name='MyApp',         # 应用名

    version='1.0',        # 版本号

    packages=['myapp'],   # 包括在安装包内的Python包

    include_package_data=True    # 启用清单文件MANIFEST.in

)
```

之后再次打包或者安装，”myapp/static”目录下的所有文件都会被包含在内。如果你想排除一部分文件，可以在setup.py中使用”exclude_package_date”参数，比如：

```

setup(

    ...

    include_package_data=True,    # 启用清单文件MANIFEST.in

    exclude_package_date={'':['.gitignore']}

)

```

上面的代码会将所有”.gitignore”文件排除在包外。如果上述”exclude_package_date”对象属性不为空，比如”{‘myapp’:[‘.gitignore’]}”，就表明只排除”myapp”包下的所有”.gitignore”文件。

### 自动安装依赖

我们的应用会依赖与第三方的python包，最傻的办法就是在运行的时候根据错误不断的安装依赖包，或者提前根据文档来安装依赖包，但是很麻烦，而且可能安装错版本。

    

我们可以在setup.py中指定依赖包，然后在使用setuptools安装应用时，依赖包的相应版本就会被自动安装。我们修改上面的setup.py文件， 加入"install_requires"参数:

- setup.py

```

#coding:utf8

from setuptools import setup

 
setup(

    name='MyApp',         # 应用名

    version='1.0',        # 版本号

    packages=['myapp'],   # 包括在安装包内的Python包

    include_package_data=True,    # 启用清单文件MANIFEST.in

    exclude_package_date={'':['.gitignore']},

    install_requires=[    # 依赖列表

        'Flask>=0.10',

        'Flask-SQLAlchemy>=1.5,<=2.1'

    ]

)

```

上面的代码中，我们声明了应用依赖Flask 0.10及以上版本，和Flask-SQLAlchemy 1.5及以上、2.1及以下版本。setuptools会先检查本地有没有符合要求的依赖包，如果没有的话，就会从PyPI中获得一个符合条件的最新的包安装到本地。

大家可以执行下试试，你会发现不但Flask 0.10.1（当前最新版本）被自动安装了，连Flask的依赖包Jinja2和Werkzeug也被自动安装了，很方便吧。

如果应用依赖的包无法从PyPI中获取怎么办，我们需要指定其下载路径：

***下载路径***

```

setup(

    ...

    install_requires=[    # 依赖列表

        'Flask>=0.10',

        'Flask-SQLAlchemy>=1.5,<=2.1'

    ],

    dependency_links=[    # 依赖包下载路径

        'http://example.com/dependency.tar.gz'

    ]

)

```

路径应指向一个egg包或tar.gz包，也可以是个包含下载地址（一个egg包或tar.gz包）的页面。文章作者个人建议直接指向文件。

###自动搜索python包

之前我们在setup.py中指定了”packages=[‘myapp’]”，说明将Python包”myapp”下的源码打包。如果我们的应用很大，Python包很多怎么办。大家看到这个参数是一个列表，我们当然可以将所有的源码包都列在里面，但肯定很多人觉得这样做很傻。的确，setuptools提供了”find_packages()”方法来自动搜索可以引入的Python包：

***setup.py***

```

#coding:utf8

from setuptools import setup, find_packages

 
setup(

    name='MyApp',               # 应用名

    version='1.0',              # 版本号

    packages=find_packages(),   # 包括在安装包内的Python包

    include_package_data=True,   # 启用清单文件MANIFEST.in

    exclude_package_date={'':['.gitignore']},

    install_requires=[          # 依赖列表

        'Flask>=0.10',

        'Flask-SQLAlchemy>=1.5,<=2.1'

    ]

）

```

这样当前项目内所有的Python包都会自动被搜索到并引入到打好的包内。”find_packages()”方法可以限定你要搜索的路径，比如使用”find_packages(‘src’)”就表明只在”src”子目录下搜索所有的Python包。

##补充

***zip_safe参数***
决定应用是否作为一个zip压缩后的egg文件安装在当前Python环境中，还是作为一个以.egg结尾的目录安装在当前环境中。因为有些工具不支持zip压缩文件，而且压缩后的包也不方便调试，所以建议将其设为False：”zip_safe=False”。

***描述信息***
部分参数提供了更多当前应用的细节信息，对打包安装并无任何影响，比如：

```

setup(

    ...

    author = "Billy He",

    author_email = "billy@bjhee.com",

    description = "This is a sample package",

    license = "MIT",

    keywords = "hello world example",

    url = "http://example.com/HelloWorld/",   # 项目主页

    long_description=__doc__,   # 从代码中获取文档注释

)

```

##更多内容

[setuptools官方文档]（）

##python requiremnts.txt

### requiremnts.txt的生成

```

pip freeze > requirements.txt
```

###手动安装

```

pip install -r requirements.txt

```

#我们的setup.py

***setup.py***

```

#!/usr/bin/env python



import sys

from setuptools import setup, find_packages



with open('README.txt') as f:

    long_description = f.read()



with open('CHANGES.txt') as f:

    long_description += "\n\n" + f.read()



with open('requirements.txt') as f:

    requires = f.read()





setup(name='platform', version='1.3',

      long_description=long_description,

      packages=find_packages(),

      include_package_data=True,

      zip_safe=False,

      install_requires=requires,

      description='Cereson Platform.',

      )

```

可以看的出来，我们的setup.py更简洁了，没有把 requires写到这里面。而是分到了requirements.txt中，这样也符合职责分明的原则。



