match = ["bedhellohaitryjackfeihl"]

pat = input("Enter to Find: ")

for word in match:
    for i in range(len(word) - len(pat) + 1):
        if word[i:i+len(pat)] == pat:
            in_ = i
            out_ = i + len(pat) - 1
            print(f"Match from index {in_} to index {out_}, length of word is {len(pat)}")
            break
    else:
        continue
    break
else:
    print("Not match!")