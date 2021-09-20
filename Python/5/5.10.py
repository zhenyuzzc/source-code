current_users = ['admin','kf','Kpy','xs','ba']
new_users = ['Admin','wkf','kpy','exs','eba']
current = []
for valve in current_users:
    current.append(valve.lower())
for new_user in new_users:
    if new_user.lower() in current:
        print(f"{new_user}已被注册，请输入其它用户名。")
