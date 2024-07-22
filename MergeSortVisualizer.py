import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random

def MergeSort (A, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    yield from MergeSort(A, start, mid)
    yield from MergeSort(A, mid + 1, end)
    yield from Merge(A, start, mid, end)
    yield A


def Merge(A, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    CopyA = np.zeros(n1, dtype=int)
    CopyB = np.zeros(n2, dtype=int)
    for i in range(n1):
        CopyA[i] = A[start+i]
    for j in range(n2):
        CopyB[j] = A[mid+1+j]
    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if CopyA[i] <= CopyB[j]:
            A[k] = CopyA[i]
            i+=1
        else:
            A[k] = CopyB[j]
            j+=1
        k+=1
    while i<n1:
        A[k] = CopyA[i]
        i+=1
        k+=1
    while j<n2:
        A[k] = CopyB[j]
        j+=1
        k+=1
    yield A

def ShowGraph():
    n=100
    a = [i for i in range (1, n+1)]
    random.shuffle(a)
    datasetName = 'Random'

    generator = MergeSort(a, 0, len(a) - 1)
    algoName = 'Merge Sort'

    plt.style.use('fivethirtyeight')
    
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap( 
        "my_map", 
        { 
            "red": [(0, 1.0, 1.0), 
                    (1.0, .5, .5)], 
            "green": [(0, 0.5, 0.5), 
                      (1.0, 0, 0)], 
            "blue": [(0, 0.50, 0.5), 
                     (1.0, 0, 0)] 
        } 
    )

    fig, ax = plt.subplots()
    
    bar_rects = ax.bar(range(len(a)), a, align = "edge", color = color_map(data_normalizer(range(n))))

    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title("ALGORITHM : "+algoName+"\n"+"DATA SET : "+datasetName)

    text = ax.text(0.01, 0.95, "", transform = ax.transAxes, color="#E4365D")

    iteration = [0]

    def animate(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("iterations: {}".format(iteration[0]))
    
    anim = FuncAnimation(fig, func=animate, fargs=(bar_rects, iteration), frames = generator, interval=50, repeat=False)

    plt.show()

ShowGraph()