"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def test_node_is_obj(self):
        self.assertIsInstance(Node("A"), object)

    def test_node_content(self):
        node1 = Node("A")
        self.assertEqual(node1.data, "A")
        self.assertEqual(node1.next_node, None)

    def test_stack_is_obj(self):
        self.assertIsInstance(Stack(), object)

    def test_stack_content(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push("A")
        self.assertEqual(stack.top.data, "A")
        stack.push("B")
        self.assertEqual(stack.top.data, "B")
        self.assertEqual(stack.top.next_node.data, "A")


