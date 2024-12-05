# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    default chieftain_caste = False
    default warrior_caste = False
    default peasantry_caste = False
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_palace with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show mc at left with dissolve
    narrator "Welcome to Swaza, we're here to find out who you are in this society and how it scuplted you into the leader you are today"
    narrator "Which caste where you born into?"
    menu:
        "Motho Kosi, the Warrior Caste":
            $ warrior_caste = True
            narrator "You are a warrior."
            narrator "Your father, Dumelo fought for the Royal Magnia Army, not for the love of the colonizer but the heavy purse of gold they offered."
            narrator "Your mother, Mpule gave birth to you in 1925, under the colonial yolk of the Magnian Empire."
            narrator "When you were only five, your parents chose to move to the capital, your father had been called to the Simbala after growing unrest."
            narrator "You saw students protesting in the city, lead by a man named Sese Moseki, an avid socialist & anti-colonialist."
            jump uprising
        "Mmunzi, the Chieftains":
            $ chieftain_caste = True
            narrator "You are a cheiftain's son" 
            narrator "Your father, Dumelo was the Chief of Mjwana, giving you great privilege and a title as the eldest son. You lived in the Royal Quarters of the town, with your small group of servants at hand."
            narrator "You saw how your father lead the people, you sat in every (Kgotla) Village Meeting; watching as the elders deliberated and decided issues in the village."
            narrator "You one day hoped to be like your father and become Chief, he sent you off to learn in the local Magnian Missionary School of Mjwana."
            narrator "It was difficult adjusting to the new language, Magnian was the sole curricular language, those who spoke Swazan in class were punished severely."
            narrator "Swaza was still the language you spoke to your friends, family and village subjects. Though you didn't stay long, after Sese Moseki, an outspoken Socialist from the Morui was arrested."
            narrator "The village was swept with rage, the peasants in the village rose up against the colonial government. The Morui Uprising had begun."
            narrator "Your father placed you under a blanket in a donkey cart and sent you off through the Imperial Highway, it took you fifteen days but you got to the gates of the capital."
            narrator "Upon reaching the capital, soldiers on high alert thoroughly searched through the cart. A young man found you but realised your birthright and gave you a conspiratorial wink."
            narrator "The soldier announced the cart was just full of fruit and let you roll into the city."
            narrator "Just because you were in the capital, didn't absolve you. You kept your head down while living in the city, taken in by a young lawyer by the name of Louise Sobotho"
            narrator "She introduced you to the fledgling movement of lawyers, teachers and students known as the Swaza National Front, you eagerly joined."
            jump uprising
        "Morui, the peasantry":
            $ peasantry_caste = True
            narrator "You are a peasant's son."
            jump uprising
        
#EXAMPLE OF IF STATEMENT LABEL REMREMBER TO REMOVE LATER         
label uprising:
    default peasant_support = False
    default peasant_dismiss = False
    default anti_socialist = False

    if warrior_caste == True:
            narrator "You are a warrior."
    elif chieftain_caste == True:
        narrator "You are a cheiftain's son" 
    else: 
        narrator "You are a peasant's son."    


#TRY TO PUT THESE LINES AS NON IF STATEMENT!!!!        
    narrator "Your loyalties were tested during the Uprising, struggling to decide who was right your heart went with..."
    menu:
        "The Peasantry":
            $ peasant_support = True
            narrator "You sided with the peasantry"


        "Didn't support the violence":
            $ peasant_dismiss = True
            narrator "aa"
        "Happy to see Moseki locked up":
            $ anti_socialist = True
            narrator "aas"

label inaugaration:
    #Inaugaration Day

    pm "I walk up the stairs of the Royal Palace, a structure that has stood the test of time; to accept my role as Prime Minister of the Royal Kingdom Of Swaza."

    show mosegi at center

    pm "I lay eyes on the king, he awaits with an entrourage, atop a flat, stoney platform overlooking the serence capital city of Simbala." 

    pm "The King wears his Royal Blue shawl lined with a golden selvedge, which drapes over his shoulders. Beneath is an golden lion decorated thobe reaching his feet, least ignorable is the large crown atop his head. A circular, golden crown with a maned lion's face edged into it." 
    
    hide mosegi

    show prince at center

    pm "First and most significant, the fresh faced young heir Prince Regent Tsimba Morogosi (Sim-ba), only just becoming a man, he looks determined to see through the ceremony, his faced marked with a stern, royal duty."

    pm "He adorns a blue shawl with white selvedge, a small silver diadem with small pebble-sized rubies patterned neatly in the royal crown."

    hide prince

    show schief at left 

    show centchief at center

    show nchief at right 

    pm "Beside the young prince are the King's Royal Advisors: The Ga Raro Mmunzi (Three Big Chiefs) of Swaza. The three closest advisors of the King since the Brothers War." 

    hide schief

    hide centchief

    hide nchief

    show cyril at left with moveinleft

    pm "Next to them is the former Prime Minister Cyril Zamaranda, a well known 'Shieldsman', a little name we like to call my colleagues in the Swaza National Front."

    pm "Zamaranda beams at me as he passes on the legacy of his party, in his hand he holds the Ministerial Tassel." 
    
    pm "a Golden Ball atop a pole made of copper, wrapped in the skin of a cheetah. Sprouting from the golden ball are hairs from the mane of a lion wedged into small holes made piercing the golden ball."

    pm "The Tassel represents a long standing Swaza tradition of Head Cheiftain established over 200 years ago. But for now I'll take the name 'Prime Minister'."

    hide cyril

    show mpule

    pm "Beside Zamaranda is Chief Justice Mpule Mogotsi (Suh-boo-two), the stern, steely Chief Justice and strict royalist, she looks elated to even be in the king's presence. Despite her wide smile, her eyes dagger me with suspicion."

    hide mpule

    show taupic

    pm "Last, but definately not least is the King's Appointed Chief of the Armed Forces, Zephaniah Tau." 
    
    pm 'His distinctive short fade is as distinctive as his military record, the man who signle-handedly defended our country from those Somfosan Bulldogs during the Qazid War; depsite what he may be accused of.'

    pm "Or so the news would have you believe." 
    
    pm "While Tau is a respected military man he too will die for his King, rumours spread about his involvement in our first Prime Minister's resignation, but nothing has been proven yet." 

    hide taupic

    show mosegi at right with moveinright

    show president at left with moveinleft

    pm "As is custom, I walk towards the King first. He outstretches his hand, it is time for the ceremony to begin with the 'Dumela Kgo', the royal greeting."
    
    pm "in response I get down onto one knee, pressing my head against his knuckles for five seconds before lifting myself again."

    kng "Prime Minister Mjwana.  Welcome to the Blue Palace." 
    
    kng "I've welcomed so many leaders in the past, yet I am happy to see one of our own lead the country. Not to mention without much fuss, couldn't say as much for our neighbours."

    pm "Many thanks, your highness. I am humbled in your presence and in the presence of God."

    kng "Mena to that! I hope to see that my government brings my subjects prosperity and peace."

    pm "That I shall guarantee, your Highness."

    kng "What a momentous occasion and to be joined by my son and heir for the first time as well. He shall observe the long standing customs of our people and becoming as wise a King as I."

    pm "It certainly is a wonderful occasion, your majesty and twice as such with the presence of our young prince."

    pm 'I shuffle towards the Prince Regent.'

    tsh "It is a pleasure to meet you, Prime Minister. I hope you're as ready for the responsibility of this nation as I am."

    pm "I couldn't have said it better myself, Your Princeship, I look forward to my five years and the challenges and success they will bring."

    tsh "More success than challenges, I hope (!)."

    pm 'The comment got a light chuckle out of myself and the entourage.'




label game_start: 
    "Hey"
    
    
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
