initial_amount = input("what is ")
initial_amount = Integer.initial_amount
yearly_add = 2400
interest_rate = 1.1
years = 20
years = years - 1

count = 0
set_amount = initial_amount*interest_rate

while count < years:
   set_amount = (set_amount + yearly_add)*interest_rate
   count = count + 1

print(set_amount)



