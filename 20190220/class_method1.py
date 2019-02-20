#!/usr/bin/env python3

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day


    @classmethod
    def creat_date(cls,str_date):
        date_list=str_date.split('-')
        y=int(date_list[0])
        m=int(date_list[1])
        d=int(date_list[2])

        return cls(y,m,d)


    @staticmethod
    def is_date_valid(str_date):
        y,m,d=map(int,str_date.split('-'))
        return y <4000  and 1<= m <= 12  and 1 <= d <=31


if __name__ == '__main__':
    d1=Date(2019,2,20)
    d2=Date.creat_date('2019-2-21')
    print(d2.year)
    print(Date.is_date_valid('2019-2-2'))