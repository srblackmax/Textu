class Verb:
	def __init__(self, root, is_transitive, is_intrasitive, kind = None):
		self.root = root
		self.text = self.root
		self.is_transitive = is_transitive
		self.is_intransitive = is_intrasitive
		self.kind = kind
	def change_tense(self, tense):
		if self.text == self.root:
			self.text += "i"
		elif tense == "infinitive":
			self.text = self.root + "i"
		elif tense == "past":
			self.text = self.root + "is"
		elif tense == "present":
			self.text = self.root + "as"
		elif tense == "future":
			self.text = self.root + "os"
		elif tense == "conditional":
			self.text = self.root + "us"
		elif tense == "imaginary":
			self.text = self.root + "us"
		elif tense == "imperative":
			self.text = self.root + "u"
		else:
			print("Unknown Tense")
			exit()
