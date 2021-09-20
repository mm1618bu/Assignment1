def reverse(numb):
    revers = 0
      while numb > 0:
            remain = numb % 10
            revers = (revers * 10) + remain
            numb = numb // 10
    print(revers)
reverse(2345)
