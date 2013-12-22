Introduction
============
This is a simple script that tells you how much DOGE you can buy with an 
amount of BTC.


Usage
=====
The script takes a single command line argument that is the amount of BTC
that you want to convert to DOGE.

`./doge.py .0018`

The script will then pull the current rate of DOGE to BTC from Cryptsy
and print out how much doge you can buy with .0018 BTC at the rate of the most
recent trade. It will also print out the average and median price of the last 
100 trades.
