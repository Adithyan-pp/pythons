#order_summary

orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

order_count={}

for iteam in orders:

    if iteam in order_count:

        order_count[iteam]+=1
    else:

         order_count[iteam]=1

print(order_count)

#print character count
text="ABBACB"

character_count={}

for ch in text:

    if ch in character_count:

        character_count[ch]+=1

    else:

        character_count[ch]=1

print(character_count)