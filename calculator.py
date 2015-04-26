import random
class Calculator:


    def calculateStats(self,past):
        baseStats=[100,5,5,5,100]
        if(past=="Chosen"):
            baseStats[1]+=1
            baseStats[2]+=1
            baseStats[3]+=1
        if(past=="Magician"):
            baseStats[4]+=50
        if(past=="Poet"):
            pass #for now
        return baseStats


    def calculateDamage(self,playerAttack, monsterDefense, modifiers, element, weaknesses):
        dice = [0,1,2,3,4]
        if(playerAttack>monsterDefense):
            damage=playerAttack - monsterDefense * (modifiers/10) + random.choice(dice)
            if(element==weaknesses):
                damage*1.5

        else:
            damage=1 + random.choice(dice)
        if(damage<0):
            damage=0
        return damage
    def calculateReturnDamage(self,playerDefense, monsterAttack, modifiers):
        dice = [0,1,2,3]
        if(monsterAttack>playerDefense):
            damage=monsterAttack - playerDefense * (modifiers/10) + random.choice(dice)
        else:
            damage=1+ random.choice(dice)
        if(damage<0):
            damage=0
        return damage

    def CalculateEffect(self,item, inventory, pick):
        change = []
        if(item[pick][0]=="healing"):
            change = ["hp", item[pick][1]]
            note = "You feel Much Better. You've healed {} life".format(item[pick][1])
        if(item[pick][0]=="energizing"):
            change = ["energy",item[pick][1]]
            note = "You feel rejuvinated. You've gained {} energy".format(item[pick][1])
        if(item[pick][0] == "buff"):
            change = [item[pick][1],item[pick][2]]
        for x in inventory.split(","):
            quantity = x.split("X")
            for y in list(item.keys()):
                if(y==quantity[0]):
                    amount = int(quantity[1])
                    amount -= 1
                    newInventory = inventory.replace(x,"{}X{}".format(y,amount))
        return [change, newInventory, note]


    def calculateContents(rarity, wepNarm, items):
        contents = ""
        for equip in random.choice(list(range(3))):
            shuf = random.choice(list(range(wepNarm.keys())))
            contents = contents + shuf + ","

        for item in random.choice(list(range(2))):
            shuf2 = random.choice(list(range(items.keys())))
            contents+= shuf2 + ","
        return [contents]



