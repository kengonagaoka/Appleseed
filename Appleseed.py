import random

print("_____________________________________________________________")
print("||/–––––––––––––––––––––––––––––––––––––––––––––––––––––––\||")
print("||   W e l c o m e  t o                                    ||")
print("||       __   ___  ___  _    ____  __  ____ ____ ___       ||")
print("||       /\   |  \ |  \ |    |    /  \ |    |    |  \      ||")
print("||      /__\  |__/ |__/ |    |––  '––, |––  |––  |   |     ||")
print("||     /    \ |    |    |__/ |___ \__/ |___ |___ |__/      ||")
print("||                                                         ||")
print("||   Sow joy and prosperity throughout the countryside...  ||")
print("||     One seed at a time.                                 ||")
print("||                                                         ||")
print("||      (  (  ) )      Press Enter to Start         (  ) ) ||")
print("||    (  (       )                               (       ) ||")
print("||  (  ( •    •  ) )                           (• ( •    • ||")
print("||  ( (• (  )•  ) • )                          ( (• (  )  )||")
print("||    ( ( •( •) )•)       _0_                    ( (•( •) •||")         
print("||         | |          |/\ /\•                        | | ||")
print("||         | |    ___   | |||      _|_|_|_|_|_|_|_|_|_|_|_|||")
print("||   •  • /   \ • \_/•  | |||      _|_|_|_|_|_|_|_|_|_|_|_|||")
print("||                   Kengo Nagaoka 2016                    ||")
print("||\–––––––––––––––––––––––––––––––––––––––––––––––––––––––/||")
print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
input(": ")
print(" ")
while True:
    player_name = input("Enter your name: ")
    if len(player_name) > 16:
        print("Your name must be 16 characters or less")
        continue
    else:
        break
while True:
    player_gender = input("Enter your preferred pronoun (he, she, or they): ")
    if player_gender == "he" or player_gender == "she" or player_gender == "they":
        break
    else:
        print("Invalid answer")
        continue
if player_gender == "he":
    lad_lady = "lad"
    mister_missus = "mister"
    sir_madam = "sir"
    mr_ms = "Mr. Appleseed"
    bro_sis = "brother"
elif player_gender == "she":
    lad_lady = "lady"
    mister_missus = "missus"
    sir_madam = "madam"
    mr_ms = "Ms. Appleseed"
    bro_sis = "sister"
elif player_gender == "they":
    lad_lady = "friend"
    mister_missus = "friend"
    sir_madam = "friend"
    mr_ms = "Mx. Appleseed"
    bro_sis = "friend"
        
print("\nWelcome to the quaint town of Longmeadow! As a humble merchant, you, " + player_name + " Appleseed, will travel the countryside planting and peddling appleseeds. The sun is shining, the water is clear, the soil is fertile, and the people are good. Your dream is to estalish apple tree nurseries in three of Longmeadow's neighboring towns: Licking Creek, Green Town, and Venango County. Along the way, you will meet and trade with many a folk and spread the appleseed far and wide.")
print("\nYour family owns a nursery here in your hometown of Longmeadow. Every time you enter a town, you will have to pay a certain amount of gold pieces to maintain your nursery. In return, you will receive appleseeds and gold pieces from your nursery every time you come home. You will begin your journey with 100 gold pieces and 1000 appleseeds. Just make sure you don't run out of gold, or you'll have to come home to borrow money from your sister!")

gold_player = 100###
seed_player = 1000###
location = "Venango County"
cust_index = 22
first_round = True
sack = ["Tin Cap","Spoon","Town Map"]
nurs_lc = False
nurs_gt = False
nurs_vc = False
nurs_maint = 80###
game_over = False

hap_farmer_jacob = 1.1
hap_martha = 1.2
hap_neighbor_pete = 1.4
hap_farmer_goffe = 1.2
hap_storekeeper_samantha = 1.1 #6/10

hap_angler_wyman = 1
hap_young_arthur = 1.5
hap_mill_operator_swatley = 1
hap_mother_erwin = 0.9
hap_orchard_keeper_stevens = 0.9 #5.3/10

hap_gardener_sherman = 0.8
hap_jeremiah = 0.7
hap_father_adam = 0.6
hap_young_julia = 1.2
hap_elder_hawthorne = 0.5 #3.8/10

hap_town_beggar_popo = 0.1
hap_councilman_pitts = 0.3
hap_gravedigger_tehwehron = 0.2
hap_baker_lila = 1.2
hap_nurseryman_jon = 0.3 #2.1/10

def nurs(location):
    if location == "Longmeadow":
        return " √"
    elif location == "Licking Creek" and nurs_lc == True:
        return " √"
    elif location == "Green Town" and nurs_gt == True:
        return " √"
    elif location == "Venango County" and nurs_vc == True:
        return " √"
    else:
        return "  "

def cust_prog(cust_index):
    if cust_index == 0 or cust_index == 6 or cust_index == 12 or cust_index == 18:
        return " 1"
    elif cust_index == 1 or cust_index == 7 or cust_index == 13 or cust_index == 19:
        return " 2"
    elif cust_index == 2 or cust_index == 8 or cust_index == 14 or cust_index == 20:
        return " 3"
    elif cust_index == 3 or cust_index == 9 or cust_index == 15 or cust_index == 21:
        return " 4"
    elif cust_index == 4 or cust_index == 10 or cust_index == 16 or cust_index == 22 or cust_index == 5 or cust_index == 11 or cust_index == 17 or cust_index == 23:
        return " 5"

def proceed_msg(cust_index):
    if cust_index == 5 or cust_index == 11 or cust_index == 17 or cust_index == 23:
        return "Proceed to next town    "
    else:
        return "Proceed to next trade   "

def offer_func(total_offer):
    while True:
        try:
            total_offer_1 = int(input("What price will you offer?: "))
        except ValueError:
            print("Your offer must be an integer.")
            continue
        if total_offer <= total_offer_1 or total_offer_1 <= 0:
            print("Your offer must be more than 0, less than 100000, and less than your last offer.")
            continue
        elif total_offer_1 % 1 == 0:
            return total_offer_1 

def price_calc(price,price_c,offer,offer_count):
    a = price_c / offer
    if a > 1:
        a = 1
    b = price + ((((min(price_c,offer) - price) / 4) * (offer_count - 1)) * a)
    return b

def add_hap(final_price,seed_sold,price_c):
    a = 0.04 / ((final_price / seed_sold) / price_c)
    if a > 0.4: # happiness max increase
        a = 0.4
    return a
    
while True:
    if game_over == True:
        break
    if cust_index == 0:
        location = "Longmeadow"           
    elif cust_index == 6:
        location = "Licking Creek"
    elif cust_index == 12:
        location = "Green Town"
    elif cust_index == 18:
        location = "Venango County"
    print("\nWelcome to " + location + "!")
    if location == "Longmeadow" and first_round == False:
        gold_player += 320###
        seed_player += 1100###
        print("You received 320 gold and 1100 seeds from your Longmeadow nursery.")
    elif location == "Licking Creek" and nurs_lc == True:
        gold_player += 600###
        seed_player += 500###
        print("You received 600 gold and 500 seeds from your Licking Creek nursery.")
    elif location == "Green Town" and nurs_gt == True:
        gold_player += 800###
        seed_player += 700###
        print("You received 800 gold and 700 seeds from your Green Town nursery.")
    elif location == "Venango County" and nurs_vc == True:
        gold_player += 1000###
        seed_player += 1000###
        print("You received 1000 gold and 1000 seeds from your Venango County nursery.")
        
    while True:
        if game_over == True:
            break
        print(" ")
        print(" ––––––––––––––––––––––––––––")
        print("| " + player_name + " Appleseed" + (" " * (17 - len(player_name))) + "|")
        print("| " + location + nurs(location) + cust_prog(cust_index) + "/5"+ (" " * (21 - len(location))) + "|")
        print("|    Gold Pieces: " + str(int(gold_player)) + (" " * (11 - len(str(int(gold_player))))) + "|")
        print("|    Appleseeds: " + str(int(seed_player)) + (" " * (12 - len(str(int(seed_player))))) + "|")
        print("|                            |")
        end_menu = input("| What would you like to do? |\n| 1. " + proceed_msg(cust_index) + "|\n| 2. Open sack               |\n| 3. Establish nursery       |\n ––––––––––––––––––––––––––––\n: ")
        
        if end_menu == "1":
            if cust_index == 5 or cust_index == 11 or cust_index == 17 or cust_index == 23:
                input("\nYou are about to leave " + location + ". It is time to pay your nursery dues. You are due " + str(nurs_maint) + " gold for the upkeep of your nurseries. Press Enter to continue: ")
                if gold_player < nurs_maint:
                    game_over = True
                    print("\n –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
                    print("|           Oh no! You don't have enough gold pieces!           |")
                    print("|   Better run back home to ask your sister for some money...   |")
                    print("|                                                               |")
                    print("|                             _0                                |")
                    print("|                            /\\\\_|                              |")
                    print("|                             |\ |                              |")
                    print("|                      . . . / | |                              |")
                    print("|                                                               |")
                    print("|                      G A M E  O V E R                         |")
                    print(" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
                    break
                else:
                    gold_player -= nurs_maint
                    print("\nYou paid " + str(nurs_maint) + " gold to maintain your nurseries.\n")
                    if cust_index == 23:
                        cust_index = 0
                        first_round = False
                    else:
                        cust_index += 1
                    break
                
            print("\nProceeding to next trade...\n")
            if cust_index == 0:
                print(" ||||||||")
                print("||       |")
                print("|  .  \ .")
                print("C  -  _| )")
                print("|\_ / -\\'")
                cust_name = "Farmer Jacob"
                cust_item = "Old Jeans"
                btrlo = 80
                btrhi = 90
                sslo = 50
                sshi = 70
                hap = hap_farmer_jacob
                init_price_c = 2
                message_grt = "Hello there my friend, nice day isn't it? Would you do an old farmer a favor and hash me a good price for these here seeds? I'd like to buy "
                message_op = "Holy knickerbockers! I'd rather throw myself in the River Muskingum!"
                message_angry = "Thanks."
                message_neutral = "I know I can always depend on you, my friend. Take care now."
                message_happy = "You've darn near done it this time! I'll never buy my appleseeds from anyone else!"
                message_cancel = "That's a bummer. Maybe neighbor Jed has some I can hussy."
                message_item = "You're always wearing those same raggety pants. Here, take these."
            elif cust_index == 1:
                print(" cCCCcCcc")
                print("cCc     Cc")
                print("Cc ,  \ , c")
                print("C    c_)  )")
                print("|\ '  v  /")
                cust_name = "Martha"
                cust_item = "Pear Seeds"
                btrlo = 70
                btrhi = 90
                sslo = 5
                sshi = 10
                hap = hap_martha
                init_price_c = 2
                message_grt = "Good morning " + lad_lady + ", I hope you can spare me a few of 'em nice appleseeds you sell? I'd like to plant 'em in my yard. Maybe it'll be a treat for them ol' chillun! I want to get me "
                message_op = "Oh good heavens. Maybe I'll plant a pear tree instead."
                message_angry = "Ya ain't doin' me a favor but I'll take 'em."
                message_neutral = "Thanks, my " + lad_lady + ", I hope they grow as good as you say!"
                message_happy = "Golly gee am I excited about this! You've done me a real treat, my " + lad_lady
                message_cancel = "I guess I'll hafta go find me a pear seed seller."
                message_item = "You've done good to me, darlin'. Have these " + cust_item + ". I hope you won' be mad at me."
            elif cust_index == 2:
                print(" ////\\\\\ ")
                print("||     ||")
                print("|  o \ o")
                print("C    _\ '")
                print("|\  -3-/")
                cust_name = "Neighbor Pete"
                cust_item = "Longmeadow Lager"
                btrlo = 85
                btrhi = 95
                sslo = 20
                sshi = 50
                hap = hap_neighbor_pete
                init_price_c = 2
                message_grt = "Ho, well ain't it my very own neighbor " + player_name + "! Of course I want some of your appleseeds! This little town of Longmeadow ain't got enough apple trees yet. I'll take "
                message_op = "Ha HA! That's a funny joke you're playin' on me, Appleseed."
                message_angry = "Alright, well I'll take them if that's what you're offerin'. Come home and rest once in a while won't you?"
                message_neutral = "My good ol' neighbor pullin' through like always! You're always welcome here my friend."
                message_happy = "Ho! You're bein' too kind to me, Appleseed! I appreciate it. Why don't you come over for supper sometime?"
                message_cancel = "I guess I'll catch you next time you come 'round."
                message_item = "You ought to have some of this durin' your travels. It'll loosen you right up after a long days' walkin'. I made it myself."
            elif cust_index == 3:
                print("   _______")
                print("  /       \ ")
                print(" |  ==  == |")
                print(" [  -  \ - |")
                print(" |    c_)  |")
                print("/ \_ '-  _/ \ ")
                cust_name = "Farmer Goffe"
                cust_item = "Farmer Goffe's Axe"
                btrlo = 70
                btrhi = 80
                sslo = 50
                sshi = 70
                hap = hap_farmer_goffe
                init_price_c = 1.8
                message_grt = "'Afternoon. Let's take a look at what ya got. I'll take "
                message_op = "Don't act like I don't know what the prices are 'round here, kid."
                message_angry = "(cough)."
                message_neutral = "Thanks, kid."
                message_happy = "Hm! I owe you one, kid."
                message_cancel = "(cough) 'Later."
                message_item = "I'm proud of what you done 'round these parts, kid. I want you to have this."
            elif cust_index == 4:
                print("  ////\\\\\ ")
                print(" ////  \\\\\ ")
                print("||| o   o||")
                print("|C.   _\ '|")
                print("||\_  - /||")
                print("||||   ||||")
                cust_name = "Storekeeper Samantha"
                cust_item = "Fancy Letter Set"
                btrlo = 50
                btrhi = 80
                sslo = 80
                sshi = 100
                hap = hap_storekeeper_samantha
                init_price_c = 1.8
                message_grt = "My customers have been asking for appleseeds recently... I wonder what's going on? Well, gotta keep them happy so here I am! Did you know that the lower the price you offer, the happier your customer will be? Anyway, I need "
                message_op = "I'd rather not have to ask my shoppers to pay that much."
                message_angry = "I like you, " + player_name + ", but like I said you've gotta keep your customers happy..."
                message_neutral = "Us two, we're not too different are we? Though I wish I were the one wandering the woodland paths. Thank you, " + player_name + "."
                message_happy = "You've got a way with this, don't you? I wish you would stay in town longer. See you soon!"
                message_cancel = "That's too bad. I was counting on you. Maybe next time..."
                message_item = "Um... this may be a bit forward... but will you let me be your girlfriend? Please, take this. And write to me while you're away!"
            elif cust_index == 6:
                print("  ______")
                print(" /      \__")
                print("|__–––––––––")
                print("C ._   _.|")
                print("|    _\  |")
                print("|\_ -  _/")
                cust_name = "Angler Wyman"
                cust_item = "Fishing Fly"
                btrlo = 40
                btrhi = 60
                sslo = 10
                sshi = 30
                hap = hap_angler_wyman
                init_price_c = 1.6
                message_grt = "I saw you walking up the path while I was fishing. This here road's called Braddock's Road. It'll lead you all the way to Venango. The name's Wyman. I ain't looking for much. I'll take "
                message_op = "Stinkin' sturgeons, this seller's no good."
                message_angry = "(spits) I guess I'd rather take it than not."
                message_neutral = "That's reasonable. Safe travels, friend."
                message_happy = "Hah! Well I'll be! Come on by anytime, friend, and I'll show you the best fishing spots!"
                message_cancel = "Go back to Longmeadow, " + lad_lady + ", you're wasting your time here."
                message_item = "You're a good " + lad_lady + ". I made this for you."
            elif cust_index == 7:
                print("/////\\\\\ ")
                print("c . _\.|")
                print(" \_ v /")
                cust_name = "Young Arthur"
                cust_item = "Strange Pebble"
                btrlo = 50
                btrhi = 90
                sslo = 5
                sshi = 20
                hap = hap_young_arthur
                init_price_c = 1.7
                message_grt = "Hello " + sir_madam + "! I remember you! You're " + player_name + " Appletree! My name's Arthur. Can I please buy some appleseeds? I want "
                message_op = "Umm... My mum told me I shouldn't pay that much for appleseeds."
                message_angry = "That's gonna cost me my week's allowance! Oh well!"
                message_neutral = "Thanks, " + sir_madam + "! I'm gonna go plant these now!"
                message_happy = "Wow!! I'm gonna go tell my mum about this!"
                message_cancel = "Oh, okay. Can you please give me some when you come next time?"
                message_item = "I found this in the creek! You can have it if you want!"
            elif cust_index == 8:
                print("   _______")
                print("  /__–––––\_")
                print("_|_––––––––_|")
                print(" ||  o  \ o' ")
                print(" [ (    _\ )")
                print("  |\_ / -\\'")
                cust_name = "Mill Operator Swatley"
                cust_item = "Wooden Top"
                btrlo = 60
                btrhi = 70
                sslo = 70
                sshi = 90
                hap = hap_mill_operator_swatley
                init_price_c = 2
                message_grt = "As long as Mother Nature keeps giving, my mill will run, 'round and 'round. Too bad money don't grow on trees. Apples come close, though! Let's go with "
                message_op = "We're like cogs in a machine, friend. If one doesn't budge, the others won't either."
                message_angry = "I don't wish bad upon you, friend, but as they say, 'What goes around comes around'..."
                message_neutral = "I do hope to catch you when you come on 'round again!"
                message_happy = "Thank you, traveler! May the seasons work in your favor!"
                message_cancel = "Mother Nature will provide for me instead."
                message_item = "I have something for you, traveler. This top used to belong to my good friend. I hope it will remind you that even though we all run in circles, all things must come to an end."
            elif cust_index == 9:
                print(" //////\\\\\ ")
                print("////-   _\\\\ ")
                print("||| .    .'")
                print("\\\\(    _\ )")
                print(" |\_ '- '/")
                cust_name = "Mother Erwin"
                cust_item = "Nesting Dolls"
                btrlo = 50
                btrhi = 60
                sslo = 20
                sshi = 40
                hap = hap_mother_erwin
                init_price_c = 1.7
                message_grt = "Did you sell that boy appleseeds again? I told him not to go wasting his allowance on such things! That boy never listens... (sigh)... " + mr_ms + ", I need "
                message_op = "We're a poor family, can't you see? I cannot afford that."
                message_angry = "That's fine. But I wish you'd have more sympathy for a single mother and her son."
                message_neutral = "Thank you, " + mr_ms + ". Next time, please don't sell Arthur any more seeds."
                message_happy = "Thank you very much, " + mr_ms + ". Maybe I'll forgive Arthur this time around."
                message_cancel = "That's not very good for me or you, " + mr_ms + ". I'll have to look elsewhere. Where's Arthur? ARTHUR ERWIN COME BACK HERE NOW!"
                message_item = "You've been very good to me and my son, " + mr_ms + ". Please take this small gift as a token of our gratitude."
            elif cust_index == 10:
                print("    _______")
                print(" __/__–––––\____")
                print("/____–––––––––––\ ")
                print("   C|| o  \ o'")
                print("   |||   c_| |")
                print("   | \\\\ /||\/")
                cust_name = "Orchard Keeper Stevens"
                cust_item = "Earthworms"
                btrlo = 50
                btrhi = 60
                sslo = 130
                sshi = 180
                hap = hap_orchard_keeper_stevens
                init_price_c = 1.5
                message_grt = "Here at Licking Creek, the water is clean, the sun is bright, and the soil is dark. Ain't anywhere on this side of the Muskingum better than here to have an orchard. Let's get "
                message_op = "Oh! I could buy me a whole 'nother orchard for that price!"
                message_angry = "With these prices... maybe there IS a better place on the other side..."
                message_neutral = "This land's blessed, lemme tell you. Good luck now!"
                message_happy = "And the people are good, don't lemme forget that! Thanks again, Appleseed!"
                message_cancel = "Quittin' on trades ain't gonna make a customer happy, hope you understand."
                message_item = "I think this'll help you out at your nursery. These little buggers can't see and eat dirt all day, but boy do they get the job done!"
            elif cust_index == 12:
                print("  ______")
                print(" /      \ ")
                print("|| _    _|")
                print("[  -  | -'")
                print("||   c_\ |")
                print("| \\\\\\ 3//")
                print("   \\\\||/")
                print("    \|/")                
                cust_name = "Gardener Sherman"
                cust_item = "Fennel"
                btrlo = 55
                btrhi = 75
                sslo = 90
                sshi = 120
                hap = hap_gardener_sherman
                init_price_c = 1.5
                message_grt = "Welcome to Green Town! Stevens over by the Creek might not like to admit it, but the plantin' here is even better than it is over there! Heck, I can grow any type of gotdamn herb I want here! Check it out! Why don't you gimme "
                message_op = "GotDAMN! I'd rather eat a whole jar of beeswax!"
                message_angry = "GotDAMN! Why can't I get a good price anymore? Y'all sellers are as prickly as a rosebush!"
                message_neutral = "GotDAMN! I knew you'd gimme a good price. Wanna come in for some chamomile tea?"
                message_happy = "Holy gotDAMN! These prices are spicier than spiciest pepper I grow! I gotta tell my wife about this!"
                message_cancel = "GotDAMN! Nevermind, I was just about to go tend to my mint plants anyway. At least they won't quit on me!"
                message_item = "I need to tell you something straight, Appleseed. I ain't never seen appleseeds as plump, and as CHEAP, as yours! Here, have a bunch of my BEST GOTDAMN fennel!"
            elif cust_index == 13:
                print("   ZZZZZZZ")
                print(" ZZZZ Z ZZZ")
                print("ZZZZo Z\ o'Z")
                print("ZZZ   c_) )Z")
                print("ZZZ\_ =  /ZZ")
                print("Z Z        Z")
                cust_name = "Jeremiah"
                cust_item = "Mango Seeds"
                btrlo = 25
                btrhi = 45
                sslo = 20
                sshi = 45
                hap = hap_jeremiah
                init_price_c = 1.4
                message_grt = "G'mornin' dere, " + mister_missus + ". I know I don' look like I come from here but I'm willin' to pay a price for dem seeds. May I see whatchu got? I'll take "
                message_op = "Where I come from we try to help each other out, " + mister_missus + "."
                message_angry = "I hope you ain't got somethin' against me just 'cause of how I look."
                message_neutral = "Thankya much, " + mister_missus + "."
                message_happy = "Hah! From now on I call you my " + bro_sis + "!"
                message_cancel = "This here country, I can never figure out why people is always lookin' out for themselves but never each other!"
                message_item = mr_ms + ", I come from the Caribbean, and my mother before that from the heartland Africa. Now I'm a free man but I ain't got a means of gettin' around. Thank the Lord I found mah way to Green Town where people's been welcomin'. Would you take a few of these and if you's ever in someplace you think they'll grow, plant 'em for me? What I'd do to taste a sweet mango again, hah!"
            elif cust_index == 14:
                print(" //|||||\ ")
                print("||       |")
                print("C––( )\-( )")
                print("|    c_) )")
                print("|\_  -  _|")
                cust_name = "Father Adam"
                cust_item = "Blessing"
                btrlo = 50
                btrhi = 65
                sslo = 50
                sshi = 70
                hap = hap_father_adam
                init_price_c = 1.4
                message_grt = "Oh weary wanderer, traveler... what is it that you seek? Is it profit? Is it fame? Is it happiness? Or is it God you are searching for? He, whose apple condemned all mankind to this Earth... yet who everyday plants the seeds of who we are to be. What will you be, Appleseed? While you ponder, why don't you sell me "
                message_op = "My " + bro_sis + "! Is this some kind of test? Why so high the price?"
                message_angry = "I shouldn't have bought them. The price is too high! But I like them so much!"
                message_neutral = "My wife says I shouldn't eat too many apples because they give me indigestion. But I guess today I'll indulge!"
                message_happy = "Oh, I've bought too many again... why do you tempt me with such a great price?"
                message_cancel = "Why did God place the apple in the Garden of Eden? My " + bro_sis + "! Why do you come to sell me appleseeds and then refuse?"
                message_item = "My " + bro_sis + ", you have proven to be a wise and generous person. May your travels be fruitful, your search be fulfilled, and your relationship to God be ever close!"
            elif cust_index == 15:
                print(" ////\\\\\ ")
                print("///^   \\\\ ")
                print("|C o _\o|")
                print("\\\\_  v /")
                cust_name = "Young Julia"
                cust_item = "Candles"
                btrlo = 20
                btrhi = 50
                sslo = 30
                sshi = 40
                hap = hap_young_julia
                init_price_c = 1.2
                message_grt = mr_ms + "! " + mr_ms + "! " + mr_ms + "! I've been waiting for you to come back to Green Town! Did you sell a lot of appleseeds? Who did you meet? Did you see any cool wild animals? Did you see the stars that were out last night? I want to be just like you when I grow up! Can you please give me some seeds? I want "
                message_op = "I guess it's hard being an appleseed seller but I didn't bring that much money with me even!"
                message_angry = "I told my papa I want to be just like you when I grow up. He wasn't too happy about that..."
                message_neutral = "Did I ever tell you I want to be just like you when I grow up?"
                message_happy = "Wow! How did you get so nice? I want to be just like you when I grow up!"
                message_cancel = "Oh... okay. Bye " + mr_ms + "."
                message_item = "I was thinking, it would be nice for you to have some of these! For when you want to read a book at night! I'm definitely going to bring some with me when I'm an appleseed seller!"
            elif cust_index == 16:
                print("  _______")
                print(" /       \ ")
                print("|| ~    ~ |")
                print("[  :_ \ _:|")
                print("| |  c_|  |")
                print("|\_ /~ \ /")
                cust_name = "Elder Hawthorne"
                cust_item = "Deed"
                btrlo = 30
                btrhi = 50
                sslo = 90
                sshi = 130
                hap = hap_elder_hawthorne
                init_price_c = 1.2
                message_grt = "I've been in Green Town a long time now, my young friend. I've seen a lot of people come and go. Are you the kind of person who'll stay? Or are you one of them young'uns who can't seem to sit still? Let's hear your price for "
                message_op = "I ain't gonna stand for that."
                message_angry = "It just ain't like the good old days..."
                message_neutral = "It looks like you may be the reasonable type. Be careful in Venango now."
                message_happy = "I like you, young " + lad_lady + ". And believe me when I tell you I don't say that often."
                message_cancel = "Just like the rest of 'em. Can't seem to sit still."
                message_item = "Appleseed, come and sit down over here by me. I know you've been goin' around opening nurseries around these parts. I seen a lot of people come and go but I ain't never seen anyone do such a thing to help people like that. You're a mighty fine young " + lad_lady + ". When you're ready to open a nursery in Green Town, I'll give you some of my land. Here, have this."
            elif cust_index == 18:
                print("   ....")
                print(" :      \ ")
                print(":  === ==")
                print("C  - c_)-'")
                print("|\_ (–––)'")
                cust_name = "Town Beggar Popo"
                cust_item = "Glass Eye"
                btrlo = 20
                btrhi = 25
                sslo = 10
                sshi = 40
                hap = hap_town_beggar_popo
                init_price_c = 0.5
                message_grt = "The town gets bigger, the poor get poorer. The liars get stronger, the honest get weaker. Which one are you, Appleseed? Venango's a place where you're one or the other. You seem to know yourself pretty well. I'm sure you can spare me "
                message_op = "Who do you think I am? Councilman Pitts??"
                message_angry = "You ever WONDER why people buy your appleseeds? Because they PITY you, Appleseed! You're just like me but you think you're some kind of saint!"
                message_neutral = "You act like you're going around doing everyone a favor. We're all just cogs in a big machine, Appleseed. But at least you talk to me."
                message_happy = "Maybe you aren't as conceited as I thought you were..."
                message_cancel = "You can't run from me! You can't pretend I don't exist! You don't know it yet but you NEED me!"
                message_item = "You know I'm not mad like they say. I actually have a degree from Oxford. This is just the cog in the machine I decided I was gonna be. Have this. I found it, maybe you can make some use out of it."
            elif cust_index == 19:
                print("    _–––––_")
                print("   |       |")
                print("   |__––––_|")
                print("   |__––|><|_")
                print("  |_––––––––_|")
                print("  //  .  \ .\ ")
                print(" C  (   c_3  )")
                print(" |      \=/  |")
                print("/ \__      _/ \ ")
                cust_name = "Councilman Pitts"
                cust_item = "Upstanding Citizen Award"
                btrlo = 40
                btrhi = 60
                sslo = 150
                sshi = 170
                hap = hap_councilman_pitts
                init_price_c = 2.5
                message_grt = "Hello there my friend, I welcome you here to Venango! Don't let Popo get to you. As you know I'm a councilman of this county, and a very busy one too! I've got a lunch to go to in fifteen minutes! Can you give me a good price in a jiffy? I'd like "
                message_op = "I AM a councilman but that doesn't mean I live beyond my means, my friend."
                message_angry = "Your price is so high, it's given me a stomachache! And lunch is lamb chops too!"
                message_neutral = "Looks like you've come to your senses. Good day, Appleseed."
                message_happy = "That's what I'm talking about! I'll make sure that the policies surrounding fruit trees and nurseries will be favorable to you!"
                message_cancel = "You be careful about upsetting a councilman. I know people, you know."
                message_item = "You've turned out to be just the upstanding citizen I like to see in my county. You've earned this! Will you come to our next meeting to accept the award?"
            elif cust_index == 20:
                print(" ///||||\\\\ ")
                print(" __======_")
                print("[  ._ \ _.|")
                print("| (   _|  )")
                print("|\ \ -   /")
                cust_name = "Gravedigger Tehwehron"
                cust_item = "Wampum Bracelet"
                btrlo = 10
                btrhi = 40
                sslo = 80
                sshi = 110
                hap = hap_gravedigger_tehwehron
                init_price_c = 0.8
                message_grt = "Every day I walk over here with my trusty shovel and dig all day. A lot of them o' them are my own Indian brothers and sisters, come down with some illness. You start to wonder if God really meant all this to be. I plant a little appleseed on top of every one of 'em. This time I need "
                message_op = "Bah! You serious?"
                message_angry = "Bah! You settlers, always lookin' to make a profit off of the land and our people. Don't you understand?"
                message_neutral = "I like watching the apple trees grow. Pretty soon this grave ain't gonna be a grave at all, and I'll have nice juicy apples to eat!"
                message_happy = "I've been hearing stories about you, " + bro_sis + ". They say you've been good to them, even curing a sick person or two! And camping like we Indians do when we're on the road! I'll be! Haha!"
                message_cancel = "Bah! You settlers come here and sit on your porch, act like you've been here for as long as you know! Be gone now, I don't want to see you around these parts."
                message_item = "Here, my " + bro_sis + ". I make these myself when I got some time. There ain't many of these around no more, not like the old days. Have it as a token of my gratitude."
            elif cust_index == 21:
                print("  cccc__")
                print(" CCc/    \ ")
                print("CcC/__––––_\ ")
                print(" C|/ –    –|")
                print("  C  o  \ o'")
                print("   |    _\ |")
                print("   |\_ v  /")
                cust_name = "Baker Lila"
                cust_item = "Apple Danish"
                btrlo = 20
                btrhi = 40
                sslo = 30
                sshi = 40
                hap = hap_baker_lila
                init_price_c = 0.9
                message_grt = "Hi again, " + player_name + "! Everybody here in Venango seems to always be in a sour mood. That's why I make sweets and pastries... I like seeing people smile. I even give them out for free sometimes. But you wouldn't understand, would you? I'll have "
                message_op = "Now you wouldn't do that to me, would you?"
                message_angry = "It's hard to be happy when everyone around ignores you or tries to get something out of you."
                message_neutral = "Is it true that some towns won't let you built a nursery until they reach some sort of happiness? And you're trying to build one in Venango?"
                message_happy = "I'm always hoping my good deeds will someday pay off... that someone is watching. I'm finally starting to get a feeling that they are!"
                message_cancel = "What's a town if everyone's just looking out for themselves?"
                message_item = player_name + ", I don't think I ever told you that my most popular pastry is made with apples from your trees! I this one skinny, twisted tree out back that grows the most delicious fruits! Here, I baked some today!"
            elif cust_index == 22:
                print(" |\|\|\/|")
                print("|\\\\     /|")
                print("\\\\ ~    ~/")
                print("[  .  \ .'")
                print("|    c_\ |")
                print("| \ \__ /")
                cust_name = "Nurseryman Jon"
                cust_item = "Business Card"
                btrlo = 15
                btrhi = 25
                sslo = 300
                sshi = 420
                hap = hap_nurseryman_jon
                init_price_c = 0.8
                message_grt = "Howdy there, " + bro_sis + "! They say money don't buy happiness but I can't think of nothin' else that comes close! And I been hearin' people say you're practically givin' out seeds! I'd be shanked if I say the money I'm makin' ain't makin' me happier! Lemme hear your price for "  
                message_op = "Now ya gonna hit me with that ridiculous price, " + bro_sis + "?"
                message_angry = "'Makin' people happy'... Hah! If ya think you can live without feedin' yourself you're as mad as old Popo!"
                message_neutral = "Life's a game, " + bro_sis + "! With real winners and real losers! And the main character is yourself!"
                message_happy = "If you really are makin' a profit offa this price then I'll be shanked, " + bro_sis + "."
                message_cancel = "I ain't no nosy man but I gotta wonder if you even know the basics of runnin' a business!"
                message_item = "My " + bro_sis + "! Let me show you this newfangled thing some sellers are gettin' these days! They say this thing'll TRIPLE your sales! Check it out, I got one made for myself!"
     
            #print("happiness" + str(hap)) #

            btrlo = (btrlo * (hap ** 0.6)) // 1
            if btrlo <= 5: # barter absolute minimum
                btrlo = 5
            elif btrlo > 100:
                btrlo = 100
            btrhi = (btrhi * (hap ** 0.6)) // 1 # btr/hap coefficient - how much hap will affect btr range - the closer x is to 0, the closer btr will be to btr. The closer x is to 1, the closer btr will be to btr * hap
            if btrhi < btrlo:
                btrhi = btrlo
            elif btrhi <= 8:
                btrhi = 8
            elif btrhi > 100:
                btrhi = 100

            btr = random.randint(btrlo,btrhi)/100

            #print("btr before" + str(btr)) #
            
            #btr = btr - ((btr / 30) * round_index) # round hardness coefficient - determines by what percent each round will decrease btr
            
            #print("btr after" + str(btr)) #

            price_c = init_price_c * hap # happiness coefficient - how much hap will affect price_c. hap = 1 is neutral hap = 2 will double init_price_c hap = 0 will half init_price_c

            #print("price_c" + str(price_c)) #

            price_i = price_c * btr

            #print("price_i" + str(price_i))#
            
            price = price_i
            
            seed_sold = random.randint(sslo,sshi)
            
            print("\n" + cust_name + ": \"" + message_grt + str(seed_sold) + " appleseeds.\"")

            sale_made = None
            if seed_sold > seed_player:
                print("\nYou don't have enough seeds.")
                sale_made = False
            elif input("\nProceed with trade? (y/n) ") != "y":
                if input("Cancel trade? (y/n) ") == "y":
                    sale_made = False
            if sale_made == None:                    
                offer_count = 0
                total_offer = 99999
                while True:
                    print("\nYou have " + str(4 - offer_count) + " offer(s) left to make.")
                    total_offer_1 = offer_func(total_offer)
                    total_offer = total_offer_1
                    offer_count += 1
                    offer = total_offer / seed_sold
                    if offer <= price_i or total_offer <= price * seed_sold + 3: # leniency coefficient - if the offer is within x gold of the last offer, the sale will be made
                        final_price = total_offer
                        print(cust_name + ": \"That's a good price. I'll take them.\"")
                        while True:
                            if input("Sell " + str(seed_sold) + " seeds for " + str(final_price) + " gold? (y/n) ") == "y":
                                sale_made = True
                                break
                            else:
                                if input("Cancel trade? (y/n) ") == "y":
                                    sale_made = False
                                    break
                                else:
                                    continue
                        break
                    elif offer > price_c:
                        offer_count += 1
                        print(cust_name + ": \"" + message_op + "\"")
                    price = price_calc(price,price_c,offer,offer_count) # the price will be raised by a fraction of the amount x between (whichever is lower, the offer or the price ceiling) and the previous price. The amount x is divided into 4 sections then multiplied by the number of offers already made minus 1, resulting in a number 0/4 (after 1st offer), 1/4 (2nd), 2/4 (3rd), or 3/4 (4th) of x by which the price is raised. 
                    final_price = int((price * seed_sold) // 1)
                    if final_price == 0:
                        final_price = 1
                    print(cust_name + ": \"I'll pay you " + str(final_price) + " gold for these " + str(seed_sold) + " seeds.\"")
                    if offer_count >= 4:
                        print("This is your last chance!")
                    while True:
                        if input("Sell " + str(seed_sold) + " seeds for " + str(final_price) + " gold? (y/n) ") == "y":
                            sale_made = True
                            break
                        else:
                            if offer_count >= 4:
                                if input("Cancel trade? (y/n) ") == "y":
                                    sale_made = False
                                    break
                                else:
                                    continue
                            else:
                                break
                    if sale_made == None:
                        continue
                    else:                         
                        break

            if sale_made == True:
                gold_player += final_price
                seed_player -= seed_sold

                #print(str((final_price / seed_sold) / price_c)) #
                
                hap += add_hap(final_price,seed_sold,price_c) # happiness increaser coefficient - the ratio of price per seed to price ceiling x is taken (a number in between 0 to 1). A coefficient y is divided by x to produce the amount of happiness added after trade. 
                if hap < 0:
                    hap = 0.1
                elif hap > 2:
                    hap = 2
                print("\nYou sold " + str(seed_sold) + " seeds for " + str(int(final_price)) + " gold to " + cust_name + ".")
                if 0 <= hap < 0.5:
                    print(cust_name + ": \"" + message_angry + "\"")
                elif 0.5 <= hap <= 1.5:
                    print(cust_name + ": \"" + message_neutral + "\"")
                elif 1.5 < hap <= 2:
                    print(cust_name + ": \"" + message_happy + "\"")
                if hap == 2 and cust_item not in sack:
                    sack.append(cust_item)
                    print("\n" + cust_name + ": \"" + message_item + "\"")
                    print(" ––––––––––––––––––" + ("–" * (len(cust_item) + len(cust_name))))
                    print("| Received " + cust_item + " from " + cust_name + "! |")
                    print(" ––––––––––––––––––" + ("–" * (len(cust_item) + len(cust_name))))
                    print("You put " + cust_item + " in your sack.\n")
                    if cust_item == "Earthworms":
                        nurs_maint -= 25
            elif sale_made == False:
                hap -= 0.2 # happiness decreaser coefficient - determines the amount a canceled trade will take off from customer's happiness
                if hap <= 0:
                    hap = 0.1
                print("\nYou cancelled your trade with " + cust_name + ".")
                print(cust_name + ": \"" + message_cancel + "\"")
            if cust_index == 0:
                hap_farmer_jacob = hap
            elif cust_index == 1:
                hap_martha = hap
            elif cust_index == 2:
                hap_neighbor_pete = hap
            elif cust_index == 3:
                hap_farmer_goffe = hap
            elif cust_index == 4:
                hap_storekeeper_samantha = hap
            elif cust_index == 6:
                hap_angler_wyman = hap
            elif cust_index == 7:
                hap_young_arthur = hap
            elif cust_index == 8:
                hap_mill_operator_swatley = hap
            elif cust_index == 9:
                hap_mother_erwin = hap
            elif cust_index == 10:
                hap_orchard_keeper_stevens = hap
            elif cust_index == 12:
                hap_gardener_sherman = hap
            elif cust_index == 13:
                hap_jeremiah = hap
            elif cust_index == 14:
                hap_father_adam = hap
            elif cust_index == 15:
                hap_young_julia = hap
            elif cust_index == 16:
                hap_elder_hawthorne = hap
            elif cust_index == 18:
                hap_town_beggar_popo = hap
            elif cust_index == 19:
                hap_councilman_pitts = hap
            elif cust_index == 20:
                hap_gravedigger_tehwehron = hap
            elif cust_index == 21:
                hap_baker_lila = hap
            elif cust_index == 22:
                hap_nurseryman_jon = hap
                
            cust_index += 1 #######
                
        elif end_menu == "2":
            print("\nOpening sack...")
            for item in sack:
                print(item)
            while input("\nExamine item? (y/n) ") == "y":
                item_name = input("Enter item name: ")
                if item_name in sack:
                    if item_name == "Tin Cap":
                        print(" ________")
                        print("| \  –––")
                        print("|_____|")
                        print("\nIt's an old, beat up metal cap. You can also cook mush in it.")
                    elif item_name == "Spoon":
                        print("( )====")
                        print("\nGreat for eating mush. Also great for sowing appleseeds!")
                    elif item_name == "Town Map":
                        print(" ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ")
                        print("| ^^ ^^^ ^^^^ ^^ ^ ^^^^ ^^ ^ /   ___ /   ___________  / /   |")
                        print("| ^^^ ^ ^^^^ ^ ^^^ ^ _______|__/________/ _________ \/ /    |")
                        print("| ^ Longmeadow      / ___________________/         \ •|   ^ |")
                        print("|  ________________/ / ^^ ^ |  \            Venango | |  ^^ |")
                        print("|_/ ____• __________/ ^^^ ^  \  |  ^ ^^^ ^^^ County  \ \ ^^ |")
                        print("|__/    \ \          ^ ^^ ^^^ | | ^^^ ^^ ^^ ^^^ ^     | | ^ |")
                        print("|        \ \       ^^ ^^^ __ /  | ^ _____ ^^^ ^^ ^    | |   |") 
                        print("|         \ \        ^^ /   __ / ^ |•___ \ ^^^^ ^^    | |   |")
                        print("|          \ \        /   / ^^ Green Town \  ________/ /    |")   
                        print("|––––––     \ \      |  / ^^^^ ^^ ^^ ^^^ \ \/ ________/     |")
                        print("|       \    \ \_____|_|_   ^^ ^^^^ ^^^ ^ \  / ^^^ ^        |")
                        print("|         \   \__________ \  ^^^ ^  ______/ / ^^ ^^         |")
                        print("|–––        \       /  | \ \       / ______/           –––––|")
                        print("|    \        \   /   /   \ \_____/ /                /      |")
                        print("|      \        –   /      \•______/     –––––––––––        |")
                        print("|        \           \  Licking Creek  /                  ––|")
                        print("|          \           –––––––––––––––                  /   |")
                        print("| ^^^        ––––                           –––––––––––  ^^ |")
                        print("| ^^ ^^^          \  THE RIVER MUSKINGUM  /    ^^^^ ^^^ ^ ^ |")
                        print("| ^ ^^ ^^^^ ^^^     –––––––––––––––––––––    ^^^^ ^^ ^^^ ^^ |")
                        print(" ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– ")
                    elif item_name == "Old Jeans":
                        print(" _______")
                        print("| -|-|- |")
                        print("|_| l |_|")
                        print("|  / \  |")
                        print("|  | | _|")
                        print("|  | ||_|")
                        print("|  | |  |") 
                        print("|==| |==|")
                        print("\nThey are faded and patched all over. Someone used these well.")
                    elif item_name == "Pear Seeds":
                        print("____")
                        print("\==/    ,,,")
                        print("|__| , ,,,,,")
                        print("\nThey look like appleseeds, but they are pear seeds.")
                    elif item_name == "Longmeadow Lager":
                        print("  ==")
                        print("C/__\ ")
                        print("| LL |")
                        print("|____|")
                        print("\nSpecial homebrew made from wheat, barley, and fresh apples! It's sweet and tangy.")
                    elif item_name == "Farmer Goffe's Axe":
                        print(" /-\ ")
                        print("\\\__\ ")
                        print(" \\\ ")
                        print("  \\\ ")
                        print("   \\\ ")
                        print("    \\\ ")
                        print("\nA small and sturdy axe with a beautiful maple handle.")
                    elif item_name == "Fancy Letter Set":
                        print(" ____")
                        print("_\   \ ")
                        print("\ \___\  =")
                        print(" \___\  |_| ====-")
                        print("\nParchment, a shiny black pen, and a bottle of ink from Samantha in Longmeadow. Remember to write her back!")
                    elif item_name == "Fishing Fly":
                        print(" |")
                        print(" ,")
                        print(" J\\ ")
                        print("\nMade out of a hook and a colorful feather... Wait, is that an appleseed in the middle?")
                    elif item_name == "Strange Pebble":
                        print("(//)")
                        print("\nA smooth, greenish pebble with stripes across it.")
                    elif item_name == "Wooden Top":
                        print("__N__")
                        print("\___/")
                        print("  V  ")
                        print("\nA small top carved out of hazelwood. It used to belong to a friend of Swatley's.")
                    elif item_name == "Nesting Dolls":
                        print(" ( )")
                        print("(***)   0   o")
                        print(" \_/   (*)  0  8")
                        print("\nA rare, imported item. Inside each intricately painted doll is another one just like it, but smaller.")
                    elif item_name == "Earthworms":
                        print("(_)")
                        print("|  |  ~~ ~")
                        print("|__| ~ ~ ~~ ~")
                        print("\nA tin can filled with soil and wriggling worms. It has reduced nursery maintenance dues by 25 gold.")
                    elif item_name == "Fennel":
                        print("_\\\|/")
                        print("–_\\\|")
                        print("   \\\ ")
                        print("    ==")
                        print("     \\\ ")
                        print("\nApparently this is some of Gardener Sherman's \"BEST GOTDAMN\" fennel. Grind it into a medicine to cure stomach ailments.")
                    elif item_name == "Mango Seeds":
                        print("_____")
                        print("\===/")
                        print("|   |   /| /\  /|")
                        print("|___|  |/  \/ |/  ===")
                        print("\nThey're stringy and as big as the palm of your hand. They won't grow here.")
                    elif item_name == "Blessing":
                        print("\nYou received a blessing from Father Adam: 'May your travels be fruitful, your search be fulfilled, and your relationship to God be ever close!'")
                    elif item_name == "Candles":
                        print(":  :  :")
                        print("|| || ||")
                        print("|| || ||")
                        print("|| || ||")
                        print("\nThey're some nice beeswax candles. It looks like Julia made them herself!")
                    elif item_name == "Deed":
                        print(" _______")
                        print("( ) --- )")
                        print("  | --- |")
                        print("  | --$ |")
                        print("  |_____|")
                        print("\nEntitles you to **** acres of Elder Hawthorne's land! It has reduced the cost of establishing a nursery in Green Town by 600 gold.")
                    elif item_name == "Glass Eye":
                        print("  __")
                        print("/ .  \ ")
                        print("(•) . |")
                        print("\ __./")
                        print("\nA dirty stone eye with a brown pupil. How did someone manage to lose their glass eye?")
                    elif item_name == "Upstanding Citizen Award":
                        print("  _n_")
                        print("  ( )")
                        print("  \\:)")
                        print(" _|||_")
                        print("|_____|")
                        print("\nAn award given to you by the County of Venango. It's a polished pewter figurine of a plump man. He looks a bit like Councilman Pitts. Too bad you don't have a desk to put it on.")
                    elif item_name == "Wampum Bracelet":
                        print(" _=====_")
                        print("'-=====-'")
                        print("\nA intricate work of Mohawk art, made from white and purple beads carved from shell. I must have taken Tehwehron a long time to drill those tiny holes.")
                    elif item_name == "Apple Danish":
                        print(" _ _ _ _")
                        print("( \ \•\ \ ")
                        print(" \_)_)_)_)")
                        print("\nA buttery, flaky pastry straight from the oven... made from your very own apples! What a treat!")
                    elif item_name == "Business Card":
                        print("________")
                        print("\ 0 --- \ ")
                        print(" \_______\ ")
                        print("\nIt's a small piece of parchment stamped with Jon's beaming face and his address. You can see at least 10 of Jon's sparkling white teeth.")
                else:
                    print("Item unavailable.")
            else:
                continue
        elif end_menu == "3":
            if location == "Longmeadow":
                print("\nYou already have a nursery in Longmeadow.")
                continue
            elif location == "Licking Creek":
                if nurs_lc == True:
                    print("\nYou already have a nursery in Licking Creek.")
                    continue
                else:
                    cost_gold_nurs = 1200###
                    cost_seed_nurs = 400###
            elif location == "Green Town":
                if nurs_gt == True:
                    print("\nYou already have a nursery in Green Town.")
                    continue
                else:
                    if "Deed" in sack:
                        cost_gold_nurs = 2000
                    else:
                        cost_gold_nurs = 2600###
                    cost_seed_nurs = 600###
            elif location == "Venango County":
                if nurs_vc == True:
                    print("\nYou already have a nursery in Venango County.")
                    continue
                else:
                    cost_gold_nurs = 4200###
                    cost_seed_nurs = 1000###
            if input("\nUse " + str(cost_gold_nurs) + " gold and " + str(cost_seed_nurs) + " seeds to establish a nursery in " + location + "? (y/n): ") == "y":
                if location == "Licking Creek" and hap_angler_wyman + hap_young_arthur + hap_mill_operator_swatley + hap_mother_erwin + hap_orchard_keeper_stevens < 6.5:
                    print("\nLicking Creek is not ready to accept your nursery. You must make the residents happier before a nursery can be established.")
                elif location == "Green Town" and hap_gardener_sherman + hap_jeremiah + hap_father_adam + hap_young_julia + hap_elder_hawthorne < 6.5:
                    print("\nGreen Town is not ready to accept your nursery. You must make the residents happier before a nursery can be established.")
                elif location == "Venango County" and hap_town_beggar_popo + hap_councilman_pitts + hap_gravedigger_tehwehron + hap_baker_lila + hap_nurseryman_jon < 6.5:
                    print("\nVenango County is not ready to accept your nursery. You must make the residents happier before a nursery can be established.")
                if cost_gold_nurs >= gold_player:#####
                    print("\nYou do not have enough gold. You need more than " + str(cost_gold_nurs) + " gold to establish a nursery here.")
                elif cost_seed_nurs >= seed_player:
                    print("\nYou do not have enough appleseeds. You need more than " + str(cost_seed_nurs) + " seeds to establish a nursery here.")
                else:
                    print("\nEstablishing nursery...")
                    gold_player -= cost_gold_nurs
                    seed_player -= cost_seed_nurs
                    print("Congratulations! You established a nursery in " + location + "! With regular maintenance, it will provide you with gold and plentiful seeds every time you return.")
                    if location == "Licking Creek":
                        nurs_lc = True
                        nurs_maint += 100 ###
                    elif location == "Green Town":
                        nurs_gt = True
                        nurs_maint += 150 ###
                    elif location == "Venango County":
                        nurs_vc = True
                        nurs_maint += 200 ###
                    print("You are now expected to pay " + str(nurs_maint) + " gold before entering each town to keep your nurseries healthy and productive.")
                    if nurs_lc == True and nurs_gt == True and nurs_vc == True:
                        print("\n –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
                        print("|              * C O N G R A T U L A T I O N S ! *              |")
                        print("|                                                               |")
                        print("|   You have achieved your dream of establishing nurseries in   |")
                        print("|        all three of Longmeadow's neighboring towns!           |")
                        print("|                                                               |")
                        print("|  You have brought happiness and health to those you have met, |")
                        print("|        and for that you will forever be remembered as         |")
                        print("|                the Great " + player_name + " Appleseed!" + (" " * (26 - len(player_name))) + "|")
                        print("|                                                               |")
                        print("|          __n              0                                   |")
                        print("|         |__'\_––____–––––//|_  •••••••       _0_              |")
                        print("|            \  ||––––)––––||_|_•••••••••_   |/\ /\•            |")
                        print("|             |||–––|| \   L/  \LLLLL/  \|   | |||  •••         |")
                        print("|             |||  |||      \__/     \__/    | |||  \_/         |")
                        print("|                                                               |")
                        print(" –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
                        if input("\nWould you like to continue the game? (y/n): ") != "y":
                            game_over = True
                            break
        else:
            print("\nInvalid action")




