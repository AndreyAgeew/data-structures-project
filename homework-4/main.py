from src.queue import Queue

if __name__ == '__main__':
    # Создаем пустую очередь
    queue = Queue()

    # Добавляем данных в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    print(queue)

