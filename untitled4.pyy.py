import time
import threading

# Program 1
def program1():
    for i in range(5):
        print(f"Program 1 Çıktısı: {i}")
        time.sleep(0.5)  

# Program 2
def program2():
    for i in range(5):
        print(f"Program 2 Çıktısı: {i}")
        time.sleep(0.5)  

thread1 = threading.Thread(target=program1)
thread2 = threading.Thread(target=program2)

# Thread'leri başlat
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Tamamlandı!")

