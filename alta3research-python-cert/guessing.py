#!/usr/bin/env python3
import random
import crayons

def main():
    """Run time code"""

print("A Coin was flipped")
coin = random.randint(0, 1)
print("Guess 0 for Tails")
print("Guess 1 for Heads")
guess = int(input() )
#guess = int(input('Out of these options(0,1)Heads is 1 and Tails is 0?'))

#print(coin)
if guess == coin:
#    print('you guessed it')
    print(crayons.green('You guessed it correct!!!', bold=True))
elif guess != coin and guess >1:
#elif guess >1:
#    print('That is weird, there is no MEGA sided coin...Cheat Much!!!')
    print(crayons.magenta('That is weird, there is no MEGA sided coin...Cheat Much!!!', bold=True))
elif guess != coin:
    print(crayons.yellow('Almost, Try Again!'))
else:
    print('Well ths is awkward, you should not be here')

if __name__ == "__main__":
    main()

