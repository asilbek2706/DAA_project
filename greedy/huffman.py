import random


def quick_sort(arr):
    """
    Tezkor saralash (Quick Sort) algoritmi.
    """
    # 1. Asosiy shart: Agar ro'yxatda 1 ta yoki 0 ta element bo'lsa,
    # u allaqachon saralangan bo'ladi va uni to'g'ridan-to'g'ri qaytaramiz.
    if len(arr) <= 1:
        return arr

    # 2. Tayanch element (Pivot) tanlash:
    # Ro'yxat ichidan tasodifiy bitta elementni "tayanch" (orta nuqta) qilib olamiz.
    # Bu yomon holatlardan (Worst-case) qochishga yordam beradi.
    pivot = random.choice(arr)

    # 3. Uchta guruhga ajratish (List Comprehension orqali):
    # left: Tayanch elementdan kichik bo'lgan barcha sonlar
    left = [x for x in arr if x < pivot]

    # middle: Tayanch elementga teng bo'lgan barcha sonlar
    middle = [x for x in arr if x == pivot]

    # right: Tayanch elementdan katta bo'lgan barcha sonlar
    right = [x for x in arr if x > pivot]

    # 4. Rekursiya va Birlashtirish:
    # Kichiklar (left) va kattalar (right) guruhini yana qaytadan quick_sort'ga beramiz.
    # Oxirida ularni tartib bilan [kichiklar] + [tenglar] + [kattalar] qilib yopishtiramiz.
    return quick_sort(left) + middle + quick_sort(right)


# Dasturni ishga tushirish qismi
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Asl ro'yxat:", arr)
    print("Saralangan ro'yxat:", quick_sort(arr))