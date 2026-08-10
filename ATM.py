class Atm:
	def __init__(self):
		print("Scan your card and enter your pin code to login..")
		self.pin=3245
		self.balance=50000
	
	
	
	def check_balance(self):
		print(f"Your Current Balance is {self.balance}\n")
		
	
		
	
	
	def deposit_money(self):
		Amount=int(input("Enter amount  to deposit: "))
		if Amount <=0:
			print("Invalid amount. Please enter a Positive amount ❌ \n ")
		self.balance+=Amount
		print("Deposit Done succesfully ✅ \n")
	
	
	
	def withdrawl_money(self):
		Amount=int(input("Enter Amount of withdrawl: "))
		if Amount > self.balance:
			print("Insufficient Balance ❌ \n")
		elif Amount <= 0:
			print("Invalid amount. Please enter a positive value. ❌ \n")
		else:
			self.balance-=Amount
			print("Withdrawl Done Successfully ✅ \n")
		
	
	
	def Change_pin(self):
		old_pin=int(input("Enter Old Pin code : "))
		
		if old_pin==self.pin:
			new_pin=int(input("Enter New Pin: "))
			if 1000 <= new_pin <=9999:
				self.pin=new_pin
				print("Pin Changed Sucessfully✅")
		else:
			print("Wrong Pin..❌")
			
	
	
		
	

def main():
	obj=Atm()
	while True:
		print("1.Check balance.")
		print("2. Deposit Money.")
		print("3. Make a withdrawl..")
		print("4. Change pin")
		print("5.Exit. \n")
	
		choice=int(input("Enter choice 1- 5: "))
		
		if choice==1:
			obj.check_balance()
		
		elif choice==2:
			obj.deposit_money()
		
		elif choice==3:
			obj.withdrawl_money()
		
		elif choice==4:
			obj.Change_pin()
		
		elif choice==5:
			print("Thanks for using our service..")
			break


obj=Atm()
def Login():
	while True:
		print("Type 0 for quit program ")
		
		pin_code=int(input("Enter login pin: "))
		if pin_code==obj.pin:
			main()
		elif pin_code==0:
			print("Thanks for using our service..")
			break
		else:
			print("Wrong Pin")
Login()