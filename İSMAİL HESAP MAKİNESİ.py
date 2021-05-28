giriş = """
1=topla
2=çıkar 
3=çarp
4=böl
5=karesini hesapla
6=karekök hesapla
"""

print("MİLLİ HESAP MAKİNESİNE HOŞGELDİNİZ",giriş)
anahtar = 1

islem = input("Yapmak istediğiniz işlemi seçiniz : ")

if islem == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı girin" ))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

elif islem == "2":
    sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
    sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
    print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

elif islem == "3":
    sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
    sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
    print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

elif islem == "4":
    sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
    sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
    print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

elif islem == "5":
    sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
    print(sayı9, "sayısının karesi =", sayı9 ** 2)

elif islem == "6":
    sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
    print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

else:
    print("Yanlış giriş.")
    print("Aşağıdaki seçeneklerden birini giriniz:", giriş)