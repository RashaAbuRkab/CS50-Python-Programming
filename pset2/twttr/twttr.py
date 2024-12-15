txt = input("Input: ").strip()
output=""
for i in txt:
    if i.upper() not in "AEIOU" :
        output+= i
print(f"Output: {output}")
