import platform, os, psutil, json, time #Агента основана на билиотеке psutil, реализация этой библиотеки не проверялась. Страница разработчиков на GitHub https://github.com/giampaolo/psutil/
def rounding(value): #Функция округляет значение переданного ей аргумента в случае если аргумент имеет тип float или вслучае если аргумент является списком, в котором есть элементы типа float
    value1 = value[1]
    if type(value1) is float:
        value1 = round(value1)
    elif type(value1) is list:
        for i in range(len(value1)):
            if type(value1[i]) is float:
                value1[i] = round(value1[i])
    return (value[0], value1)
def hui():    #Функция возвращает строку в формате json с информацией о использовании апаратных ресурсов компьютера
    hfile = open('hardware_usage_info.json', 'w')
    dic = {}
    path = '/'
    dic.update({'disktot':psutil.disk_usage(path).total/2**20}) #Объем жесткого диска, на котором установленна программа (Мбайт)
    dic.update({'diskav':psutil.disk_usage(path).free/2**20})  #Объем свободной памяти на жестком диске, на котором установленна программа (Мбайт)
    dic.update({'diskus':psutil.disk_usage(path).used/2**20})  #Объем занятой памяти памяти на жестком диске, на котором установленна программа (Мбайт)
    dic.update({'diskpct':psutil.disk_usage(path).percent})  #Процент использования памяти жесткого диска, на котором установленна программа (%)

    vmt = psutil.virtual_memory().total / 2 ** 20 # Общий объем виртуальной памяти (Мбайт)
    dic.update({'vmtot':vmt})
    vma = psutil.virtual_memory().available / 2 ** 20 # Объем незанятой виртуальной памяти (Мбайт)
    dic.update({'vmav':vma})
    vmu = psutil.virtual_memory().used / 2 ** 20 # Объем используемой виртуальной памяти (Мбайт)
    dic.update({'vmus':vmu})
    dic.update({'vmpct':psutil.virtual_memory().percent})  # Процент использования виртуальой памяти (%)

    ramt = psutil.swap_memory().total / 2 ** 20 - vmt  # Объем оперативной памяти компьютера (Мбайт)
    dic.update({'ramtot':ramt})

    dic.update({'ramav':psutil.swap_memory().free/2**20 - vma})  # Объем свободной оперативной памяти компьютера (Мбайт)
    ramu = psutil.swap_memory().used / 2 ** 20 - vmu  # Объем используемой оперативной памяти компьютера (Мбайт)
    dic.update({'ramus':ramu})
    dic.update({'rampct':ramu/ramt*100})  # Процент использования оперативной памяти компьютера (%)

    dic.update({'vm_ramtot':psutil.swap_memory().total/2**20})  # Объем виртуальной и оперативной памяти компьютера (Мбайт)
    dic.update({'vm_ramav':psutil.swap_memory().free/2**20})  # Объем свободной виртуальной и оперативной памяти компьютера (Мбайт)
    dic.update({'vm_ramus':psutil.swap_memory().used/2**20})  # Объем используемой виртуальной и оперативной памяти компьютера (Мбайт)
    dic.update({'vm_rampct':psutil.swap_memory().percent})  # Процент использования виртуальной и оперативной памяти компьютера (%)

    #print()  #Имя процесса, в котором выполняется приложение SBM
    #print()  #Состояние процесса, в котором выполняется приложение SBM (Активный/не активный)
    #print()  #Память используемая процессом, в котором выполняется приложение SBM (Мбайт)

    dic.update({'cpuname':platform.processor()})  #Имя процессора
    dic.update({'corcount':psutil.cpu_count()})  #Количество логических ядер процессора
    dic.update({'cpuuspct':psutil.cpu_percent(interval=1, percpu=True)})  #Список использования мощности в процентах для каждого логического ядра процессора за интервал 1 секунда (%)
    dic = dict(map(rounding,dic.items()))
    hfile.write(json.dumps(dic))
    hfile.close()

hui()

