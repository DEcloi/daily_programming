class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        if not self.queue:
            return None

        return_data = self.queue[0]

        for index, data in enumerate(self.queue[1:]):
            self.queue[index] = data
        self.queue.pop()

        return return_data


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.push(6)
queue.push(7)

print(f'Pop data: {queue.pop()}')
