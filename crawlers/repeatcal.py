import jieba
import math
# 使用余弦角度求相似度
def rept(s0,s1):
    vec={};
    len0=len1=dotp=0;
    # 使用jieba分词
    for word in jieba.lcut(s0):
        if(word in vec):
            vec[word][0]+=1;
        else:
            vec[word]=[1,0];
    for word in jieba.lcut(s1):
        if(word in vec):
            vec[word][1]+=1;
        else:
            vec[word]=[0,1];
    for dim in vec:
        print(vec[dim]);
        dotp+=vec[dim][1]*vec[dim][0];
        len0+=vec[dim][0]**2;
        len1+=vec[dim][1]**2;
    len0=math.sqrt(len0);
    len1=math.sqrt(len1);
    return math.acos(dotp/(len0*len1))*180/math.pi;
print(rept(input(),input()));