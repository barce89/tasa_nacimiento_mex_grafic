""" este codigo es para grafica de barras de un pastel y de columnas sirve con matplotlib """
import matplotlib.pyplot as plt
def generate_by_chart(labels,values):
    fig,ax = plt.subplots()
    bars = ax.bar(labels,values)
    
    for bar,value in zip(bars,values):
       height = bar.get_height()
       ax.text(bar.get_x()+bar.get_width()/2,height,str(value),ha = 'center',va ='top',rotation = 'vertical',fontsize=10)
    plt.show()
    

if __name__ == '__main__':
  generate_by_chart()
    
