class LinkedList:
    def __init__(self):
        self.head = None

    def addatEnd(self, item):
        node = Node(item)
        if (self.isempty()):

            self.head = node


        else:
            temp = self.head
            while (temp != None or temp == self.head):

                if temp.getNext() == None:
                    temp.setNext(node)

                    break
                temp = temp.getNext()

        return

    def addatStart(self, item):
        node = Node(item)
        if (self.isempty()):

            self.head = node
        else:
            node.next = self.head
            self.head=node
        return

    def removeAt(self,pos):
        cposition=0
        if (self.isempty()):
            return ("the list is empty")
        elif (pos==0):
            temp = self.head
            self.head = temp.next
            return temp.data
        else:
            temp = self.head
            while (temp != None):

                if (cposition==pos):
                    previous.next = temp.next
                    return temp.data
                previous = temp
                temp = temp.next
                cposition+=1

        return ("element not found")


    def remove(self, item):

        if (self.isempty()):
            return ("the list is empty")
        elif(self.head.data==item):
            temp = self.head
            self.head=temp.next
            return temp.data
        else:
            temp = self.head
            while (temp != None):

                if (temp.data == str(item)):
                    previous.next = temp.next
                    return temp.data
                previous = temp
                temp = temp.next

        return ("element not found")

    def isempty(self):
        return self.head == None

    def index(self, item):
        position = 0
        if (self.isempty()):
            return ("the list is empty")
        else:
            temp = self.head
            while (temp.next != None):

                if (temp.data == item):
                    return position

                temp = temp.next
                position += 1
        return ("element not found")

    def addSorted(self, item):
        position = 0
        if (self.isempty()):
            self.addatEnd(item)
            return
        else:
            temp = self.head
            while (temp!= None):

                while (int(temp.data) < int(item)):
                     temp = temp.next
                     position += 1

                     if (temp == None):
                         break


                self.insert(item, position)
                return

        return

    def insert(self, item, itposition):

        position = 0
        node = Node(item)
        if (self.isempty()):

            self.head = node
        elif (itposition == 0):
            self.addatStart(item)
        else:
            temp = self.head

            while (temp != None):

                if (position==itposition):
                    node.next = temp
                    previous.next = node
                    break

                previous = temp
                temp = temp.next
                if(temp==None):
                    self.addatEnd(item)
                position += 1

        return

    def size(self):
        temp = self.head
        size = 0
        while (temp != None):
            temp = temp.next
            if (temp == None):
                return size

            size += 1

    def search(self, item):
        temp = self.head
        while (temp.next != None):

            if (temp.data == str(item)):
                return True
            temp=temp.next

        return False

    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp=temp.getNext()
        return

    def writeToFile(self,filename):
        with open(filename,"w") as  file:
            temp=self.head
            while(temp!=None):
                file.write(str(temp.data))
                if(temp.next!=None):
                    file.write(",")
                temp=temp.next
        return

class Node:
    def __init__(self, edata):
        self.data = edata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, edata):
        self.data = edata

    def setNext(self, enext):
        self.next = enext
