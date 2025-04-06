"""
    Auxiliary file for 'ternary_operator-2.py' for better organization.
"""
def check_age_majority():
    print("""\n >>> Check Age Majority <<<
Welcome to the age majority checker! This version has 20
funny easter-eggs that you can find, see if you can guess
their numbers to unlock their special messages!
""")

    while True:
        user_input = input("Enter your age: ".strip())
        try: 
            age = int(user_input)
            break
        except ValueError:
            print("❌ Please, enter a valid age!")

    status = "an adult" if age >= 18 else "a minor"

    match age:
        case _ if age < 0: 
            print(f"{age} is a...wait, what? This person wasn't even born! ❓⁉️")
        case 0:
            print(f"{age} is {status}. Just born? Welcome to the world, little one! 👶🍼")
        case 1:
            print(f"{age} is {status}. Only 1 year old? That's adorable. 🥺")
        case 3:
            print(f"{age} is {status}. 3️⃣  A true toddler trinity. Half chaos, half giggles.")
        case 5:
            print(f"{age} is {status}. Still in the finger painting phase, huh? 🎨")
        case 7:
            print(f"{age} is {status}. 🍀 Lucky number seven! You must have magical powers!")
        case 18:
            print(f"{age} is {status}. 🗳️ Officially an adult (sort of). Time to pay taxes and question your life choices!")
        case 25:
            print(f"{age} is {status}. 🧠🍳 Your brain just finished cooking. Welcome to full sentience!")
        case 50:
            print(f"{age} is {status}. 🕺🪩  Half a century! Cue the disco ball and dad jokes.")
        case 42:
            print(f"{age} is {status}. 🧠 42...the answer to life, the universe, and everything.")
        case 69:
            print(f"{age} is {status}. 😏 Nice.")
        case 100:
            print(f"{age} is {status}. 🎉 A century! You've seen some things, haven't you?")
        case 130:
            print(f"{age} is {status}. 🧙 Are you a wizard? That seems...unlikely.")
        case 300:
            print(f"{age} is {status}. 👽 Are you sure you're from this planet?")
        case 420:
            print(f"{age} is {status}. 🔥 Blaze it? Just kidding! That's probably a typo...")
        case 2011:
            print(f"{age} is {status}. 😴 Hey, you. You're finally awake 😯. You were trying to cross the border, right? Walked right into that Imperial ambush ⚔️, same as us, and that thief over there. 🥷")
        case 1337:
            print(f"{age} is {status}. 💻 Leet detected. Hacker vibes intensifies! 🔥")
        case 9001:
            print(f"{age} is {status}. 🔥 IT'S OVER 9000!!!")
        case 9999:
            print(f"{age} is {status}. ⚔️   Final boss level unlocked. *Vordt of the Boreal Valley starts playing*")
            # Might use that to make a pygame later u.u
        case _:
            print(f"{age} is {status}.")


def check_even_odd():
    import random

    print("""\n--- Even or Odd Numbers ---
This version contains a lot of random responses, try it
multiple times to see them!
""")
    
    while True:
        try:
            number = int(input("Enter a number: ".strip()))
        except ValueError:
            print("❌ That isn't a valid number. Try again.\n")
            continue
        is_even = number % 2 == 0

        even_responses = [
            f"{number} is even. Perfectly balanced, as all things should be. 💎",
            f"{number} is even. Order has been maintained in the Time Variance Authority.",
            f"{number} is even. The Matrix approves of your symmetry. 🟩",
            f"{number} is even. Autobots would be proud. Roll out. 🤖🚗",
            f"{number} is even. Ah yes, divisible by 2. A mathematician's comfort zone. 🧠",
            f"{number} is is even. Balance has been restored. ⚖️",
            f"{number} is is even. Have you called Saul? ⚖️",
            f"{number} is even. Everything's right in the universe. ✨",
            f"{number} is even. The universe whispers...symmetry. ✨",
            f"{number} is even. Time to celebrate with a symmetrical dance. 💃🕺",
            f"{number} is even. As the Greybeads would say: 'Ro!' 🧙",
            f"{number} is even. Pretty balanced, just like my mood. 😵‍💫"
        ]

        odd_responses = [
            f"{number} is odd. A chaotic good rogue enters the tavern. 🗡️🎲",
            f"{number} is odd. Batman would approve. Justice doesn't follow straight lines. 🦇",
            f"{number} is odd. The Joker says: 'Why so serious about parity?' 🃏",
            f"{number} is odd. OMG! Doctor Strange just opened another dimension. 🌀",
            f"{number} is odd. Like pineapple on pizza. Controversial. 🍍🍕",
            f"{number} is odd. Just like your browser history. 🔍😬",
            f"{number} is odd. Unpredictable. Like our sleep schedule. 😴",
            f"{number} is odd. Kinda sus, not gonna lie. 🕵️‍♂️",
            f"{number} is odd. The algorithm didn't see that coming. 📉",
            f"{number} is odd. Just like my sense of humor. 😅",
            f"{number} is odd. Embrace the chaos. 🔥",
            f"{number} is odd. My pain is immesurable and my day is ruined. 😞"
        ]

        response = random.choice(even_responses) if is_even else random.choice(odd_responses)
        print(response + "\n")

        # !!! Temporary !!!
        try_again = input("Wanna try another one? (y/n): ").strip().upper()
        if try_again not in ["y", "yes"]:
            print("Alright, peace out 👋")
            break


def upper_or_lower():
    print("--- ⬆️ UPPERCASE or lowercase ⬇️ ---\n")

    empty_count = 0   
    while True:
        text = input("Enter some text: ").strip()
        
        if not text:
            empty_count += 1
            response = (
                "Wha-? You entered nothing 😐. Please try again...\n" if empty_count == 1 else
                "Y-you did it again. Please enter some text... 😶\n" if empty_count == 2 else
                "Okay, this is getting weird. Just. Type. Something. 🙃\n" if empty_count == 3 else
                "Like...ANYTHING. Just...TYPE! 🤨\n" if empty_count == 4 else
                "Bruh. You're testing my patience. ⏳. Come on bro, just press anything, you don't even have to think.\n" if empty_count == 5 else
                "Fine. I'll just wait here. Not like I have other things to do. 😤\n" if empty_count == 6 else
                "Alright, I'm done. Talk to me when you're ready. 🤖 *silent treatment engaged*\n" if empty_count == 7 else None
            )
            print(response)
            if empty_count >= 7:
                break
            continue

        empty_count = 0

        response = (
            f"'{text}' is in UPPERCASE. WHY ARE YOU SHOUTING BRO!!! 🗣️🗣️🔊" if text.isupper() else
            f"'{text}' is in lowercase. Shhhh...🤫" if text.islower() else
            f"'{text}' is a mix of cases. Pick a side bro. 🙄" if text.isalpha() else
            f"'{text}' Those are...just numbers. Are you trying to communicate in binary? 🤖" if text.isdigit() else
            f"'{text}' is...a bit chaotic, even for me — oh my! 😵‍💫"
        )

        print(response + "\n")


def test_your_precision():
    print(">>> Test Your Precision <<<")
    text = str(input("Enter a text with 100 characters: "))
    text_count = len(text)
    has_hundred = True if (text_count) == 100 else False
    has_more = True if (text_count) > 100 else False
    if has_hundred:
        print(f"The text '{text}' is FLAWLESS! Exactly {text_count} characters. 🥳 ")
    elif has_more:
        print(f"I said 100! The text '{text}' has {text_count} characters. 😠")
    else:
        print(f"Are you lazy to type? The text '{text}' has {text_count} characters. 🙄")
