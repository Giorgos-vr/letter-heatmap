print("Το script αυτό υπολογίζει το ποσοστό που το κάθε γράμμα εμφανίζεται σε ένα κείμενο.")


input = (str(input("Παρακαλώ πληκτρολογήστε ή κάντε paste (ctrl+shift+V) το κείμενο σας. (αριθμοί και λατινικοί χαρακτήρες θα αγνοηθούν από τον υπολογισμό): ")))

text = input.lower()
counter = {}
letter_percent = {}

def letter_counter(text):
    for i in text:
        if i in "αβγδεζηθικλμνξοπρστυφχψω":
            counter[i] = text.count(i)
    return counter

print("\nΚαθαρός αριθμός γραμμάτων:")
print(letter_counter(text))


def letter_perc(letter_percent):
    total = sum(counter.values())
    for key,val in counter.items():
        letter_percent[key] = round(val/total * 100, 2)
    return letter_percent


print("\nΠοσοστό εμφάνισης του κάθε γράμματος:")
print(letter_perc(letter_percent))




# for verification purposes we can also print the percentages as unrounded str
#s = sum(counter.values())
#for k, v in counter.items():
#    pct = v * 100.0 / s
#    print(k, pct)




#for verification purposes we can print the raw letter count as a dict
#print(counter)