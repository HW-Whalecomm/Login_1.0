import data_aws


lista = list(data_aws.data.keys())

for medidor in lista:
    print(medidor)
    print(data_aws.data[medidor])
