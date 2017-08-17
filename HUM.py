import platform, os, psutil,time #Агента основана на билиотеке psutil, реализация этой библиотеки не проверялась. Страница разработчиков на GitHub https://github.com/giampaolo/psutil/
print(type([5.0]) is float)
def rounding(key1):
    if type(key1) is float:
        key1 = round(key1)
    elif type(key1) is list:
        for i in range(len(key1)):
            if type(key1[i]) is float:
                key1[i] = round(key1[i])
    return key1
def hui():    #Функция возвращает строку в формате json с информацией о использовании апаратных ресурсов компьютера
    hfile = open(hardware_usage_info.json, 'w')

    path = '/'
    print(psutil.disk_usage(path).total/2**20) #Объем жесткого диска, на котором установленна программа (Мбайт)
    print(psutil.disk_usage(path).free/2**20)  #Объем свободной памяти на жестком диске, на котором установленна программа (Мбайт)
    print(psutil.disk_usage(path).used/2**20)  #Объем занятой памяти памяти на жестком диске, на котором установленна программа (Мбайт)
    print(psutil.disk_usage(path).percent)  #Процент использования памяти жесткого диска, на котором установленна программа (%)

    vmt = psutil.virtual_memory().total / 2 ** 20 # Общий объем виртуальной памяти (Мбайт)
    print(vmt)
    vma = psutil.virtual_memory().available / 2 ** 20 # Объем незанятой виртуальной памяти (Мбайт)
    print(vma)
    vmu = psutil.virtual_memory().used / 2 ** 20 # Объем используемой виртуальной памяти (Мбайт)
    print(vmu)
    print(psutil.virtual_memory().percent)  # Процент использования виртуальой памяти (%)

    ramt = psutil.swap_memory().total / 2 ** 20 - vmt  # Объем оперативной памяти компьютера (Мбайт)
    print(ramt)

    print(psutil.swap_memory().free/2**20 - vma)  # Объем свободной оперативной памяти компьютера (Мбайт)
    ramu = psutil.swap_memory().used / 2 ** 20 - vmu  # Объем используемой оперативной памяти компьютера (Мбайт)
    print(ramu)
    print(ramu/ramt*100)  # Процент использования оперативной памяти компьютера (%)

    print(psutil.swap_memory().total/2**20)  # Объем виртуальной и оперативной памяти компьютера (Мбайт)
    print(psutil.swap_memory().free/2**20)  # Объем свободной виртуальной и оперативной памяти компьютера (Мбайт)
    print(psutil.swap_memory().used/2**20)  # Объем используемой виртуальной и оперативной памяти компьютера (Мбайт)
    print(round(psutil.swap_memory().percent))  # Процент использования виртуальной и оперативной памяти компьютера (%)

    #print()  #Имя процесса, в котором выполняется приложение SBM
    #print()  #Состояние процесса, в котором выполняется приложение SBM (Активный/не активный)
    #print()  #Память используемая процессом, в котором выполняется приложение SBM (Мбайт)

    print(platform.processor())  #Имя процессора
    print(psutil.cpu_count())  #Количество логических ядер процессора
    print(psutil.cpu_percent(interval=1, percpu=True))  #Список использования мощности в процентах для каждого логического ядра процессора за интервал 1 секунда (%)


hui()

