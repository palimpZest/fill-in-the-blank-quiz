# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

number_options = ['___1___', '___2___', '___3___', '___4___']

answers_easy = ['Earth', 'Mercury', 'degrees', 'Venus']
answers_medium = ['Pluto', 'Mars', 'war', 'life']
answers_hard = ['Jupiter', 'storm', 'Saturn', 'Neptune']

welcome_message = '''
    Welcome to this entertaining galactic game!
    It's a quiz about our solar system!
    What do you know about its planets?
'''

level_choices = " " * 27 + "easy" + " " * 7  + "medium" +  " " * 7 + "hard"

not_a_level = '''
That's not a level! Please select a level (easy/medium/hard): '''

selected_level = '''
You've selected '''

correct_text = '''

That's correct!
'''

incorrect_text = '''

That's not correct. Please try again!
'''

questions = ["What can be substituted for ___1___? ",
             "What can be substituted for ___2___? ",
             "What can be substituted for ___3___? ",
             "What can be substituted for ___4___? ",]

continue_text = '''
Congratulations! You won this level!

Would you like to continue to another level? (yes/no) '''

easy_level_text = '''
The planet ___1___ is the place where we live
in our galaxy. The ___1___ is the third planet
from the sun, and the closest planet to the sun is
___2___. A planet whose temperature can go up
to 800 ___3___ Fahrenheit! The planet between
___1___ and ___2___ is ___4___, our sister planet,
named after the Roman goddess of love and beauty.
'''

medium_level_text = '''
Recently, two planets have made the news. The first
one, ___1___, is now considered a dwarf planet. The
spacecraft New Horizons arrived in its vecinity a few
months ago to gather new data and images from it.
The most interesting planet for humans still seems to
be ___2___. While ___1___ is named after the god of the
Underworld, ___2___ is named after the god of ___3___.
We are planning to send manned missions to the red planet
in the next decades to find out if ___4___ has once
existed there. That's why ___2___ is the celestial
object that captures our imagination the most.
'''

hard_level_text = '''
Some planets in the Milky Way are mostly composed of
gas, like ___1___. These are called the Gas Giants.
The sheer volume of ___1___ makes it a gigantic ball
of condensed gases which exerts an incredible amount
of gravity. Its Great Red Spot, is a never-ending
___2___, that has been raging on its surface for
centuries. Some models have suggested that it may
be a permanent feature of the planet.  ___3___
is the most recognizable by the fact that it has the
most visible planetary rings in the Solar System.
Finally, even if it isn't the largest, ___4___, is
the densest gaseous planet among them.
'''

def welcome_quiz():
    '''prints a welcome message and shows the level options from which
    the user has to select. Returns the level selection procedure.'''
    print welcome_message, '\n', level_choices
    print
    user_input = raw_input("Please select a level: ")
    return level_selection(user_input)

def level_selection(user_input):
    '''prompts a level selection to the user with three options.
    If the user doesn't choose one of those, he has to try again.
    The result is the text to fill for the chosen level.'''
    print selected_level + user_input + "!"
    if user_input == 'easy':
        print easy_level_text
        return level_game(easy_level_text, answers_easy)
    elif user_input == 'medium':
        print medium_level_text
        return level_game(medium_level_text, answers_medium)
    elif user_input == 'hard':
        print hard_level_text
        return level_game(hard_level_text, answers_hard)
    else:
        user_input = raw_input(not_a_level)
        return level_selection(user_input)

def level_game(level_text, level_answers):
    '''verifies if the user input matches the first word of answers_easy list. If there's a
    match, the easy_level_text with the first word is returned. Then asks user for the
    second word, and so on. Otherwise, it asks the user to try to guess again. If there are
    no more words in the list, it calls the continue_end procedure.'''
    count = 0
    for word in level_text:
        user_input = raw_input(questions[count])
        if user_input == level_answers[count]:
            print correct_text
            level_text = level_text.replace(number_options[count], level_answers[count])
            print level_text
            count = count + 1
            if len(level_answers) == count:
            	continue_end()
        else:
        	while user_input != level_answers[count]:
        		print incorrect_text, '\n', level_text
        		break

def continue_end():
    '''asks the user if he/she wants to continue playing,
    by going to another level, or wants to stop playing.'''
    user_input = raw_input(continue_text)
    if user_input == "yes":
    	welcome_quiz()
    if user_input == "no":
        return None

welcome_quiz() # this kickstarts the whole program.
