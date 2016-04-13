# Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules
# Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis


import nltk
import pprint
from pymedtermino.snomedct import *


with open("2.1.3.txt", "a") as myfile:
    

	essays = [
	u"Mixed appearance of lung nodules. solid which may reflect treatment response. Continued follow-up advised",
	u"Stable osseous metastases"
	]

	george = [
	'- lung nodules [lungs]',
	'- osseous metastases [bones]'
	]


	for i in range(len(essays)):
		pair_nouns_adj = []
		trio_nouns_adj = []
		print str(i+1)+'.'
		print 'Sentence in report ====> ' + essays[i]
		print ''
		c = str(i+1)+'. ' + 'Sentence in report ====> ' + essays[i] + '\n\n' 
		myfile.write(c)

		tokens = nltk.word_tokenize(essays[i])
		tagged = nltk.pos_tag(tokens)
		all_pos = zip(*tagged)[1]
		adjs = ['JJ','JJR','JJS']
		nouns = ['NN', 'NNS', 'NNP', 'NNPS']
		
		relevant_tags = [(word,pos) for word,pos in tagged if pos in adjs or pos in nouns]
		#print ''
		for j in range(len(relevant_tags)):
			print relevant_tags[j]
		
		pprint.pprint(relevant_tags, myfile)
		
		downcased = [x[0].lower() for x in relevant_tags]
		for j in range(len(downcased)):
			downcased[j] = downcased[j].encode("ascii")
		print ''
		myfile.write('\n')

		print 'Predicted from just single word nouns and adjectives' +'\n'
		for char in downcased:
			s = SNOMEDCT.search(char)
			if len(s) !=0 and '(disorder)' in s[0].term:
				print char+ ' =====> ' + s[0].term
				myfile.write(char+ ' =====> ' + s[0].term+'\n')
		print ''
		myfile.write('\n')
		#joined = " ".join(downcased).encode('utf-8')
		#into_string = str(nouns)

		#output = open("output.txt", "w")
		#output.write(joined)
		#output.close()
		#Pairs
		for k in range(len(all_pos)-1):
			if all_pos[k] in adjs and all_pos[k+1] in nouns:
				print 'Pairs =====>' + tagged[k][0] + ' ' + tagged[k+1][0]
				myfile.write('Pairs =====>' + tagged[k][0] + ' ' + tagged[k+1][0]+'\n')
				pair_nouns_adj.append(tagged[k][0].encode("ascii") + ' ' + tagged[k+1][0].encode("ascii"))
		
		print ''
		myfile.write('\n\n')
		print 'Predicted from pairs of nouns and adjectives'
		myfile.write('Predicted from pairs of nouns and adjectives' + '\n')
		for char in pair_nouns_adj:
			s = SNOMEDCT.search(char)
			#if len(s) !=0 and '(disorder)' in s[0].term:
			#	print char+ ' =====> ' + s[0].term
			if len(s) !=0:
				d = {}
				for x in s:
					x = x.term
					w = x[x.find('(')+1:x.find(')')]
					if w not in d:
						d[w] = 1
					else:
						d[w]+=1
				print 'Pair analysis of ' + char
				myfile.write('Pair analysis of ' + char+'\n')
				pprint.pprint(d)
				pprint.pprint(d, myfile)

				print '\n'
				myfile.write('\n\n')
			else:
				t1,t2 = char.split(' ')
				s = SNOMEDCT.search(t2)
				if len(s) !=0:
					d = {}
					for x in s:
						x = x.term
						w = x[x.find('(')+1:x.find(')')]
						if w not in d:
							d[w] = 1
						else:
							d[w]+=1
					print 'Single word analysis of ' + t2			
					myfile.write('Single word analysis of ' + t2+'\n')
					pprint.pprint(d)
					pprint.pprint(d, myfile)
					
					print '\n'
					myfile.write('\n\n')


		#Trios
		print ''
		myfile.write('\n\n')
		for k in range(len(all_pos)-2):
			if (all_pos[k] in adjs and all_pos[k+1] in nouns and all_pos[k+2] in nouns) or \
			(all_pos[k] in adjs and all_pos[k+1] in adjs and all_pos[k+2] in nouns):
				print 'Trios =====>' + tagged[k][0] + ' ' + tagged[k+1][0] + ' ' + tagged[k+2][0]
				myfile.write('Trios =====>' + tagged[k][0] + ' ' + tagged[k+1][0] + ' ' + tagged[k+2][0] + '\n')
				trio_nouns_adj.append(tagged[k][0].encode("ascii") + ' ' + tagged[k+1][0].encode("ascii") + ' ' + tagged[k+2][0].encode("ascii"))
		#print 'Pairs'
		#print pair_nouns_adj
		#print 'Trios'
		#print trio_nouns_adj

					#if '(disorder)' in x.term or '(finding)' in x.term:
					#	print char+ ' =====> ' + x.term
		print ''
		myfile.write('\n\n')
		print 'Predicted from trios of nouns and adjectives'
		myfile.write('Predicted from trios of nouns and adjectives' + '\n')
		for char in trio_nouns_adj:
			s = SNOMEDCT.search(char)
			if len(s) !=0 and '(disorder)' in s[0].term:
				print char+ ' =====> ' + s[0].term
				myfile.write(char+ ' =====> ' + s[0].term + '\n')
			#for x in s:
			#	if '(disorder)' in x.term or '(finding)' in x.term:
			#		print char+ ' =====> ' + x.term
		print ''
		myfile.write('\n\n')
		
		print 'George said'
		myfile.write('George said')
		
		print george[i]
		myfile.write(george[i])
		
		print ''
		myfile.write('\n\n')


#print 'Actual'
#print ''
#for char in actuals:
#	print char

