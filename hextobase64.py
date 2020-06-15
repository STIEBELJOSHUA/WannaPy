#Base64 encoding table
encode64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

#hex table
decodehex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

#turn hex string to string of decimal digits
def hex_to_dec(hex):
	hex = hex.lower()
	dec = []
	#split hex string into byte sized pieces
	hex = [(hex[i:i+2]) for i in range(0, len(hex), 2)]
	#convert hex to decimal
	try:
		for number in hex: 
			decimal = (decodehex[number[0]] * 16) + (decodehex[number[1]])
			dec.append(decimal) 
		#print(dec) 
		return(dec)
	except Exception as e:
		print('Please enter a valid hex string')
		exit()


def decimal_to_binary(dec):
	binary = []
	#loop through decimal numbers
	for number in dec:
		singlebinary = ''
		numberdiv2 = number
		#create binary
		for num in range(0,8):
			bina = numberdiv2 % 2
			numberdiv2 = numberdiv2//2
			singlebinary += str(bina)
			#append finished binary to list
			if num == 7:
				binary.append(singlebinary[::-1])
	binary = ''.join(binary)
	#print(binary)
	return(binary)


def binary_to_base64(binary):
	base64 = ''
	#decides how much padding is needed
	if len(binary) % 6 == 4:
		padding = '='
		binary += '00'
	elif len(binary) % 6 == 2:
		padding = '=='
		binary += '0000'
	else:
		padding = ''
	#loop through binary 6 bits at a time
	for i in range (0, len(binary), 6):
		base = binary[i:i+6]
		base = base[::-1]
		#turn binary into decimal
		number = [(int(base[j]) * (2**j)) for j in range(0,len(base))]
		base64 += encode64[sum(number)]
	#adds padding
	base64 += padding
	#print(base64)
	return(base64)
		


def hex_to_base64(hex):
	#takes the hex value and converts it to dec then to binary then to base64		
	return(binary_to_base64(decimal_to_binary(hex_to_dec(hex))))

	





	


