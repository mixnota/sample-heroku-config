all_messages = []

def handle_message(message, nickname="user"):
    '''handles message:
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''
    global all_messages

    message_split = message.split()

    answer = "no command found"
    if message == "\show":
        answer = ""
        for message in all_messages:
            answer += message + '\n'
    elif message_split[0] == "\write":
        answer = ' '.join(message_split[1:])
        all_messages.append(answer)
    return answer


if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)

        print(ans)
