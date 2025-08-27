# Written by Griffin Siebert
# REVISED 8/27/25 To remove Lists as per request
#
# I kinda overengineered the second helper function to allow for extendability.
# I made the first one display the banner with variable amounts of dashes,
# however in the example I found there were two counts, one with 34 Dashes,
# and another with 57 Dashes. Since I am disallowed global variables, I just
# made it vary with each menu.
def draw_menu_banner(text, num):
    print("-" * num)
    print(text)
    print("-" * num)


# Designed for as many options or candidates as needed
def prompt(options, initial_text):
    choice_is_good = False
    option_text = initial_text

    # My IDE Claims that this while loops misses a return Path,
    # but it's just supposed to loop until the user chooses a correct option.
    # Thought: It does not like my variable name that much
    while not choice_is_good:
        choice = input(option_text)
        choice.strip()
        choice = choice.lower()

        # Should get the first letter out of the response and check if it is a desired answer, then return it
        char = choice[0] # I Corrected this to not use the list operators to get it, instead using the index of the first letter.
        if char in options:
            return char
        else:
            correct_options = ""
            for option in options:
                correct_options += option + "/"
            correct_options = correct_options[:len(correct_options) - 1]
            # This still uses lists but just to dynamically provide options
            option_text = "Invalid (" + correct_options + "): "

# Just turns the list that keeps track of their scores into a banner at the end
def end(stats_i,stats_g,stats_h):
    stats_text = f"Isabella - {stats_i}, Genji - {stats_g}, Hannah - {stats_h}, Total - {stats_i + stats_g + stats_h}"
    draw_menu_banner(stats_text,57)

def vote_menu():
    draw_menu_banner("VOTE MENU", 34)
    print("v: Vote")
    print("x: Exit")
    return prompt(["v","x"], "Option: ")

def candidate_menu():
    draw_menu_banner("CANDIDATE MENU",34)
    print("1: Isabella")
    print("2: Genji")
    print("3: Hannah")
    return int(prompt(["1", "2", "3"], "Candidate: "))




def main():
    state = 1
    stats_i, stats_g, stats_h = 0, 0, 0
    # I originally thought of recursively showing panels but was thwarted with the no-parameter rule.
    # I decided on two loops, one that kept track of the menus and one that kept track of the options.
    while not state == 0:
        if (state == 1):
            response = vote_menu()
            if (response == "x"):
                state = 0
            else:
                state = 2
        elif (state == 2):
            vote = candidate_menu()
            # EDIT 8/27/25 To remove lists
            # I almost forgot to add the tiny line that confirms the user's choice.
            if vote == 1:
                stats_i += 1
                print("Voted Isabella")
            elif vote == 2:
                stats_g += 1
                print("Voted Genji")
            else:
                stats_h += 1
                print("Voted Hannah")
            state = 1
    end(stats_i, stats_g, stats_h)
main()
