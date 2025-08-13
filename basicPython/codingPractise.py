# Create a list of your 5 favorite movies.
movies = ["Inception", "Interstellar", "Avengers", "Coco", "Ashique2"]

# Print the 3rd movie.
# print(movies[2])

# Replace the 2nd movie with another one.
# movies.insert(1, "Arrival")
movies[1] = "Arrival"

# Add a new movie at the end.
movies.append("Looper")
# print(movies)

# Remove the first movie.
del movies[0]

# print(movies)


# Given a tuple (5, 10, 15), unpack the values into variables a, b, and c, and print them in this format:
# "a=5, b=10, c=15"

cordinates = (5, 10, 15)

a, b, c = cordinates
# print(f"a={a}, b={b}, c={c}")


nums = [1, 2, 3, 2, 4, 1, 5, 3]

# Convert it into a set to remove duplicates.
unique = set(nums)

# print(unique)

# Convert it back into a list and print.
unique_list = list(unique)

# print(unique_list)


# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Split it into words (list)
word_list = sentence.split()
print(word_list)

unique_list = set(word_list)

print(unique_list)
