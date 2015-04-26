class Descriptions:
    land_desc = { "Plains": "An expanse of flat green land, with many land masses in the greater distance around you.",
	"Ocean": "You're not sure how you ended up here, but it's a good thing you can swim.",
	"Shore":"You're feet make imprints in the soft, wet sand, seawater washes up against your feet as you look to the horizon",
	 "Mountain":"You breath in the cold air as you peer over the great expanse around you, a view like none other"}
    player_backstory = {"Chosen": "You are the chosen one, born ready to fight the overseer and his minions. You"
	+ "come from humble beginnings, but that doesn't mean you can't kick some monster butt. ", "Magician" : "You were once a Magician," +
	"a great boon to your village for both your showmanship and service to the people. One day, you felt a disturbance in the aether and you are " +
	"itching to find out what it is.", "Poet": " You are a poet with a habit of overdrinking and engaging in debauchery. One night you see the stars change, and " +
	"are inspired to make a name for yourself any way you can"}
    monsters ={ "Dragon":[20,30,25,10,100,["Bite","Fire Breath"],"A Fearsome Beast indeed","Dragons are known to legend as one of the fiercest minions of the overseer. It has a strong armored body, and breath of molten fire. Rumor has it, that lightning is the Dragons greatest foe.", [50,"Dragon Scale"]],
	"Lizard":[5,3,6,10,30,["Bite",],"Some lizard that crossed your path", "Lizards are common in the land of Greater Thanis, though it is only through the power of the overseer that they grow to such large sizes. Still quite the pushover though.",[10,"Lizard Tail"]],
	"Rat":[2,2,2,10,5,["Bite","Scratch"],"An ignorant rat that got mad at you for no reason", "Placeholder",[5,"Rat Claw"]],
	"Piranha":[12,3,15,10,15,["Shread"],"Vicious, ruthless killer of the water","Placeholder",[15,"Raw Fish"], "Ocean"],
	"Lion":[18,15,25,25,25,["Bite","Rip"],"Relentless killer that prays on the week", "Placeholder", [20,"Fur"], "Mountain"]}
    classes = {"Warrior":
	    {"lHand":["Copper Blade",{"attack":[5,"normal"],"abilities":{},"moves":["Stab","Slash","Lunge"]}],
	     "rHand":["Copper Shield",{"defense":[5,"normal"],"abilities":{},"moves":["Bash","Guard"]}],
	     "Head":["Copper Helm",{"defense":[2,"normal"],"abilities":{}}],
	    "Hands":["Copper Guantlets",{"defense":[2,"normal"],"abilities":{}}],
	    "Chest":["Copper Chestplate",{"defense":[5,"normal"],"abilities":{}}],
	    "Legs":["Copper Grieves",{"defense":[2,"normal"],"abilities":{}}],
	    "items":["Lesser Life PotionX5","Sprig of VigorX5"]},
        "Mage":
       {"lHand":["Basilwood Wand",{ "attack":[7,"normal"],"abilities":{},"moves":{}}],
	    "rHand":["Scroll of the Novice",{"attack":[0,"normal"],"abilities":{},"moves":["Fireball","Thunderbolt", "Ice Shards"]}],
	   "Head":["Novice Cap",{"defense":[1,"normal"],"abilities":{}}],
	  "Hands":["Novice Gloves",{"defense":[2,"normal"],"abilities":{}}],
	  "Chest":["Novice Tunic",{"defense":[2,"normal"],"abilities":{}}],
	  "Legs":["Novice Boots",{"defense":[1,"normal"],"abilities":{}}],
	  "items":["Lesser Life PotionX5","Sprig of VigorX5"]},
        "Rougue":
        {"lHand":["Twin Blades",{ "attack":[7,"normal"],"abilities":{},"moves":["Backstab","Stab","Double Slash"]}],
        "rHand":[],
        "Head":["Thief Cowl",{"defense":[2,"normal"],"abilities":{}}],
        "Hands":["Thief Gloves",{"defense":[2,"normal"],"abilities":{}}],
         "Chest":["Thief Garb",{"defense":[3,"normal"],"abilities":{}}],
        "Legs":["Thief Boots",{"defense":[2,"normal"],"abilities":{}}],
        "items":["Lesser Life PotionX5","Sprig of VigorX5"]}}
    moves = {

    #Warrior
    "Stab":[7,7,1],
    "Slash":[5,5,1],
    "Lunge":[10,10,1],
    "Windmill Slash":[15,10,3], #3 hits
    "Cross Slash":[18,15,2], #2 hits
    "Bash":[5,5,1],
    "Guard":[5,5,1],

    #Mage
    "Fireball":[20,20,1,0],
    "Thunderbolt":[20,20,1,0],
    "Ice Shards":[10,10,2,25,4], #2-4 chance hits
    "Poison Cloud":[10,15,1,0], #5 DoT per turn
    "Fire Bolts":[12,25,3,0], #3 hits
    "Thunder Storm":[5,50,50,0], #50 hits
    "Flame Vortex":[18,20,1,0], #9 DoT per turn
    "Ice Blade":[16,20,4,1,0], #4 hits

    #Rogue
    "Backstab":[11,11,1],
    "Stab":[8,8,1],
    "Double Slash":[16,16,2],#2 hits
    "Triple Slash":[8,12,1] }


    monster_moves = { "Bite":6,
    "Fire Breath":10,
    "Scratch":5,
    "Shread":8,
    "Rip":12}
    weaponsNarmour = {"Copper Blade":{"attack":[5,"normal"],"abilities":{},"moves":["Stab","Slash","Lunge"]},
               "Broad Sword":{"attack":[8,"normal"],"abilities":{},"moves":["Stab","Slash","Lunge"]},
               "Long Sword":{"attack":[12,"normal"],"abilities":{},"moves":["Slash"]},
               "Copper Shield":{"defense":[5,"normal"],"abilities":{},"moves":["Bash","Guard"]},
               "Copper Helm":{"defense":[2,"normal"],"abilities":{}},
               "Copper Guantlets":{"defense":[2,"normal"],"abilities":{}},
               "Copper Chestplate":{"defense":[5,"normal"],"abilities":{}},
               "Copper Grieves":{"defense":[2,"normal"],"abilities":{}},
               "Basilwood Wand":{ "attack":[7,"normal"],"defense":[0,"normal"],"abilities":{},"moves":{}},
               "Oak Staff":{"attack":[15,"normal"],"defense":[0,"normal"],"abilities":{},"moves":{}},
               "Scroll of the Novice":{"attack":[0,"normal"],"defense":[0,"normal"],"abilities":{},"moves":["Fireball","Thunderbolt", "Ice Shards"]},
               "Novice Cap":{"defense":[1,"normal"],"abilities":{}},
               "Novice Gloves":{"defense":[2,"normal"],"abilities":{}},
               "Novice Tunic":{"defense":[2,"normal"],"abilities":{}},
               "Novice Boots":{"defense":[1,"normal"],"abilities":{}},
               "Twin Blades":{ "attack":[7,"normal"],"abilities":{},"moves":["Backstab","Stab","Double Slash"]},
               "Poison Daggers":{"attack":[5,"poison"],"abilties":{},"moves":["Stab","Double Slash"]},
               "Thief Cowl":{"defense":[2,"normal"],"abilities":{}},
               "Thief Gloves":{"defense":[2,"normal"],"abilities":{}},
               "Thief Garb":{"defense":[3,"normal"],"abilities":{}},
               "Thief Boots":{"defense":[2,"normal"],"abilities":{}}}
    items={"Lesser Life Potion":["healing",20],
    "Sprig of Vigor":["energizing",20],
    "Aegis Nightcap":["buff","defense",5],
    "Raging Azola":["buff","attack",5],
    "Mercury Timepiece":["buff","speed",5],
    "Ice Spellstone":["damage",5,"Ice"],
    "Thunder Spellstone":["damage",5,"Thunder"],
    "Fire Spellstone":["damage",5,"Fire"],
    "Dark Spellstone":["damage",5,"Dark"],
    "Holy Spellstone":["damage",5,"Holy"],
    "Ice Spellbomb":["damage",15,"Ice"],
    "Thunder Spellbomb":["damage",15,"Thunder"],
    "Fire Spellbomb":["damage",15,"Fire"],
    "Dark Spellbomb":["damage",5,"Dark"],
    "Holy Spellbomb":["damage",5,"Holy"],
    }


    skills = {
        #"Name of skill":["type of effect", "what is affected", amount, final or percentage, description of skill"]
        "Magic gift":["buff","attack",2,"final","Magician's starter skill. when using spells, attack increases by 2"],
        "Heal":["support","health",10,"percentage","Heals 10 percent of you max health"],
        "Crit Heal":["passive","health",50,"percentage","Warrior skill that heals 50% of damage they deal"],
        "Block":["active","defense",3,"final","Warrior skill that halves all damage to the player for 3 turns"],
        "Paralizing Hit":["passive","attack",10,"percentage","A rogue skill that has a change to stop the enemy from attacking"],
        "Quick Strike":["passive","hits",15,"percentage","A theif skill that has a chance to deal 1 extra hit"]}