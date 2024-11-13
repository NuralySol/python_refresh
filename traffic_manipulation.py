from collections import defaultdict

# Dictionary to store each room's data and use defaultdict to initialize the values to 0
rooms = defaultdict(lambda: {"total_time": 0, "visits": 0, "current_visitors": {}})

# Load and parse traffic.txt data
with open("./data/traffic.txt", "r") as traffic:
    for line in traffic:
        visitor_id, room_id, action, timestamp = line.strip().split()
        # need to convert the strings to integers since the txt file is read as collection of strings
        visitor_id, room_id, timestamp = int(visitor_id), int(room_id), int(timestamp)

        # if and elif statements to determine if the visitor is entering or leaving the room
        if action == "I":  # Visitor entering the room
            rooms[room_id]["current_visitors"][visitor_id] = timestamp
        elif action == "O":  # Visitor leaving the room
            enter_time = rooms[room_id]["current_visitors"].pop(visitor_id, None)
            if enter_time is not None:
                time_spent = timestamp - enter_time
                rooms[room_id]["total_time"] += time_spent
                rooms[room_id]["visits"] += 1

# Prepare the output and store it in a list of strings
output_lines = []
for room_id, data in rooms.items():
    if data["visits"] > 0:
        average_time = data["total_time"] // data["visits"]
        total_visitors = data["visits"]
        output_line = f"Room {room_id}, {average_time} minute average visit, {total_visitors} visitor(s) total"
        output_lines.append(output_line)

# Write the output to a new file and save it in the data folder
with open("./data/traffic_report.txt", "w") as report:
    report.write("\n".join(output_lines))
# Print the output for verification purposes in the console
print("\n".join(output_lines))

# Find the most popular room based on the number of visits and print it
most_popular_room = max(rooms, key=lambda x: rooms[x]["visits"])
print("\n The most popular room is: ", most_popular_room)

# Find the least popular room based on the number of visits and print it
least_popular_room = min(rooms, key=lambda x: rooms[x]["visits"])
print("\n The least popular room is: ", least_popular_room)

# Find the room the most  time spent and print it
most_time_spent_room = max(rooms, key=lambda x: rooms[x]["total_time"])
print(f"\n The room with most time time spent is: {most_time_spent_room}")

# Total number of visitors in the gallery
total_visitors = sum(rooms[room_id]["visits"] for room_id in rooms)
print("\n The total number of visitors in the gallery is: ", total_visitors)

# What is the average time spend in the gallery as as a whole
total_time_spent = sum(rooms[room_id]["total_time"] for room_id in rooms)
average_time_spent = total_time_spent // total_visitors
print(
    "\n The average time spent in the gallery is: ", average_time_spent
)  # 67 minutes?

# What is the median time spent in the gallery
time_spent_list = [rooms[room_id]["total_time"] for room_id in rooms]
time_spent_list.sort()
n = len(time_spent_list)
if n % 2 == 0:
    median_time_spent = (time_spent_list[n // 2 - 1] + time_spent_list[n // 2]) / 2
else:
    median_time_spent = time_spent_list[n // 2]
print("\n The median time spent in the gallery is: ", median_time_spent)


"""
The Popularity of the Rooms: 
A very prestigious art gallery has contacted you regarding a job. Get to work!
Management wants to figure out how many people visit each room in the gallery, and for how long: this is to help improve the quality of the overall gallery in the future.
Your goal is to write a program that takes a formatted text file that describes the overall gallery's foot-traffic on a minute-to-minute basis. From this data you must compute the average time spent in each room, and how many visitors there were in each room.

The Input:
Each line in the text file represents either a visitor entering or leaving a room. 
It starts with an integer, representing a visitor's unique identifier. 
Next on this line is another integer, representing the room's number. 
Next is a single character, either 'I' (for "In") for this visitor entering the room, or 'O' (for "out") for the visitor leaving the room. 
Finally, at the end of this line, there is a time-stamp integer: it is an integer representing the minute the event occurred during the day. 
All of these elements are space-delimited.
You may assume that all input is logically well-formed: for each person entering a room, he or she will always leave it at some point in the future. A visitor will only be in one room at a time.
Note that the order of events in the log are not sorted in any way; it shouldn't matter, as you can solve this problem without sorting given data.
Sample Input:

        0 0 I 540
        1 0 I 540
        0 0 O 560
        1 0 O 560
        
The Output:
For each room that had log data associated with it, print the room number, then print the average length of time visitors have stayed as an integer, and then finally print the total number of visitors in the room. All of this should be on the same line and be space delimited; you may optionally include labels on this text, like in our sample output 1.
Sample Output:
Room 0, 20 minute average visit, 2 visitor(s) total Loading the Text File:
You'll find a text file traffic.txt in this repo. Import this text file and parse it to get the results.
When you are done solving the problem, write your output to another text file and save it.

"""
