import os

directory = r'C:\Users\nikla\Desktop\HYDRA 1.6F PRO\LOGS'

logs = set()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        for file in filename:
            logs.add(filename)
        # Form the complete path
        filepath = os.path.join(directory, filename)
        # Read the contents of the file
        #with open(filepath, 'r') as file:
            # Print the contents (or you can do whatever processing you need here)
        #    print(file.read())

for log in logs:
    print(os.path.join(directory, log))