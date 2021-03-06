# coding:utf-8
'''
/**
 * 观察者模式应用场景实例
 *
 * 免责声明:本文只是以哈票网举例，示例中并未涉及哈票网任何业务代码，全部原创，如有雷同，纯属巧合。
 *
 * 场景描述：
 * 哈票以购票为核心业务(此模式不限于该业务)，但围绕购票会产生不同的其他逻辑，如：
 * 1、购票后记录文本日志
 * 2、购票后记录数据库日志
 * 3、购票后发送短信
 * 4、购票送抵扣卷、兑换卷、积分
 * 5、其他各类活动等
 *
 * 传统解决方案:
 * 在购票逻辑等类内部增加相关代码，完成各种逻辑。
 *
 * 存在问题：
 * 1、一旦某个业务逻辑发生改变，如购票业务中增加其他业务逻辑，需要修改购票核心文件、甚至购票流程。
 * 2、日积月累后，文件冗长，导致后续维护困难。
 *
 * 存在问题原因主要是程序的"紧密耦合"，使用观察模式将目前的业务逻辑优化成"松耦合"，达到易维护、易修改的目的，
 * 同时也符合面向接口编程的思想。
 *
 * 观察者模式典型实现方式：
 * 1、定义2个接口：观察者（通知）接口、被观察者（主题）接口
 * 2、定义2个类，观察者对象实现观察者接口、主题类实现被观者接口
 * 3、主题类注册自己需要通知的观察者
 * 4、主题类某个业务逻辑发生时通知观察者对象，每个观察者执行自己的业务逻辑。
 *
 * 示例：如以下代码
 *
 */
'''


class Subject(object):
    """docstring for Subject"""

    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def del_observer(self, obs):
        self.observers.remove(obs)

    def notify_observer(self, *args, **kwarg):
        for obs in self.observers:
            obs.update(*args, **kwarg)


class Observer(object):
    """docstring for ClassName"""

    def update(self, *arg, **kwarg):
        pass


# 主题类（购票）

class HipiaoBuy(Subject):
    """docstring for HipiaoBuy"""

    def __init__(self):
        super(HipiaoBuy, self).__init__()

    def buy_ticket(self, ticket):
        # TODO 购票逻辑
        pass
        # notify
        self.notify_observer(ticket=ticket)

#=========================定义多个通知====================


# 短信日志通知
class HipiaoMSM(Observer):
    """docstring for HipiaoMSM"""

    def __init__(self):
        super(HipiaoMSM, self).__init__()

    def update(self, *arg, **kwarg):
        print "短信日志记录：购票成功! %s" % kwarg.get("tikcet", "new")


# 文本日志通知
class HipiaoTxt(Observer):
    def __init(self):
        super(HipiaoTxt, self).__init__()

    def update(self, *arg, **kwarg):
        print "文本日志记录：购票成功:%s" % kwarg.get("ticket", "default")


# 抵扣卷赠送通知
class HipiaoDikou(Observer):
    """docstring for HipiaoDikou"""

    def __init__(self):
        super(HipiaoDikou, self).__init__()

    def update(self, *arg, **kwarg):
        print "赠送抵扣卷：购票成功: %s" % kwarg.get("ticket", "default")


if __name__ == '__main__':
    buy = HipiaoBuy()
    buy.add_observer(HipiaoMSM())
    buy.add_observer(HipiaoTxt())
    buy.buy_ticket("hehe")
