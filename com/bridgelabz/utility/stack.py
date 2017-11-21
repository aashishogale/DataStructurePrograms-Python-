from com.bridgelabz.utility.linkedlist import LinkedList
class Stack:

    linkedlist=LinkedList()

    def push(self,item):
        self.linkedlist.addatStart(item)
        return

    def pop(self):
        self.linkedlist.removeAt(0)

    def isEmpty(self):
        if(self.linkedlist.isempty()):
            return True
        else:
            return False