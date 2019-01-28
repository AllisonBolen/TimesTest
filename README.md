# TimesTest


# Open Ended Question


Please describe a system in which you have been a technical contributor. This could be from your current role or from a previous role.
- I was a technical contributor to the Data Lake Team at my current internship with Steelcase. I have been able to contribute quite a few pieces of software to the team to improve efficiency but my favorite one was when I helped implement API logging into Microsoft Azure using ARM Templates and powershell. I was given the responsibility to implement a logging capability that would track who was calling our API, where they were accessing it from, what they were asking for and when they were accessing it. I learned a lot form this project because I was automating a configurable task in Microsoft Azure and most of everyone on my team was out of town for a conference that week. I was excited to learn how to work with the system. I got most of it working, but the project took longer than expected because we found a bug in Microsofts system. After contacting then and discussing it we solved it and are now able to track who and how our API is interacted with. Additionally I configured it to interact with an external storage system based on the security teams specifications. That way we could store the logs for longer and in a separate secure system.



# Programming Challenges


## Write a representation of a New York Times newsletter subscriber. Make sure the subscriber has a first name, last name, email address, and a list of newsletter subscriptions. Represent a newsletter subscription as a separate entity that includes a name and a code or ID. Show how you would create a new subscriber and how you would add/remove a newsletter subscription for that subscriber. Keep the solution simple. No need to interface with a database.
- I wrote a representation of a subscriber and subscription using Java and you can find the solution in the TimesJava folder. I used IntelliJ as an editor for this one. There is a main file that show the basic functionality. I decided to use a hashmap instead of an array because that ensures a unique subscription list where users can be subscribed to a service more than once. It wouldn't make sense to be subscribed to the crossword twice.

## Write a function that extracts the longest word from a string of space-separated words.
- I wrote a solution to for this function In Golang. You can find the solution in the TimesGo folder. I turned the sentence into a sorted list of words increasing in length. Thus the last word in the list should be the longest. The only edge case would be if there are words of the same length that are also the longest words in the list. I just decided to return the last one. I also went with a hardcoded version for this just because its simpler for now, command line arguments would have been a better option for real life implementation. I used Atom as an editor for this and the remaining questions.  

## Write a function that returns the median integer from an array of integers.
- I wrote a solution for this in GoLang as well. You can find the solution in the TimesGo folder. I sorted the list of integers in increasing order and calculated the middle index. If the list was an even length, (I googled how that is typically handled) I average the two middle most values and return the ceiling of that value because we should return an int. I also went with a hardcoded version for this just because its simpler for now, command line arguments would have been a better option for real life implementation.

## Write a function for each RESTful operation for a resource named “document.” Make sure each CRUD operation are represented by a single function. The hostname can be arbitrary.
- If I'm being honest, this question kind of confused me. I went with what I thought was being asked and decided to build a quick REST implementation using Python3 and Flask. The relevant files are in the TimesPython folder. You can run this one by executing the run.sh file and then opening a new terminal window and running the testCurls.sh file to run through a subset of calls that edit a json document.

## Thank you so much for your consideration, I look forward to hearing your feedback.
