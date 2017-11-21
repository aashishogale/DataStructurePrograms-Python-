from com.bridgelabz.utility.linkedlist import LinkedList
class Orderedlist:
    def run(self):
        llist = LinkedList()
        filename = "/home/bridgeit/Desktop/orderedlist"
        with open("/home/bridgeit/Desktop/orderedlist") as  file:
            list1 = file.read().rstrip("\n").split(",")
        for i in range(0, len(list1)):
            llist.addSorted(list1[i])

        char = 'y'
        while (char != 'n'):
            number = int(input("enter the name"))
            if llist.search(number):
                print("removed element", llist.remove(number))
                llist.writeToFile(filename)



            else:
                llist.addSorted(number)
                llist.writeToFile(filename)

            char = input("do you want to continue")

        return

Orderedlist().run()