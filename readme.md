# Enigma

Program to decrypt the numerical code into English words.

## Logical Framework 

- First step took to analyze the numerical code to get the pattern of numerical code sent in intercepted message.
- It's found that it's repeating first 3 digits in order of (11, 12, 13) and then starting again from 21 to 23 and same until letter "Z".
- Added all alphabets and sliced respective numeric codes to dictionary.
- Then written a method to grab each letter for their keys from the input message.

## Program

- Coded in Python programming language.

## Time Complexity
- The time is constant O(1) to return the value from the "choose_letter" function.
- It's O(n) linear time for both the "break_string" method and appending "message_list" loop.
- So the overall time complexity of the program will be **O(1)+O(2n)**.
Please make sure to update tests as appropriate.

## Best Case Scenario
- When the length of the message intercepted string is 1, like binary options (Y/N). It's O(1)

## Worst Case Scenario
- When the length of message is big, it'll be of O(1)+O(2n)