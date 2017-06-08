print('Enter the data bits')
d=input()
data=list(d)
data.reverse()
c,ch,j,r,h=0,0,0,0,[]

while ((len(d)+r+1)>(pow(2,r))):
	r=r+1

	for i in range(0,(r+len(data))):
		p=(2**c)

		if(p==(i+1)):
			h.append(0)
			c=c+1

		else:
			h.append(int(data[j]))
			j=j+1

	for parity in range(0,(len(h))):
		ph=(2**ch)
		if(ph==(parity+1)):
			startIndex=ph-1
			i=startIndex
			toXor=[]

			while(i<len(h)):
				block=h[i:i+ph]
				toXor.extend(block)
				i+=2*ph

			for z in range(1,len(toXor)):
				h[startIndex]=h[startIndex]^toXor[z]
			ch+=1

	h.reverse()
	print('Hamming code generated would be:- ', end="")
	print(int(''.join(map(str, h))))

