if __name__ == '__main__':
  print('Эта программа запущена сама по себе. Name={}'.format(__name__))
else:
  print('Меня импортировали в другой модуль. Name={}'.format(__name__))
