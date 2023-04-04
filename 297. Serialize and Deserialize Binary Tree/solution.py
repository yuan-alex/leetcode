# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recursive(root):
            if root is None:
                return None
            return [root.val, recursive(root.left), recursive(root.right)]
        result = recursive(root)
        return json.dumps(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recursive(data):
            if data is None:
                return None
            node = TreeNode(data[0])
            node.left = recursive(data[1])
            node.right = recursive(data[2])
            return node
        parsed = json.loads(data)
        return recursive(parsed)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
