import collections
class TreeNode:
    def __init__(self,name,value):
        self.map = collections.defaultdict(TreeNode)
        self.name = name
        self.value = -1


class FileSystem:

    def __init__(self):

        self.root = TreeNode('')


    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        comp = path.split('/')
        # 第一个文件路径是分割的      
        for i in range(1,len(comp)):
            if comp[i] not in cur.map:

                if i == len(path) - 1:
                    cur.map[comp[i]] = TreeNode(comp[i])
                else:
                    return False
        if cur.value != -1:
            return False
        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root
        comp = path.split('/')
        for i in range(len(comp)):
            if comp[i] not in cur.map:
                return False
            cur = cur.map[comp[i]]

        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)