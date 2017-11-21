from com.bridgelabz.utility.stack import Stack
class ArithExp:
    def run(self):
        stack=Stack()
        expression=input("enter the expression")
        for i in range(0,len(expression)):

            if(expression[i]=='('):
                stack.push(expression[i])
            if(expression[i]==')'):
                stack.pop()

        if(stack.isEmpty()==True):
            print("expression is balanced")
        else:
            print("expression is not balanced")

        return


ArithExp().run()