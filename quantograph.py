try:
    from qiskit import *
except:
    agree = input("Do you want to install the required package 'qiskit'? (y/n)\n")=='y'
    if agree:
        from pip._internal import main
        main(['install','qiskit'])
    from qiskit import *
    
try:
    from apng import APNG
except:
    agree = input("Do you want to install the required package 'apng' (y/n)\n")=='y'
    if agree:
        from pip._internal import main
        main(['install','apng'])
    from apng import APNG

from PIL import Image
from IPython.display import display
import numpy as np
import ipywidgets as widgets
from IPython.display import display, Markdown
import time
import os

n = 6

red_plumber = {(0, 0): (255, 255, 255), (0, 1): (255, 255, 255), (0, 2): (255, 255, 255), (0, 3): (255, 0, 0), (0, 4): (255, 0, 0), (0, 5): (255, 0, 0), (0, 6): (255, 255, 255), (0, 7): (92, 64, 51), (1, 0): (255, 255, 255), (1, 1): (255, 0, 0), (1, 2): (255, 255, 255), (1, 3): (0, 0, 255), (1, 4): (0, 0, 255), (1, 5): (0, 0, 255), (1, 6): (0, 0, 255), (1, 7): (92, 64, 51), (2, 0): (255, 0, 0), (2, 1): (255, 0, 0), (2, 2): (255, 192, 203), (2, 3): (255, 0, 0), (2, 4): (0, 0, 255), (2, 5): (0, 0, 255), (2, 6): (255, 255, 255), (2, 7): (255, 255, 255), (3, 0): (255, 0, 0), (3, 1): (255, 0, 0), (3, 2): (255, 192, 203), (3, 3): (255, 0, 0), (3, 4): (0, 0, 255), (3, 5): (0, 0, 255), (3, 6): (255, 255, 255), (3, 7): (255, 255, 255), (4, 0): (255, 255, 255), (4, 1): (255, 0, 0), (4, 2): (255, 255, 255), (4, 3): (0, 0, 255), (4, 4): (0, 0, 255), (4, 5): (0, 0, 255), (4, 6): (0, 0, 255), (4, 7): (92, 64, 51), (5, 0): (255, 255, 255), (5, 1): (255, 255, 255), (5, 2): (255, 255, 255), (5, 3): (255, 0, 0), (5, 4): (255, 0, 0), (5, 5): (255, 0, 0), (5, 6): (255, 255, 255), (5, 7): (92, 64, 51), (6, 0): (255, 255, 255), (6, 1): (255, 255, 255), (6, 2): (255, 255, 255), (6, 3): (255, 255, 255), (6, 4): (255, 255, 255), (6, 5): (210, 180, 140), (6, 6): (255, 255, 255), (6, 7): (255, 255, 255), (7, 0): (255, 255, 255), (7, 1): (255, 255, 255), (7, 2): (255, 255, 255), (7, 3): (107, 92, 72), (7, 4): (210, 180, 140), (7, 5): (107, 92, 72), (7, 6): (255, 255, 255), (7, 7): (255, 255, 255)}
green_plumber = {}
for pos in red_plumber:
    if red_plumber[pos]==(255,0,0):
        green_plumber[pos] = (0,255,0)
    else:
        green_plumber[pos] = red_plumber[pos]
flower = {(0, 0): (115, 294, 255), (0, 1): (115, 294, 255), (0, 2): (115, 294, 255), (0, 3): (255, 0, 0), (0, 4): (255, 0, 0), (0, 5): (0, 225, 0), (0, 6): (0, 225, 0), (0, 7): (0, 225, 0), (1, 0): (115, 294, 255), (1, 1): (115, 294, 255), (1, 2): (255, 0, 0), (1, 3): (225, 0, 0), (1, 4): (225, 0, 0), (1, 5): (255, 0, 0), (1, 6): (0, 225, 0), (1, 7): (0, 225, 0), (2, 0): (115, 294, 255), (2, 1): (255, 0, 0), (2, 2): (255, 0, 0), (2, 3): (225, 0, 0), (2, 4): (225, 0, 0), (2, 5): (255, 0, 0), (2, 6): (255, 0, 0), (2, 7): (0, 225, 0), (3, 0): (255, 0, 0), (3, 1): (225, 0, 0), (3, 2): (225, 0, 0), (3, 3): (255, 255, 0), (3, 4): (255, 255, 0), (3, 5): (225, 0, 0), (3, 6): (225, 0, 0), (3, 7): (255, 0, 0), (4, 0): (255, 0, 0), (4, 1): (225, 0, 0), (4, 2): (225, 0, 0), (4, 3): (255, 255, 0), (4, 4): (255, 255, 0), (4, 5): (225, 0, 0), (4, 6): (225, 0, 0), (4, 7): (255, 0, 0), (5, 0): (115, 294, 255), (5, 1): (255, 0, 0), (5, 2): (255, 0, 0), (5, 3): (225, 0, 0), (5, 4): (225, 0, 0), (5, 5): (255, 0, 0), (5, 6): (255, 0, 0), (5, 7): (0, 225, 0), (6, 0): (115, 294, 255), (6, 1): (115, 294, 255), (6, 2): (255, 0, 0), (6, 3): (225, 0, 0), (6, 4): (225, 0, 0), (6, 5): (255, 0, 0), (6, 6): (0, 225, 0), (6, 7): (0, 225, 0), (7, 0): (115, 294, 255), (7, 1): (115, 294, 255), (7, 2): (115, 294, 255), (7, 3): (255, 0, 0), (7, 4): (255, 0, 0), (7, 5): (0, 225, 0), (7, 6): (0, 225, 0), (7, 7): (0, 225, 0)}

white = {}
for pos in red_plumber:
    white[pos] = (255, 255, 255)
images = {'Flower':flower,'Red Plumber':red_plumber,'Green Plumber':green_plumber,'White':white}

L = int(2**(n/2))
k = 0
grid = {(0, 0): '000000',
 (0, 1): '000100',
 (0, 2): '000110',
 (0, 3): '000010',
 (0, 4): '000011',
 (0, 5): '000111',
 (0, 6): '000101',
 (0, 7): '000001',
 (1, 0): '100000',
 (1, 1): '100100',
 (1, 2): '100110',
 (1, 3): '100010',
 (1, 4): '100011',
 (1, 5): '100111',
 (1, 6): '100101',
 (1, 7): '100001',
 (2, 0): '110000',
 (2, 1): '110100',
 (2, 2): '110110',
 (2, 3): '110010',
 (2, 4): '110011',
 (2, 5): '110111',
 (2, 6): '110101',
 (2, 7): '110001',
 (3, 0): '010000',
 (3, 1): '010100',
 (3, 2): '010110',
 (3, 3): '010010',
 (3, 4): '010011',
 (3, 5): '010111',
 (3, 6): '010101',
 (3, 7): '010001',
 (4, 0): '011000',
 (4, 1): '011100',
 (4, 2): '011110',
 (4, 3): '011010',
 (4, 4): '011011',
 (4, 5): '011111',
 (4, 6): '011101',
 (4, 7): '011001',
 (5, 0): '111000',
 (5, 1): '111100',
 (5, 2): '111110',
 (5, 3): '111010',
 (5, 4): '111011',
 (5, 5): '111111',
 (5, 6): '111101',
 (5, 7): '111001',
 (6, 0): '101000',
 (6, 1): '101100',
 (6, 2): '101110',
 (6, 3): '101010',
 (6, 4): '101011',
 (6, 5): '101111',
 (6, 6): '101101',
 (6, 7): '101001',
 (7, 0): '001000',
 (7, 1): '001100',
 (7, 2): '001110',
 (7, 3): '001010',
 (7, 4): '001011',
 (7, 5): '001111',
 (7, 6): '001101',
 (7, 7): '001001'}

def save_image(image,filename='output.png',scale=None):

    img = Image.new('RGB',(8,8))

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            img.load()[x,y] = image[x,y]

    if scale:
        img = img.resize((256,256))

    img.save(filename)

    
def image2state(image,grid):
    
    N = len(grid)
    state = [[0]*N,[0]*N,[0]*N] # different states for R, G and B

    for pos in image:
        for j in range(3):
            state[j][ int(grid[pos],2) ] = np.sqrt( image[pos][j] ) # amplitude is square root of colour value

    for j in range(3):        
        Z = sum(np.absolute(state[j])**2)
        state[j] = [amp / np.sqrt(Z) for amp in state[j]] # amplitudes are normalized
        
    return state


def ket2counts (ket):
    counts = {}
    N = len(ket)
    n = int( np.log(N)/np.log(2) ) # figure out the qubit number that this state describes
    for j in range(N):
        string = bin(j)[2:]
        string = '0'*(n-len(string)) + string
        counts[string] = np.absolute(ket[j])**2 # square amplitudes to get probabilities
    return counts


def counts2image(counts,grid):
    
    image = { pos:[0,0,0] for pos in grid}

    for j in range(3):

        rescale = 255/max(counts[j].values()) # rescale so that largest probability becomes value of 255

        for pos in image:
            try:
                image[pos][j] = int( rescale*counts[j][grid[pos]] )
            except:
                image[pos][j] = int( rescale*counts[j][grid[pos]] )

    for pos in image:
        image[pos] = tuple(image[pos])

    return image


def control_panel():

    children = []
    children.append(widgets.Dropdown(options=list(images.keys()),value='Red Plumber',description='Base Image:'))
    children.append(widgets.IntSlider(value=20,max=100,description='Frames',show=True))
    for channel in ['Red','Green','Blue']:
        for qubit in range(n):
            children.append( widgets.IntSlider(value=1,max=6,step=1,description=channel+' qubit '+str(qubit)+'',show=True) )

    box = widgets.VBox(children)
    
    return box


def renderer(box):
    
    image = images[box.children[0].value]
    frame_num = box.children[1].value
    fraction = [[],[],[]]
    k = 2
    for j in range(3):
        for qubit in range(n):
            fraction[j].append( box.children[k].value)
            k += 1

    state = image2state(image,grid)

    bar = widgets.IntProgress(value=0,max=frame_num,step=1,description='Rendering:')
    display(bar)
    
    backend = Aer.get_backend('statevector_simulator')
    q = QuantumRegister(n)

    filenames = []
    for f in range(frame_num):

        circuits = []
        for j in range(3):
            qc = QuantumCircuit(q)
            qc.initialize(state[j],q)
            for qubit in range(n):
                qc.ry(2*np.pi*fraction[j][qubit]*f/frame_num,q[qubit])
            circuits.append( qc )

        job = execute(circuits, backend, shots=1)

        counts = []
        for j in range(3):
            counts.append( ket2counts( job.result().get_statevector(circuits[j]) ) )

        frame = counts2image(counts,grid)

        bar.value = f+1

        filename = 'outputs/temp_'+str(f)+'.png'
        save_image( counts2image(counts,grid), scale=[300,300], filename=filename)
        filenames.append( filename )
        
    bar.close()

    t = time.localtime()
    animation = 'outputs/'+box.children[0].value.replace(' ','_')+'_'+str(t.tm_year)+'_'+str(t.tm_mon)+'_'+str(t.tm_mday)+'@'+str(t.tm_hour)+':'+str(t.tm_min)+':'+str(t.tm_sec)+'.png'
    
    APNG.from_files(filenames,delay=250).save( animation )
    
    for filename in filenames:
        os.remove(filename)
    
    return animation