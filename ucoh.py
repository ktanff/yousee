def cover(secret,pcode,keepSpaces):
	from random import choice
	from random import choices
	from random import randint
	charpool='aabcdeeefghiijklmnoopqrrssttuuvwxyz0123456789'*2+'ABCDEFGHIJKLMNOPQRSTUVWXYZ.:;,()[]{}<>=+*^/|\\\'\"_'+'!!@##$$%&&-??'*5
	with open('voc.txt') as f:
		voc=[r.strip() for r in f]
	psmap={}
	for v in voc:
		for i,a in enumerate(v):
			if a not in psmap:
				psmap[a]=[ [] for _ in range(9) ]
			if i<9:
				psmap[a][i].append(v)
	minpsf={}
	for v in voc:
		minpsf[v]=min(len(psmap[a][i]) for i,a in enumerate(v))
	
	l=len(secret)
	n=len(pcode)
	coverage=[]
	i=j=0
	while i<l and j<288:
		cover=choices(charpool,k=9)
		p=int(pcode[j%n])
		if p==0 or (p>=4 and randint(0,4)==0):
			if p==0: p=10
			else: j-=1
			s=cover[-1]
			sl=s.lower()
			if sl in psmap:
				cover=choice([v for v in voc if len(v)<p])
				if s!=sl:
					cover=cover.upper()
			else:
				lim=min(p-1,randint(3,9))
				if '0'<=s<='9':
					cover=choices('0011122234567899',k=lim)
				else:
					cover=cover[:lim]
				cover="".join(cover)
		else:
			s=secret[i]
			if s==' ' and not keepSpaces:
				i+=1
				continue
			sl=s.lower()
			p-=1
			if sl in psmap:
				pool=psmap[sl][p]
				pre=""
				if len(pool)<=1 and p>=4:
					pre=choice([v for v in voc if len(v)<=p])
					pool=psmap[sl][p-len(pre)]
				if len(pool)>1:
					recpw=[minpsf[v] for v in pool]
					m=max(recpw)
					m=m+m//2
					cover,=choices(pool,weights=[m//z for z in recpw])
					cover=pre+cover
					if s!=sl:
						cover=cover.upper()
			if cover[p]!=s:
				if '0'<=s<='9':
					cover=choices('0011122234567899',k=9)
				if s==' ':
					cover[p]='_'
					if p>0: cover[p-1]='['
					if p<8: cover[p+1]=']'
					else: cover.append(']')
				else:
					cover[p]=s
				cover="".join(cover)
			i+=1
		j+=1
		coverage.append(cover)
	if i<l:
		raise Exception("FAIL: too long coverage; try with another passcode or a shorter secret.")
	return "   "+"   ".join(coverage)

secret=input('Secret ? ')
pcode=input('Passcode ? ')
keepSpaces=input('Keep spaces ? ').lower()
keepSpaces=(keepSpaces=='y' or keepSpaces=='yes')
for _ in range(3):
	print(cover(secret,pcode,keepSpaces),'\n')
