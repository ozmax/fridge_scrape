from fridge import Fridge
import multiprocessing

def worker(fridge, page):
    fridge.get_page_data(page)
    
f = Fridge('http://fridge.gr/tag/movies/')

for page in range(1, 75):
    p = multiprocessing.Process(target=worker, args=(f, page))
    p.start()
