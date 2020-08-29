# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class DoubleLinklist(object):
    pass


class LRUCache:

    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.cache = {}
        self.mostRecentNode = DoubleLinklist()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictleastRecent(key, value)
            else:
                self.currentSize += 1
                self.addrecentUse(key, value)
            self.cache[key] = DoubleLinklist(key,value)
        else:
            self.replaceKeyfromAdd(key, value)
        self.updateMostRecentNode(self.cache[key])

    def getValueFromKey(self, key):
        # Write your code here.
        pass

    def getMostRecentKey(self):
        # Write your code here.
        pass

    def evictleastRecent(self, key, value):
        pass

    def addrecentUse(self, key, value):
        pass

    def updateMostRecentNode(self):
        pass
