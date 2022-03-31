#
# The DatingSite.py file will contain the source code for my creative project.
#

# The main() function will control the flow of the program.
# Parameters: None
# Returns: None

def main():

    # Run the program.

    welcome()
    while(True):
        menu()

# The welcome() function will print the welcome message.
# Parameters: None
# Returns: None

def welcome():

    # Show the welcome prompt.

    print('\n-----------------------------------')
    print('Welcome to Tinder for the Olympians')
    print('-----------------------------------')

# The menu() function will allow the user to navigate the application.
# Parameters: None
# Returns: None

def menu():

    # Print options.

    while(True):
        print('\nPlease select one of the following options:')
        print('(0) Logout')
        print('(1) Show Male Profiles')
        print('(2) Show Female Profiles')
        print('(3) Show Messages')
        print('(4) Show Breaking News')
        choice = input()

        # Validate user input.

        try:
            choice = int(choice)
        except ValueError:
            print('Choice must be a number!')
            continue
        if choice > 4 or choice < 0:
            print('Choice must be a number between 0 and 4!')
            continue
        break

    # Navigate to the corresponding function.

    if choice == 0:
        goodbye()
    elif choice == 1:
        males()
    elif choice == 2:
        females()
    elif choice == 3:
        messages()
    else:
        news()

# The goodbye() function will print the exit message and end the program.
# Parameters: None
# Returns: None

def goodbye():

    # Print the exit message and end the program.

    print('\nThank you for using Tinder for the Olympians!')
    exit()

# The males() function will show the profiles for the male Olympians.
# Parameters: None
# Returns: None

def males():

    # Set up data.

    profiles = {
        'Zeus' : {
            'job' : 'Prime Minister',
            'hobbies' : ['Meeting Young Women', 'Winning', 'Being Powerful'],
            'bio' : 'To all the young and pretty girls: send me a message if you are looking for the night of your life! I am the one and only Zeus! My mansion is the size of a mall! I have so many unused supercars that they are starting to gather dust! I used to be the CEO of OlympianAir (an airline company) until I became the ruler--I mean, leader--of this country! To anyone else: do not get in my way or you will be destroyed with l(ightning)awsuits!'},
        'Hades' : {
            'job' : 'CEO of the Pluto Casket Company',
            'hobbies' : ['Staying Home', 'Gardening', 'Being Labelled as Evil (🤦)'],
            'bio' : 'Hello, my name is Hades. I am the CEO of the Pluto Casket Company, the leading global coffin designers. We also specialize in funeral services for loved ones. When I am not working (which is never) I like to spend time at home with my dog. I am married but my wife will not be home for a few months. I also enjoy gardening. I have many different types of vegetation, my favourite of which, my pomegranate trees. I also have pent up resentment for Tinder as they keep banning my profile because I am supposedly "evil".'},
        'Poseidon' : {
            'job' : 'Marine Biologist',
            'hobbies' : ['Swimming with the Dolphins', 'Sea Environmentalist', 'Global Warming'],
            'bio' : 'I like the ocean and sea creatures more than I like people. When I am not working, I enjoy spending time with my doplhins in the sea. I love advocating for sea life. In sercret, I am a supporter of global warming. My love for the ocean is so great, that I would have global warming speed up so that the entire world is nothing but ocean!'},
        'Apollo' : {
            'job' : 'Doctor',
            'hobbies' : ['Musician', 'Poet', 'Archer'],
            'bio' : 'Hey there girls/boys! You might be wondering who this young and handsome figure is! It is none other than I, Apollo! I used to be a doctor, but now my son took over my position. This gives me more time to play my lyre. I also write poetry when I feel bursts of inspiration! Every now and then, you will see me at the nearby archery range. On another note, you might hear about my last tragic relationship. I think it is best if we ignore that. Send me a text if you think you are the one for me!'},
        'Hephaestus' : {
            'job' : 'Mechanic',
            'hobbies' : ['Inventing', 'Programming', 'Playing with Lego'],
            'bio' : 'My name is Hephaestus. I work as a mechanic and designer for Tesla. In my free time, I enjoy inventing new products, developing software, and building amazing Lego figures! I have 73 patents to my name and I am aiming for 100. When I was a child, my parents "dropped" me from the stairs. I am in a loveless marriage and my wife enjoys cheating on me. I have a limp, I am fairly ugly, and no one ever appreciates me (except my android servant I created). I think real beauty is on the inside.'},
        'Ares' : {
            'job' : 'Military General',
            'hobbies' : ['Working Out', 'Bullying Others', 'Getting Into Bar Fights'],
            'bio' : 'I am Ares. I enjoy torturing other people so I became a military general. Using my high position, I try and convince Zeus (my boss) to invade other helpless and defenseless countries. I like to work out and I have terrible gym ettiquite. For instance, just last week, I watched a kid struggle to finish his bench press rep. He was calling for help, but I just watched and laughed! Oh also, you do not want to pick a fight with me.'},
        'Hermes' : {
            'job' : 'Mailman',
            'hobbies' : ['Gossiping', 'Hustling (Side Businesses)', 'Magic'],
            'bio' : 'Hey there! I am your local mailman, Hermes! I love to gossip and spread rumors about other people! If you forgot to pay your electricity bill for the month, the entire neighbourhood will know, trust me! On the weekends, I buy and sell products on eBay. I flip old and broken products and sell them for regular price. It is not a scam, it is just good marketing. I also love to play tricks and pranks on my friends. For that reason, I learned to do magic!'},
        'Dionysus' : {
            'job' : 'Casino Owner',
            'hobbies' : ['Partying', 'Gambling', 'Live Theatre'],
            'bio' : 'Hey there ladies and gentlemen! If you want an unforgettable time (on second thought, you might not remember in the morning), send me a message! I own a Olympian Grand casino in Las Vegas. I also have a couple of (il)legal side businesses where I produce and sell moonshine and all sorts of other reacreational material! I love to party and I have terrible spending habits. In fact, I am 6 figures in debt. I am also an avid fan of live theatre! Whenever I am sober (who am I kidding, I am never sober!), I enjoy watching plays and live events. The new Marvel movies just cannot keep up.'}}

    # Show options to select a profile.

    while(True):
        print('\nSelect a profile from below, or press "-1" to exit.')
        i = 0
        print('{:<3}{:<20}'.format('#', 'Name'))
        for name in profiles.keys():
            print('{:<3}{:<20}'.format(i, name))
            i += 1
        choice = input()

        # Validate user input.

        try:
            choice = int(choice)
        except ValueError:
            print('Choice must be a number!')
            continue
        if choice < -1 or choice > 7:
            print('Choice must be a number between -1 and 7!')
            continue
        if choice == -1:
            return
        break

    # Print profile information.

    print('\nYou are viewing the profile for {}.'.format(list(profiles.keys())[choice]))
    print('\nOccupation: {}'.format(list(profiles.values())[choice]['job']))
    print('Hobbies: {}'.format(', '.join(list(profiles.values())[choice]['hobbies'])))
    print('Biography: {}'.format(list(profiles.values())[choice]['bio']))
    input()

# The females() function will show the profile for the female Olympians.
# Parameters: None
# Returns: None

def females():

    # Set up data.

    profiles = {
        'Hera' : {
            'job' : 'First Lady',
            'hobbies' : ['Spying on Zeus', 'Wedding Planner', 'Etsy Business'],
            'bio' : 'Please do not message me. I am not interested in a date. I am faithfully married to my husband Zeus. However, I fear he is not faithfully married to me. Quite frankly, I am only here to spy on him. Usually, I hire private investigators to do the dirty work, but they are all terrible at their jobs. If you are the girl currently having an affair with Zeus, mark my words, I will do everything in my power to ruin your life. When I am not grumpy at my husband, I plan weddings for couples. I also have an Etsy business where I sell cow-themed merchandise.'
        },
        'Demeter' : {
            'job' : 'Farmer',
            'hobbies' : ['Gardening', 'Environmental Activism', 'Babysitting'],
            'bio' : 'My name is Demeter. I work as the head of a farm because I have a passion for growing things! My favourite crop to grow is wheat. I also have a beautiful garden. My favourite flower is the poppy! When I am not outside with nature, I love to spend time with my daughter. Unfortunately, she is married and I do not get to see her often. I will be quite honest, I am not a fan of her husband. I also enjoy babysitting children of my friends when they are busy.'
        },
        'Hestia' : {
            'job' : 'Nanny',
            'hobbies' : ['Spending Time with Family', 'Cooking', 'Knitting'],
            'bio' : 'To be quite honest, I did not know this was a dating site. I thought it was more like Facebook, where I could spend time with my amazing family and see what everyone is up to! I am a pacifist by nature, and I work as a full-time nanny. I love spending time with children, even if they can be quite a burden. I like to cook for my loved ones and love to knit everyone sweaters for Christmas!'
        },
        'Artemis' : {
            'job' : 'Feminist YouTuber',
            'hobbies' : ['Hunting', 'Animal Rights Activism', 'Camping'],
            'bio' : 'I signed up for a Tinder account to promote asexualism and feminism. Follow my YouTube channel: @ArtemisHunts for more info! I love to talk about women empowerment and animal rights! I am a hunter, but only if strict ethical conditions are met. I love spending time in the wilderness. In fact, I am the winner of the last season of Outdoor Survival! In that reality show, a group of people were thrown into the middle of the woods to survive, and I came out on top! Send me a message to learn more!'
        },
        'Athena' : {
            'job' : 'Historian',
            'hobbies' : ['Chess', 'Writing', 'Podcast'],
            'bio' : 'Hello, everyone! My name is Athena. Currently, I work as a historian for the national museum. I chose this career because I am passionate about learning new things! In my youth, I was the national chess champion. I am still up for a game anytime. My last job was working as the Minister of National Defense for my father, Zeus. I am also the best-selling author of "Thinking Fast", an award winning self-help book! In my spare time, I invite speakers onto my podcast where we talk about all sorts of topics!'
        },
        'Aphrodite' : {
            'job' : 'Instagram Model/Influencer',
            'hobbies' : ['Going Out', 'Fashion Designing', 'Photography'],
            'bio' : 'Hey guys! I am the one and only Aphrodite. Supermodel, businesswoman, brand ambassador, makeup artist, etc. I mean, is there anything I do not know how to do? Make sure you follow my Instagram, Snapchat, YouTube, Twitter, and everything else at @Aphrodite for more amazing content! I love to go out to fancy new restaurants and clubs. I have also designed a handful of the next trends (not to brag or anything). I really think photography is my calling because I love taking photos almost as much as I love being in them!'
        }}

    # Show options to select a profile.

    while(True):
        print('\nSelect a profile from below, or press "-1" to exit.')
        i = 0
        print('{:<3}{:<20}'.format('#', 'Name'))
        for name in profiles.keys():
            print('{:<3}{:<20}'.format(i, name))
            i += 1
        choice = input()

        # Validate user input.

        try:
            choice = int(choice)
        except ValueError:
            print('Choice must be a number!')
            continue
        if choice < -1 or choice > 5:
            print('Choice must be a number between -1 and 5!')
            continue
        if choice == -1:
            return
        break

    # Print profile information.

    print('\nYou are viewing the profile for {}.'.format(list(profiles.keys())[choice]))
    print('\nOccupation: {}'.format(list(profiles.values())[choice]['job']))
    print('Hobbies: {}'.format(', '.join(list(profiles.values())[choice]['hobbies'])))
    print('Biography: {}'.format(list(profiles.values())[choice]['bio']))
    input()

# The messages() function will show the user their messages.
# Parameters: None
# Returns: None

def messages():

    # Show the messages.

    while(True):
        print('\nSelect a message from below or press "-1" to exit.')
        print('(0) Message from Zeus')
        print('(1) Message from Hera')
        print('(2) Message from Apollo')
        choice = input()

        # Validate user input.

        try:
            choice = int(choice)
        except ValueError:
            print('Choice must be a number!')
            continue
        if choice < -1 or choice > 2:
            print('Choice must be a number between -1 and 2.')
            continue
        if choice == -1:
            return
        break

    # Show the corresponding message.

    message = [
        'You charismatic girl. Definitely worthy of my love. All of your exes are lucky to have been in a relationship with you. I will protect you and provide you with great luxuries. For I am the king of this nation! I have more money than you could count! More power and status than anyone!',
        'Unless I am mistaken, you are having an affair with my husband. Did you think I would not find out? I know his tricks and schemes. You best break it off with him, or else I will have someone break your bones.',
        'Hey there! I saw your profile and thought you were cute. Some tell me that I can see into the future. Well, I prophesize you and me on a romantic date. I know I have bad history with relationships, but trust me, this time will be different.']
    print('\n{}'.format(message[choice]))
    input()

# The news() function will allow the user to access the recent Tinder headlines.
# Parameters: None
# Returns: None

def news():

    # Show the headlines.

    while(True):
        print('\nPick a headline from below to read more or press "-1" to exit.')
        print('(0) Zeus Scandalous Affair With Young Girl! Hera\'s Terrible Wrath!')
        print('(1) Apollo\'s String of Doomed Relationships Adds Another Lover to its List')
        print('(2) Hephaestus Catches Wife Cheating!')
        choice = input()

        # Validate user input.

        try:
            choice = int(choice)
        except ValueError:
            print('Choice must be a number!')
            continue
        if choice < -1 or choice > 2:
            print('Choice must be a number between -1 and 2.')
            continue
        if choice == -1:
            return
        break

    # Show the corresponding story.

    stories = [
        'BREAKING NEWS: Our sources tell us that Zeus was having an affair with a young girl named Io! It seems as though she was reluctant to participate in the scandal but Zeus beguiled her with his power and money to the point where she had no choice! However, Zeus needs to fear no legal persecution. His legal defense team has fought off countless charges in the past, and this is no different. What\'s more, our sources tell us that his wife Hera found out and tortured the young girl! From what we know, Zeus and Io were at a five-star hotel, but Hera found out! It looks like she has hired private investigators to follow Zeus around. When she entered the hotel room, Zeus, who realized she was coming, hid Io in the bedroom closet. Hera ordered one of her bodyguards to shoot their weapon through the closet unless Zeus confesses the truth! After a few tense seconds, Zeus gives in. He begs his wife to let Io go, and Hera abides, as long as Zeus promises not to cheat on her again. The couple returned to their secluded mansion, and Io, received many gifts from Zeus, as an apology for his wife\'s wrath. - Source: Ovid',
        'BREAKING NEWS: Poor Apollo adds another heartbreak to his list of doomed relationships! Just recently, Apollo was known to be intimate with a man named Hyacinthos. But yesterday, their relationship ended in tragedy, after Hyacinthos ended up in the hospital. Our sources say that the (ex) couple were out in the field playing discus. In fact, Apollo was teaching Hyacinthos to throw the discus. As Apollo threw the discus up into the air, a strong burst of wind altered the discus\' flight and struck Hyacinthos in the back! Apollo rushed him to a hospital and he suffered a direct hit to his upper spine. Unfortunately, this incident left him paralyzed from the neck down. Despite Apollo\'s great experience working in the hospital, he could not help his beloved. The last words Hyacinthos told Apollo was that he never wants to see him again. Ouch! This comes just after Apollo\'s previous relationship with Daphne, where she changed cities to get away from him as she couldn\'t stand him! Poor Apollo! - Source: Lucian',
        'BREAKING NEWS: The world-famous engineer, Hephaestus, caught his supermodel wife cheating! What\'s more, she didn\'t cheat on just anyone. It was the military general Ares! Sources say this was not a one-time affair, but had been going on for quite some time. When Hephaestus was forced to work late at the Tesla factory, Aphrodite and Ares would be spending the night together, in his bed! Quite scandalous! One day, their neighbour Helios caught Ares leaving the house in the morning and told Hephaestus of the situation. Hephaestus, filled with seething rage, designed tiny micro cameras, almost invisible to the naked eye, and placed them around his house. He told his wife that he was going to be working late that day. To no one\'s surprise, Ares and Aphrodite decided to spent the evening together. Later that night, Hephaestus showed up to catch his wife red-handed! Looking for vengeance, Hephaestus took the clips recorded by the camera and posted it all over the internet in an effort to smear the reputations of Aphrodite and Ares. To his dismay, this only increased Aphrodite\'s popularity. Hephaestus, still in love, could not bare to file for divorce. - Source: Homer']
    print('\n{}'.format(stories[choice]))
    input()

main()