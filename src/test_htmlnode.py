import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://boot.dev"},
            )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_init(self):
        node = LeafNode("p", "This is a paragraph.", {"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph.")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "text"})

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph.", {"class": "text"})
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph., {'class': 'text'})")

    def test_to_html(self):
        node = LeafNode("a", "This is a paragraph.", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a paragraph.</a>')

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph.</p>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph without a tag.")
        self.assertEqual(node.to_html(), 'This is a paragraph without a tag.')

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph without props.", None)
        self.assertEqual(node.to_html(), '<p>This is a paragraph without props.</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span><b>grandchild</b></span></div>')

    def test_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", {"class": "text"})
        parent_node = ParentNode("div", [child_node], {"id": "main"})
        self.assertEqual(parent_node.to_html(), '<div id="main"><span class="text">child</span></div>')

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), '<div><span>child1</span><span>child2</span></div>')

if __name__ == "__main__":
    unittest.main()