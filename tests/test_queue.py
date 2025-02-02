"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):

    def test_node_is_obj(self):
        self.assertIsInstance(Node("A"), object)

    def test_node_content(self):
        node1 = Node("A")
        self.assertEqual(node1.data, "A")
        self.assertEqual(node1.next_node, None)

    def test_queue_is_obj(self):
        self.assertIsInstance(Queue(), object)

    def test_queue_content(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        queue.enqueue("A")
        self.assertEqual(queue.head.data, "A")
        queue.enqueue("B")
        self.assertEqual(queue.head.next_node.data, "B")
        queue.enqueue("C")
        self.assertEqual(queue.tail.data, "C")
        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)
        """тесты на метод dequeue()"""
        self.assertEqual(str(queue.dequeue()), "A")
        self.assertEqual(queue.head.data, "B")
        queue.dequeue()
        self.assertEqual(queue.head.data, "C")
        queue.dequeue()
        self.assertEqual(queue.head, None)

    def test_queue_str(self):
        queue = Queue()
        self.assertEqual(str(Queue()), "")
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        self.assertEqual(str(queue), "A\nB\nC")
