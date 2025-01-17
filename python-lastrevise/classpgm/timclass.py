class Time:
    def __init__(self,hour,min,sec):
        self.__hour=hour
        self.__min=min
        self.__sec=sec
    def __add__(self,other):
        totsec=(self.__hour*3600)+(self.__min*60)+self.__sec+(other.__hour*3600)+(other.__min*60)+other.__sec
        hr=(totsec//3600)%24
        mins=(totsec%3600)//60
        secs=(totsec%60)
        print(f"{hr:02}:{mins:02}:{secs:02}")
        
t1=Time(5,30,25)
t2=Time(19,00,20)
t1+t2