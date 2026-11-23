"""Existing product tests; the agent adds tests for the new behavior live."""
import unittest
from app import greet


class GreetingTests(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("  Luka  "), "Hello, Luka!")

    def test_blank_name_uses_default(self):
        self.assertEqual(greet("  "), "Hello, World!")
