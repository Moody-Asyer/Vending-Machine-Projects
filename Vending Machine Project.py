def memastikan_kelipatan (nilai) :
    if nilai >= 10_000 and modulo_bil_positif(nilai,10000) == 0  :
        return True
    else :
        return False

def modulo_bil_positif(x,y) :
    sisa_bagi = 0
    while x >= 0 :
        if x < y:
            return sisa_bagi
        if x >= y :
            x = x-y
        sisa_bagi = x
    else :
        return sisa_bagi

def jumlah_lembar (uang_total, sisa, nominal):
    lembar = (uang_total- sisa)/ nominal
    return int(lembar)


def pertanyaan_melanjutkan() :
    jawab = str(input("Apakah anda ingin melanjutkan? [Y/T] "))
    kemungkinan_jawaban = ["Y", "y", "T", "t"]
    if jawab not in kemungkinan_jawaban :
        print("Silahkan Tekan tombol 'Y' untuk melanjutkan dan 'T' untuk berhenti")
        pertanyaan_melanjutkan()
    else :
        if jawab == "y" or jawab == "Y" :
            main()
        else :
            print("Sampai Ketemu")

def urut_angka(numbers):
    for a in range(0, len(numbers)):
        for b in range(0, len(numbers) - 1):
            if numbers[b] < numbers[b + 1]:
                numbers[b], numbers[b + 1] = numbers[b + 1], numbers[b]
    return numbers


def main ():
    uang_masuk = int(input("Masukkan Uang Kelipatan Rp10.000:"))
    nominal_penukaran = [50_000, 20_000, 10_000]

    urut_angka(nominal_penukaran)

    if memastikan_kelipatan(uang_masuk) == True :
        print ("Anda Mendapatkan")


        for x in range (0, len(nominal_penukaran)):
            if uang_masuk >= nominal_penukaran[x] :
                sisa = modulo_bil_positif(uang_masuk, nominal_penukaran[x])
                jumlah = jumlah_lembar(uang_masuk, sisa, nominal_penukaran[x])
                uang_masuk = sisa
                if jumlah != 0 :
                    print(str(nominal_penukaran[x]), "x", jumlah)
        pertanyaan_melanjutkan()

    else :
        print("Proses Penukaran Tidak Dapat Dilakukan.\nAnda harus memasukkan uang kelipatan Rp10.000")

main()





# test
def test_memastikan_kelipatan() :
    expected = False
    result = memastikan_kelipatan(1_000)
    assert expected == result, "salah"

def test_modulo_bilangan_positif() :
    expected = 30_000
    result = modulo_bil_positif(130_000,50000)
    assert expected == result ,"salah"

def test_jumlah_lembar () :
    expected = 2
    result = jumlah_lembar(130_000, 30_000, 50_000)
    assert expected == result , "salah"

def test_urut_angka () :
    expected = [123,35,23,2]
    result = urut_angka([2, 35, 123,23])
    assert expected == result, "salah"



def test_all () :
    test_memastikan_kelipatan()
    test_modulo_bilangan_positif()
    test_jumlah_lembar()
    test_urut_angka()
test_all()
