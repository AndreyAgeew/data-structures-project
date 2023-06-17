"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(str(self.stack), "Stack: 3 -> 2 -> 1")

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty_stack(self):
        self.assertRaises(Exception, self.stack.pop)

    def test_iteration(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        result = [item for item in self.stack]
        self.assertEqual(result, [3, 2, 1])

    def test_str_empty_stack(self):
        self.assertEqual(str(self.stack), "Stack is empty")

    def test_str_non_empty_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(str(self.stack), "Stack: 3 -> 2 -> 1")

    def test_multiple_push_pop(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)

    def test_push_pop_alternate(self):
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.stack.push(3)
        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()
