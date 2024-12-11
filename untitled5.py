import os
import multiprocessing
import time

# Her işlem için çalıştırılacak fonksiyon
def process_task(task_name):
    print(f"İşlem adı: {task_name}, İşlem Kimliği: {os.getpid()}")
    time.sleep(2) 
    print(f"{task_name} tamamlandı!")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=process_task, args=("İşlem 1",))
    process2 = multiprocessing.Process(target=process_task, args=("İşlem 2",))

    # İşlemleri başlat
    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Tüm işlemler tamamlandı!")


