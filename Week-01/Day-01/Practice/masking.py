# Masking phone number except last 4 digits
my_phone_num = "8056129665"
masked_ph_num = "*"*10 + my_phone_num[-4:]
print(masked_ph_num)  # ************9665