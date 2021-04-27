#!/usr/bin/env python3
from operator import xor

# author: Ayo-Salami Ayobami
# csc 421
# lab 1
# --- script to add two unsigned binary numbers


# func def::
# binary XOR... with variable arguments
def bxor(*digits):
  res, carry = 0, 0
  
  for d in digits:
    d = int(d)
    if res == 1 and d == 1:
      carry = 1
    res = xor(bool(res), bool(d))
    res = int(res)
  return res, carry

def stringify(lists):
  return ''.join([str(elem) for elem in reversed(lists)])

# func def::
# function to add two binary numbers
def add(first, second):
  # i always want the first number to be the longer one.
  first_num = first if len(first) > len(second) else second
  second_num = second if len(first) > len(second) else first

  # function variables
  # reverse the array of each variable for easy access.
  carry = 0
  first_num = list(reversed(list(first_num)))
  second_num = list(reversed(list(second_num)))
  result = []

  for i in range(len(first_num)):
    res = 0

    if i < len(second_num):
      res, carry = bxor(first_num[i], second_num[i], carry)
      result.append(res)
    else:
      res, carry = bxor(first_num[i], carry)
      result.append(res)

    if i == len(first_num) - 1:
      result.append(carry)
  
  # return list(reversed(result))

  return stringify(result)


# say hello!
def welcome(text):
  print("-----------------------------")
  print("--- welcome to " , text, "!")
  print("--- made with love by bami :)")
  print("-----------------------------")
  return


# main function?? :p
def main():
  first, second = "", ""

  # hi
  welcome("binary adder")

  # for the sake of simplicity, we will assume
  # that all inputs are correct binary.
  # i'll still check for numeric data tho
  while not first.isnumeric():
    print("Enter the first binary number =>")
    first = input("> ")

  while not second.isnumeric():
    print("Enter the second binary number =>")
    second = input("> ")

  print()
  print("your result is =>", add(first, second))
  return


# call!!
main()
