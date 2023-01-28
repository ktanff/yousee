def uncover(coverage,pcode):
	n=len(pcode)
	uc=""
	semis=[]
	j=0
	for cover in coverage.split():
		clen=len(cover)
		p=int(pcode[j%n])-1
		if p<clen:
			j+=1
			semi=cover
			if p>=0:
				s=semi[p]
				if s=='_' and (p==0 or semi[p-1]=='[') and semi[p+1]==']':
					s=' '
				uc=uc+s
				semi=semi[:p]+'|'+s+'|'+semi[p+1:]
			semis.append(semi)
	return '   '.join(semis),uc

coverage=input('Coverage ? ')
pcode=input('Passcode ? ')
semi,uc=uncover(coverage,pcode)
print(semi)
print(uc)
