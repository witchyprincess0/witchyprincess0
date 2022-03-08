The Collatz sequence, also called the 3n + 1 problem, is the simplest impossible math problem. (But don’t worry, the program itself is easy enough for beginners.) From a
starting number, n, follow three rules to get the next number in the sequence:
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.


When you run collatz.py, the output will look like this:
Collatz Sequence, or, the 3n + 1 Problem

--snip--
Enter a starting number (greater than 0) or QUIT:
> 26
26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1


your_input = input('Enter your number or Quit:')
if your_input == 'Quit':
  quit()

def collatz_sequence(i):
  
  new_list = [i]
  while i > 1:
    if i %2 == 0:
      i = i//2
    else:
      i = i*3 + 1
    new_list.append(i)
      
  return new_list
  
result = collatz_sequence(int(your_input))
print (result)
  
