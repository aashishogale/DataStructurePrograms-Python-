from com.bridgelabz.utility.linkedlist import LinkedList
class UnorderedList:

    def run(self):
         llist = LinkedList()
         filename="/home/bridgeit/Desktop/unorderedlist"
         with open("/home/bridgeit/Desktop/unorderedlist") as  file:

                list1=file.read().rstrip("\n").split(",")


         for i in range(0,len(list1)):
                    llist.addatEnd(list1[i])





         char='y'
         while(char!='n'):
            name=input("enter the name")
            if llist.search(name):
               print("removed element",llist.remove(name))
               llist.writeToFile(filename)



            else:
                llist.addatEnd(name)
                llist.writeToFile(filename)

            char=input("do you want to continue")


         return







UnorderedList().run()
