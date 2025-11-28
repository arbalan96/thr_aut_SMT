from sys import *
from re import *

def formula_master(text):


	#Negating a statement
	def negator(st):
		if '->' in st:
			n_text = 'And('
			l = st.split('->')
			nlast = negator(l[-1])
			for t in l[:-1]:
				n_text = n_text + t + ', '
			n_text = n_text + nlast[:-1] + ')'
			n_text = sub(' ,',',',n_text)
			n_text = sub('  ',' ',n_text)
			return n_text
			
	
		else:	
			n_text = ''
			i = 0
			while i in range(len(st)):
				letter = st[i]
				if letter == '!':
					n_text = n_text + '='
				elif letter == '=' and st[i+1] == '=':
					n_text = n_text + '!'
				elif letter == '<' and st[i+1] == '=':
					n_text = n_text + '>'
					i+=1
				elif letter == '>' and st[i+1] == '=':
					n_text = n_text + '<'
					i+=1
				elif letter == '>' and st[i+1] == ' ':
					n_text = n_text + '<='
				elif letter == '<' and st[i+1] == ' ':
					n_text = n_text + '>='
				elif letter == 'O' and st[i+1] == 'r':
					n_text = n_text + 'And'
					i+=1	
				elif letter == 'A' and st[i+1] == 'n':
					n_text = n_text + 'Or'
					i+=2
				elif letter == 'F' and st[i+1] == '(':
					n_text = n_text + 'G'
				elif letter == 'G' and st[i+1] == '(':
					n_text = n_text + 'F'
				else:
					n_text = n_text + letter
				i+=1

			n_text = sub(' ,',',',n_text)
			return n_text


	prefix = negator(text) #Get the negated statement


	##############Checkpoint 1################
	#print(prefix + '\n')	


	#Marking special Ands

	def all_the_words(st):
		words_arr = [] #Self-explanatory name :P
		count = 0
		word = ''

		index = 0
		while(index < len(st) - 1): #End before the last bracket
			letter = st[index]
		
			if count == -1 or letter == ';':
				word = word[:-1]
				break

			word = word + letter
			index+=1
			if letter == ')':
				count-=1
			elif letter == '(':
				count+=1

			if (st[index] == ',' and count == 0):
				words_arr.append(word)
				count = 0
				word = ''
				index+=2 #Have to get over the comma and the space
		
		if word != '':
			words_arr.append(word)
	
		return(words_arr)


	sp_prefix = ''
	for i in range(len(prefix)):
		letter = prefix[i]
		if letter == 'A' and prefix[i+1] == 'n': #We are seeing an And. Need to decide if this is a special And
			temp_arr = all_the_words(prefix[i+4:])
			fl = 0
			for word in temp_arr:
				if 'F(' in word or 'G(' in word:
					fl = 1
					break
			if fl == 1:
				sp_prefix = sp_prefix + 'SA'
		
			else:
				sp_prefix = sp_prefix + 'A'
	
		else:
			sp_prefix = sp_prefix + letter



	#########Checkpoint 2############
	#print(sp_prefix + '\n')





	#Eliminating unnecessary and's, sand's and or's

	stack = []
	i = 0
	easy_prefix = ''
	while(i < (len(sp_prefix))):
		letter = sp_prefix[i]


		if letter == ')':
			if stack == []:
				i+=1
			else:
				x,count = stack.pop()
				count-=1
				if count != 0:
					stack.append((x,count))
				else:
					easy_prefix = easy_prefix + ')'
				i+=1
		
		elif letter == 'A' and sp_prefix[i+1] == 'n':
			if stack == []:
				stack.append(('And',1))
				easy_prefix = easy_prefix + 'And('
				i+=4

			elif stack != []: 
				x,count = stack.pop()

				if x == 'And': #No alternation. Have to elimiate this And
					count+=1
					stack.append((x,count))
					i+=4
		
				else: #Alternation exists. Cannot eliminate this And
					stack.append((x,count))
					stack.append(('And',1))
					easy_prefix = easy_prefix + 'And('
					i+=4
	
		elif letter == 'O' and sp_prefix[i+1] == 'r':
			if stack == []:
				stack.append(('Or',1 ))
				easy_prefix = easy_prefix + 'Or('
				i+=3

			elif stack != []:
				x,count = stack.pop()

				if x == 'Or':
					count+=1
					stack.append((x,count))
					i+=3
				else:
					stack.append((x,count))
					stack.append(('Or',1))
					easy_prefix = easy_prefix + 'Or('
					i+=3
	
		elif letter == 'S' and sp_prefix[i+1] == 'A':
			if stack == []:
				stack.append(('SAnd',1))
				easy_prefix = easy_prefix + 'SAnd('
				i+=5

			elif stack != []:
				x,count = stack.pop()
				if x == 'SAnd':
					count+=1
					stack.append((x,count))
					i+=5
				else:
					stack.append((x,count))
					stack.append(('SAnd',1))
					easy_prefix = easy_prefix + 'SAnd('
					i+=5
	
		elif (letter == 'F' or letter == 'G') and (sp_prefix[i+1] == '('):
			stack.append((letter+'(',1))
			easy_prefix = easy_prefix + letter + '('
			i+=2
	
		else:
			easy_prefix = easy_prefix + letter
			i+=1



	#################Checkpoint 3##############
	#print(easy_prefix + '\n')


	
	#Constructing syntax tree

	text = easy_prefix

	#print(text + '\n\n')

	syntax_tree = []

	def modi_all_the_words(st):
		words_arr = [] #Self-explanatory name :P
		count = 0
		word = ''

		
		index = 0
		while(index < len(st)):

			letter = st[index]
			word = word + letter
			if letter == ')':
				count-=1
			elif letter == '(':
				count+=1

			if (st[index] == ',' and count == 0):
				words_arr.append(word[:-1]) #Have to remove the comma
				count = 0
				word = ''
				index+=2 #Have to get over the comma and the space
			else:
				index+=1
				
		words_arr.append(word)
	
		return(words_arr)



	def parser(st,direction):

		if st[0] != 'S' and st[0] != 'F' and st[0] != 'G': #A proposition
			syntax_tree.append(('P',st,'True',direction))
			return ('P',st,'True')

		if st[0] == 'S': #First word is SAnd. Hence we have to create new nodes.
			temp_arr = modi_all_the_words(st[5:-1])
			Gprop = 'True'
			Pprop = 'True'

			#for word in temp_arr:
			#	print(word)
			#	print('\n')
				
			 #Combining multiple G's into one G
			Gwords = [word for word in temp_arr if word[0] == 'G'] #Collecting all such words
			if (len(Gwords) > 1): #We need to combine multiple G's
				temp_arr = [word for word in temp_arr if word[0] != 'G'] #Removing all such words
				#Now we need to decide whether to use And or SAnd
				fl = 0
				for word in Gwords:
					even_more_temp_arr = modi_all_the_words(word[2:-1])
					for even_more_word in even_more_temp_arr:
						if 'F(' in even_more_word or 'G(' in even_more_word: #######Important: Check this statement if something wrong happens later on
							fl = 1
							break

				#Assume there are no G's inside G's
				if(fl == 0): #Only need to use And
					mega_Gword = 'G(And('
					for word in Gwords:	
						modi_word = word[2:-1]
						mega_Gword = mega_Gword + modi_word + ', '
					mega_Gword = mega_Gword[:-2] + '))'
					temp_arr.append(mega_Gword)

				else:
					mega_Gword = 'G(SAnd('
					for word in Gwords: #First add all F's
						modi_word = word[2:-1]
						if modi_word[0] == 'F':
							mega_Gword = mega_Gword + modi_word + ', '
					
					mega_Gword = mega_Gword + 'And('
					for word in Gwords: #Next add all propositions
						modi_word = word[2:-1]
						if modi_word[0] != 'F':
							mega_Gword = mega_Gword + modi_word + ', '

					if mega_Gword[-1] != '(':
						mega_Gword = mega_Gword[:-2] + ')))'
					else:
						mega_Gword = mega_Gword[:-6] + '))'
					temp_arr.append(mega_Gword)

			child_no = 0		
			for word in temp_arr:
				if word[0] == 'F':
					parser(word,direction + '.' + str(child_no))
				elif word[0] == 'G':
					(_,_,Gprop) = parser(word,direction + '.' + str(child_no))
				else:
					(_,Pprop,_) = parser(word,direction + '.' + str(child_no))
				child_no+=1

			return ('S',Pprop,Gprop)
	
		if st[0] == 'F': #First word is F. Hence we have to create a new node.

			temp_arr = modi_all_the_words(st[2:-1])
			Gprop = 'True'
			Pprop = 'True'
			
			child_no = 0		
			for word in temp_arr:
				if word[0] == 'F':
					parser(word,direction + '.' + str(child_no))
				elif word[0] == 'G':
					(_,_,Gprop) = parser(word,direction + '.' + str(child_no))
				elif word[0] == 'S':
					(_,Pprop,Gprop) = parser(word,direction)
				else:
					(_,Pprop,_) = parser(word,direction + '.' + str(child_no))
				child_no+=1

			syntax_tree.append(('F',Pprop,Gprop,direction))

		if st[0] == 'G':

			temp_arr = modi_all_the_words(st[2:-1])
			Gprop = 'True'
			Pprop = 'True'

			child_no = 0		
			for word in temp_arr:
				if word[0] == 'F':
					parser(word,direction + '.' + str(child_no))
				elif word[0] == 'G':
					(_,_,Gprop) = parser(word,direction + '.' + str(child_no))
				elif word[0] == 'S':
					(_,Pprop,Gprop) = parser(word,direction)
				else:
					(_,Pprop,_) = parser(word,direction + '.' + str(child_no))
				child_no+=1

			syntax_tree.append(('G',Pprop,Gprop,direction))
			return ('G','True',Pprop)
	

	if text[-1] == '\n':
		text = text[:-1]

	if text[-1] == ';':
		text = text[:-1]

	if text[0] != 'S':
		text = 'SAnd(' + text + ', ' + 'True' + ')'
		

	#################Checkpoint 4###################
	#print(text)


	(_,Pprop,Gprop) = parser(text,'0')
	syntax_tree.append(('R',Pprop,Gprop,'0'))


	syntax_tree = sorted(syntax_tree, key = lambda tup: tup[3])


	##################Checkpoint 5##########################
	#for node in syntax_tree:
	#	print(node)
	#	print('\n')


	#Extract vertices 
	vertices = [('loop_st',-1,[]),('loop_end',-1,[])]
	set_of_ids = []

	for line in syntax_tree:
		label = line[0]
		identity = line[3]

		if label == 'G': #A G node. Store its id and check if any future node is covered by this id
			set_of_ids.append(identity)
	
		elif label == 'F':
			fl = 0
			for ide in set_of_ids:
				if ide == identity[:len(ide)]: #Covered by a G node
					fl = 1
					break
		
			vertices.append(('F',fl,line))
	

	#for vertex in vertices:
	#	print(vertex)
	#	print('\n')



	#Extract edges
	edges = [(('loop_st',-1,[]),('loop_end',-1,[]))]
	indegree = [0 for vertex in vertices]
	indegree[1] = 1

	for i in range(len(vertices)):
		for j in range(len(vertices)):
			if i == j:
				continue
			outgoing = vertices[i]
			incoming = vertices[j]

			if outgoing[0] == 'F' and outgoing[1] == 0:
				if incoming[0] == 'loop_st':
					edges.append((outgoing,incoming))
					indegree[j]+=1

				if incoming[0] == 'F' and incoming[1] == 0: #Check ancestor relation
					outid = outgoing[2][3]
					inid = incoming[2][3]
					if outid == inid[:len(outid)]:
						edges.append((outgoing,incoming))
						indegree[j]+=1

			if outgoing[0] == 'F' and outgoing[1] == 1:
				if incoming[0] == 'loop_end':
					edges.append((outgoing,incoming))
					indegree[j]+=1
			
				if incoming[0] == 'F' and incoming[1] == 1: #Check if edge is already present
					if (incoming,outgoing) not in edges:
						edges.append((outgoing,incoming))
						indegree[j]+=1


			if outgoing[0] == 'loop_st':
				if incoming[0] == 'F' and incoming[1] == 1:
					edges.append((outgoing,incoming))
					indegree[j]+=1

	#for edge in edges:
	#	print(edge)
	#	print('\n')



	all_orders = []

	def all_topo_sort(topo_ord,marked):	
		fl = False
		for i in range(len(vertices)):
			vertex = vertices[i]
			if indegree[i] == 0 and marked[i] == False:
			
				topo_ord.append(vertex)
				marked[i] = True
				for j in range(len(vertices)):
					node = vertices[j]
					if (vertex,node) in edges:
						indegree[j]-=1

				all_topo_sort(topo_ord,marked)

				topo_ord.pop()
				marked[i] = False
				for j in range(len(vertices)):
					node = vertices[j]
					if (vertex,node) in edges:
						indegree[j]+=1

				fl = True
	
		if fl == False:
			all_orders.append(topo_ord[:])


	visited = [0 for vertex in vertices]
	all_topo_sort([],visited)

	#for topo_ord in all_orders:
	#	for node in topo_ord:	
	#		print(node)
	#		print('\n')
	#	print('\n\n')

	return(syntax_tree,all_orders)

#f = open('bosco_spec_fast1','r')
#line = f.readline()
#syntax_tree, all_orders = formula_master(line)
