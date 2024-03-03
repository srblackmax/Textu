from random import choice

from Words import nouns, adjectives, verbs, adverbs, pronouns

class System:
	def __init__(self):
		pass
	def change_word(self, word, type):
		if type == "noun":
			word.text = word.root + "o"
		elif type == "adjective":
			word.text = word.root + "a"
		elif type == "verb":
			word.text = word.root + "i"
		elif type == "adverb":
			word.text = word.root + "e"
	def define_subject(self):
		subject = ""
		subject_type = choice(["pronoun", "noun", "adjective + noun", "adverb + adjective + noun"])
		if subject_type == "pronoun":
			subject = choice(pronouns).text
		elif subject_type == "noun":
			subject = choice(nouns).text
		elif subject_type == "adjective + noun":
			subject = choice(adjectives).text + " " + choice(nouns).text
		elif subject_type == "adverb + adjective + noun":
			subject = choice(adverbs).text + " " + choice(adjectives).text + " " + choice(nouns).text
			
		return subject
	def define_predicate(self):
		predicate = ""
		verb = ""
		transitive_verbs = []
		intransitive_verbs = []
		for verb in verbs:
			if verb.is_transitive == True:
				transitive_verbs.append(verb)
			if verb.is_intransitive == True:
				intransitive_verbs.append(verb)
		verb_type = choice(["transitive", "intransitive"])
		if verb_type == "transitive":
			verb = choice(transitive_verbs)
			
		elif verb_type == "intransitive":
			verb = choice(intransitive_verbs)
		
