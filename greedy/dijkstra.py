import heapq  # Ustuvorlik navbati (Priority Queue) bilan ishlash uchun kutubxona


def dijkstra(graph, start):
    """
    Dijkstra algoritmi - Yo'naltirilgan/yo'naltirilmagan vaznli grafda
    bitta nuqtadan boshqa barcha nuqtalargacha bo'lgan eng qisqa masofani topadi.
    """

    # 1. Barcha tugunlargacha bo'lgan masofani cheksiz (inf) deb belgilaymiz.
    # Masalan: {'A': inf, 'B': inf, 'C': inf, 'D': inf}
    distances = {node: float('inf') for node in graph}

    # Boshlang'ich tugunning o'zigacha bo'lgan masofani 0 qilamiz.
    # Masalan, 'A' dan boshlasak: {'A': 0, 'B': inf, ...}
    distances[start] = 0

    # Ustuvorlik navbatini yaratamiz. Ichiga (masofa, tugun) ko'rinishida ma'lumot solamiz.
    # Boshlanishiga navbatda faqat boshlang'ich tugun bo'ladi: [(0, 'A')]
    priority_queue = [(0, start)]

    # Navbatda elementlar tugaguncha sikl davom etadi
    while priority_queue:
        # Navbatdan hozirgi vaqtda eng yaqin (masofasi eng kichik) bo'lgan tugunni sug'urib olamiz.
        # heapq.heappop har doim eng kichik masofaligini birinchi chiqaradi.
        current_distance, current_node = heapq.heappop(priority_queue)

        # AGAR navbatdan olingan masofa, biz avvalroq topgan eng qisqa masofadan
        # kattaroq bo'lsa, bu tugunni tekshirib o'tirmasdan tashlab ketamiz (skip qilamiz).
        if current_distance > distances[current_node]:
            continue

        # Hozirgi tugunning barcha qo'shnilarini birma-bir ko'rib chiqamiz.
        # graph[current_node].items() -> qo'shni nomi (neighbor) va unga bo'lgan masofa (weight)
        for neighbor, weight in graph[current_node].items():
            # Boshlang'ich nuqtadan hozirgi tugungacha bo'lgan masofaga
            # qo'shnigacha bo'lgan masofani qo'shamiz (Yangi muqobil yo'l)
            distance = current_distance + weight

            # Agar bu yangi topilgan yo'l, shu paytgacha ushbu qo'shniga
            # borish uchun topilgan yo'ldan qisqaroq bo'lsa:
            if distance < distances[neighbor]:
                # Qo'shnigacha bo'lgan eng qisqa masofani yangilaymiz
                distances[neighbor] = distance
                # Bu qo'shnini va yangi masofani navbatga qo'shamiz,
                # chunki uning orqali boshqa tugunlarga ham yo'l qisqarishi mumkin.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Barcha tugunlar tekshirib bo'lingach, eng qisqa masofalar lug'atini qaytaramiz.
    return distances


# Dasturni ishga tushirish (Test) qismi
if __name__ == "__main__":
    # Grafni lug'at (dictionary) ko'rinishida e'lon qilamiz.
    # Har bir harf - shahar, ichidagi harflar va sonlar - qaysi shaharga qancha masofada borish mumkinligi.
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Algoritmni 'A' nuqtadan boshlab ishga tushiramiz
    natija = dijkstra(graph, 'A')

    # Natijani ekranga chiqaramiz
    print("A nuqtadan boshqa barcha nuqtalargacha eng qisqa masofalar:")
    print(natija)