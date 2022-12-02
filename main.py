#pop-up0==digital rain https://inventwithpython.com/bigbookpython/project20.html if I have time I need to go back there an look up how to use a bext lib
import random, shutil, sys, time
#constants
MIN_STREAM_LENGTH=6
MAX_STREAM_LENGTH=100
PAUSE = 0.01#it ends up looking like a 2600 noise map if I don't have end" " instead of end""
STREAM_CHARS = ["0","1","ロ","マ","ジ","ひ","ヒ","か","が","ご","こ","き","ぎ","カ","ガ","ゴ","コ","キ","ギ","あ","い","う","え","お","く","ぐ","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ","ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め",]
DEN = 0.02
WIDTH = shutil.get_terminal_size()[0]#get term win size 
WIDTH-= 1
print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
  columns = [0]*WIDTH
  while True:
    for i in range(WIDTH):
      if columns [i]==0:
        if random.random() <= DEN: #restart stream 
          columns[i] = random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)
          #display a char or ""
      if columns [i] >0:
        print(random.choice(STREAM_CHARS),end="")
        columns[i]-=1
      else:
        print(" ",end="")
    print()#newline at end of row
    sys.stdout.flush() #Make sure text appears on the screen.
    time.sleep(PAUSE)
except KeyboardInterrupt:
  sys.exit()