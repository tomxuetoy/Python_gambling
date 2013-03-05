# can play repeatly
# from link: http://idongnou.com/2012/02/fristpython/

import random

class touzi:

     def u1(self):
          self.num = random.randint(1,4)
          if self.num == 1 or self.num == 3:
               print "User:%s \t Computer:%s \n Draw!" % (str,self.num)
          elif self.num == 2:
               print "User:%s \t Computer:%s \n You lose !" % (str,self.num)
          else :
               print "User:%s \t Computer:%s \n You win !" % (str,self.num)
             
     def u2(self):
          self.num = random.randint(1,4)
          if self.num == 2 or self.num == 4:
               print "User:%s \t Computer:%s \n Draw!" % (str,self.num)
          elif self.num == 3:
               print "User:%s \t Computer:%s \n You lose !" % (str,self.num)
          else :
               print "User:%s \t Computer:%s \n You win !" % (str,self.num)
             
     def u3(self):
          self.num = random.randint(1,4)
          if self.num == 1 or self.num == 3:
               print "User:%s \t Computer:%s \n Draw!" % (str,self.num)
          elif self.num == 4:
               print "User:%s \t Computer:%s \n You lose !" % (str,self.num)
          else :
               print "User:%s \t Computer:%s \n You win !" % (str,self.num)
             
     def u4(self):
          self.num = random.randint(1,4)
          if self.num == 2 or self.num == 4:
               print "User:%s \t Computer:%s \n Draw!" % (str,self.num)
          elif self.num == 1:
               print "User:%s \t Computer:%s \n You lose !" % (str,self.num)
          else :
               print "User:%s \t Computer:%s \n You win !" % (str,self.num)

   
if __name__ == '__main__':
     p = touzi()
     while True:
          str = raw_input('you show: (1/2/3/4/q)')
          if str == '1':
               p.u1()
          elif str == '2':
               p.u2()
          elif str == '3':
               p.u3()
          elif str == '4':
               p.u4()
          else:
               print "wrong!"
               break
