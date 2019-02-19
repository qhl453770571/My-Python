
try:
    num=int(input('请输入在数字：'))

    result=100/num


except (ValueError,ZeroDivisionError):
    print('无效输入！')


# except ZeroDivisionError:
#     print('不能输入0')

except (KeyboardInterrupt,EOFError):
    print('\nBye-Bye')


# except:
#     print('请按要求输入和退出！')

else:
    print('\033[33;1m%s\033[0m' % result)

finally:
    print('\033[32;1mDone\033[0m')