#JS, 1st, Who are You?
code_running = "yes"
user_info = {
    "user_name": "",
    "user_age": 0,
    "user_fav_color": "" 
}
past_names = []
past_ages = []
past_fav_colors = []
def user_input():
    user_info["user_name"] = input("What is your name?\n").capitalize().strip()
    if user_info["user_name"] not in past_names:
        user_info["user_age"] = input("How old are you?\n").strip()
        user_info["user_fav_color"] = input("What is your favorite color?\n").lower().strip()
    else:
        index = past_names.index(user_info["user_name"])
        past_info = input("Would you like to use your past information?\n").lower().strip()
        if past_info == "yes":
            user_info["user_age"] = past_ages[index]
            user_info["user_fav_color"] = past_fav_colors[index]
        else:
            user_info["user_age"] = input("How old are you?\n").strip()
            user_info["user_fav_color"] = input("What is your favorite color?\n").lower().strip()
    print(f"Hi, {user_info["user_name"]}, you are {user_info["user_age"]} years old and your favorite color is {user_info["user_fav_color"]}.")
while code_running == "yes":
    user_input()
    past_names.append(user_info["user_name"])
    past_ages.append(user_info["user_age"])
    past_fav_colors.append(user_info["user_fav_color"])
    code_running = input("Would you like to continue?\n").strip().lower()
    if code_running != "yes":
        exit()
    user_info["user_name"] = ""
    user_info["user_age"] = 0
    user_info["user_fav_color"] = ""