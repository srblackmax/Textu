class Noun:
	def __init__(self, root, quantity, kind = None):
		self.root = root
		self.text = self.root + "o"
		if quantity == "plural":
			self.text += "j"
		self.quantity = quantity
		self.kind = kind
	def change_to_plural(self):
		self.text = self.root + "oj"
	def change_to_singular(self):
		self.text = self.root + "o"
