import random

names = ["Tom Humbles",
"Amy Shaw",
"Sanjeet Chatterjee",
"Zev Cooper-Bennun",
"Oscar Berry",
"Edwin Shepherd",
"Toby Newey",
"Pralish Satyal",
"Annie Noonari",
"Murats Seidovs",
"Arnav Koshy",
"Aly Champion",
"Florence Miller",
"James Granville",
"Ellison Linsley",
"Loreta Paliakaite",
"Sarah Berry",
"Ellie Gaggs",
"Arunav Bagla"]

emails = ["TH127675@hillsroad.ac.uk",
"As128203@hillsroad.ac.uk",
"sc129263@hrsfc.ac.uk",
"zc127309@hillsroad.ac.uk",
"origamidos@gmail.com",
"es128207@hrsfc.ac.uk",
"TN130031@hillsroad.ac.uk",
"PS128179@hrsfc.ac.uk",
"an130043@hrsfc.ac.uk",
"MS130286@hillsroad.ac.uk",
"AK129817@hrsfc.ac.uk",
"ac129249@hillsroad.ac.uk",
"FM127909@hrsfc.ac.uk",
"jg128508@hrsfc.ac.uk",
"el129876@hillsroad.ac.uk",
"LP130085@hrsfc.ac.uk",
"SB128488@hrsfc.ac.uk",
"ellie.gaggs@gmail.com",
"AB129068@hillsroad.ac.uk"]

people = []

for i in range(0, len(names)):
    people.append((names[i],emails[i]))

print("----------------PEOPLE GOING----------------")

random.seed()

for i in range(0,14):
    person_going = people.pop(random.randint(0, len(people)-1))
    print(i + 1, ' :', person_going[0])