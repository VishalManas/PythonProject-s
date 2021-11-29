class vishal:
    def Q(self):
        print("hai vishal")

    def w(self):
        print("hai manas")
class Manas(vishal):
    def s(self):
        print("hai ")
class p(Manas):
    def r(self):
        print("hello")
class o(p):
    def h(self):
        print("vishal")

t=o()

t.Q()
t.w()
t.s()
t.r()
t.h()