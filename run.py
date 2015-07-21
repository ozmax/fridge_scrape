from fridge import Fridge

f = Fridge('http://fridge.gr/tag/movies/')

f.get_page_limit()
f.loop_pages()
f.loop_links()
