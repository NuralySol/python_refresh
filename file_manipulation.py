
# Open a file and write to it with a with keyword

with open("./data/myfile.txt", "w") as banana:
	banana.write("I love bananas")

# Open a file and read from it with a with keyword

with open("./data/myfile.txt", "r") as banana:
    # print the content of the file to the console using the read() method
    print(banana.read())

print("-" * 50)

string1 = "Hello Everyone"
string2 = "Chat GPT will take over the world"

# How to write using write() method to a file w kills the content of the file and writes the new content
with open("./data/myfile.txt", "a") as banana:
    banana.write("\n")
    banana.write(string1)
    banana.write("\n")
    banana.write(string2)
    banana.write("\n")

numbers = [100, 200, 300, 400, 500]
# Write the numbers on the file
with open("./data/myfile.txt", "a") as banana:
    for number in numbers:
        banana.write(str(number))
        banana.write("\n")
        
# Read the content of the file
with open("./data/myfile.txt", "r") as banana:
    print(banana.read())