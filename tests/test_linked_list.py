"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def test_node_is_obj(self):
        self.assertIsInstance(Node("A"), object)

    def test_node_content(self):
        node1 = Node("A")
        self.assertEqual(node1.data, "A")
        self.assertEqual(node1.next_node, None)

    def test_is_obj(self):
        self.assertIsInstance(LinkedList(), object)

    def test_linked_list_content(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        ll.insert_at_end({'id': 0})
        self.assertEqual(ll.head.next_node.next_node.data, {'id': 0})
        # str tests
        self.assertEqual(str(ll), "{'id': 2} -> {'id': 1} -> {'id': 0} -> None")
        ll2 = LinkedList()
        with self.assertRaises(AssertionError):
            self.assertEqual(str(ll2), None)
