import unittest


class ProductInCart(object):

    def __init__(self, sale_price, coupon_discount, slot_type, slot_real_width):
        self.sale_price = sale_price
        self.coupon_discount = coupon_discount
        self.slot_type = slot_type
        self.slot_real_width = slot_real_width

    def __cmp__(self, other):
        if self.sale_price - self.coupon_discount < other.sale_price - other.coupon_discount:
            return -1
        elif self.sale_price - self.coupon_discount > other.sale_price - other.coupon_discount:
            return 1
        else:
            if self.slot_type < other.slot_type:
                return -1
            elif self.slot_type > other.slot_type:
                return 1
            else:
                if self.slot_real_width < other.slot_real_width:
                    return -1
                elif self.slot_real_width > other.slot_real_width:
                    return 1
                else:
                    return 0


class TestClassCmp(unittest.TestCase):
    """docstring for CmpTest"""
    def __init__(self, arg):
        super(TestClassCmp, self).__init__()
        self.arg = arg
        
    def test_sale_price(self):
        pass
        # products = []
        # a = ProductInCart(10, 9.9, "h", 250)
        # b = ProductInCart(10, 0, "l", 80)
        # products.append(a)
        # products.append(b)
        # print sorted(products)
        # print sorted(products, reversed=True)


if __name__ == '__main__':
    # unittest.main()
    products = []
    a = ProductInCart(10, 9.9, "h", 250)
    b = ProductInCart(10, 0, "l", 80)
    products.append(a)
    products.append(b)
    n = sorted(products)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20
    n = sorted(products, reverse=True)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20

    products = []
    a = ProductInCart(10, 9.9, "h", 250)
    b = ProductInCart(10, 9.9, "l", 80)
    products.append(a)
    products.append(b)
    n = sorted(products)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20
    n = sorted(products, reverse=True)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20

    products = []
    a = ProductInCart(10, 9.9, "l", 250)
    b = ProductInCart(10, 9.9, "l", 80)
    products.append(a)
    products.append(b)
    n = sorted(products)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20
    n = sorted(products, reverse=True)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20

    products = []
    a = ProductInCart(10, 9.9, "h", 250)
    b = ProductInCart(10, 9.9, "h", 80)
    products.append(a)
    products.append(b)
    n = sorted(products)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20
    n = sorted(products, reverse=True)
    for i in n:
        print "price: %s, discount:%s, type:%s, width:%s" % (i.sale_price, i.coupon_discount, i.slot_type, i.slot_real_width)
    print "#" * 20
    