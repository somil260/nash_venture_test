# nash_venture_test



Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want ‘a random number between 1 to 10’ 100 times then it should give ‘number more than 5’ 73 times and ‘less than 5’ 27 times. You’re not allowed to use any predefined random number generation function nor use of any kind of third party library to generate random number.




1. Intialize/get(from user) range of number. Minimum value and Maximum value

2. Initialize two output lists. Maximum number list and minimum number list.

3. Calculate mid value  of minimum value and maximum value.

4. Write random fuction to generate random number.
	a. Get current time.
	b. Remove integer value of time.
	c. Get number between given range
		and return its integer part.

5. Call random function 73 times (biased) with middle and max value

6  Call random fucntion 27 time with low and middle value.
