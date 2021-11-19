def make_pizza(size, *t):
    print(f"制作的尺寸是 {size} 大的pizza，配料有：")
    for to in t:
        print(f"-{to}")
