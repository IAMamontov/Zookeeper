# put your python code here
hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
print(sec2 + min2 * 60 + hour2 * 3600
      - (sec1 + min1 * 60 + hour1 * 3600))