import utils 
import read_csv
import charts

def run():
    data = read_csv.read_csv('./proyecto_final/tasas_de_nacimiento.csv') #importamos el modulo para traer el diccionarios    
    labels,values = utils.get_labels_values(data)
    result = charts.generate_by_chart(labels,values)
    return result
    


if __name__ == '__main__':
        run()
    
