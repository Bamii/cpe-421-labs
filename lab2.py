#!/usr/bin/env python3
from operator import xor

# author: Ayo-Salami Ayobami
# csc 421
# lab 2
# --- script to subtract two digits.


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
  
  # return list(reversed(result))

  return stringify(list(reversed(result)))


# func def::
# function for 2s complement
def twos_complement(digit):
  digit = list(digit)
  result = []
  
  # something about python inserting backwards?
  for i in range(len(digit)):
    neg = not int(digit[i])
    result.append(int(neg))

  resStr = stringify(result)
  if result[0] == 1:
    resStr = resStr.rjust(len(result) + 4, '1')

  return add(resStr, "1")


# func def::
# function to pad the digits on the left.
def padBits(digits):
  mod = len(digits) % 4
  if mod != 0:
    return digits.zfill(len(digits) + (4 - mod))
  else:
    return digits.zfill(len(digits) + 4)


# func def::
# function to subtract numbers
def subtract(first, second):
  # pad both numbers to make it a workable size i.e: 4, 8000
  first = padBits(first)
  second = padBits(second)

  print("----------------------------------")
  print("first number =>", first)
  print("second number =>", second)
  print("second number' (complement) =>", twos_complement(second))
  print("----------------------------------")

  return add(first, twos_complement(second))


# func def::
# say hello!
def welcome(text):
  print("-----------------------------")
  print("--- welcome to " , text, "!")
  print("--- made with love by bami :)")
  print("-----------------------------")
  return


# func def::
# main function?? :p
def main():
  first, second = "", ""

  # hi
  welcome("binary substractor")

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
  print("your result is =>", subtract(first, second))
  # print("original>>", padBits(first))
  # print("complement>> ", twos_complement(padBits(first)))
  return


# call!!
main()