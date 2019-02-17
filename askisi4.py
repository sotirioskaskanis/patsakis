sum=""

def plus():
	return "+"
	
def minus():
	return"-"
	
def times():
	return"*"
	
def zero():
	return "0"
	
def one():
	return "1"
	
def two():
	return "2"
	
def three():
	return "3"
	
def four():
	return "4"
	
def five():
	return "5"
	
def six ():
	return "6"
	
def seven():
	return "7"

def eight():
	return "8"
	
def nine():
	return "9"
	
CallFunc= {"plus":plus, "minus":minus, "times":times, "zero":zero, "one":one, "two":two, "three":three, "four":four, "five":five, "six":six, "seven":seven, "eight":eight, "nine":nine}

ent = input( " Give the Operations: " )

operations= ent.split("(")

for i in range(len(operations) -1 ):
	sum += CallFunc[operations[i]]()

sum2= eval(sum)
print(sum2)
