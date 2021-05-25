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

        if not root:
            str += 'None,'
        else:
            str += str(root)+','
            str += self.serialize(root.left)
            str += self.serialize(root.right)

        return str


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        encode = data.split(',')
        encoding = []
        for enc in encode:
            encoding.append(enc)

        return self.deserial(encoding)

    def deserial(self, encoding):
        if encoding[0] is None:
            encoding.pop(0)
            return None
        else:
            root = TreeNode(encoding[0])
            encoding.pop(0)
            root.left = self.deserial(encoding)
            root.right = self.deserial(encoding)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))