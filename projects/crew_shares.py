# JS, 1st, Crew Shares
total_money, crew_members = [int(input("How much money (in total) did you get from the excursion?\n ").strip().strip("$")), int(input("How many crew members? (Does not include Captain and First Mate)\n ").strip())]
share = total_money/(crew_members+10)
crew_remainder, first_mate, captain = [share - 500, share * 3, share * 7]
print(f"The captain gets ${captain:.2f}.\nThe first mate gets ${first_mate:.2f}.\nThe crew still needs ${crew_remainder:.2f} to each of them.")