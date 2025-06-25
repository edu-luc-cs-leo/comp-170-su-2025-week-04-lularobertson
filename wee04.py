
words = ["cat", "house", "television", "flower", "rose", "pottery"]

def longest_word(words: list[str]) -> str:
  if words is not None and len(words) > 0:
    largest = words[0]
    for i in range(1, len(words)):
      if len(words[i]) > len(largest):
        largest = words[i]
    return largest

print(longest_word(words))

def shortest_word(words: list[str]) -> str:
  if words is not None and len(words) > 0:
  # checks exist and then non empty
    shortest = words[0]
    for i in range(1, len(words)):
      if len(words[i]) < len(shortest):
          shortest = words[i]
    return shortest

print(shortest_word(words))

def odd_words(words: list[str]) -> list[str]:
  if words is not None and len(words) > 0:
    odd = []
    for i in range(len(words)):
      if len(words[i]) % 2 == 1:
        odd.append(words[i])
    return odd
# .append() makes sure the program prints every element that works in the function, not just one.
# [] says that when we return "odd", it's going to print a list inside these brackets.

print(odd_words(words))

def average_words(words: list[str]) -> list[str]:
  if words is not None and len(words) > 0:
    sum = 0
    for i in range(len(words)):
      sum = sum + len(words[i])
    ave = sum / len(words)
    result = []
    for word in words:
      if abs(len(word) - ave) <= 1:
        result.append(word)
    return result

print(average_words(words))

words2 = ["mower", "sun", "rose", "guitar", "pillow"]

def intersect(words: list[str], words2: list[str]) -> bool:
  if words is not None and len(words) > 0:
    if words2 is not None and len(words2) > 0:
      found = False
      i = 0
      while i < len(words) and not found:
        found = (words[i] in words2) # we can use in, because you can't compare a word to a list.
        i = i + 1
      return found

print(intersect(words, words2))



"""
reflection:

All my code runs well I think. It draws the correct shapes and they are centered.

DIAMOND:
I think my main mistake with the diamond is that its only changing dimension is the
width versus the width and the hieght changing together. I should have scaled the two
toegther like I did in the square and triangle. By making each half a loop, 
I could then loop it how ever many times the height of the half would be.

Another issue was my program just used a print statement to tell the user that the width
was invalid if the input was an even number, and then instructed them to rerun the program
and choose a different number. Even if I didn't just get the program to round the number to an
odd one, I should have figured out a way to make it loop back to the question regarding width
versus intructing them to rerun the program.

RIGHT TRIANGLE:
My code for the right triangle was good ...  I think. The only option was it make it
with the angle on the left, but adding an option for the angle to be on the right would
be a good idea.

COMPOUNT INTEREST:
Our code differed a little in this one too. I had the program print the amount of money
that would be in the account every year until year N (the amount of years they wanted it in the account).
I thought that was the intructions because the directions had multiple years listed.
I also had to look up the .2f to round the number so it wouldn't be over 2 decimals since
we are dealing with money.

HOLLOW SQUARE:
I think the hollow square was my best program. Plus it looks pretty cool depending on what character
you use. Like the diamond, I did not round or change the inputs if the thickness of the walls
was too large, I just intructed the user to rerun and imput a smaller size for the walls.


Overall, we had different code. Mine was more similar to our sears tower we made in class.
I also set the variables as inputs in the terminal versus parameters in the function.

Other than the diamond shape, I would say my code for the rest of them was very functional
and worked well.

"""
















#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
