from json import dump, load

покупатель = load(open('покупатель'))
магазин = load(open('магазин'))
продажа = load(open('продажа'))

print (покупатель , магазин, продажа)