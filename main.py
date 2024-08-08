tvShow = input("What is your favorite tv show? ")
if tvShow.lower() == "justice league":
  print("Ah, the animated version of the show!")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter.lower() == "superman":
    print("League's Leader!")
    y_sup = input("Why do you like Superman? ")
    qualities = ["best","strongest"]
    if any(quality in y_sup.lower() for quality in qualities):
      print("You are a true Superman fan!")
    else:
      print("oh, I dont know that.")
  else:
    print("Nah, Superman's the best!")
elif tvShow.lower() == "paw patrol":
  print("Aww, sad times")
elif "dora" in tvShow.lower():
    print("Swiper stop swiping!!!")
elif tvShow.lower() == "you":
  joe = input("So, Joe was right or wrong? ")
  if joe.lower() == "right":
    print("You are a Creep!")
  else:
    print("Thats it!")
else:
  print("Yeah, that's cool and all…")