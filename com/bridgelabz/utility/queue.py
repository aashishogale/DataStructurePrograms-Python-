from com.bridgelabz.utility.linkedlist import LinkedList
class Queue:

      linkedlist=LinkedList()

      def enqueue(self,item):
            self.linkedlist.addatEnd(item)
            return

      def dequeue(self):

          return   self.linkedlist.removeAt(0)

      def dequeuerear(self):
          return self.linkedlist.removeAt(self.linkedlist.size())




      def isempty(self):
          return self.linkedlist.isempty()
      def display(self):
          self.linkedlist.display()


