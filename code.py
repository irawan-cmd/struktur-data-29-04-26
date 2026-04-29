class Queue:
    def __init__(self):
        self._data = []
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        return self._data.pop(0)
    def isEmpty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def __repr__(self):
        return str(self._data)

# Soal 2
values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)

print("Soal 2 - Isi Queue:", values)
# Output: [0, 3, 6, 9, 12, 15]

#-----------------------------------------------------------------------

# Soal 3
values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)
    elif i % 4 == 0:
        values.dequeue()

print("Soal 3 - Isi Queue:", values)
# Output: [6, 9, 12, 15]

#-----------------------------------------------------------------------

print("Soal 6 - Reverse Queue")
def reverseQueue(queue):
    stack = []
    # Keluarkan semua isi queue ke stack
    while not queue.isEmpty():
        stack.append(queue.dequeue())
    # Masukkan kembali dari stack ke queue (urutan terbalik)
    while stack:
        queue.enqueue(stack.pop())
    return queue

# Uji coba
q = Queue()
for val in [10, 20, 30, 40, 50]:
    q.enqueue(val)

print("Sebelum dibalik:", q)
reverseQueue(q)
print("Sesudah dibalik :", q)
# Sebelum: [10, 20, 30, 40, 50]
# Sesudah : [50, 40, 30, 20, 10]
