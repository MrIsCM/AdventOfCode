with open('Day11/in.txt', 'r') as f:
	data = f.read().splitlines()

with open('Day11/test.txt', 'r') as f:
	test = f.read().splitlines()


def parse(data):
	"""
		Converts the data into a list of monkeys with their attributes
	"""
	monkeys = []
	for line in data:
		if line.strip()[:6] == 'Monkey':
			identif = int(line.strip()[-2])

		elif line.strip()[:8] == 'Starting':
			items = [int(x) for x in line.strip()[15:].split(',')]

		elif line.strip()[:9] == 'Operation':
			if line.strip()[-9:] == 'old * old':
				operation = tuple('**', 2)
			else:
				operation = tuple(line.strip()[21:].split(' '))
		elif line.strip()[:4] == 'Test':
			test = []
			test.append(int(line.strip()[19:]))
		elif line.strip()[:7] == 'If true':
			test.append(int(line.strip()[-1]))
		elif line.strip()[:8] == 'If false':
			test.append(int(line.strip()[-1]))
			monkeys.append(monkey(identif, items, operation, tuple(test)))
		elif line.strip() == '':
			pass

		else:
			print('Error')
			print(line)
			
	return monkeys
	


class monkey():

	"""
		Starting items: values of the items that the monkey has
		Operation: how the value of the items changes. Tuple: first value is the operation (+, -, *, /), second value is the amount (int).
		Test: 3-element tuple. First: int, the value of the item is divided by this number. If the remainder is 0, the item is thrown to monkey[second value], else, the item is thrown to monkey[third value].

	"""

	def __init__(self, id, items, operation, test):
		monkey.id = id
		monkey.operation = operation
		monkey.test = test
		monkey.items = [*items]
		monkey.inspected = 0

	def inspect(self):
		if monkey.items != None:
			for item in monkey.items:
				monkey.inspected += 1
				if monkey.operation[0] == '+':
					item += monkey.operation[1]
				elif monkey.operation[0] == '-':
					item -= monkey.operation[1]
				elif monkey.operation[0] == '*':
					item *= monkey.operation[1]
				elif monkey.operation[0] == '/':
					item /= monkey.operation[1]
			return True
		else:
			return False

	def throw(self, test, monkeys):
		if monkey.items != None:
			for item in monkey.items:
				if item % test[0] == 0:
					monkeys[test[1]].items.append(item)
					monkey.items.remove(item)
					
				else:
					monkeys[test[2]].append(item)
					monkey.items.remove(item)


monkeys = parse(data)
print(monkeys[0].items)