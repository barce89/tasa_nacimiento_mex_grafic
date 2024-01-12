
def get_labels_values(data):
    labels = []
    values = []
    for entry in data:
        year = int(entry['Periodo'])
        births = int(entry['Nacimientos registrados'].replace(',', ''))
        labels.append(year)
        values.append(births)

    return labels,values



if __name__ == '__main__': 
    result2 = get_labels_values()# 
