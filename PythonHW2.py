
my_movies = []
for i in range(5):
    my_txt = "Enter favorite movie #" + str(i+1) + ":"
    entry = input(my_txt)
    my_movies.append(entry)
print("Your favorite movies in reverse order:")
for i in range(5):
    print(my_movies[4-i])

palindrome = input("Enter a word: ")
if (palindrome == palindrome[::-1]):
    print(palindrome, "is a palindrome!")
else:
    print(palindrome, "is NOT a palindrome!")