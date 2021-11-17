magnitude = float(input("What is the magnitude of the earthquake: ")) #asks the user to input the magnitude

if 0 < magnitude < 2.0: #prints out the type of earthquace based on the range that the magnitude is in
    print("micro earthquake")
elif 2.0<= magnitude < 3.0:
    print("very minor earthquake")
elif 3.0<= magnitude < 4.0:
    print("minor earthquake")
elif 4.0<= magnitude < 5.0:
    print("light earthquake")
elif 5.0<= magnitude < 6.0:
    print("moderate earthquake")
elif 6.0<= magnitude < 7.0:
    print("strong earthquake")
elif 7.0<= magnitude < 8.0:
    print("major earthquake")
elif 8.0<= magnitude < 10.0:
    print("great earthquake")
else:
    print("meteoric earthquake")