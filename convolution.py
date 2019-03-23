# Convolution Algorithm in Python v1.0 by Memphis 😎

# ---------- PART 1 -----------

import os

# Function to just clear the console


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print("\n======== CONVOLUTION MADE EASY ========\n")

# Declaration of list variables to store
# x[n] and h[n] signals
xn = []
hn = []

# ---------- PART 2 -----------

print("Enter signal inputs for x[n]")
# Loop to input x[n] signal values
while True:
    xn.append(int(input("> ")))
    cont = input("Continue? Y/n ").lower()
    if cont == "n":
        break
    else:
        continue


print("\nEnter signal inputs for h[n]")
# Loop to input h[n] signal values
while True:
    hn.append(int(input("> ")))
    cont = input("Continue? Y/n ").lower()
    if cont == "n":
        break
    else:
        continue

# ---------- P.T.O -----------

# ---------- PART 3 -----------

# A really helpful variable I thought of
# It will store literal zeros to be used
# to append and prepend to interim h[n] signals/delays
# during calculation when the h[n] shifts right
zeros = range(len(hn) - len(xn))

# Function to formulate h[n] delays based on the
# zeros (remember zeros?)
# Function simply returns a list of lists of
# these interim signals
def hn_delays(zeros, hn):
    hn_delays = []
    z = 0
    while z <= len(zeros):
        hn_delays.append(hn[:])
        zeros_back = []
        zeros_front = []
        for x in range(len(zeros) - z):
            zeros_back.append(0)
        for y in range(z):
            zeros_front.append(0)
        hn_delays[z] += zeros_back
        hn_delays[z] = zeros_front + hn_delays[z]
        z += 1
    return hn_delays

# ---------- P.T.O -----------

# ---------- PART 4 -----------
# I guess this function does most of the convolution
def convolve(xn, hn_delays):
    yn = []
    interim_yn_addition = []
    for x in range(len(xn)):
        to_addition = []
        for hn in range(len(hn_delays[x])):
            yn_interim = 0
            yn_interim += xn[x] * hn_delays[x][hn]
            to_addition.append(yn_interim)
        interim_yn_addition.append(to_addition)

    for a in range(len(interim_yn_addition[0])):
        sum = 0
        for b in range(len(interim_yn_addition)):
            sum += interim_yn_addition[b][a]
        yn.append(sum)
    return yn

# House Cleaning LOL
# Output decor...
print("\n------------------")
print("\nx[n] = [" + "  ".join(str(x) for x in xn) + "]")
print("\nh[n] = [" + "  ".join(str(h) for h in hn) + "]")
str_yn = "[" + "  ".join(str(y)
                         for y in convolve(xn, hn_delays(zeros, hn))) + "]"
print("\ny[n] = x[n] (*) h[n] = " + str_yn + "\n")
