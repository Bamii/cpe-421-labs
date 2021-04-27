#!/usr/bin/env python3
from operator import xor

# author: Ayo-Salami Ayobami
# csc 421
# lab 3
# --- script to multiply two digits.


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


# function to turn list to string.
def stringify(lists):
  return ''.join([str(elem) for elem in lists])


# func def::
# function to add two binary numbers
def add(first, second):
  # i always want the first number to be the longer one.
  first_num = first if len(first) > len(second) else second
  second_num = second if len(first) > len(second) else first

  # print('ad = ', first_num)
  # print('ad = ', second_num)

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

    if i == len(first_num) - 1 and carry == 1:
      result.append(carry)

  return stringify(list(reversed(result)))


# func def::
# function to multiply two binary numbers
def multiply(first, second):
  # i always want the first number to be the longer one.
  first_num = first if len(first) > len(second) else second
  second_num = second if len(first) > len(second) else first
  res = ""

  shift = 0
  second_num_len = len(second_num)
  for i in range(second_num_len):
    curr = second_num_len - 1 - i

    if second_num[curr] == 0:
      continue

    partial = first.ljust(len(first) + shift, '0')
    res = add(res, partial)
    shift = shift + 1
    
  return res


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
  welcome("binary multiplicator")

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
  print("your result is =>", multiply(first, second))
  return


main()