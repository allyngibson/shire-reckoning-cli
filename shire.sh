#!/bin/bash

# A very light reworking of the mint-fortune command from Linux Mint 5.
# In the Python file I have a .bash_alias I cobbled together, but I wanted
# something with a little more variety, and mint-fortune, which randomized
# the cow and whether it was a speech bubble or thought balloon did the
# trick.

# Let's pick a location.
RANGE=5
number=$RANDOM
let "number %= $RANGE"
case $number in
	0)
		location="In the Shire, today is "
		;;
	1)
		location="At the Green Dragon in Bywater, today is "
		;;
	2)
		location="In Hobbiton, on Bagshot Row, today is "
		;;
	3)
		location="In the Great Smials of the West Farthing, today is "
		;;
  4)
    location="According to the Red Book of Westmarch, today is "
    ;;
esac

# Do we have a regular dragon or the dragon with the alarmed cow?
RANGE=2
number=$RANDOM
let "number %= $RANGE"
case $number in
	0)
		dragon="dragon"
		;;
	1)
		dragon="dragon-and-cow"
		;;
esac

python3 shire-reckoning.py | sed "s/^/$location/g" | cowsay -f $dragon -W 32
