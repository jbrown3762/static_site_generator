import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        tn1 = TextNode("This is a string", TextType.BOLD, None)
        tn2 = TextNode("This is a string", TextType.BOLD)
        self.assertEqual(tn1, tn2)
    
    def test_not_eq_url(self):
        tn1 = TextNode("This is a string", TextType.BOLD, None)
        tn2 = TextNode("This is a string", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(tn1, tn2)

    def test_not_eq_type(self):
        tn1 = TextNode("This is a string", TextType.BOLD, "https://boot.dev")
        tn2 = TextNode("This is a string", TextType.ITALIC, "https://boot.dev")
        self.assertNotEqual(tn1, tn2)


if __name__ == "__main__":
    unittest.main()