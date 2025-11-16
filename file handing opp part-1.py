# 1. Open file in write mode ('w') and write content
# This step uses logic from image_84716f.png
file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode ...")
file_write.write("Hi! I am Mahdiya. I am 12 years old")
file_write.write("I love sports!.") # New line for filtering
file_write.write("I'm an athlete in fact!")
file_write.close()

# 2. Open original file for reading ('r') and new file for writing ('w')
# This step uses logic from image_84718f.png
file3 = open('Codingal.txt', 'r')
file4 = open('CodingalUpdated.txt', 'w')

# 3. Read lines, filter, and write the filtered lines
# This loop and conditional uses logic from image_84718f.png
for line in file3.readlines():
    if not (line.startswith('Coding')):
        print(line) # Print the line as shown
        file4.write(line) # Store the line

# 4. Close all files
# This step uses logic from all screenshots
file4.close()
file3.close()

# 5. Open and read the final, updated file contents to demonstrate the result
# This uses the simple read logic from image_846ec2.png
file_read = open('CodingalUpdated.txt', 'r')
print(file_read.read())
file_read.close()