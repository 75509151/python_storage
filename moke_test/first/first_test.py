# coding: utf-8

from mock import Mock, MagicMock, patch
import unittest
from client import visit_ustack
from contextlib import nested


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass


class Count():

    def add(self):
        pass


class Class(object):
    def method(self):
        pass


def function(a, b, c):
    pass

# test Count class


class TestCount(unittest.TestCase):

    def test_return_value(self):
        # return value
        count = Count()
        count.add = Mock(return_value=13)
        result = count.add(8, 5)
        self.assertEqual(result, 13)

        m = Mock()
        m.return_value = 5
        self.assertEqual(m(), 5)

        m = Mock(return_value=3)
        self.assertEqual(m(), 3)

    def test_db(self):
        m = Mock()
        cursor = m.connection.cursor.return_value
        cursor.execute.return_value = ["foo"]
        ret = m.connection.cursor().execute("SELECT 1")
        self.assertEqual(["foo"], ret)

    def test_assert_called(self):
        # 函数是否被以指定的参数调用
        real = ProductionClass()
        real.something = MagicMock()
        real.method()
        # real.something.assert_called_once_with(2, 2, 3)
        real.something.assert_called_once_with(1, 2, 3)
        self.assertEqual(real.something.called, True)

    def test_exception(self):
        m = Mock(side_effect=KeyError('foo'))
        with self.assertRaises(KeyError):
            m()

        m = Mock(side_effect=Exception('Boom!'))

        with self.assertRaises(Exception):
            m()

    def test_side_effect2(self):
        m = Mock(side_effect=KeyError('foo'))
        m.side_effect = [5, 4, 3, 2, 1]
        self.assertEqual(m(), 5)
        self.assertEqual(m(), 4)
        self.assertEqual(m(), 3)

    def test_side_effect_use(self):
        side_effect = lambda value: value + 1
        m = Mock(side_effect=side_effect)
        self.assertEqual(4, m(3))
        self.assertEqual(-8, m(-9))

        m = Mock(side_effect=KeyError, return_value=3)
        with self.assertRaises(KeyError):
            m()
        m.side_effect = None
        self.assertEqual(3, m())

    def test_call(self):
        m = Mock(return_value=None)
        self.assertIsNone(m.call_args)
        m()
        self.assertEqual((), m.call_args)
        m(3, 4)
        print m.call_args
        m(3, 4, 5, key='fish', next='w00t!')
        print m.call_args

    def test_base_path(self):
        pass

    def test_auto_spec(self):
        from mock import create_autospec
        mf = create_autospec(function, return_value="hehe")
        self.assertEqual("hehe", mf(1, 2, 3))
        mf.assert_called_with(1, 2, 3)
        with self.assertRaises(TypeError):
            mf("wrong arguments")


class TestPathClient(unittest.TestCase):
    """
    在了解了mock对象之后，我们来看两个方便测试的函数：patch和patch.object。这两个函数都会返回一个mock内部的类实例，这个类是class _patch。返回的这个类实例既可以作为函数的装饰器，也可以作为类的装饰器，也可以作为上下文管理器。使用patch或者patch.object的目的是为了控制mock的范围，意思就是在一个函数范围内，或者一个类的范围内，或者with语句的范围内mock掉一个对象。我们看个代码例子即可："""

    def test_success_request(self):
        status_code = '200'
        success_send = Mock(return_value=status_code)
        with patch('client.send_request', success_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

    def test_patch_func(self):
        status_code = '404'
        fail_send = Mock(return_value=status_code)
        with patch('client.send_request', fail_send):
            self.assertEqual(visit_ustack(), status_code)

    def test_patch_func2(self):
        status_code = '404'
        fail_send = Mock(return_value=status_code)
        import client
        with patch.object(client, 'send_request', fail_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

    def test_patch_class(self):

        with patch('__main__.Class') as MockClass:
            instance = MockClass.return_value
            instance.method.return_value = 'foo'
            assert Class() is instance
            assert Class().method() == 'foo'

    @patch("client.Form.fetch_product")
    def test_path_use(self, fetch_mock):
        import client
        fetch_mock.return_value = "success"
        self.assertEqual("success", client.Form().do_sell())


from client import rm


class RmTestCase(unittest.TestCase):

    @patch('client.os.path')
    @patch('client.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")

        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
