import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )


if __name__ == "__main__":
    unittest.main()