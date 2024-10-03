nilai = int(input("Masukkan nilai ujian anda (0-100): "))

if nilai >= 90 : 
    print("Feedback : Sangat Baik")
elif nilai >= 80 :
    print ("Feedback : Baik")
elif nilai >= 70 :
    print ("Feedback : Cukup")
elif nilai >= 60 :
    print ("Feedback : Kurang")
else :
    print ("Feedback : Sangat Kurang")