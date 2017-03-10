import csv

def load_interactions(file_name) :
	with open(file_name, 'rb') as f :
		reader = csv.reader(f)
		list = map(tuple, reader)
	return list

def interact(interactions, id1, id2) :
	if(id1, id2) in interactions :
		return true
	else if(id2, id1) in interactions :
		return true
	else
		return false

def get_interactions(interactions, id) :


if __name__ == '__main__' :
	interactions = load_interactions('yeast_interactions.data')
	protein1 = 'YPL094C'
	protein2 = 'YPR086W'

	print("do " + protein1 + " protein " + protein2 + "interact? " +
		interact(interactions, protein1, protein2))

	print ("the number of interactions of " + protein1 " : " +
		str(len(get_interactions(interactions, protein1)))

	print("the average number of interactions per protein: " +
		str(average_interactions(interactions)))
