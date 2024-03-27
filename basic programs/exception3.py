try:
    klu1 = open("file.txt","w+")
    try:
        klu1.write("xyzThis is s17 Section crt class")
    finally:
        klu1.close()
except IOError:
 print("file not found")
else:
    print("the file opened successfully")
    klu1.close