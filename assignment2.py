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
	#n = 0
	for x in (range(0,len(mymap))):
		for y in range(0,len(mymap[x])):
			mymap[x][y] = Node(x,y,int(mymap[x][y]))
			#print mymap[x][y].x,mymap[x][y].y, mymap[x][y].typeN
		#n = n+1
	return mymap

def newCost(n, node):
	return 10 + int(n.x != node.x and n.y != node.y)*4 + n.typeN*10

class astar:
	
	def __init__(self, mymap, heuristic):
		#self.Open = []
		self.Open = {}
		self.Close = {}
		self.mymap = mymap
		self.length = len(mymap)
		self.goal = mymap[0][9]
		self.start = mymap[7][0]
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
		man_val = abs(x-self.goal.x) + abs(y-self.goal.y)
		return man_val
	
	def pyth(self, x, y):
		#use the a^2 + b^2 = c^2 theory!
		return ((math.sqrt(x-self.goal.x)**2) + (math.sqrt(y-self.goal.y)**2))
		
	#A* search!	
	def starsearch(self):
		locations = 0
		node = self.start
		self.Open[node] = node.f 
		while self.Open != {}:
			locations = locations + 1
			#find node.f that is the smallest
			min_val_find = min(self.Open, key=self.Open.get)
			min_val = self.Open[min_val_find]
			for value in self.Open:
			#	print "In Open: ", val.x, val.y, val.f
				if self.Open[value] == min_val:
					node = value
					break
			#		print "min_val", min_val
			#print "remove: ", node.f
			#self.Open.remove(node)
			del self.Open[node]
			if node.x == self.goal.x and node.y == self.goal.y:
				#print "goal: ", self.goal.x, " ",self.goal.y
				#print "current: ", node.x, node.y
				#print "p of current: ", node.p.x, node.p.y
				#time_to_print
				#print "Locations evaluated: ", locations
				self.time_to_print(node)
				break
				
			#print "*********************"
			#print "Adding to close: (", node.x, ", ",node.y,")"
			#print "*********************"
			
			self.Close[node] = node.f
			node_adj = self.getAdj(node)
			for n in node_adj:
				if (n.typeN != 2 and not(n in self.Close)):
					#n.setParent(node,self.h)#calculates the f value
					if not(n in self.Open) or (n.f > (node.f + newCost(n,node))):
						n.f = node.f + newCost(n,node)
						n.setParent(node,self.h)
						if not(n in self.Open):
							#n.setParent(node,self.h)
							self.Open[n] = n.f
							#print "adding to open: ", n.x, n.y
	
	def time_to_print(self, nextNode):
		print "This is my path: "
		cost = 0
		stringArr = []
		while not(nextNode.x == self.start.x and nextNode.y == self.start.y):
			#print "(", nextNode.x, ",", nextNode.y, ")"
			stringArr.append(["(", nextNode.x, ",", nextNode.y, ")"])
			cost += newCost(nextNode, nextNode.p)
			nextNode = nextNode.p
		stringArr.append(["(", nextNode.x, ",", nextNode.y, ")"])
		for lis in reversed(stringArr):
			print lis[0],lis[1],lis[2],lis[3],lis[4]
		print "Total Cost: ", cost
		
		


mymap = getMap(sys.argv[1])
searched = astar(mymap, int(sys.argv[2]))
searched.starsearch()
#print "searched"
'''

import sys
import math


def calcCost(n1,n2):
	return 10 + int(n1.x != n2.x and n1.y != n2.y)*4 + n2.typeN*10	

def getMap():
	with open(sys.argv[1], 'r') as f:
		mapMatrix = []
		for line in f:
			line = line.strip()
			if len(line) > 0:
				mapMatrix.append(map(int, line.split()))
		#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mapMatrix]))
		for x in (range(0,len(mapMatrix))):
			for y in (range(0,len(mapMatrix[x]))):
				mapMatrix[x][y] = Node(x,y,int(mapMatrix[x][y]))
				#print x,y, " ",mapMatrix[x][y].typeN
		return mapMatrix
	
class Node:
	def __init__(self, x, y, typeN):
		self.x = x
		self.y = y
		self.typeN = typeN #0 = good, 1 == mtn, 2 = wall
		self.cost = 0
		self.p = None
		self.f = 0
		
	def setparent(self, parent, h):
		self.p = parent
		self.cost = parent.cost + 10 + int(self.x != parent.x and self.y != parent.y)*4 + self.typeN*10	
		self.f = self.cost + h(self.x,self.y)
		
class WorldAstar:
	#the map starts at the bottom left
	#where the horse starts is (0,0)
	def __init__(self,world,htype):
		self.Openl = {}
		self.Closedl = {}
		self.goal = world[0][9]
		self.world = world
		self.start = world[7][0]
		if htype == 1:
			self.htype = self.calcManhattan
		else:
			self.htype = self.calcother
		
	def calcManhattan(self,x,y):
		return abs(x - self.goal.x) + abs(y - self.goal.y)
		
	def calcother(self,x,y):
		return math.sqrt((x-self.goal.x)**2 + (y-self.goal.y)**2)
		return math.sqrt((x-self.goal.x)**2 + (y-self.goal.y)**2)
	
	def getAdj(self, baseN):
		adjl = []
		for x in range(baseN.x - 1, baseN.x + 2):
			for y in range(baseN.y - 1, baseN.y + 2):
				if(x >= 0 and x < len(self.world) and y >= 0 and y < len(self.world[x]) and not(x == baseN.x and y == baseN.y)):
					if (self.world[x][y].typeN != 2):
						adjN = self.world[x][y]
						adjl.append(adjN)
		return adjl
	
	def getPath(Self,node):
		print "Path taken:"
		while (Self.start.x != node.x and Self.start.y != node.y):
			print "(",node.x,", ",node.y,")"
			node = node.p
			
	def Astar(self):
		#open and closed lists defined in the class initializer
		locationseval = 0
		self.Openl[self.start] = self.start.f
		while self.Openl != {}:
			#finds node with smallest cost
			min_val_loc = min(self.Openl, key=self.Openl.get)
			min_val = self.Openl[min_val_loc]
			locationseval = locationseval +1
			for val in self.Openl:
				if (self.Openl[val] == min_val):
					node = val
					break
			del self.Openl[node]
			if (node.x == self.goal.x and node.y == self.goal.y):
				print "goal: ",self.goal.x, self.goal.y
				print "current: ", node.x, node.y
				print "parent of cur: ", node.p.p.p.x, node.p.p.p.y
				self.getPath(node)
				break
			print "adding to close: (",node.x,", ",node.y,")"
			self.Closedl[node] = node.f
			node_adj = self.getAdj(node)
			for n in node_adj:
				if (n.typeN != 2 and not(n in self.Closedl)):
					n.setparent(node,self.htype)#calculates n.f
				if not(n in self.Openl) or (n.f > (node.f + calcCost(n,node))):
					#print "n is in open"
					#print node.f + calcCost(n,node)
					#replace if f(n) is lower than n.f
					#if (n.f > (node.f + calcCost(n,node))):
					n.f = node.f + calcCost(n,node)
					#n.setparent(node,self.htype)
					if not(n in self.Openl):
						#n.setparent(node,self.htype)
						self.Openl[n] = n.f
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX	

'''

