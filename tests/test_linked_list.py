"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(str(self.ll),
                         "{'id': 0, 'username': 'serebro'} -> {'id': 1, 'username': 'lazzy508509'} -> None")

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.assertEqual(str(self.ll),
                         "{'id': 1, 'username': 'lazzy508509'} -> {'id': 2, 'username': 'mik.roz'} -> {'id': 3, 'username': 'mosh_s'} -> None")

    def test_to_list(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = self.ll.to_list()
        expected = [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                    {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}]
        self.assertEqual(lst, expected)

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        user_data = self.ll.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id_nonexistent_id(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        user_data = self.ll.get_data_by_id(3)
        self.assertIsNone(user_data)

    def test_get_data_by_id_incorrect_data(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end('idusername')
        self.ll.insert_at_end([1, 2, 3])
        self.ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertIsNone(self.ll.get_data_by_id(4))

    def test_str_method_empty_list(self):
        self.assertEqual(str(self.ll), " -> None")

    def test_str_method_nonempty_list(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.assertEqual(str(self.ll),
                         "{'id': 1, 'username': 'lazzy508509'} -> {'id': 2, 'username': 'mik.roz'} -> {'id': 3, 'username': 'mosh_s'} -> None")


if __name__ == '__main__':
    unittest.main()
