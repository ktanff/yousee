def cover(secret,pcode,keepSpaces):
	ls=[3]+[4]*2+[5]*4+[6]*5+[7]*7+[8]*6+[9]*5
	charpool='aabcdeeefghiijklmnoopqrrssttuuvwxyz'*2+'0123456789'*5+'ABCDEFGHIJKLMNOPQRSTUVWXYZ!!@##$$%&&-??'+'.:;,()[]{}<>=+*^/|\\\'\"_'
	with open('voc.txt') as f:
		voc=[r.strip() for r in f]
	psmap={}
	for v in voc:
		for i,a in enumerate(v):
			if a not in psmap:
				psmap[a]=[]
			g=i-len(psmap[a])+1
			if g>0:
				psmap[a]+=[[] for _ in range(g)]
			psmap[a][i].append(v)
	#print(psmap)
	#print([len(psmap[i]) for i in psmap])
	
	from random import choice
	from random import choices
	from random import randint
	
	l=len(secret)
	n=len(pcode)
	coverage=""
	
	melt=''.join(choices(voc,k=96))
	i=j=0
	r=100
	while i<l and j<288:
		cover=choices(charpool,k=choice(ls))
		clen=len(cover)
		p=int(pcode[j%n])
		if p<=clen:
			j+=1
			if p>0:
				s=secret[i]
				if s==' ':
					if not keepSpaces: i+=1; j-=1; continue
					s='_'
					if p>1:
						cover[p-2]='['
					if p<len(cover): 
						cover[p]=']'
					elif p>1:
						cover.append(']')
				cover[p-1]=s
				if melt[i]!=s:
					r=(r+1)%clen
					for _ in range(20):
						if cover[r]!=s and cover[r]!='_' and cover[r]!='[' and cover[r]!=']':
							cover[r]=melt[i] if randint(0,4)>0 else melt[i].upper()
							break
						r=randint(0,clen-1)
				i+=1
		coverage=coverage+'  '+''.join(cover)+' '
	if i<l:
		raise Exception("FAIL: too long coverage; try with another passcode or a shorter secret.")
	return coverage

secret=input('Secret ? ')
pcode=input('Passcode ? ')
keepSpaces=input('Keep spaces ? ').lower()
keepSpaces=(keepSpaces=='y' or keepSpaces=='yes')
for _ in range(3):
	print(cover(secret,pcode,keepSpaces),'\n')
