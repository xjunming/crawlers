import pandas as pd
import re

df = pd.read_csv('data.csv', encoding='utf-8-sig')

# 汇率
Exchange = []
Exchange_pattern = re.compile(r'(?<=1.00 USD = )\d+\.?\d*')
for s in df['Exchange-Fee-Service_time']:
    if Exchange_pattern.findall(s):
        Exchange.append(Exchange_pattern.findall(s)[0])
    else:
        Exchange.append(None)

# 费用
fee = []
fee_pattern = re.compile(r'(?<= fee2\+ )\d+\.?\d*')
for s in df['Exchange-Fee-Service_time']:
    if fee_pattern.findall(s):
        fee.append(fee_pattern.findall(s)[0])
    else:
        fee.append(None)

# 交易时间
Service_time = []
Service_time_pattern = re.compile(r'Service time:1(.*)')
for s in df['Exchange-Fee-Service_time']:
    if Service_time_pattern.findall(s):
        Service_time.append(Service_time_pattern.findall(s)[0])
    else:
        Service_time.append(None)

new_Service_time = []
for s in Service_time:
    if ',' in s:
        pattern = re.compile(r'days(.*)')
        new_Service_time.append(pattern.findall(s))
    else:
        new_Service_time.append(s[0:len(s)//2].rstrip('0'))

nn_Service_time = []
for s in new_Service_time:
    if 'In minutes' in s:
        nn_Service_time.append(0)
    else:
        pattern = re.compile(r'(.*)Business days')
        if len(s) == 1:
            nn_Service_time.append(pattern.findall(s[0])[0])
        else:
            nn_Service_time.append(pattern.findall(s)[0])

Limit = []
for s in df['Limit']:
    Limit.append(s.lstrip('Send up to ').rstrip(' USD'))
df['Limit'] = Limit

print(Limit)
print(Exchange)
print(fee)
print(nn_Service_time)

df['Exchange'] = Exchange
df['fee'] = fee
df['Service_time'] = nn_Service_time

df.to_csv('westernunion.csv', encoding='utf-8-sig')
