
def saveFile(str: str, fileName: str) -> None:
    with open(f'{fileName}.txt', 'w', encoding="utf-8") as f:
        f.write(str)
        # print(str, file=f)


def createKey(n: int) -> str:
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    n = -n
    alph = list(alph)
    if n < 0:
        n = abs(n)
        for i in range(n):
            alph.append(alph.pop(0))
    else:
        for i in range(n):
            alph.insert(0, alph.pop())
    return ''.join(alph)


def encrypt(str: str, n: int):
    alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph = alph.lower()
    ln = len(alph)
    res = []
    noAlph = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in str:
        if not l in noAlph:
            res.append(alph[(alph.find(l)+n) % ln])
        else:
            res.append(l)
    return ''.join(res)


if __name__ == '__main__':
    text = "Потребность шифровать и передавать шифрованные сообщения возникла очень давно. Так, еще в древние греки применяли специальное шифрующее устройство. По описанию Плутарха, оно состояло из двух палок одинаковой длины и толщины. Одну оставляли себе, а другую отдавали отъезжающему. Эти палки называли скиталами. Когда правителям нужно было сообщить какую-нибудь важную тайну, они вырезали длинную и узкую, вроде ремня, полосу папируса, наматывали ее на свою скиталу, не оставляя на ней никакого промежутка, так чтобы вся поверхность палки была охвачена этой полосой. Затем, оставляя папирус на скитале в том виде, как он есть, писали на нем все, что нужно, а написав, снимали полосу и без палки отправляли адресату. Так как буквы на ней разбросаны в беспорядке, то прочитать написанное он мог, только взяв свою скиталу и намотав на нее без пропусков эту полосу"
    text = text.lower()
    saveFile(text, "original")
    saveFile(createKey(1), "key")
    saveFile(encrypt(text, 1), "encrypted")
