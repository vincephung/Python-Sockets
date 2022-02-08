Project 1:

Notes: client opens a file named "in-proj0.txt" and creates a file "out-proj0.txt"
If you want to open a different file, you must go inside client.py and change the file name

Observations: 
(2) Try running the program immediately again when it finishes
    successfully. What do you see? Why? What happens when you remove the various
    sleep()s in the program?

After running the original proj0.py again immediately, the port number for the client changed. For example the first call, the client port was 43904, and the immediate call after was 43906.

When removing the various sleeps(), sometimes the order of the output would be messed up. For example main would print "done" before the server sent the "got a connection request"