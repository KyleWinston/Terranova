from flask import Flask, render_template, request, jsonify
import mysql.connector
from Tiles import Tile
from game import Game
import random
from descriptions import Descriptions
from calculator import Calculator


app = Flask(__name__)



game=Game()

descriptions=Descriptions()
calculator = Calculator()

@app.route('/')
def index():
    return render_template("intro.html",)

@app.route('/mod/351797Aa')
def moderator():
    return render_template("moderate.html",)

@app.route('/mod/')
def worldMaker():
    world()
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    for x in range(4000):
        dice = random.choice(list(descriptions.monsters.keys()))
        mons = descriptions.monsters[dice]
        monsAttacks = mons[5]
        monsAttacksString = ""
        monsDrops = ""

        for a in list(monsAttacks):
            monsAttacksString = monsAttacksString + a + ","
        for b in mons[8]:
            monsDrops = monsDrops + str(b) + ","
        shuf1 = random.choice(list(range(200)))
        shuf2 = random.choice(list(range(200)))

        c.execute("INSERT INTO monsters VALUES(%s, %s, %s, %s, %s, %s,"
        + "%s, %s, %s, %s, %s, %s)",(dice, mons[0], mons[1], mons[2], mons[3], mons[4],
        monsAttacksString, mons[6], mons[7],monsDrops, shuf1,shuf2))

        chestShuf = random.choice(list(range(10)))
        if(chestShuf>=7):
            shuf1 = random.choice(list(range(200)))
            shuf2 = random.choice(list(range(200)))
            c.execute("INSERT INTO chests VALUES(%s,%s,%s,%s)",(1,
            calculator.calculateContents(chestShuf,
            Descriptions.weaponsNarmour, Descriptions.items), shuf1, shuf2))
            c.execute("UPDATE players SET status='alive'")
            game.gameStatus="started"
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result="")
@app.route('/player/')
def playerCount():
    return jsonify(result=game.players)

@app.route('/finish/')
def clear():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    game.gameStatus="working on it"
    c.execute("delete from players")
    c.execute("delete from world")
    c.execute("delete from monsters")

    sql.commit()
    c.close()
    sql.close()
    return jsonify(result="cleared")

@app.route('/chat/', methods=["GET"])
def chat():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    chatter=[]
    message = request.args.get('value')
    user = request.args.get('user')
    if(message[0:2]=="::"):
        c.execute("INSERT INTO chatPending(user,message) VALUES(%s,%s)",
        (user,message[2:]))
    else:
        del chatter[:]
        c.execute("SELECT * from chatPending")
        row = c.fetchall()
        for r in row:
            if row is not None:
                chatter.append("<p>" + r[0] + ":: " + r[1] + "</p>")
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result=chatter)


@app.route('/load/', methods=["GET"])
def intro():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    status=None
    answer = request.args.get('value')
    ID = request.args.get('ID')
    c.execute("SELECT * FROM players WHERE name=%s", (ID,))
    row = c.fetchone()
    if row is not None:
        status = row[3]
    if(game.gameStatus=="started" or game.players>=200):
        status="access denied"
    if(status == None):
        c.execute("INSERT INTO players (name, status) VALUES('" + answer + "', 'entering name')")
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        row = c.fetchone()
        if row is not None:
            status = row[3]
    if(status == 'entering name'):
        data = "<p>What is in your past: choose one: <ul> <li> Chosen </li> <li> Magician </li> <li> Poet </li></ul></p>"
        c.execute("UPDATE players SET status='entering past' WHERE name=%s",(ID,))
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        row = c.fetchone()
        if row is not None:
            status = row[3]
    elif(status == 'entering past'):
        data = "<p>What is your class. Choose one: <ul> <li> Warrior </li> <li> Mage </li> <li> Rougue </li> <li> Bard </li></ul></p>"
        c.execute("UPDATE players SET status='entering class' WHERE name=%s", (ID,))
        c.execute("UPDATE players SET past=%s WHERE name=%s",(answer.capitalize(), ID))
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        row = c.fetchone()
        if row is not None:
            status = row[3]
    elif(status == 'entering class'):
        data = "<p>What is your secret code?</p>"
        c.execute("UPDATE players SET status='entering code' WHERE name=%s", (ID,))
        c.execute("UPDATE players SET class=%s WHERE name=%s",(answer.capitalize(), ID))
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        row = c.fetchone()
        if row is not None:
            status = row[3]
    elif(status == 'entering code'):
        data = "<p>OK all set. Waiting on the moderator!</p>"
        c.execute("UPDATE players SET status='waiting' WHERE name=%s", (ID,))
        c.execute("UPDATE players SET code=%s WHERE name=%s",(answer.capitalize(), ID))
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        game.players+=1
        row = c.fetchone()
        if row is not None:
            status = row[3]
            past = row[1]
            Class = row[2]
        stats = calculator.calculateStats(past)
        attacks = []
        attackString=""
        equipmentString=""
        equipment = descriptions.classes[Class.capitalize()]
        for a in list(equipment["lHand"][1]["moves"]):
            attacks.append(a)
        for b in list(equipment["rHand"][1]["moves"]):
            attacks.append(b)
        for att in attacks:
            attackString=attackString + att + ","
        for d in list(equipment.keys()):
            if(d=="items"):
                for e in equipment["items"]:
                    equipmentString = equipmentString + e + ","
            else:
                equipmentString = equipmentString + equipment[d][0] + ","


        c.execute("UPDATE players SET hp=%s,attack=%s,defense=%s,speed=%s, attacks=%s,"
        + "level=1, experience=0, nextLevel=50, energy=%s,inventory=%s, lHand=%s,rHand=%s,head=%s,hands=%s,chest=%s,legs=%s where name=%s",(stats[0],
        stats[1],stats[2],stats[3],attackString,stats[4],equipmentString,
        equipment["lHand"][0],equipment["rHand"][0],equipment["Head"][0],
        equipment["Hands"][0],equipment["Chest"][0],equipment["Legs"][0],ID))

    elif(status == 'waiting'):
        data = "<p>Still waiting, please be patient.</p>"
    elif(status=="access denied"):
        data = "<p>Sorry. The player queue is full.</p>"
    else:
        data="error"
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result=data)

@app.route('/check/')
def checker():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    status=None
    ID = request.args.get('user')
    c.execute("SELECT * FROM players WHERE name=%s", (ID,))
    row = c.fetchone()
    if row is not None:
        status = row[3]
    if(status=="alive"):
        data="<p>Ready! Press >> to begin.</p>"
        head="ok"
    else:
        data=""
        head="not"
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result=data, header=head)

@app.route('/move/')
def move():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    data=""
    answer = request.args.get('value')
    ID = request.args.get('ID')
    c.execute("SELECT * FROM players WHERE name=%s", (ID,))
    row = c.fetchone()
    if row is not None:
        status = row[3]
        x = row[5]
        y = row[6]
        HP = row[7]
        attack = row[8]
        defense = row[9]
        speed = row[10]
        level = row[13]
        energy = row[17]
        Class = row[2]
        past = row[1]
        attacks = row[11]
        exp = row[14]
        nextLevel = row[15]
        inventory = row[16]
        weaponL = row[22]
        weaponR = row[23]
        head = row[18]
        arms = row[19]
        body = row[20]
        legs = row[21]
    c.execute("Select * FROM monsters WHERE X=%s AND Y=%s",(x,y))
    row=c.fetchone()
    if row is not None:
        name = row[0]
        mAttack = row[1]
        mDefense = row[2]
        mDrops = row[9].split(",")
        mHitpoints = row[5]
        mAttacks = row[6]
    c.execute("SELECT * FROM world WHERE X=%s AND Y=%s",(x,y))
    row=c.fetchone()
    if row is not None:
        land = row[0]
        desc = row[3]
    c.close()
    c = sql.cursor()
    if(answer=="start"):
        c.execute("UPDATE players SET X=%s, y=%s WHERE name=%s",(random.randrange(200),random.randrange(200),ID))
        c.execute("SELECT * FROM players WHERE name=%s",(ID,))
        row = c.fetchone()
        if row is not None:
            x = row[5]
            y = row[6]
            c.execute("SELECT * FROM world WHERE X=%s AND Y=%s", (x,y))
            row = c.fetchone()
            if row is not None:
                land = row[0]
                desc = row[3]
        data = "You are on a {} tile <br> {} <br>".format(land, desc)
    c.close()
    c = sql.cursor()
    if(status!="dead"):
        if(answer=='profile'):
            data = "You're name is {} <br> You are a {} <br> {} <br> Your class is: {} <br> Your stats are: <br> Level:{} HP:{} <br> Attack:{} <br> Defense:{} <br> Speed:{} <br> Energy:{}".format(ID,past,descriptions.player_backstory[past],Class,level,HP,attack,defense,speed,energy)
        elif(answer == "inventory"):
            items = inventory.split(",")
            data = "Inventory: <br>"
            for x in items:
                data = data + x + "<br>"
        elif(answer[:3] == "Use"):
            items = inventory.split(",")
            ret = calculator.CalculateEffect(descriptions.items, inventory, answer[4:])
            if(ret[0][0] == "hp"):
                c.execute("UPDATE players SET inventory=%s,hp=%s WHERE name=%s", (ret[1],(HP + ret[0][1]),ID))
            elif(ret[0][0] == "energy"):
                c.execute("UPDATE players SET inventory=%s,energy=%s WHERE name=%s", (ret[1],(energy + ret[0][1]),ID))
            data = ret[2]
        elif(answer=="North" or answer=="N" and status!="fighting"):
            c.execute("SELECT * FROM players WHERE name=%s", (ID,))
            row = c.fetchone()
            if row is not None:
                y = row[6]
            c.close()
            c=sql.cursor()
            if(y>0):
                c.execute("UPDATE players SET y=%s WHERE name=%s", (y-1,ID))
                c.execute("SELECT * FROM players WHERE name=%s", (ID,))
                row = c.fetchone()
                if row is not None:
                    y = row[6]
                c.execute("SELECT * FROM world WHERE X=%s AND Y=%s", (x,y))
                row = c.fetchone()
                if row is not None:
                    land = row[0]
                    desc = row[3]
            data = "You are on a {} tile <br> {} <br>".format(land, desc)
        elif(answer=="East" or answer=="E" and status!="fighting"):
            c.execute("SELECT * FROM players WHERE name=%s", (ID,))
            row = c.fetchone()
            if row is not None:
                x = row[5]
            c.close()
            c=sql.cursor()
            if(x<199):
                c.execute("UPDATE players SET X=%s WHERE name=%s", (x+1,ID))
                c.execute("SELECT * FROM players WHERE name=%s", (ID,))
                row = c.fetchone()
                if row is not None:
                    x = row[5]
                c.execute("SELECT * FROM world WHERE X=%s AND Y=%s", (x,y))
                row = c.fetchone()
                if row is not None:
                    land = row[0]
                    desc = row[3]
            data = "You are on a {} tile <br> {} <br>".format(land, desc)
        elif(answer=="South" or answer=="S" and status!="fighting"):
            c.execute("SELECT * FROM players WHERE name=%s", (ID,))
            row = c.fetchone()
            if row is not None:
                y = row[6]
            c.close()
            c=sql.cursor()
            if(y<199):
                c.execute("UPDATE players SET y=%s WHERE name=%s", (y+1,ID))
                c.execute("SELECT * FROM players WHERE name=%s", (ID,))
                row = c.fetchone()
                if row is not None:
                    y = row[6]
                c.execute("SELECT * FROM world WHERE X=%s AND Y=%s", (x,y))
                row = c.fetchone()
                if row is not None:
                    land = row[0]
                    desc = row[3]
            data = "You are on a {} tile <br> {} <br>".format(land, desc)
        elif(answer=="West" or answer=="W" and status!="fighting"):
            c.execute("SELECT * FROM players WHERE name=%s", (ID,))
            row = c.fetchone()
            if row is not None:
                x = row[5]
            c.close()
            c=sql.cursor()
            if(x>0):
                c.execute("UPDATE players SET X=%s WHERE name=%s", (x-1,ID))
                c.execute("SELECT * FROM players WHERE name=%s", (ID,))
                row = c.fetchone()
                if row is not None:
                    x = row[5]
                c.execute("SELECT * FROM world WHERE X=%s AND Y=%s", (x,y))
                row = c.fetchone()
                if row is not None:
                    land = row[0]
                    desc = row[3]
            data = "You are on a {} tile <br> {} <br>".format(land, desc)
        elif(answer=="Attack"):
                data = data + "The {} wakes up, the battle begins".format(name)
                c.execute("UPDATE players SET status='fighting' WHERE name=%s",(ID,))
        elif(answer == "Moves" and status=="fighting"):
            c.execute("SELECT * FROM players WHERE name=%s", (ID,))
            row = c.fetchone()
            if row is not None:
                attacks=row[11]
            listOfAttacks=attacks.split(",")
            for y in listOfAttacks:
                data = data + y.capitalize() + "<br>"
        elif(status=="fighting"):
            for a in attacks.split(","):
                hitting=True
                hits=0
                if(answer == a):
                    while(hitting):
                        equipA = descriptions.weaponsNarmour[weaponL]["attack"][0] + descriptions.weaponsNarmour[weaponR]["attack"][0]
                        equipD = descriptions.weaponsNarmour[weaponL]["defense"][0] + descriptions.weaponsNarmour[weaponR]["defense"][0] + descriptions.weaponsNarmour[head]["defense"][0] + descriptions.weaponsNarmour[arms]["defense"][0] + descriptions.weaponsNarmour[body]["defense"][0] + descriptions.weaponsNarmour[legs]["defense"][0]
                        damage = calculator.calculateDamage((attack + equipA) ,mDefense,
                        descriptions.moves[answer][0],
                        "normal","thunder")
                        data = data + "you deal {} damage to {} <br>".format(damage,name)
                        hits+=1
                        if(hits>=descriptions.moves[answer][2]):
                            hitting=False
            c.execute("UPDATE monsters SET hitpoints=%s WHERE X=%s AND Y=%s",((mHitpoints-damage),x,y))
            sql.commit()
            c.execute("SELECT * FROM monsters WHERE X=%s AND Y=%s",(x,y))
            row = c.fetchone()
            if row is not None:
                mHitpoints = row[5]
            data = data + "{} has {} hitpoints left <br>".format(name,mHitpoints)
            if(mHitpoints <=0):
                data = data + "<br> You killed the {}. You gain {} exp.".format(name,mDrops[0])
                c.execute("UPDATE players SET experience=%s WHERE name=%s",(int(exp) + int(mDrops[0]),ID))
                c.execute("UPDATE players SET status='alive' WHERE name=%s",(ID,))
                c.execute("DELETE FROM monsters WHERE X=%s AND Y=%s",(x,y))
                if(int(exp) + int(mDrops[0]) >= nextLevel):
                    data = data + "You've leveled up!!"
                    c.execute("UPDATE players SET level=%s, attack=%s, defense=%s, speed=%s, hp=%s WHERE name=%s",(level + 1,
                    attack + random.choice(list(range(3))),defense + random.choice(list(range(3))),
                    speed + random.choice(list(range(3))), HP +random.choice(list(range(20))),ID))

            else:
                shuf =""
                while(shuf==""):
                    shuf = random.choice(mAttacks.split(","))
                damageReturn = calculator.calculateReturnDamage(mAttack, (defense + equipD), descriptions.monster_moves[shuf])
                c.execute("SELECT * FROM players WHERE name=%s",(ID,))
                row=c.fetchone()
                if row is not None:
                    HP = row[7]
                c.execute("UPDATE players SET hp=%s WHERE name=%s",((HP - damageReturn),ID))
                data=data + "{} deals {} damage to you".format(name,damageReturn)
                if(HP<=0):
                    data= data + "You have perished at the hands of a {}".format(name)
                    c.execute("UPDATE players SET status='dead' WHERE name=%s",(ID,))
    else:
        data = "Sorry, but you are dead. Dead people don't move"
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result=data, header=status)


@app.route('/event/')
def eventManager():
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    data = ""
    x=0
    y=0
    ID=request.args.get("ID")
    c.execute("SELECT * FROM players WHERE name=%s", (ID,))
    row = c.fetchone()
    if row is not None:
        x = row[5]
    c.execute("SELECT * FROM players WHERE name=%s", (ID,))
    row = c.fetchone()
    if row is not None:
        y = row[6]
    c.execute("SELECT * FROM monsters WHERE X=%s AND Y=%s", (x,y))
    row = c.fetchone()
    if row is not None:
        name = row[0]
        data += "A {} is sleeping nearby!".format(name)
    count = c.execute("SELECT COUNT(*) FROM monsters")
    c.execute("SELECT * FROM chests WHERE X=%s AND Y=%s", (x,y))
    if row is not None:
        data += "You found a chest!".format(name)
    sql.commit()
    c.close()
    sql.close()
    return jsonify(result=data, header=count)


def world():
    grid = [[Tile() for x in range(200)]for y in range(200)]
    for y in range(len(grid)):
        for x in range(len(grid)):
            rand = random.choice(list(range(600)))
            if(rand==1):
                grid[x][y].land = "Ocean"
                grid[x][y].moisture = 15
                grid[x][y].height= 0-15
            else:
                grid[x][y].land = "Plains"
                grid[x][y].moisture = 10
    for y in range(len(grid)):
        for x in range(len(grid)):
            if(grid[x][y].land == "Ocean" and x<199 ):
                    grid[x+1][y].land = "Ocean"
                    if(grid[x][y].height <= -2 and x<199):
                        grid[x+1][y].height = grid[x][y].height+1
                        grid[x+1][y].land = "Ocean"
                    if(grid[x][y].height <= -2 and x>0):
                        grid[x-1][y].height = grid[x][y].height+1
                        grid[x-1][y].land = "Ocean"
                    if(grid[x][y].height <= -2 and y<199):
                        grid[x][y+1].height = grid[x][y].height+1
                        grid[x][y+1].land = "Ocean"
                    if(grid[x][y].height <= -2 and y>0):
                        grid[x][y-1].height = grid[x][y].height+1
                        grid[x][y-1].land = "Ocean"
                    for y in range(len(grid)):
                        for x in range(len(grid)):
                            if(grid[x][y].height>-1 and grid[x][y].land is "Ocean"):
                                 grid[x][y].land = "Shore"
                                 grid[x][y].moisture = 15
    for y in range(len(grid)):
        for x in range(len(grid)):
            count=0
            if(x<199 and grid[x][y].land != "Ocean" and grid[x+1][y].land != "Ocean"):
                count+=1
            if(x>0 and grid[x][y].land != "Ocean" and grid[x-1][y].land != "Ocean"):
                count+=1
            if(y<199 and grid[x][y].land != "Ocean" and grid[x][y+1].land != "Ocean"):
                count+=1
            if(y>0 and grid[x][y].land != "Ocean" and grid[x][y-1].land != "Ocean"):
                count+=1
            if(count>=4):
                grid[x][y].moisture-=1
                grid[x][y].land = "Plains"

    for y in range(len(grid)):
        for x in range(len(grid)):
            rand=random.choice(list(range(1000)))
            if(rand==1):
                grid[x][y].height = random.choice(list(range(10)))
                grid[x][y].land = "Mountain"


    for y in range(200):
        for x in range(200):
            if(grid[x][y].land == "Ocean"):
                grid[x][y].description = descriptions.land_desc["Ocean"]
            if(grid[x][y].land == "Plains"):
                grid[x][y].description = descriptions.land_desc["Plains"]
            if(grid[x][y].land == "Shore"):
                    grid[x][y].description = descriptions.land_desc["Shore"]
            if(grid[x][y].land == "Mountain"):
                grid[x][y].description = descriptions.land_desc["Mountain"]
    sql = mysql.connector.connect(user="elvishknight1", password="351797asd", host="mysql.server", database="elvishknight1$Overseer", buffered=True)
    c = sql.cursor()
    for y in range(len(grid)):
        for x in range(len(grid)):
            c.execute("INSERT INTO world VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            ,(grid[x][y].land,grid[x][y].height,grid[x][y].moisture,grid[x][y].description,grid[x][y].village,grid[x][y].treasure,x,y))
    sql.commit()
    c.close()
    sql.close()

