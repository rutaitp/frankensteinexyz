'''
Spacy pos tagging documentation: https://spacy.io/docs/usage/pos-tagging
'''

import spacy
import random

#load English spacy model
nlp = spacy.load('en')

def trump(text):

	#load original speech
	trump_text = open('speech.txt', 'r').read()
	#load frankenstein
	# replacement_text = open('twelve_monkeys.txt').read()
	replacement_text = open(text + '.txt').read()

	trump_text_nlp = nlp(unicode(trump_text))
	replacement_nlp = nlp(unicode(replacement_text))

	#create lists for replacement text pos
	#verbs
	replacement_vb = []
	replacement_vbd = []
	replacement_vbg = []
	replacement_vbn = []
	#nouns
	replacement_nn = []
	replacement_nns = []
	#adjectives
	replacement_adj = []
	replacement_det = []
	replacement_intj = []

	#get pos for each trump original speech token
	'''VERB is a verb, NOUN is a noun, adj is an adjective,
	det is a determiner, intj is an interjection'''
	for replacement_word in replacement_nlp:
		if replacement_word.tag_ == "VB":
			replacement_vb.append(replacement_word.text)
		elif replacement_word.tag_ == "VBD":
			replacement_vbd.append(replacement_word.text)
		elif replacement_word.tag_ == "VBG":
			replacement_vbg.append(replacement_word.text)
		elif replacement_word.tag_ == "VBN":
			replacement_vbn.append(replacement_word.text)
		elif replacement_word.tag_ == "NN":
		 	replacement_nn.append(replacement_word.text)
		elif replacement_word.tag_ == "NNS":
		 	replacement_nns.append(replacement_word.text)
		elif replacement_word.pos_ == "ADJ":
		 	replacement_adj.append(replacement_word.text)
		elif replacement_word.pos_ == "DET":
		 	replacement_det.append(replacement_word.text)
		elif replacement_word.pos_ == "INTJ":
			replacement_intj.append(replacement_word.text)
		pass

	#generate new speech
	#define a new speech as an empty string for now
	trump_new_speech = ""

	for word in trump_text_nlp:
		if word.tag_ == "VB":
			trump_new_speech += (random.choice(replacement_vb) + " ")
		elif word.tag_ == "VBD":
			trump_new_speech += (random.choice(replacement_vbd) + " ")
		elif word.tag_ == "VBG":
			trump_new_speech += (random.choice(replacement_vbg) + " ")
		elif word.tag_ == "VBN":
			trump_new_speech += (random.choice(replacement_vbn) + " ")
		elif word.tag_ == "NN":
			trump_new_speech += (random.choice(replacement_nn) + " ")
		elif word.tag_ == "NNS":
			trump_new_speech += (random.choice(replacement_nns) + " ")
		elif word.pos_ == "ADJ":
			trump_new_speech += (random.choice(replacement_adj) + " ")
		elif word.pos_ == "DET":
			trump_new_speech += (random.choice(replacement_det) + " ")
		elif word.pos_ == "INTJ":
			trump_new_speech += (random.choice(replacement_intj) + " ")
		else:
			trump_new_speech += (word.text + " ")

	#remove all the white spaces
	trump_new_speech = trump_new_speech.replace(" , ", ", ")
	trump_new_speech = trump_new_speech.replace(" . ", ". ")
	trump_new_speech = trump_new_speech.replace(" ; ", "; ")
	trump_new_speech = trump_new_speech.replace(" : ", ": ")
	return trump_new_speech
	#print trump_new_speech

	# #save new speech
	# replacement_text_saved = open("new_armageddon.txt", "w")
	# replacement_text_saved.write(trump_text_new_speech)
	# replacement_text_saved.close()