from queue import Queue

queue = Queue()
id = 0


class Request:

    def __init__(self, value):
        self.value = value
        self.id = None

    def __str__(self):
        return str(self.value)

    def setId(self, id):
        self.id = id


def queue_to_string():
    temp_list = []

    while not queue.empty():
        item = queue.get()
        temp_list.append(str(item))

    for item in temp_list:
        queue.put(Request(item))

    return ', '.join(temp_list)


def generate_requests(request: Request):
    global id
    request.setId(id)
    id = id+1
    return queue.put(request)


def process_request():
    if not queue.empty():
        queue.get()
        return queue_to_string()
    else:
        print("Черга пуста")


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    sentense = " ".join(args)
    return cmd, sentense


def main():

    while True:
        command, *args = parse_input(input())

        if command in ['break', 'stop', 'exit']:
            break
        if command in ['generate']:
            request = Request(args[0])
            generate_requests(request)
            print("Generated!")
        if command in ['process']:
            print(f"Request processed: {process_request()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
