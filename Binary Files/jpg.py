with open("aswad_purple.png", "rb") as f:
    data= f.read()

with open("asu.txt", "wb") as f:
    f.write(data)
    print("Data written to asu.txt done! ")