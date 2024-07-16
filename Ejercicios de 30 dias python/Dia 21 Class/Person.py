class PersonAccount:
	def __init__(self,first_name,last_name,incomes,expenses):
		self.first_name=first_name
		self.last_name=last_name
		self.incomes=incomes
		self.expenses=expenses

	def total_incomes(self):
		total=0
		for income in self.incomes:
			total+=income["value"]
		return total
	def total_expenses(self):
		total=0
		for expense in self.expenses:
			total+=expense["value"]
		return total*-1
	def add_income(self,description,value):
		self.incomes.append({"description":description,"value":value})
	def add_expense(self,description,value):
		self.expenses.append({"description":description,"value":value})
	def account_balance(self):
		total_in_account=self.total_incomes()+self.total_expenses()
		return f'total en la cuenta {total_in_account}'
	def account_info(self):
		return f'Esta cuenta le pertenece a {self.first_name} {self.last_name} con un {self.account_balance()}'

first_name="Luis"
last_name="Ahumedo"
incomes=[{"description":"Sueldo","value":2970000}]
expenses=[{"description":"icetex","value":283000},{"description":"arriendo","value":55000},{"description":"comida","value":300000}]

cuenta_luis=PersonAccount(first_name,last_name,incomes,expenses)
print(cuenta_luis.account_info())
print(cuenta_luis.total_incomes())
print(cuenta_luis.total_expenses())
print(cuenta_luis.account_balance())
cuenta_luis.add_expense("viaje",170000)
cuenta_luis.add_income("prima",1240000)
print(cuenta_luis.total_incomes())
print(cuenta_luis.total_expenses())
print(cuenta_luis.account_balance())
print(cuenta_luis.account_info())
