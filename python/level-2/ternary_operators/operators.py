"""
    Auxiliary file for 'ternary_operator-2.py' for better organization.
"""
def handle_retry() -> bool | None:
    """Helper function to handle retry logic for all functions.
    
    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        choice = input("\nWhat would you like to do?\n[R] Retry\n[X] Exit\n[M] Return to menu\nChoice: ").strip().upper()
        if choice in ["R", "X", "M"]:
            return True if choice == "R" else (None if choice == "M" else False)
        print("❌ Please enter R, X, or M")


def check_age_majority():
    """Function to check if the user is a minor or an adult, including funny easter eggs for multiple specific values.
    This function uses a match-case statement to handle different age inputs and provide corresponding responses.

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")  # ANSI escape code to clear the terminal
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
                print("\n❌ Please, enter a valid age!\n")

        status = "an adult" if age >= 18 else "a minor"

        match age:
            case _ if age < 0: 
                print(f"\n{age} is a...wait, what? This person wasn't even born! ❓⁉️")
            case 0:
                print(f"\n{age} is {status}. Just born? Welcome to the world, little one! 👶🍼")
            case 1:
                print(f"\n{age} is {status}. Only 1 year old? That's adorable. 🥺")
            case 3:
                print(f"\n{age} is {status}. 3️⃣  A true toddler trinity. Half chaos, half giggles.")
            case 5:
                print(f"\n{age} is {status}. Still in the finger painting phase, huh? 🎨")
            case 7:
                print(f"\n{age} is {status}. 🍀 Lucky number seven! You must have magical powers!")
            case 18:
                print(f"\n{age} is {status}. 🗳️ Officially an adult (sort of). Time to pay taxes and question your life choices!")
            case 25:
                print(f"\n{age} is {status}. 🧠🍳 Your brain just finished cooking. Welcome to full sentience!")
            case 50:
                print(f"\n{age} is {status}. 🕺🪩  Half a century! Cue the disco ball and dad jokes.")
            case 42:
                print(f"\n{age} is {status}. 🧠 42...the answer to life, the universe, and everything.")
            case 69:
                print(f"\n{age} is {status}. 😏 Nice.")
            case 100:
                print(f"\n{age} is {status}. 🎉 A century! You've seen some things, haven't you?")
            case 130:
                print(f"\n{age} is {status}. 🧙 Are you a wizard? That seems...unlikely.")
            case 300:
                print(f"\n{age} is {status}. 👽 Are you sure you're from this planet?")
            case 420:
                print(f"\n{age} is {status}. 🔥 Blaze it? Just kidding! That's probably a typo...")
            case 2011:
                print(f"\n{age} is {status}. 😴 Hey, you. You're finally awake 😯. You were trying to cross the border, right? Walked right into that Imperial ambush ⚔️, same as us, and that thief over there. 🥷")
            case 1337:
                print(f"\n{age} is {status}. 💻 Leet detected. Hacker vibes intensifies! 🔥")
            case 9001:
                print(f"\n{age} is {status}. 🔥 IT'S OVER 9000!!!")
            case 9999:
                print(f"\n{age} is {status}. ⚔️   Final boss level unlocked. *Vordt of the Boreal Valley starts playing*")
                # Might use that to make a pygame later u.u
            case _:
                print(f"\n{age} is {status}.")
        
        retry = handle_retry()
        if retry is not True:
            return retry


def check_even_odd():
    """Function to check if a number is even or odd, including funny easter eggs for each attempt.
    This function uses the random module to provide different responses for even and odd numbers.

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    import random
    
    while True:
        while True:
            print("\033[H\033[J", end="")
            print("""\n>>> Even or Odd Numbers <<<
              
    Welcome to the even or odd number checker!
This version contains a lot of random responses, try it
multiple times to see them!
    """)
            try:
                number = int(input("Enter a number: ".strip()))
            except ValueError:
                print("\n❌ That isn't a valid number. Try again.\n")
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
                f"{number} is odd. Kinda sus, not gonna lie. 🕵️",
                f"{number} is odd. The algorithm didn't see that coming. 📉",
                f"{number} is odd. Just like my sense of humor. 😅",
                f"{number} is odd. Embrace the chaos. 🔥",
                f"{number} is odd. My pain is immesurable and my day is ruined. 😞"
            ]

            response = random.choice(even_responses) if is_even else random.choice(odd_responses)
            print(response)
        
            retry = handle_retry()
            if retry is not True:
                return retry


def upper_or_lower():
    """Function to check if a string is in UPPERCASE, lowercase, or MiXeD CaSe.
    This function uses a while loop to handle user input and provides different responses based on the case of the string.
    
    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:

        empty_count = 0   
        while True:
            # print("\033[H\033[J", end="") | Couldn't get this to work. Was conflicting with the input, 'if not text:' was never triggered.
            print(">>> ⬆️ UPPERCASE or lowercase ⬇️ <<<\n")
            text = input("Enter some text: ")
            
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
                if empty_count > 7:
                    return
                continue

            empty_count = 0

            response = (
                f"'{text}' is in UPPERCASE. YOU SHOUTING!!! 🗣️ 🔊" if text.isupper() else
                f"'{text}' is in lowercase. Shhhh...🤫" if text.islower() else
                f"'{text}' is a mix of cases. Pick a side bro. 🙄" if text.isalpha() else
                f"'{text}' Those are...just numbers. Are you trying to communicate in binary? 🤖" if text.isdigit() else
                f"'{text}' is...a bit chaotic, even for me — oh my! 😵‍💫"
            )

            print(response + "\n")
            retry = handle_retry()
            if retry is not True:
                return retry


def test_your_precision():
    """Function to test the user's precision in typing a text with a specific number of characters.
    This function generates a random number and asks the user to type a text with that exact number of characters.

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        import random

        print("\033[H\033[J", end="")
        print(">>> Test Your Precision <<<")

        random_number = random.randint(1, 200)
        print(f"""\nLet's test how precise you are! 🎯
Type a text with EXACTLY {random_number} characters!""")
        
        user_input = str(input("Enter a text: ").strip())
        text_count = len(user_input)

        is_flawess = True if (text_count) == (random_number) else False
        is_greater = True if (text_count) > (random_number) else False

        if is_flawess:
            print(f"""\n🥳 The text: 
        '{user_input}' 
    is FLAWLESS! Exactly {random_number} characters. 🎉""")
            
        elif is_greater:
            print(f"""\n🤨 I said {random_number}! The text: 
        '{user_input}' 
    has {text_count} characters. 😠""")
            
        else:
            print(f"""\n🙄 Are you lazy to type? The text: 
        '{user_input}' 
    has only {text_count} characters. 🤦""")
    
        retry = handle_retry()
        if retry is not True:
            return retry
