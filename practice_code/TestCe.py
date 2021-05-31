from collections import defaultdict



user_dict = {}
users = ["baoshan1", "baoshan2", "baoshan3","baoshan1", "baoshan2", "baoshan2"]
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1
print(user_dict)


user_dict = defaultdict(int)
users = ["baoshan1", "baoshan2", "baoshan3","baoshan1", "baoshan2", "baoshan2"]
for user in users:
    user_dict[user] += 1
print(user_dict)


user_dict = {}
users = ["baoshan1", "baoshan2", "baoshan3","baoshan1", "baoshan2", "baoshan2"]
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1
print(user_dict)