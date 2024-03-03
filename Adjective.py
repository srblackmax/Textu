class Adjective:
	def __init__(self, root, quantity, kind = None):
		self.root = root
		self.quantity = quantity
		self.text = self.root + "a"
		if self.quantity == "plural":
			self.text += "j"
		self.kind = kind
