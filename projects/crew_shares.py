# JS, 1st, Crew Shares 
print("\033c", end="")
total_money = int(input("How much money (in total) did you get from the excursion?\n ").strip().strip("$"))
crew_members = int(input("How many crew members? (Does not include Captain and First Mate)\n "))
share = total_money/(crew_members+10)
crew_remainder = share - 500
first_mate = share * 3
captain = share * 7
print("\033c", end="")
print(f"The captain gets ${captain:.2f}.\nThe first mate gets ${first_mate:.2f}.\nThe crew still needs ${crew_remainder:.2f} to each of them.")