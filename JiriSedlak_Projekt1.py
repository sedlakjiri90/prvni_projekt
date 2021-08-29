text1 = """Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley."""

text2 = """At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick."""

text3 = """The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present."""

cara = "-" * 40
user1 = "bob"
password1 = "123"
user2 = "ann"
password2 = "pass123"
user3 = "mike"
password3 = "password123"
user4 = "liz"
password4 = "pass123"

user = input("Username:")
password = input("Password:")

if user == user1 and password == password1 \
        or user == user2 and password == password2 \
        or user == user3 and password == password3 \
        or user == user4 and password == password4:
    print(cara, "\n"
                "Welcome to the app, ", user, "\n"
                                              "We have 3 texts to be analyzed.")
    print(cara)
else:
    print("Invalid username or password")
    quit()

num = int(input("Enter a number btw. 1 and 3 to select:"))
print(cara)

if num == 1:
    words = len(text1.split())
    print("There are", words, "words in the selected text.")
    # There are 12 titlecase words
    x1 = [str(s) for s in text1.split() if s[0].isupper()]
    tcw = len(x1)
    print("There are", tcw, "titlecase words.")
    # There are 1 uppercase words
    x2 = [str(s) for s in text1.split() if s.isupper()]
    x1 = [str(x) for x in x2 if not any(c.isdigit() for c in x)]
    ucw = len(x1)
    print("There are", ucw, "uppercase words.")
    # There are 38 lowercase words
    x3 = [str(s) for s in text1.split() if s.islower()]
    lcw = len(x3)
    print("There are", lcw, "lowercase words.")
    # There are 3 numeric strings
    i = [int(s) for s in text1.split() if s.isdigit()]
    nstr = len(i)
    print("There are", nstr, "numeric strings.")
    # The sum of all numbers 8510
    i2 = [int(s) for s in text1.split() if s.isdigit()]
    snum = sum(i2)
    print("The sum of all numbers", snum)

    newtext1 = text1.replace(".", " ")
    new_text1 = newtext1.replace(",", " ")

    l1 = [str(s) for s in new_text1.split() if len(s) == 1]
    l2 = [str(s) for s in new_text1.split() if len(s) == 2]
    l3 = [str(s) for s in new_text1.split() if len(s) == 3]
    l4 = [str(s) for s in new_text1.split() if len(s) == 4]
    l5 = [str(s) for s in new_text1.split() if len(s) == 5]
    l6 = [str(s) for s in new_text1.split() if len(s) == 6]
    l7 = [str(s) for s in new_text1.split() if len(s) == 7]
    l8 = [str(s) for s in new_text1.split() if len(s) == 8]
    l9 = [str(s) for s in new_text1.split() if len(s) == 9]
    l10 = [str(s) for s in new_text1.split() if len(s) == 10]
    l11 = [str(s) for s in new_text1.split() if len(s) == 11]

    len1 = "1|"
    len2 = "2|"
    len3 = "3|"
    len4 = "4|"
    len5 = "5|"
    len6 = "6|"
    len7 = "7|"
    len8 = "8|"
    len9 = "9|"
    len10 = "10|"
    len11 = "11|"

    occur1 = "*" * len(l1)
    occur2 = "*" * len(l2)
    occur3 = "*" * len(l3)
    occur4 = "*" * len(l4)
    occur5 = "*" * len(l5)
    occur6 = "*" * len(l6)
    occur7 = "*" * len(l7)
    occur8 = "*" * len(l8)
    occur9 = "*" * len(l9)
    occur10 = "*" * len(l10)
    occur11 = "*" * len(l11)

    nr1 = ("|" + str(len(l1)))
    nr2 = ("|" + str(len(l2)))
    nr3 = ("|" + str(len(l3)))
    nr4 = ("|" + str(len(l4)))
    nr5 = ("|" + str(len(l5)))
    nr6 = ("|" + str(len(l6)))
    nr7 = ("|" + str(len(l7)))
    nr8 = ("|" + str(len(l8)))
    nr9 = ("|" + str(len(l9)))
    nr10 = ("|" + str(len(l10)))
    nr11 = ("|" + str(len(l11)))

    print(cara)
    len = "LEN|"
    occur = "OCCURENCES"
    nr = "|NR."
    print(f"{len : <3}{occur : ^20}{nr : >3}")
    print(cara)
    print(f"{len1 : >4}{occur1 : <20}{nr1 : >2}")
    print(f"{len2 : >4}{occur2 : <20}{nr2 : >2}")
    print(f"{len3 : >4}{occur3 : <20}{nr3 : >2}")
    print(f"{len4 : >4}{occur4 : <20}{nr4 : >2}")
    print(f"{len5 : >4}{occur5 : <20}{nr5 : >2}")
    print(f"{len6 : >4}{occur6 : <20}{nr6 : >2}")
    print(f"{len7 : >4}{occur7 : <20}{nr7 : >2}")
    print(f"{len8 : >4}{occur8 : <20}{nr8 : >2}")
    print(f"{len9 : >4}{occur9 : <20}{nr9 : >2}")
    print(f"{len10 : >4}{occur10 : <20}{nr10 : >2}")
    print(f"{len11 : >4}{occur11 : <20}{nr11 : >2}")



elif num == 2:
    words = len(text2.split())
    print("There are", words, "words in the selected text.")

    x1 = [str(s) for s in text2.split() if s[0].isupper()]
    tcw = len(x1)
    print("There are", tcw, "titlecase words.")

    x2 = [str(s) for s in text2.split() if s.isupper()]
    x1 = [str(x) for x in x2 if not any(c.isdigit() for c in x)]
    ucw = len(x1)
    print("There are", ucw, "uppercase words.")

    x3 = [str(s) for s in text2.split() if s.islower()]
    lcw = len(x3)
    print("There are", lcw, "lowercase words.")

    i = [int(s) for s in text2.split() if s.isdigit()]
    nstr = len(i)
    print("There are", nstr, "numeric strings.")

    i2 = [int(s) for s in text2.split() if s.isdigit()]
    snum = sum(i2)
    print("The sum of all numbers", snum)

    newtext2 = text2.replace(".", " ")
    new_text2 = newtext2.replace(",", " ")

    l1 = [str(s) for s in new_text2.split() if len(s) == 1]
    l2 = [str(s) for s in new_text2.split() if len(s) == 2]
    l3 = [str(s) for s in new_text2.split() if len(s) == 3]
    l4 = [str(s) for s in new_text2.split() if len(s) == 4]
    l5 = [str(s) for s in new_text2.split() if len(s) == 5]
    l6 = [str(s) for s in new_text2.split() if len(s) == 6]
    l7 = [str(s) for s in new_text2.split() if len(s) == 7]
    l8 = [str(s) for s in new_text2.split() if len(s) == 8]
    l9 = [str(s) for s in new_text2.split() if len(s) == 9]
    l10 = [str(s) for s in new_text2.split() if len(s) == 10]
    l11 = [str(s) for s in new_text2.split() if len(s) == 11]

    len1 = "1|"
    len2 = "2|"
    len3 = "3|"
    len4 = "4|"
    len5 = "5|"
    len6 = "6|"
    len7 = "7|"
    len8 = "8|"
    len9 = "9|"
    len10 = "10|"
    len11 = "11|"

    occur1 = "*" * len(l1)
    occur2 = "*" * len(l2)
    occur3 = "*" * len(l3)
    occur4 = "*" * len(l4)
    occur5 = "*" * len(l5)
    occur6 = "*" * len(l6)
    occur7 = "*" * len(l7)
    occur8 = "*" * len(l8)
    occur9 = "*" * len(l9)
    occur10 = "*" * len(l10)
    occur11 = "*" * len(l11)

    nr1 = ("|" + str(len(l1)))
    nr2 = ("|" + str(len(l2)))
    nr3 = ("|" + str(len(l3)))
    nr4 = ("|" + str(len(l4)))
    nr5 = ("|" + str(len(l5)))
    nr6 = ("|" + str(len(l6)))
    nr7 = ("|" + str(len(l7)))
    nr8 = ("|" + str(len(l8)))
    nr9 = ("|" + str(len(l9)))
    nr10 = ("|" + str(len(l10)))
    nr11 = ("|" + str(len(l11)))

    print(cara)
    len = "LEN|"
    occur = "OCCURENCES"
    nr = "|NR."
    print(f"{len : <3}{occur : ^20}{nr : >3}")
    print(cara)
    print(f"{len1 : >4}{occur1 : <20}{nr1 : >2}")
    print(f"{len2 : >4}{occur2 : <20}{nr2 : >2}")
    print(f"{len3 : >4}{occur3 : <20}{nr3 : >2}")
    print(f"{len4 : >4}{occur4 : <20}{nr4 : >2}")
    print(f"{len5 : >4}{occur5 : <20}{nr5 : >2}")
    print(f"{len6 : >4}{occur6 : <20}{nr6 : >2}")
    print(f"{len7 : >4}{occur7 : <20}{nr7 : >2}")
    print(f"{len8 : >4}{occur8 : <20}{nr8 : >2}")
    print(f"{len9 : >4}{occur9 : <20}{nr9 : >2}")
    print(f"{len10 : >4}{occur10 : <20}{nr10 : >2}")
    print(f"{len11 : >4}{occur11 : <20}{nr11 : >2}")



elif num == 3:
    words = len(text3.split())
    print("There are", words, "words in the selected text.")
    # There are 12 titlecase words
    x1 = [str(s) for s in text3.split() if s[0].isupper()]
    tcw = len(x1)
    print("There are", tcw, "titlecase words.")
    # There are 1 uppercase words
    x2 = [str(s) for s in text3.split() if s.isupper()]
    x1 = [str(x) for x in x2 if not any(c.isdigit() for c in x)]
    ucw = len(x1)
    print("There are", ucw, "uppercase words.")
    # There are 38 lowercase words
    x3 = [str(s) for s in text3.split() if s.islower()]
    lcw = len(x3)
    print("There are", lcw, "lowercase words.")
    # There are 3 numeric strings
    i = [int(s) for s in text3.split() if s.isdigit()]
    nstr = len(i)
    print("There are", nstr, "numeric strings.")
    # The sum of all numbers 8510
    i2 = [int(s) for s in text3.split() if s.isdigit()]
    snum = sum(i2)
    print("The sum of all numbers", snum)

    newtext3 = text3.replace(".", " ")
    new_text3 = newtext3.replace(",", " ")

    l1 = [str(s) for s in new_text3.split() if len(s) == 1]
    l2 = [str(s) for s in new_text3.split() if len(s) == 2]
    l3 = [str(s) for s in new_text3.split() if len(s) == 3]
    l4 = [str(s) for s in new_text3.split() if len(s) == 4]
    l5 = [str(s) for s in new_text3.split() if len(s) == 5]
    l6 = [str(s) for s in new_text3.split() if len(s) == 6]
    l7 = [str(s) for s in new_text3.split() if len(s) == 7]
    l8 = [str(s) for s in new_text3.split() if len(s) == 8]
    l9 = [str(s) for s in new_text3.split() if len(s) == 9]
    l10 = [str(s) for s in new_text3.split() if len(s) == 10]
    l11 = [str(s) for s in new_text3.split() if len(s) == 11]

    len1 = "1|"
    len2 = "2|"
    len3 = "3|"
    len4 = "4|"
    len5 = "5|"
    len6 = "6|"
    len7 = "7|"
    len8 = "8|"
    len9 = "9|"
    len10 = "10|"
    len11 = "11|"

    occur1 = "*" * len(l1)
    occur2 = "*" * len(l2)
    occur3 = "*" * len(l3)
    occur4 = "*" * len(l4)
    occur5 = "*" * len(l5)
    occur6 = "*" * len(l6)
    occur7 = "*" * len(l7)
    occur8 = "*" * len(l8)
    occur9 = "*" * len(l9)
    occur10 = "*" * len(l10)
    occur11 = "*" * len(l11)

    nr1 = ("|" + str(len(l1)))
    nr2 = ("|" + str(len(l2)))
    nr3 = ("|" + str(len(l3)))
    nr4 = ("|" + str(len(l4)))
    nr5 = ("|" + str(len(l5)))
    nr6 = ("|" + str(len(l6)))
    nr7 = ("|" + str(len(l7)))
    nr8 = ("|" + str(len(l8)))
    nr9 = ("|" + str(len(l9)))
    nr10 = ("|" + str(len(l10)))
    nr11 = ("|" + str(len(l11)))

    print(cara)
    len = "LEN|"
    occur = "OCCURENCES"
    nr = "|NR."
    print(f"{len : <3}{occur : ^20}{nr : >3}")
    print(cara)
    print(f"{len1 : >4}{occur1 : <20}{nr1 : >2}")
    print(f"{len2 : >4}{occur2 : <20}{nr2 : >2}")
    print(f"{len3 : >4}{occur3 : <20}{nr3 : >2}")
    print(f"{len4 : >4}{occur4 : <20}{nr4 : >2}")
    print(f"{len5 : >4}{occur5 : <20}{nr5 : >2}")
    print(f"{len6 : >4}{occur6 : <20}{nr6 : >2}")
    print(f"{len7 : >4}{occur7 : <20}{nr7 : >2}")
    print(f"{len8 : >4}{occur8 : <20}{nr8 : >2}")
    print(f"{len9 : >4}{occur9 : <20}{nr9 : >2}")
    print(f"{len10 : >4}{occur10 : <20}{nr10 : >2}")
    print(f"{len11 : >4}{occur11 : <20}{nr11 : >2}")
else:
    print("Incorrect number! You have been logged out.")



