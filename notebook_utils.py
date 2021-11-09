import numpy as np
from sklearn.preprocessing import MinMaxScaler


def change_width(ax, new_value: float) :
    #initialx = 0
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff*.5)
        #ax.text(patch.get_height(), initialx+patch.get_width()/8, '{:1.0f}'.format(patch.get_width()))
        
        #initialx += 1

def get_alpha_values(column):
    scaler = MinMaxScaler()
    alphas = scaler.fit_transform(np.flip(column.values.reshape(-1,1)))

    alphas = [value + 0.2 if value <= 0.2 else value for value in np.flip(alphas)[:,0]]
    return alphas
