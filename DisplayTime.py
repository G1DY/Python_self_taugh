# Prompt the user to enter time in seconds
seconds = eval(input("Enter time in seconds:"))

#convert seconds to minutes and remaining seconds
minutes = seconds // 60 # Find minutes in seconds
remainingSeconds = seconds % 60 # finds remaining seconds

# Display results
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds\
        ,"seconds")
