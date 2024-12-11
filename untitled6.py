import os
import threading
import multiprocessing

# Çoklu programlama (iş parçacıkları)
def thread_task():
    print(f"Thread ID: {threading.get_ident()}, Process ID: {os.getpid()}")

# Çoklu işlem
def process_task():
    print(f"Process ID: {os.getpid()}")

def coklu_programlama():
    threads = []
    for _ in range(3):  # 3 iş parçacığı oluştur
        thread = threading.Thread(target=thread_task)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def coklu_islemci():
    processes = []
    for _ in range(3):  # 3 işlem oluştur
        process = multiprocessing.Process(target=process_task)
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

if __name__ == "__main__":
    print("Çoklu Programlama (Threads):")
    coklu_programlama()
    
    print("\nÇoklu İşlemci (Processes):")
    coklu_islemci()


