class Monster:
	name = "lizard"
	attack = 0
	defense = 0
	speed = 0
	awareness = 0
	hitpoints = 10
	attacks = {}
	description = "Default monster"
	bookDescription = "Default"
	drops = []
	X = 0
	Y = 0

	def __init__(self,nme,atk, defnse, spd, aware, hp, atks, desc, bookDesc,drops, x, y):
		self.name = nme
		self.attack = atk
		self.defense = defnse
		self.speed = spd
		self.awareness = aware
		self.hitpoints = hp
		self.attacks = atks
		self.description = desc
		self.bookDescription = bookDesc
		self.drops = drops
		self.X = x
		self.Y = y
