import datetime

def date_frequency(dates):
    date_format = '%Y年%m月%d日%H時'
    frequencies = []
    for i in range(len(dates) - 1):
        freq = datetime.datetime.strptime(dates[i+1], date_format) - datetime.datetime.strptime(dates[i], date_format)
        frequencies.append(freq)
    ave = sum(frequencies, datetime.timedelta()) / len(frequencies)
    return ave

date_test = ['2021年12月24日09時', '2021年12月26日09時', '2022年01月04日09時', '2022年01月09日09時', '2022年01月28日09時', '2022年02月04日09時', '2022年02月11日09時', '2022年02月18日09時', '2022年02月25日09時', '2022年03月06日09時', '2022年03月19日09時', '2022年03月26日09時', '2022年04月03日09時', '2022年04月18日09時', '2022年04月30日09時', '2022年05月07日09時', '2022年05月28日09時', '2022年06月03日09時', '2022年06月10日09時', '2022年06月24日09時', '2022年07月01日09時', '2022年07月08日09時', '2022年07月16日09時', '2022年07月23日09時', '2022年08月01日09時', '2022年08月13日09時', '2022年08月21日09時', '2022年08月29日09時', '2022年09月11日09時', '2022年09月19日09時', '2022年09月28日09時', '2022年10月07日09時', '2022年10月16日09時', '2022年10月30日08時', '2022年11月12日09時', '2022年11月18日09時', '2022年11月25日09時', '2022年12月02日09時', '2022年12月09日09時', '2022年12月16日09時', '2022年12月23日09時', '2023年01月06日09時', '2023年01月13日09時', '2023年01月27日09時', '2023年02月11日09時', '2023年02月25日09時', '2023年03月04日09時', '2023年03月18日09時', '2023年04月08日08時', '2023年04月16日08時']
result = date_frequency(date_test)
print("平均経過日数:", result.days)
