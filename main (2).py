class bank_account:
  def __init__(self):
      self.__name=str(input("enter the name of account holder:"))
      self.__ano=int(input("enter the type of account number:"))
      self.__balance=0
      print ("hello!!! welcome to the deposit & withdrawal machine ")
  def deposit(self):
      __amount=float(input("enter amount to be deposited:"))
      if __amount>0:
         self.__balance+= __amount
         print("\n amount deposited:",__amount)
  def withdraw(self):
      __amount=float(input("enter amount to be withdrawn:"))
      if self.__balance>=__amount:
          self.__balance-=__amount
          print("\n you withdraw:",__amount)
          print("\n balance:",self.__balance)
      else:
          print("\n insufficient balance ")
  def display(self):
      print("\n accountholder name:",self.__name)
      print("\n account number:",self.__ano)
      print("\n net available balance=",self.__balance)
s=bank_account()
s.deposit()
s.withdraw()
s.display()
  
