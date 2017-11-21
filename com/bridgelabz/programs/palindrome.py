from com.bridgelabz.utility.queue import Queue
class Palindrome:
    def run(self):
        queue=Queue()
        stringp=""
        string=input("enter string")
        for i in range(0,len(string)):
            queue.enqueue(string[i])

        for i in range(0,len(string)):
            stringp=stringp+queue.dequeuerear()

        if(string==stringp):
            print("string is a palindrome")
        else:
            print("not a palindrome")

        return

Palindrome().run()