# a6.py
# ebc68 and mca74
# Sources/people consulted: NONE
# 04/25/23
# Skeleton by Prof. Bracy, AWB93, April, 2023

import printer, dice

# STUDENTS: Complete these 8 methods.
# Make sure this file has NO PRINT STATEMENTS.
# Print anything you need to print by using the printer.py helper functions

class Hand():
    """ An instance is a list of dice. The dice can be rolled, re-rolled, and
    printed in a cool ASCII art format. The hand can also add up all the values
    of its dice and state whether or not the hand has a particular number
    in it or not. (e.g., "Does this hand have any 3s?")
    """

    """ The standard terminal is 80 characters wide. Each ASCII art Die
    requires 9 characters, so we limit the number of dice in a hand to 8.

    A hand must have at least MIN_DICE dice and at most MAX_DICE dice.
    If the user asks for too many dice, they get MAX_DICE instead.
    If the user asks for too few dice, the get MIN_DICE instead.
    """
    MIN_DICE = 1
    MAX_DICE = 8

    def __init__(self, n_dice=1, dice_list=None):
        """
        Initializes the hand in one of two possible ways:
        * using the dice_list provided
        * constructing a list of dice that is n_dice long

        STUDENTS: you decide what instance attributes you'll need
                  and what to call them.

        Prints the hand after it's been initialized.

        Precondition: n_dice == len(dice_list) (if dice_list is not None)
                      MIN_DICE <= len(dice_list) <= MAX_DICE (if not None)
        """
        if dice_list != None:
            
            assert len( dice_list) >= Hand.MIN_DICE, \
                "dice_list must have at least "+str(Hand.MIN_DICE)+" dice"
            assert len(dice_list) <= Hand.MAX_DICE, \
                "dice_list must have at most "+str(Hand.MAX_DICE)+" dice"
            assert n_dice == len(dice_list), \
                "if dice_list is not None, its length must be n_dice"
        
        ###* Implement the n_dice first
        if dice_list == None: 
            self.n_dice = n_dice
        if n_dice > Hand.MAX_DICE:
            printer.print_it('Too many dice given so 8 dice allocated instead') 
            self.n_dice = Hand.MAX_DICE
        elif n_dice < Hand.MIN_DICE: 
            printer.print_it('Too few dice given so 1 die allocated instead') 
            self.n_dice = Hand.MIN_DICE

         #* if dicelist is given and n_dice meets length constraints assigns self to n_dice 
        elif n_dice <= Hand.MAX_DICE and n_dice >= Hand.MIN_DICE: 
            self.n_dice = n_dice


        self.dice_list = []


        

        if dice_list != None and len(self.dice_list) != n_dice: #* if dicelist is not None. Checks if len of selfdicelist is equal to n_dice 
                                                                #* Appends the elements of dicelist in self.dicelist
            for die in dice_list:
                self.dice_list.append(die)
    
        printer.print_it(self)

    def get_n_dice(self):
        """ At various times, a user will need to know how many dice are in
        the Hand. So the user can call this method and be told.

        Returns: an int that represents how many dice are in the hand.
        """
        # STUDENTS: implement this method so it doesn't always return 1

        return self.n_dice

    def get_dice(self):
        """ At various times, a user will need access to the dice list
        So the user can call this method and be given a list of dice.

        Returns: a list of Die that represents the hand.
        """
        # STUDENTS: implement this method so it doesn't always return []

        return self.dice_list

    def mask_valid(self, mask):
        """ A valid mask must be either:
        * the empty string
        OR
        * a string of length equal to the number of dice in the hand.
          the string must contain only 0's and/or 1's

        If the mask is the wrong length, use the helper function
        print_bad_mask_len() to inform the user.

        If the mask contains anything besides a 0 or a 1, use the helper
        function print_bad_mask_01() to inform the user.

        Returns True if the mask is valid by this definition. Otherwise False.
        """
        # STUDENTS: Implement this instance method

        if mask == '':
            return True
        elif len(mask) == self.get_n_dice():
            for numm in mask: 
                bollist = []
                if str(numm) in ['0', '1']:
                    bollist.append(True)
                else:
                    bollist.append(False)
                if False in bollist: 
                    printer.print_bad_mask_01()
                    return False
                else: 
                    return True
        elif len(mask) != self.get_n_dice(): 
            printer.print_bad_mask_len(self.get_n_dice())
            return False
        else: 
            return False

        

    def contains(self, value):
        """ Checks every die in the hand, looking for `value`

            Returns True if any die in the hand has the value `value`
            Otherwise, returns False.
        """
        # STUDENTS: Implement this instance method
        check = []
        for die in self.dice_list: 
            check.append(die.value)
        if value in check:
            return True
        else:
            return False

    def score(self):
        """Sums up the values of all the dice in the Hand.

        Example:
        if the hand has 4 dice and all of them have the value 2, Return 8
        """ 
        # STUDENTS: Implement this instance method
        summ = 0
        for die in self.dice_list: 
            summ += die.value
            
        return summ

    def reroll(self, mask):
        """Given a mask, rerolls the die in the hand where the mask
        has a 1

        Example: if the hand has 4 dice,
           - the mask "1000" will reroll only the first die
           - the mask "1111" will reroll all the dice
           - the mask "0000" will reroll none of the dice

        A Die knows how to roll itself. Make use of that instance method.

        Returns True if any dice were rerolled. False if the mask directed
        that no die be rerolled.

        Precondition: mask is a string of exclusively 0s and 1s
                      len(mask) == number of dice in this hand
        """
        # STUDENTS: Implement this instance method
        #! When we have a list given

        bolister = []
        if len(self.dice_list) > 0:
            for i in range(len(mask)):
                printer.print_it('Now rerolling die: ' + str(i)) 
                if mask[i] in ['1']:
                    self.dice_list[i].roll() #* Using Die.dice.roll() to change die's value
                    printer.print_it(self)
                    bolister.append(True)
                elif mask[i] in ['0']:
                    bolister.append(False)
                    printer.print_it(self)
            if True in bolister: 
                return True
            else: 
                return False
        
        #! When we DO NOT have a list given
        else: 
            for i in range(len(mask)):
                printer.print_it('Now rerolling die: ' + str(i)) 
                if mask[i] in ['1']:
                    printer.print_it(self)
                    bolister.append(True)
                elif mask[i] in ['0']:
                    bolister.append(False)
                    printer.print_it(self)
            if True in bolister: 
                return True
            else: 
                return False


        

    def __str__(self):
        """Returns the string that represents the Hand. The pseudo code will
        help you return something like:
        6, 5, 2, 1, 4
        but ultimately, you'll need to return the ASCII art version that
        will print:
        .-------..-------..-------..-------..-------.
        | O   O || O   O || O     ||       || O   O |
        | O   O ||   O   ||       ||   O   ||       |
        | O   O || O   O ||     O ||       || O   O |
        .-------..-------..-------..-------..-------.
        Note: you should not be typing '|' or 'O' or '_'
        You should look in dice.py to see how to use the pre-set strings.

        To begin with, try something simple that prints out the values of
        each Die. But ultimately, you'll want to print out the ASCII art
        version of the Hand.
        """
        # STUDENTS: Implement this instance method
        mystring = ""
        # Below is some pseudo code that you can
        # use until you get the ascii art version working.
        #
        # for each die in your hand:
        #    mystring += str(d.value) + ", "
        
        for die in self.dice_list: 
            mystring += str(die.value)          
        line1 = ''
        line2 = ''
        line3 = ''
        line4 = ''
        line5 = '' 

        linelist = [line1, line2, line3, line4, line5]

        for dienumber in mystring:
            diex = dice.Dots().art[int(dienumber)]
            for i in range(len(diex)):
                linelist[i] += diex[i]     
        laststr = ''
        for x in linelist: 
            laststr += x + '\n'

        return laststr

    # --------- STUDENTS: Do not change these instance methods ---------

    def initiate_reroll(self):
        # STUDENTS: do not change this function it will be called by a7 code
        printer.prompt_roll(self.get_n_dice())
        mask = self.get_mask()
        return self.reroll(mask)

    def get_mask(self):
        """Prompts the user for a mask. Keeps prompting the
        user until the mask is valid. returns the valid
        Mask. If the user enters the empty string, converts
        this to all 0s. """
        choice = input("Your reroll mask: ")
        while not self.mask_valid(choice):
            choice = input("Your reroll mask: ")
        if choice == "":
            choice = "0"*self.get_n_dice()
        return choice

if __name__=='__main__':
    n = int(input("How many dice would you like to roll? "))
    #ONE_DIE_LIST = [dice.Die(3)]
    #FIVE_DIE_LIST = [dice.Die(3), dice.Die(2), dice.Die(1), dice.Die(6), dice.Die(5)]
    hand = Hand(n)
    printer.print_score(hand.score())
    while hand.initiate_reroll():
        printer.print_score(hand.score())

    # an excuse to use contains()
    for i in range(1, dice.Die.NUM_SIDES+1):
        printer.print_tally(i, hand.contains(i))

    # we are nothing if not polite
    printer.print_thanks()
