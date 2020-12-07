class documentation():

    def Abs(self):
        """
        The abs() function returns the absolute value of the specified number.
        :return:
        """
    def int(self):
        """
        The int() function converts the specified value into an integer number.
        :return:
        """
    def raw_input(self):
        """
        raw_input() function is used to accept user input.It presents a prompt to the user
        :return:
        """
documentation()

#exercice2
class Currency():
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)
str(c1)
#'5 dollars'
int(c1)
#5
repr(c1)
#'5 dollars'
c1 + 5
#10
c1 + c2
#15
#c1
#5 dollars
c1 += 5
#>>> c1
#10 dollars
c1 += c2
#>>> c1
#20 dollars
#c1 + c3
#TypeError: Cannot add between Currency type <dollar> and <shekel>