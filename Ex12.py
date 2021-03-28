'''Create a function that receivesan IP address and returns a list with both: 
original IP, original IP withoutits leading zeros(eg.: ['128.005.055.190', '128.5.55.190']).'''

ip_adress= '128.005.055.190'

# convert to a list
ip_adress = [*ip_adress]

ip_clean = []

for i in ip_adress:
    if i == '0' and ip_clean[-1] == '.':
        continue
    else:
        ip_clean.append(i)

ip_clean = ''.join(ip_clean)

print(ip_clean)