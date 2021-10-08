def show_messages(txt):
        print(txt)

def send_messages(txt,sent):
    while txt:
        value = txt.pop()
        print(value)
        sent.append(value)

t = ['您好','看这里','有没有','很喜欢','太棒了']
sent_messages = []

send_messages(t[:],sent_messages)
show_messages(t)
show_messages(sent_messages)