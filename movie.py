class Movie:
    def __init__(self,name,year,cost,earning):
        self.name=name
        self.year=year
        self.cost=cost
        self.earning=earning
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_cost(self):
        return self.cost
    def get_earning(self):
        return self.earning
    def display(self):
        print('movie name',self.name)
        print('movie year', self.year)
        print('movie cost', self.cost)
        print('movie earning', self.earning)


a=Movie("DDLG",1995,920000,1023326)
b=Movie("KLPD",2016,9216546,124215412)
c=Movie("kkkmn",2017,92132435,323662656)
d=Movie("Rag",2010,92655565,2425683)
ls=[a.year,b.year,c.year,d.year]
ls1=[a.name,b.name,c.name,d.name]
ls2=[a.profit,b.profit,c.profit,d.profit]
ls3=[a.cost,b.cost,c.cost]
for i in range(3):
    if(ls[i]>2015):
        print(ls1[i])
    if(ls2[i]>ls3[i]):
        print(ls1[i])
