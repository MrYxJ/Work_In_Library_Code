import re

def write(ulist,name):
    with open(name,'w') as f:
        for line in ulist:
            f.writelines(line+'\n')

def read(name):
    ulist = []
    with open(name,'r') as f:
       for line in f.readlines():
           line = line[:-1]
           ulist.append(line)
    return ulist

def postman(strs): # 复制的一段请求文&形式转变成字典
    ans = {}
    key =''
    value = ''
    flag = True
    for s in strs:
        if s == '&':
            #if value.isdigit(): value = int(value)
            ans[key] = value
            key = ''
            value = ''
            flag = True
        elif s == '=':
            flag = False
        else:
            if flag : key = key + s
            else : value = value +s
    return ans

def clean_word(self,sstr):  # 消除一段话中所有转义符号
        return "".join(sstr.split())

if __name__ == '__main__':
    str = 'currentPage=1&pageSize=10&outcomeCategory=010&searchOutCome010.author=&searchOutCome010.title=&searchOutCome010.journalName=&searchOutCome010.year=2017&searchOutCome010.day=&searchOutCome010.page=&searchOutCome010.organization=&searchOutCome010.projectTranceNo=&searchOutCome020.author=&searchOutCome020.title=&searchOutCome020.conferenceName=&searchOutCome020.year=&searchOutCome020.month=&searchOutCome020.day=&searchOutCome020.venue=&searchOutCome020.organization=&searchOutCome020.projectTranceNo=&searchOutCome030.author=&searchOutCome030.title=&searchOutCome030.publication=&searchOutCome030.year=&searchOutCome030.ISBN=&searchOutCome030.organization=&searchOutCome030.projectTranceNo=&searchOutCome090.code=&searchOutCome090.title=&searchOutCome090.author=&searchOutCome090.organization=&searchOutCome090.category=&searchOutCome090.level=&searchOutCome090.year=&searchOutCome090.month=&searchOutCome090.day=&searchOutCome090.awardOrganization=&outcomePatent.pid=&outcomePatent.title=&outcomePatent.author=&outcomePatent.organization=&outcomePatent.patenttype=&outcomePatent.area=&outcomePatent.firstAuthorOrganization=&checkCode=%E8%AF%B7%E8%BE%93%E5%85%A5%E9%AA%8C%E8%AF%81%E7%A0%81'
    print(postman(str))


