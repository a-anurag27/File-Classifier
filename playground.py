import os

path = '/Users/anurag/Downloads/test'
subd = []

"""
Write into a text file
"""
def writeRep():
    


# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for subs in d:
        subd.append(subs)
print(path)
for i in subd:
    new_path = os.path.join(path, i)
    print("\t%s [%s]" %(i,new_path))
    for r,d,f in os.walk(new_path):
        for fn in f:
            print("\t|-> ",end='')
            print(fn)

