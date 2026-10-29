# Preventing from accessing cloud.tags["PYTHON"]; TO PREVENT KeyError: 'PYTHON'
# To make it inaccessible or private form the outside, prefix it with 2-underlines
# Point to the instance tags = {} and click Fn+F2, and edit it with prefix 2-underlines
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
# print(cloud._TagCloud__tags["python"]) this is still accessible
