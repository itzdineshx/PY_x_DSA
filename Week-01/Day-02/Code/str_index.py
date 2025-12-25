# Indexing in strings 
# String Indexing and Slicing [Start:End:Step]
s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n'
print(s[1:4])    # 'yth'
print(s[::-1])   # Reverse: 'nohtyP'

credit_card = "1234-5678-9101-1121"
print(credit_card[4:])
print(credit_card[5:9])
print(credit_card[:4])
print(f"xxxx-xxxx-xxxx-{credit_card[-4:]}")
print(credit_card)  # Every second character
credit_card = credit_card[::-1]
print(credit_card)
