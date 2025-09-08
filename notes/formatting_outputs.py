# JS, 1st, Formatting Outputs Notes

# how do I write the format method?
name = "baby"
age = .00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
money = 0.01
percent = .67
print("Hello {}, you are {:E}. That is so old. You have ${:.2f} you must be rich! Your percent is {:%}".format(name, age, money))

# :, - adds commas to a number when needed
# :E - puts in scientific notation
# :b - puts in binary
# :.#f - rounds the float to the given number
# :% - turns decimal into percentage

print(f"Hello {name}, you are {age:,}. That is so old! You have ${money:.2f} you must be rich! Random percent is {88/100:.1f}%")