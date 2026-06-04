def merge_sort(arr):
    """
    Bo'lib tashla va hukmronlik qil (Divide & Conquer) usuli yordamida
    massivni saralash algoritmi.
    """
    # 1-Asosiy shart: Agar ro'yxatda 1 ta yoki 0 ta element bo'lsa,
    # u allaqachon saralangan hisoblanadi va o'zini qaytaramiz.
    if len(arr) <= 1:
        return arr

    # Ro'yxatning o'rtasini topamiz (indeksini)
    mid = len(arr) // 2

    # Ro'yxatni o'rtasidan ikkiga bo'lib, har bir yarmini
    # rekursiv ravishda yana merge_sort funksiyasiga uzatamiz.
    left_half = merge_sort(arr[:mid])  # Chap yarmi
    right_half = merge_sort(arr[mid:])  # O'ng yarmi

    # Maydalangan va tartiblangan ikki yarimni bir-biriga
    # to'g'ri joylashtirib birlashtiruvchi funksiyaga beramiz.
    return merge(left_half, right_half)


def merge(left, right):
    """
    Ikkita tartiblangan kichik ro'yxatni olib, ularni solishtirib,
    bitta katta tartiblangan ro'yxatga birlashtiruvchi yordamchi funksiya.
    """
    result = []  # Saralangan elementlarni yig'ish uchun bo'sh ro'yxat
    i = j = 0  # i - chap ro'yxat uchun, j - o'ng ro'yxat uchun ko'rsatkichlar (pointer)

    # Ikkala ro'yxatda ham elementlar tugamaguncha sikl davom etadi
    while i < len(left) and j < len(right):
        # Chap tomondagi element kichik bo'lsa, uni natijaga qo'shamiz
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # Chap ro'yxat ko'rsatkichini bittaga suramiz
        # O'ng tomondagi element kichik yoki teng bo'lsa, uni natijaga qo'shamiz
        else:
            result.append(right[j])
            j += 1  # O'ng ro'yxat ko'rsatkichini bittaga suramiz

    # Sikl tugagach, qaysidir ro'yxatda elementlar ortib qolgan bo'lishi mumkin.
    # Ularni to'g'ridan-to'g'ri natijaviy ro'yxatning oxiriga qo'shib qo'yamiz.
    result.extend(left[i:])  # Agar chap ro'yxatda element qolgan bo'lsa
    result.extend(right[j:])  # Agar o'ng ro'yxatda element qolgan bo'lsa

    return result  # Saralangan yakuniy ro'yxatni qaytaramiz


# Dasturni ishga tushirish qismi
if __name__ == "__main__":
    # Sinov uchun tartibsiz sonlar ro'yxati
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Asl (tartibsiz) ro'yxat:", arr)

    # Funksiyani chaqiramiz va natijani chiqaramiz
    sorted_arr = merge_sort(arr)
    print("Saralangan (tartibli) ro'yxat:", sorted_arr)