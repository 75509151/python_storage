# coding:utf-8
import copy

from collections import Counter

name = ["pid", "quantity", "status"]

# for k, v in data.items():
#     for slot in v:
#         slot_info = dict(zip(name, slot))
#         print slot_info


def change_mode(t):
    return dict(zip(name, t))


def get_machine_slots(data):
    machine_slots = {k: map(change_mode, v) for k, v in data.items()}
    return machine_slots


def fake_get_best_rows_01():
    data = {
        1: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        2: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        3: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        4: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        5: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        6: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        7: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        8: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        9: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        10: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        11: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        12: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        13: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        14: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        15: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
    }
    slots = get_machine_slots(data)
    return slots


def fake_get_best_rows_02():
    data = {
        1: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        2: [("02", 1, "g"), ("02", 1, "g"), ("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        3: [("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        4: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        5: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        6: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("03", 1, "g"), ("01", 1, "g")],
        7: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        8: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        9: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        10: [("01", 1, "g"), ("01", 1, "g"), ("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        11: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        12: [("01", 1, "g"), ("03", 1, "g"), ("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        13: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        14: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        15: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
    }
    slots = get_machine_slots(data)
    return slots


def fake_get_best_rows_03():
    data = {
        1: [("0A", 1, "g"), ("0B", 1, "g"), ("0C", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        2: [("0A", 1, "g"), ("0B", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        3: [("0A", 1, "g"), ("0B", 1, "g"), ("0E", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        4: [("0A", 1, "g"), ("0D", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        5: [("0C", 1, "g"), ("0D", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        6: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("03", 1, "g"), ("01", 1, "g")],
        7: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        8: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        9: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        10: [("01", 1, "g"), ("01", 1, "g"), ("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        11: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        12: [("01", 1, "g"), ("03", 1, "g"), ("03", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        13: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        14: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
        15: [("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g"), ("01", 1, "g")],
    }
    slots = get_machine_slots(data)
    return slots


# print fake_get_best_rows_01()


def get_product_rows_info(slots, product):
    """
    商品的曹位信息
    """
    pid = product[0]
    occupy_rows = set()
    occupy_rows_info = {}  # {行号: 数量, 行号: 数量}
    for row in slots.keys():
        for slot in slots[row]:
            if slot["pid"] == pid and slot["quantity"] and slot["status"] == "g":
                if row not in occupy_rows_info:
                    occupy_rows.add(row)
                    occupy_rows_info.setdefault(row, 1)
                else:
                    if occupy_rows_info[row]:
                        occupy_rows_info[row] += 1

    return occupy_rows, occupy_rows_info


def get_product_rows_pro(rows_info, product):
    need_quantity = product[1]


def get_rows(slots, products):
    products_row_info = {}

    for pid, sale_num in products.items():
        occupy_rows, occupy_rows_info = get_product_rows_info(slots, product)
        products_row_info[pid] = occupy_rows_info

    print "products_row_info", products_row_info

    products_row_pro = {}
    for product in products:
        pid = product[0]
        need_quantity = product[1]
        product_rows_pro = get_product_rows_pro(products_row_info[pid], product)

    # print "most_common", most_common - most_bad_row_set
    # if len(products_occupy_rows_l) <= 2:
    #     row_count = Counter(products_occupy_rows_l)
    #     return row_count.most_common(1)
    # else:
    #     print "len", len(products_occupy_rows_l)
    # row_count = Counter(products_occupy_rows_l)
    # best_rows = row_count.most_common(2)
    # print "temp_rows", best_rows
    # if len(best_rows) >= 2:
    #     first_num = best_rows[0][1]
    #     second_num = best_rows[1][1]
    #     if first_num == second_num:
    #         print "need contin"
    #         new_slots = copy.deepcopy(slots)
    #         del new_slots[best_rows[0][0]]
    #         print "new_slots1", new_slots
    #         fist_best_row = get_best_rows(new_slots, products)
    #         new_slots = copy.deepcopy(slots)
    #         del new_slots[best_rows[1][0]]
    #         print "new_slots2", new_slots
    #         second_best_row = get_best_rows(new_slots, products)
    #         if fist_best_row[0][1] > second_best_row[0][1]:
    #             return fist_best_row[0]
    #         elif fist_best_row[0][1] < second_best_row[0][1]:
    #             return second_best_row[0]
    # return best_rows


products = {"p1": 2, "p2": 3}

best_rows = get_rows(fake_get_best_rows_01(), products)

print "best_rows", best_rows

# products_02 = [("01", 2), ("02", 3), ("03", 2)]

# best_rows = get_best_rows(fake_get_best_rows_02(), products_02)

# print "best_rows", best_rows


# products_03 = [("0A", 2), ("0B", 3), ("0C", 2), ("0D", 2), ("0E", 1), ("01", 3)]

# best_rows = get_best_rows(fake_get_best_rows_03(), products_03)

# print "best_rows", best_rows


import unittest


class TestOrder(unittest.TestCase):
    """docstring for TestOrder"""

    def __init__(self, arg):
        super(TestOrder, self).__init__()
        self.arg = arg

    # def test_get_best_rows(self):
    #     products = [("01", 2), ("02", 3)]
    #     rows = get_best_rows(fake_get_best_rows_01(), products)
        # self.assertEqual(6, rows)


if __name__ == '__main__':
    unittest.main()


# 0 0 0 4 4 4
# 1 2 3
# 1 2 3
# 1 2
# 1 3


#
