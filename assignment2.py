#Brooke Robinson
#Assignment 2
import sys



class Node:
  
	def __init__(self, locationx, locationy, typeN):
		self.x = locationx 
		self.y = locationy
		self.p = None
		self.f = 0
		self.cost = 0
		self.typeN = typeN #0 is free, 1 is mountain, 2 is wall
	
	def setParent(self, parent, h):
		self.p = parent
		self.cost = parent.cost + 10 + int(self.x != parent.x and self.y !=parent.y)*4 + self.typeN*10
		self.f = self.cost + h(self.x, self.y)

def getMap(arg):
	mymap = []
	with open(arg, 'r') as f:
	  for line in f:
		line = line.strip()
		if len(line) > 0:
			mymap.append(map(int, line.split()))
	n = 0
	for x in reversed(range(0,len(mymap))):
		for y in range(0,len(mymap[x])):
			mymap[x][y] = Node(x,y,int(mymap[x][y]))
	#		print mymap[x][y].x,mymap[x][y].y, mymap[x][y].typeN
		n = n+1
	return mymap

def newCost(n, node):
	return 10 + int(n.x != node.x and n.y != node.y)*4 + n.typeN*10

class astar:
	
	def __init__(self, mymap, heuristic):
		self.Open = []
		self.Close = []
		self.mymap = mymap
		self.goalx = len(mymap[1])-1#measures the x length
		self.goaly = len(mymap)-1
		if heuristic == 1:
			self.h = self.man
		else:
			self.h = self.pyth
		
	def getAdj(self, n):
		adj_matrix = []
		for x in range(n.x-1, n.x+2): #we add +2 because the range does not include the final value
			for y in range(n.y-1, n.y+2):
				if(x>= 0 and  y>=0 and x<len(self.mymap) and y<len(self.mymap[x]) and not (x== n.x and y==n.y)):
					#we have to make sure it is within bounds
					#we also have to make sure we do not add the same node
					if(self.mymap[x][y].typeN != 2):
						adj = mymap[x][y]
						adj_matrix.append(adj)
		return adj_matrix
		
	def man(self,x,y):
		man_val = abs(x-self.goalx) + abs(y-self.goaly)
		return man_val
	
	def pyth(self, x, y):
		#use the a^2 + b^2 = c^2 theory!
		return ((math.sqrt(x-self.goalx)**2) + (math.sqrt(y-self.goaly)**2))
		
	
	#A* search!	
	def starsearch(self):
		node = self.mymap[0][0]
		self.Open.append(node)
		while self.Open != []:
			#find node.f that is the smallest
			min_val = 10000000
			for val in self.Open:
			#	print "In Open: ", val.x, val.y, val.f
				if val.f <= min_val and val.typeN != 2:
					node = val
					min_val = val.f
			#		print "min_val", min_val
			#print "remove: ", node.f
			self.Open.remove(node)
			if node.x != self.goalx and node.y != self.goaly:
			#	print "*********************"
			#	print "currently at: ", node.x, node.y
			#	print "*********************"
				self.Close.append(node)
				nodes_adj = self.getAdj(node)
				for n in nodes_adj:
					if n.typeN != 2 and not(n in self.Close):
						n.setParent(node, self.h)
						if (n in self.Open):
							if (n.f > (node.f + newCost(n, node))):
								n.f = node.f + newCost(n, node)
						else:
							if n.typeN != 2:
								self.Open.append(n)
			#					print "adding to open: ", n.x, n.y
			else:
				#print
			#	print "Locations Evaluated: "
				break
				
	def time_to_print(self, node):
		print "This is my path: "
		


mymap = getMap(sys.argv[1])
searched = astar(mymap, int(sys.argv[2]))
searched.starsearch()
#print "searched"
	
