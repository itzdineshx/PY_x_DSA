#Check the room for tenants
ac_veg_rent = 5000
ac_non_veg_rent = 4000
non_ac_veg_rent = 3000
non_ac_non_veg_rent = 2000

#Applied amout based on user Requirements
ac = input("want ac or non-ac Room?: ")
food = input("want Veg or non-veg?: ")
if (ac == "ac"):
    if (food == "veg"):
        print("Your room rent is {}".format(ac_veg_rent))
    else:
        print("Your room rent is {}".format(ac_non_veg_rent))
else:
    if (food == "veg"):
        print("Your room rent is {}".format(non_ac_veg_rent))
    else:
        print("Your room rent is {}".format(non_ac_non_veg_rent))

        