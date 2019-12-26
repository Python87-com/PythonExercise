"""
    将1970年到2050年中的闰年，存入列表
"""
list_leap_year = []

for year  in range(1970 ,2051):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        list_leap_year.append(year)

print(list_leap_year)

# [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]