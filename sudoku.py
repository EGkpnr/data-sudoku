# pylint: disable=missing-docstring


def sudoku_validator(grid):
    """
    Verilen 9x9 Sudoku gridinin geçerli olup olmadığını kontrol eder.
    Satırlar, sütunlar ve 3x3 kutuların hepsi 1-9 arası sayıları içermelidir.
    """
    # Bir satırın/sütunun geçerli olması için sahip olması gereken küme
    valid_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 1. SATIR KONTROLÜ (ROWS)
    for row in grid:
        # Satırı kümeye çevir (tekrarları siler) ve valid_set ile kıyasla
        if set(row) != valid_set:
            return False

    # 2. SÜTUN KONTROLÜ (COLUMNS)
    # 0'dan 8'e kadar her sütun indeksi için dönüyoruz
    for col_index in range(9):
        column = []
        for row in grid:
            # Her satırın o anki sütunundaki elemanı alıyoruz
            column.append(row[col_index])

        if set(column) != valid_set:
            return False

    # 3. 3x3 KUTU KONTROLÜ (BOXES)
    # Kutuların sol üst köşeleri: (0,0), (0,3), (0,6), (3,0)... diye gider.
    # Bu yüzden range(0, 9, 3) kullanıyoruz (0, 3, 6 değerlerini verir).
    for i in range(0, 9, 3):  # Kutu satır başlangıcı
        for j in range(0, 9, 3):  # Kutu sütun başlangıcı
            box = []
            # Kutunun içindeki 3x3 hücreyi geziyoruz
            for x in range(3):
                for y in range(3):
                    # i+x ve j+y ile kutunun içindeki hücreye ulaşıyoruz
                    box.append(grid[i + x][j + y])

            if set(box) != valid_set:
                return False

    # Hiçbir kural ihlal edilmediyse Sudoku doğrudur
    return True
