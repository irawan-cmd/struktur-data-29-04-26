# struktur-data-29-04-26

# 🎫 Ticket Counter Simulation — Latihan Bab 8

Proyek ini merupakan implementasi simulasi antrian loket tiket menggunakan struktur data **Queue ADT** berbasis Python. Dibuat sebagai bagian dari latihan Bab 8 mata kuliah Struktur Data.

---

## 📋 Deskripsi

Program ini mensimulasikan sistem antrian pada loket tiket, di mana penumpang datang secara acak dan dilayani oleh sejumlah agen tiket. Simulasi mencatat rata-rata waktu tunggu, jumlah penumpang yang dilayani, dan sisa antrian.

---

## 📁 Struktur File

```
├── queue_adt.py       # Implementasi Queue ADT
├── people.py          # Kelas Passenger dan TicketAgent
├── ticket_sim.py      # Kelas utama TicketCounterSimulation
└── README.md
```

---

## ⚙️ Cara Kerja Simulasi

Simulasi berjalan per satuan waktu dengan tiga aturan utama:

| Rule | Metode | Deskripsi |
|------|--------|-----------|
| #1 | `_handleArrival` | Penumpang datang berdasarkan probabilitas `1 / betweenTime` |
| #2 | `_handleBeginService` | Agent bebas mengambil penumpang dari antrian |
| #3 | `_handleEndService` | Agent yang selesai dibebaskan kembali |

---

## 🚀 Cara Menjalankan

```python
from ticket_sim import TicketCounterSimulation

sim = TicketCounterSimulation(
    numAgents=2,
    numMinutes=100,
    betweenTime=2,
    serviceTime=3
)
sim.run()
sim.printResults()
```

**Output contoh:**
```
Number of passengers served    = 47
Number of passengers remaining = 4
The average wait time was        4.15 minutes.
```

---

## 📊 Kompleksitas Waktu

| Operasi | Kompleksitas | Keterangan |
|---------|-------------|------------|
| `__init__` | O(n) | Inisialisasi n agen |
| `run` | O(m × n) | m waktu × n agen |
| `printResults` | O(1) | Hanya aritmatika |
| `_handleArrival` | O(1) | Satu operasi enqueue |
| `_handleBeginService` | O(n) | Scan semua agen |
| `_handleEndService` | O(n) | Scan semua agen |

---

## 🧪 Latihan yang Dikerjakan

### Soal 2 — Eksekusi Manual Enqueue
```python
values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)
# Hasil: [0, 3, 6, 9, 12, 15]
```

### Soal 3 — Eksekusi Manual Enqueue + Dequeue
```python
values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)
    elif i % 4 == 0:
        values.dequeue()
# Hasil: [6, 9, 12, 15]
```

### Soal 6 — Fungsi Membalik Queue
```python
def reverseQueue(queue):
    stack = []
    while not queue.isEmpty():
        stack.append(queue.dequeue())
    while stack:
        queue.enqueue(stack.pop())
    return queue

# Input  : [10, 20, 30, 40, 50]
# Output : [50, 40, 30, 20, 10]
```
> Kompleksitas: **O(n)** — setiap item diproses tepat dua kali.

---

## 📈 Hasil Eksperimen (Soal 5 — Versi Detik)

| Agents | Seconds | Between (s) | Service (s) | Avg Wait (s) | Served | Remaining |
|--------|---------|-------------|-------------|-------------|--------|-----------|
| 2 | 6000 | 120 | 180 | 50.20 | 51 | 0 |
| 2 | 30000 | 120 | 180 | 122.60 | 255 | 0 |
| 2 | 6000 | 120 | 240 | 172.62 | 48 | 3 |
| 2 | 30000 | 120 | 240 | 709.41 | 238 | 17 |
| 3 | 6000 | 120 | 240 | 18.92 | 51 | 0 |
| 3 | 30000 | 120 | 240 | 42.51 | 255 | 0 |

> **Kesimpulan:** Menambah jumlah agen secara signifikan mengurangi waktu tunggu dan sisa antrian, terutama saat service time tinggi.

---

## 🛠️ Requirements

- Python 3.x
- Tidak memerlukan library eksternal
