# TODO Найдите количество книг, которое можно разместить на дискете

volume_string = 4 * 25
volume_list = 50 * volume_string
volume_book = 100 * volume_list
volume_disk = 1.44 * 1024 * 1024
cout_book = int(volume_disk // volume_book)

print("Количество книг, помещающихся на дискету:", cout_book)