class Student:
    L = []
    count = 0
    sum1 = 0 
    __slots__ = ['name','age','score']
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
    
    #将所有的信息输入到文件中
    # def shuru_wenjian(self):
    #     # print(self.name,self.age,self.score,file = './s1.txt')
    #     fr = open("./s1.txt",'wt')
    #     fr.write(self.name)
    #     fr.write(',')
    #     fr.write(str(self.age))
    #     fr.write(',')
    #     fr.write(str(self.score))
    #     fr.write('\n')
    #     print(self.name,"输入成功")
    # def __del__(self):
    #     fr.close()
    #修改成绩
    def xiugai_score(self,score):
        self.score = score
    
    #修改年龄
    def xiugai_age(self,age):
        self.age = age
    
    #在屏幕上输出学生信息
    def shuchu_xuesheng_xinxi(self):
        print("姓名:%s,年龄:%s,成绩:%s"%(self.name,self.age,self.score))
    
    # 将学生信息全部填入列表中
    @classmethod
    def cunru_lst(cls,l):
        cls.L.append(l)
        cls.count += 1

　　 #　打印学生的平均成绩
    @classmethod
    def pingjun_score(cls):
        for x in cls.L:
            cls.sum1 += x.age
        return cls.sum1/cls.count 
    
    # 将文件内的所有信息存入列表
    @classmethod
    def file_lst(cls):
        fr = open('./s1.txt','rt')
        while True:
            d = fr.readline()
            if d == '':
                break
            e = d.strip()
            l=e.split(',')
            s = Student(l[0],int(l[1]),int(l[2]))
            cls.L.append(s)

    

