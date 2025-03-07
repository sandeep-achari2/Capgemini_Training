# import threading   #1
# import time  #2

# print("Main thread started:")
# def single_task():
#     print("Task started")#4
#     time.sleep(2)#5
#     print("Task completed")#6
    
# time.sleep(5)
# thread=threading.Thread(target=single_task) #3
# thread.start()#4
# #thread.join()#7
# print("Main thread")#8

# import threading
# import time

# def attending_college():
#     for i in range(0,10):
#         time.sleep(1)
#         if i%2==0:
#             print(f"{i} Sandeep is coming")
#     time.sleep(2)
#     print("Harish is coming")
    
# time.sleep(2)

# def not_attending():
#     for i in range(0,10):
#         if i%2!=0:
#             time.sleep(1)
#             print(f"{i} Deepu is not attending")
#     time.sleep(1)
    
# thread=threading.Thread(target=attending_college)
# thread2=threading.Thread(target=not_attending)
# thread.start()
# thread.join()
# thread2.start()
# thread2.join()
# print("Its mandatory to attend college")

# import threading
# import time
# import requests

# def fetch_url(url,results):
#     response=requests.get(url)
#     html_content=response.text
#     results.append(f"fetched {url}:\n {html_content}\n")
    
# urls={
#     "https://example.com"
# }
# threads=[]
# results=[]

# for url in urls:
#     thread=threading.Thread(target=fetch_url,args=(url,results))
#     threads.append(thread)
#     thread.start()
    
# for thread in threads:
#     thread.join()
    
# # for result in results:
# #     print(result)
    
# print("All urls fetched")

# with open("context.html","w") as file:
#         for result in results:
#              file.write(result)


import threading
import requests
def scrape_website(url,results):
    response=requests.get(url)
    html_content=response.text
    results.append(f"fetched data from {url}\n and response is {html_content}\n")
url=[
    "https://www.ibomma.com/"
] 
results=[]
threads=[]
for site in url:
    thread=threading.Thread(target=scrape_website,args=(site,results))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
with open("context3.html","w") as file:
        for result in results:
             file.write(result)

print("All are fetched")

# import threading

# data_chunks = [
#     list(range(1,11)),   
#     list(range(11, 21)),  
#     list(range(21, 31))   
# ]

# def process_data(data):
#     print(f"Processing: {len(data)}")
#     result = sum(data)
#     print(f"Result: {result}")

# for data_chunk in data_chunks:
#     thread = threading.Thread(target=process_data, args=(data_chunk,))
#     thread.start()
#     thread.join() 

# print("All tasks completed.")


# import threading
# import time
# import queue

# def producer(q):
#     for i in range(5):
#         time.sleep(1)
#         q.put(i)
#         print(f'Produced: {i}')
        
# def consumer(q):
#     while True:
#         item=q.get()
#         if item is None:
#             break
#         print(f'Consumed: {item}')
#         time.sleep(2)
        
# q=queue.Queue()
# producer_thread=threading.Thread(target=producer,args=(q,))
# consumer_thread=threading.Thread(target=consumer,args=(q,))

# producer_thread.start()
# consumer_thread.start()

# producer_thread.join()
# q.put(None)
# consumer_thread.join()
# print("Thread communication completed")

# import threading
# import time

# def task(lock):
#     with lock:
#         print(f'{threading.current_thread().name} has acqired the lock')
#         time.sleep(2)
#         print(f'{threading.current_thread().name} has released the lock')
#         time.sleep(2)
        
# lock=threading.Lock()
# thread1=threading.Thread(target=task,args=(lock,))
# thread2=threading.Thread(target=task,args=(lock,))

# thread1.start()
# thread2.start()
# thread2.join()
# thread2.join()

#implementing demon
# import threading
# import time
# def task():
#     for i in range(10):
#         print(f'task {i}')
#         time.sleep(2)
        
# thread=threading.Thread(target=task,daemon=True)
# thread.start()
# thread.join()
# print("Main thread execute!!")

# import threading
# import time
# def task():
#     for i in range(10):
#         print(f'task {i}')
#         time.sleep(2)
        
# thread=threading.Thread(target=task)
# thread.start() 
# print("Main thread execute!!")


