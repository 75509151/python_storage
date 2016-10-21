![sour](http://coolshell.cn/articles/11265.html)

# the simple example
``` hello.py
def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodbey, %s" % fn.__name__
        return wrapper


@hello
def foo():
    print "i am jay"

if __name__ == "__main__":
    foo()

```

if you run this file , you can see
```
    hello, foo
    i am jay
    goodbey, foo
```


# the nature of decorator 

```
@decorator_name
def func():
    pass
```
if you use @decorator_name to decorate one function ,
the interperter will interperte it to such statements below :
```
    func = decorator_name(func)
```

it not only  be interperted  to this statements,
but also run. we can see example below:
```
def fuck(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()
 
@fuck
def wfg():
    pass
``` 
only this code, print the output.

the decorator must return a function to func, if not, when we call the func(), excetion will be thrown.

if the decorator 


# more than one decorator

```
@decorator_one
@decorator_two
def func():
    pass
```
it equal to :

```
func = decorator_one(decorator_two(func))

```

# decorator with paramters

```
@decorator(arg1, arg2)
def func():
    pass
```
equal:
```
func = decorator(arg1, arg2)(func)
```

## example
``` python
def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator
 
@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"
 
print hello()
 
# 输出：
# <b class='bold_css'><i class='italic_css'>hello world</i></b>
```

# class decorator

```
class MyDecorator(object):
    def __init__(self, fn):
        print "__init__"
        self.fn = fn
    def __call__(self):
        self.fn()
        print "over"

@MyDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"
aFunction()

```
output:
```
# inside myDecorator.__init__()
# Finished decorating aFunction()
# inside aFunction()
# inside myDecorator.__call__()
```
> 
> 上面这个示例展示了，用类的方式声明一个decorator。我们可以看到这个类中有两个成员：
1）一个是__init__()，这个方法是在我们给某个函数decorator时被调用，所以，需要有一个fn的参数，也就是被decorator的函数。
2）一个是__call__()，这个方法是在我们调用被decorator函数时被调用的。
上面输出可以看到整个程序的执行顺序。