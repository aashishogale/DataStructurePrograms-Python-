from com.bridgelabz.utility.queue import Queue
class Banking:
    def run(self):
        queue=Queue()
        money=0
        char ='y'
        while(char!='n'):

            choice=input("select e for enqueue and d for dequeue")
            if(choice=='e'):

               name=input("enter name")
               queue.enqueue(name)
               select=input("enter w for withdraw and d for deposit")
               if(select=='w'):
                   amount=int(input("withdraw amount"))
                   if(money<amount):
                       print("insufficient funds")
                   else:
                       print("funds added")
                       money=money+amount
               else:
                   amount = int(input("deposit amount"))
                   amount=amount+money


            else:
                queue.dequeue()

            char=input("do you want to continue")

        queue.display()
        return



Banking().run()
