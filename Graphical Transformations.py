import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
import math
import os
import center_tk_window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = tk.Tk()
win.geometry("840x620")
win.title('Graphical Transformations')
win.resizable(False, False)
center_tk_window.center_on_screen(win)
font = ("Segoe Boot Semilight", 10)

Frame1 = tk.Frame(win, padx=10, pady=30, width=840, height=230, relief='sunken')
Frame1.grid_propagate(0)
Frame1.grid()

Frame3 = tk.Frame(win, width=840, height=70)
Frame3.grid_propagate(0)
Frame3.grid(sticky=tk.W)

Frame4 = tk.Frame(win, width=415, height=319)
Frame4.grid_propagate(0)
Frame4.grid(sticky=tk.SE, row=8)

Frame2 = tk.Frame(win, width=840, height=319)
Frame2.grid_propagate(0)
Frame2.grid( row=8)    


   
#Selecting Transformation Type                    

def radCall():
    if radVar.get() == 1: 
        
        word2 = 'Select Number of Coordinates: '
        Label2 = tk.Label(Frame1, text=word2, fg = 'black', font=font)
        Label2.grid(row=1, column=0, sticky=tk.W, pady=5, padx=(190, 0))
        box_values = StringVar()
        number_chosen = ttk.Combobox(Frame1, width=25, textvariable=box_values, state='readonly', 
                                     values = ["2 Coordinates", "3 Coordinates", "4 Coordinates"])
        number_chosen.grid(column=0, row=1, padx=(350, 0), pady=5)
        number_chosen.current(2)
        def comando():
            global coord_1, coord_2, coord_3, coord_4
            if box_values.get() == "2 Coordinates":
                
                Frame2 = tk.Frame(win, width=840, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid( row=8)    
                coord_1.destroy()
                coord_2.destroy()
                coord_3.destroy()
                coord_4.destroy()
                
                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                    
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                    
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                word4 = 'Enter the translation rate: '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                        
                tx = tk.StringVar()
                ty = tk.StringVar()
                
                word5 = 'Tx: '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(195, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(250,0))
                tx_1.focus()
                
                word6 = 'Ty: '
                Label6 = tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(320, 0))
                
                ty_2 = ttk.Entry(Frame1, width=5, textvariable=ty)
                ty_2.grid(column=0, row=4, padx=(380,0))
                ty_2.focus()
                
                def define_2coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    Tx = tx.get()
                    Ty = ty.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    Tx = eval(Tx)
                    Ty = eval(Ty)
                    X_new_c1 = c1[0] + Tx 
                    Y_new_c1 = c1[1] + Ty

                    X_new_c2 = c2[0] + Tx 
                    Y_new_c2 = c2[1] + Ty
                    
                    all_2points = ((X_new_c1, Y_new_c1), (X_new_c2, Y_new_c2))
                    all_2points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1)) + '\n' + str((X_new_c2, Y_new_c2))
                    print(all_2points)
                
                    text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                    text.insert(tk.END, all_2points_text)
                    text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                    
                    import numpy as np
                    import matplotlib.pyplot as plt
                    from matplotlib.patches import Polygon
                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
                    pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                    figure = plt.Figure(figsize=(6,3), dpi=100)
                    plot1 = figure.add_subplot(111)
                    chart_type = FigureCanvasTkAgg(figure, Frame2)
                    #chart_type.draw()
                    chart_type.get_tk_widget().grid(padx=(120,0))
                    xs, ys=zip(*pts1)
                    xs1, ys1=zip(*pts2)
                    plot1.plot(xs,ys)
                    plot1.plot(xs1,ys1)
                    plot1.axis('equal')
                    plot1.set_title('2D Translation (2 Coordinates System)')
                    
                    
                    
                tk.Button(Frame1, text="Calculate", width=20, command=define_2coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
                
            elif box_values.get() == "3 Coordinates":
                Frame2 = tk.Frame(win, width=840, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid( row=8)    
                
                coord_1.destroy()
                coord_2.destroy()
                coord_3.destroy()
                coord_4.destroy()
                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                C3 = tk.StringVar()
                
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                coord_3 = ttk.Entry(Frame1, width=5, textvariable=C3)
                coord_3.grid(column=0, row=3, padx=(370,0))
                coord_3.focus()
                
                word4 = 'Enter the translation rate: '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                tx = tk.StringVar()
                ty = tk.StringVar()
                
                word5 = 'Tx: '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(195, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(250,0))
                tx_1.focus()
            
                word6 = 'Ty: '
                Label6 = tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(320, 0))
                
                ty_2 = ttk.Entry(Frame1, width=5, textvariable=ty)
                ty_2.grid(column=0, row=4, padx=(380,0))
                ty_2.focus()
        
                def define_3coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    c3 = C3.get()
                    Tx = tx.get()
                    Ty = ty.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    c3 = eval(c3)
                    Tx = eval(Tx)
                    Ty = eval(Ty)
                    
                    X_new_c1 = c1[0] + Tx 
                    Y_new_c1 = c1[1] + Ty
                    
                    X_new_c2 = c2[0] + Tx 
                    Y_new_c2 = c2[1] + Ty
                    
                    X_new_c3 = c3[0] + Tx 
                    Y_new_c3 = c3[1] + Ty
                    
                    all_3points = ((X_new_c1, Y_new_c1), (X_new_c2, Y_new_c2), (X_new_c3, Y_new_c3))
                    all_3points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1)) + '\n' + str((X_new_c2, Y_new_c2)) + '\n' + str((X_new_c3, Y_new_c3))
                    print(all_3points)
                
                    text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                    text.insert(tk.END, all_3points_text)
                    text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                    
                    import numpy as np
                    import matplotlib.pyplot as plt
                    from matplotlib.patches import Polygon
                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]], [c3[0], c3[1]]]
                    pts2 = [[all_3points[0][0], all_3points[0][1]],[all_3points[1][0], all_3points[1][1]],[all_3points[2][0], all_3points[2][1]]]
                    pts1.append(pts1[0])
                    pts2.append(pts2[0])
                    figure = plt.Figure(figsize=(6,3), dpi=100)
                    plot1 = figure.add_subplot(111)
                    chart_type = FigureCanvasTkAgg(figure, Frame2)
                    #chart_type.draw()
                    chart_type.get_tk_widget().grid(padx=(120,0))
                    xs, ys=zip(*pts1)
                    xs1, ys1=zip(*pts2)
                    plot1.plot(xs,ys)
                    plot1.plot(xs1,ys1)
                    plot1.axis('equal')
                    plot1.set_title('2D Translation (3 Coordinates System)')

                tk.Button(Frame1, text="Calculate", width=20, command=define_3coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
                
            elif box_values.get() == "4 Coordinates":
                Frame2 = tk.Frame(win, width=840, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid( row=8)    
                
                #coord_1.destroy()
                #coord_2.destroy()
                #coord_3.destroy()
                #coord_4.destroy()

                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
        
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                C3 = tk.StringVar()
                C4 = tk.StringVar()
            
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                coord_3 = ttk.Entry(Frame1, width=5, textvariable=C3)
                coord_3.grid(column=0, row=3, padx=(370,0))
                coord_3.focus()
                    
                coord_4 = ttk.Entry(Frame1, width=5, textvariable=C4)
                coord_4.grid(column=0, row=3, padx=(450,0))
                coord_4.focus()
            
                word4 = 'Enter the translation rate: '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                    
                tx = tk.StringVar()
                ty = tk.StringVar()
                    
                word5 = 'Tx: '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(195, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(250,0))
                tx_1.focus()
                
                word6 = 'Ty: '
                Label6 = tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(320, 0))
                
                ty_2 = ttk.Entry(Frame1, width=5, textvariable=ty)
                ty_2.grid(column=0, row=4, padx=(380,0))
                ty_2.focus()
                
                def define_4coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    c3 = C3.get()
                    c4 = C4.get()
                    Tx = tx.get()
                    Ty = ty.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    c3 = eval(c3)
                    c4 = eval(c4)
                    Tx = eval(Tx)
                    Ty = eval(Ty)
                
                    X_new_c1 = c1[0] + Tx 
                    Y_new_c1 = c1[1] + Ty

                    X_new_c2 = c2[0] + Tx 
                    Y_new_c2 = c2[1] + Ty

                    X_new_c3 = c3[0] + Tx 
                    Y_new_c3 = c3[1] + Ty
                    
                    X_new_c4 = c4[0] + Tx 
                    Y_new_c4 = c4[1] + Ty

                    all_4points = ((X_new_c1, Y_new_c1), (X_new_c2, Y_new_c2), (X_new_c3, Y_new_c3), (X_new_c4, Y_new_c4))
                    all_4points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1)) + '\n' + str((X_new_c2, Y_new_c2)) + '\n' + str((X_new_c3, Y_new_c3)) + '\n' + str((X_new_c4, Y_new_c4))
                    print(all_4points)
                    
                    text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                    text.insert(tk.END, all_4points_text)
                    text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                    
                    import numpy as np
                    import matplotlib.pyplot as plt
                    from matplotlib.patches import Polygon
                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]],[c3[0], c3[1]],[c4[0], c4[1]]]
                    pts2 = [[all_4points[0][0], all_4points[0][1]],[all_4points[1][0], all_4points[1][1]],
                                    [all_4points[2][0], all_4points[2][1]],[all_4points[3][0], all_4points[3][1]]]
                    pts1.append(pts1[0])
                    pts2.append(pts2[0])
                    figure = plt.Figure(figsize=(6,3), dpi=100)
                    plot1 = figure.add_subplot(111)
                    chart_type = FigureCanvasTkAgg(figure, Frame2)
                    #chart_type.draw()
                    chart_type.get_tk_widget().grid(padx=(120,0))
                    xs, ys=zip(*pts1)
                    xs1, ys1=zip(*pts2)
                    plot1.plot(xs,ys)
                    plot1.plot(xs1,ys1)
                    plot1.axis('equal')
                    plot1.set_title('2D Translation (3 Coordinates System)')
                    
                tk.Button(Frame1, text="Calculate", width=20, command=define_4coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
        tk.Button(Frame1, text="Compute", command=comando, width=20).grid(row=2, column=0, padx=(320,0), pady=5)
        
    elif radVar.get() == 2: 
        
        word2 = 'Select Number of Coordinates: '
        Label2 = tk.Label(Frame1, text=word2, fg = 'black', font=font)
        Label2.grid(row=1, column=0, sticky=tk.W, pady=5, padx=(190, 0))
        box_values = StringVar()
        number_chosen = ttk.Combobox(Frame1, width=25, textvariable=box_values, state='readonly', 
                                     values = ["2 Coordinates", "3 Coordinates", "4 Coordinates"])
        number_chosen.grid(column=0, row=1, padx=(350, 0), pady=5)
        number_chosen.current(2)
        


        def comando():
            global coord_1, coord_2, coord_3, coord_4
            if box_values.get() == "2 Coordinates":

                Frame2 = tk.Frame(win, width=415, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid(sticky=tk.SW, row=8) 

                Frame4 = tk.Frame(win, width=415, height=319)
                Frame4.grid_propagate(0)
                Frame4.grid(sticky=tk.SE, row=8)

                coord_1.destroy()
                coord_2.destroy()
                coord_3.destroy()
                coord_4.destroy()
                
                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                    
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                    
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                word4 = 'Enter rotation angle & axis '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                
                tx = tk.StringVar()
                
                word5 = 'Angle '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(215, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(290,0))
                tx_1.focus()
            
                word6 = 'Axis: '
                Label6= tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(370, 0))
                ax_values = StringVar()
                ax_chosen = ttk.Combobox(Frame1, width=5, textvariable=ax_values, state='readonly', 
                                             values = ["x-axis", "y-axis", "z-axis"])
                ax_chosen.grid(column=0, row=4, padx=(450, 0))
                ax_chosen.current(0)
                
                def define_2coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    rot_angle = tx.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    rot_angle = eval(rot_angle)
                    ax = ax_values.get()
                    
                    
                    if ax == "x-axis":
                        
                        X_new_c1 = c1[0] = 1
                        Y_new_c1 = c1[1] * math.cos(rot_angle) - c1[2] * math.sin(rot_angle)
                        Z_new_c1 = c1[1] * math.sin(rot_angle) + c1[2] * math.cos(rot_angle)
        
                        X_new_c2 = c2[0] = 1
                        Y_new_c2 = c2[1] * math.cos(rot_angle) - c2[2] * math.sin(rot_angle)
                        Z_new_c2 = c2[1] * math.sin(rot_angle) + c2[2] * math.cos(rot_angle)
                        
                        all_2points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2))
                        all_2points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2))
                        print(all_2points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_2points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0]]
                        yline2 = [c1[1], c2[1]]
                        zline3 = [c1[2], c2[2]]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('2 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_2points[0][0], all_2points[1][0]]
                        yline = [all_2points[0][1], all_2points[1][1]]
                        zline = [all_2points[0][2], all_2points[1][2]]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('2 Coodinates (X Rotated)')
                        
                    elif ax == "y-axis":
                        
                        X_new_c1 = c1[2] * math.sin(rot_angle) + c1[0] * math.cos(rot_angle)
                        Y_new_c1 = c1[1] = 2
                        Z_new_c1 = c1[1] * math.cos(rot_angle) - c1[0] * math.sin(rot_angle)
        
                        X_new_c2 = c2[2] * math.sin(rot_angle) + c2[0] * math.cos(rot_angle)
                        Y_new_c2 = c2[1] = 2
                        Z_new_c2 = c2[1] * math.cos(rot_angle) - c2[0] * math.sin(rot_angle)
                        
                        all_2points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2))
                        all_2points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2))
                        print(all_2points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_2points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0]]
                        yline2 = [c1[1], c2[1]]
                        zline3 = [c1[2], c2[2]]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('2 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_2points[0][0], all_2points[1][0]]
                        yline = [all_2points[0][1], all_2points[1][1]]
                        zline = [all_2points[0][2], all_2points[1][2]]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('2 Coodinates (Y Rotated)')
                        
                        
                    elif ax == "z-axis":
                        
                        X_new_c1 = c1[0] * math.cos(rot_angle) - c1[1] * math.sin(rot_angle)
                        Y_new_c1 = c1[0] * math.sin(rot_angle) + c1[1] * math.cos(rot_angle)
                        Z_new_c1 = c1[2] = 3
        
                        X_new_c2 = c2[0] * math.cos(rot_angle) - c2[1] * math.sin(rot_angle)
                        Y_new_c2 = c2[0] * math.sin(rot_angle) + c2[1] * math.cos(rot_angle)
                        Z_new_c2 = c2[2] = 3
                        all_2points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2))
                        all_2points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2))
                        print(all_2points)
                    
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_2points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                    
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0]]
                        yline2 = [c1[1], c2[1]]
                        zline3 = [c1[2], c2[2]]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('2 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_2points[0][0], all_2points[1][0]]
                        yline = [all_2points[0][1], all_2points[1][1]]
                        zline = [all_2points[0][2], all_2points[1][2]]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('2 Coodinates (Z Rotated)')
                        
                        Frame4.update()
                        Frame2.update()
                tk.Button(Frame1, text="Calculate", width=20, command=define_2coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
                
            elif box_values.get() == "3 Coordinates":
                Frame2 = tk.Frame(win, width=415, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid(sticky=tk.SW, row=8) 

                Frame4 = tk.Frame(win, width=415, height=319)
                Frame4.grid_propagate(0)
                Frame4.grid(sticky=tk.SE, row=8)
                
                coord_1.destroy()
                coord_2.destroy()
                coord_3.destroy()
                coord_4.destroy()
                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                C3 = tk.StringVar()
                
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                coord_3 = ttk.Entry(Frame1, width=5, textvariable=C3)
                coord_3.grid(column=0, row=3, padx=(370,0))
                coord_3.focus()
                
                word4 = 'Enter rotation angle & axis '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                
                tx = tk.StringVar()
                
                word5 = 'Angle '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(215, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(290,0))
                tx_1.focus()
            
                word6 = 'Axis: '
                Label6= tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(370, 0))
                ax_values = StringVar()
                ax_chosen = ttk.Combobox(Frame1, width=5, textvariable=ax_values, state='readonly', 
                                             values = ["x-axis", "y-axis", "z-axis"])
                ax_chosen.grid(column=0, row=4, padx=(450, 0))
                ax_chosen.current(0)
        
                def define_3coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    c3 = C3.get()
                    rot_angle = tx.get()
                    ax = ax_values.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    c3 = eval(c3)
                    rot_angle = eval(rot_angle)
                    
                    
                    if ax == "x-axis":
                        
                        X_new_c1 = c1[0] = 1
                        Y_new_c1 = c1[1] * math.cos(rot_angle) - c1[2] * math.sin(rot_angle)
                        Z_new_c1 = c1[1] * math.sin(rot_angle) + c1[2] * math.cos(rot_angle)
        
                        X_new_c2 = c2[0] = 1
                        Y_new_c2 = c2[1] * math.cos(rot_angle) - c2[2] * math.sin(rot_angle)
                        Z_new_c2 = c2[1] * math.sin(rot_angle) + c2[2] * math.cos(rot_angle)
                        
                        X_new_c3 = c3[0] = 1
                        Y_new_c3 = c3[1] * math.cos(rot_angle) - c3[2] * math.sin(rot_angle)
                        Z_new_c3 = c3[1] * math.sin(rot_angle) + c3[2] * math.cos(rot_angle)
                
                        all_3points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3))
                        all_3points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3))
                        print(all_3points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_3points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        
                        xline1 = [c1[0], c2[0], c3[0], c1[0]]
                        yline2 = [c1[1], c2[1], c3[1], c1[1]]
                        zline3 = [c1[2], c2[2], c3[2], c1[2]]
                        
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('3 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_3points[0][0], all_3points[1][0], all_3points[2][0], all_3points[0][0]]
                        yline = [all_3points[0][1], all_3points[1][1], all_3points[2][1], all_3points[0][1]]
                        zline = [all_3points[0][2], all_3points[1][2], all_3points[2][2], all_3points[0][2]]
                        
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('3 Coodinates (X Rotated)')
                        
                    elif ax == "y-axis":
                        
                        X_new_c1 = c1[2] * math.sin(rot_angle) + c1[0] * math.cos(rot_angle)
                        Y_new_c1 = c1[1] = 2
                        Z_new_c1 = c1[1] * math.cos(rot_angle) - c1[0] * math.sin(rot_angle)
        
                        X_new_c2 = c2[2] * math.sin(rot_angle) + c2[0] * math.cos(rot_angle)
                        Y_new_c2 = c2[1] = 2
                        Z_new_c2 = c2[1] * math.cos(rot_angle) - c2[0] * math.sin(rot_angle)
                        
                        
                        X_new_c3 = c2[2] * math.sin(rot_angle) + c3[0] * math.cos(rot_angle)
                        Y_new_c3 = c2[1] = 2
                        Z_new_c3 = c2[1] * math.cos(rot_angle) - c3[0] * math.sin(rot_angle)
                        
                        all_3points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3))
                        all_3points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3))
                        print(all_3points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_3points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0], c3[0]]
                        yline2 = [c1[1], c2[1], c3[1]]
                        zline3 = [c1[2], c2[2], c3[2]]
                        xline1.append[0]
                        yline2.append[0]
                        zline3.append[0]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('3 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_3points[0][0], all_3points[1][0]. all_3points[2][0]]
                        yline = [all_3points[0][1], all_3points[1][1], all_3points[2][1]]
                        zline = [all_3points[0][2], all_3points[1][2], all_3points[2][2]]
                        xline.append[0]
                        yline.append[0]
                        zline.append[0]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('3 Coodinates (Y Rotated)')
                        
                        
                    elif ax == "z-axis":
                        
                        X_new_c1 = c1[0] * math.cos(rot_angle) - c1[1] * math.sin(rot_angle)
                        Y_new_c1 = c1[0] * math.sin(rot_angle) + c1[1] * math.cos(rot_angle)
                        Z_new_c1 = c1[2] = 3
        
                        X_new_c2 = c2[0] * math.cos(rot_angle) - c2[1] * math.sin(rot_angle)
                        Y_new_c2 = c2[0] * math.sin(rot_angle) + c2[1] * math.cos(rot_angle)
                        Z_new_c2 = c2[2] = 3

                        X_new_c3 = c3[0] * math.cos(rot_angle) - c3[1] * math.sin(rot_angle)
                        Y_new_c3 = c3[0] * math.sin(rot_angle) + c3[1] * math.cos(rot_angle)
                        Z_new_c3 = c3[2] = 3
                                                
                        all_3points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3))
                        all_3points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3))
                        print(all_3points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_3points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0], c3[0]]
                        yline2 = [c1[1], c2[1], c3[1]]
                        zline3 = [c1[2], c2[2], c3[2]]
                        xline1.append[0]
                        yline2.append[0]
                        zline3.append[0]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('3 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_3points[0][0], all_3points[1][0]. all_3points[2][0]]
                        yline = [all_3points[0][1], all_3points[1][1], all_3points[2][1]]
                        zline = [all_3points[0][2], all_3points[1][2], all_3points[2][2]]
                        xline.append[0]
                        yline.append[0]
                        zline.append[0]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('3 Coodinates (Z Rotated)')
                        
                        Frame4.update()
                        Frame2.update()
                tk.Button(Frame1, text="Calculate", width=20, command=define_3coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
                
            elif box_values.get() == "4 Coordinates":
                Frame2 = tk.Frame(win, width=415, height=319)
                Frame2.grid_propagate(0)
                Frame2.grid(sticky=tk.SW, row=8) 

                Frame4 = tk.Frame(win, width=415, height=319)
                Frame4.grid_propagate(0)
                Frame4.grid(sticky=tk.SE, row=8)
                
                #coord_1.destroy()
                #coord_2.destroy()
                #coord_3.destroy()
                #coord_4.destroy()

                word3 = 'Enter the coordinates: '
                Label3 = tk.Label(Frame1, text=word3, fg = 'black', font=font)
                Label3.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(190, 0))
        
                C1 = tk.StringVar()
                C2 = tk.StringVar()
                C3 = tk.StringVar()
                C4 = tk.StringVar()
            
                coord_1 = ttk.Entry(Frame1, width=5, textvariable=C1)
                coord_1.grid(column=0, row=3, padx=(210,0))
                coord_1.focus()
                
                coord_2 = ttk.Entry(Frame1, width=5, textvariable=C2)
                coord_2.grid(column=0, row=3, padx=(290,0))
                coord_2.focus()
                
                coord_3 = ttk.Entry(Frame1, width=5, textvariable=C3)
                coord_3.grid(column=0, row=3, padx=(370,0))
                coord_3.focus()
                    
                coord_4 = ttk.Entry(Frame1, width=5, textvariable=C4)
                coord_4.grid(column=0, row=3, padx=(450,0))
                coord_4.focus()
            
                word4 = 'Enter rotation angle & axis '
                Label4 = tk.Label(Frame1, text=word4, fg = 'black', font=font)
                Label4.grid(row=4, column=0, sticky=tk.W, pady=5, padx=(190, 0))
                
                
                tx = tk.StringVar()
                
                word5 = 'Angle '
                Label5 = tk.Label(Frame1, text=word5, fg = 'black', font=font)
                Label5.grid(row=4, column=0, padx=(215, 0))
                
                tx_1 = ttk.Entry(Frame1, width=5, textvariable=tx)
                tx_1.grid(column=0, row=4, padx=(290,0))
                tx_1.focus()
            
                word6 = 'Axis: '
                Label6= tk.Label(Frame1, text=word6, fg = 'black', font=font)
                Label6.grid(row=4, column=0, padx=(370, 0))
                ax_values = StringVar()
                ax_chosen = ttk.Combobox(Frame1, width=5, textvariable=ax_values, state='readonly', 
                                             values = ["x-axis", "y-axis", "z-axis"])
                ax_chosen.grid(column=0, row=4, padx=(450, 0))
                ax_chosen.current(0)
                
                def define_4coordinates():
                    c1 = C1.get()
                    c2 = C2.get()
                    c3 = C3.get()
                    c4 = C4.get()
                    rot_angle = tx.get()
                    ax = ax_values.get()
                    c1 = eval(c1)
                    c2 = eval(c2)
                    c3 = eval(c3)
                    c4 = eval(c4)
                    rot_angle = eval(rot_angle)
                    
                    
                    if ax == "x-axis":
                        
                        X_new_c1 = c1[0] = 1
                        Y_new_c1 = c1[1] * math.cos(rot_angle) - c1[2] * math.sin(rot_angle)
                        Z_new_c1 = c1[1] * math.sin(rot_angle) + c1[2] * math.cos(rot_angle)
        
                        X_new_c2 = c2[0] = 1
                        Y_new_c2 = c2[1] * math.cos(rot_angle) - c2[2] * math.sin(rot_angle)
                        Z_new_c2 = c2[1] * math.sin(rot_angle) + c2[2] * math.cos(rot_angle)
                        
                        X_new_c3 = c3[0] = 1
                        Y_new_c3 = c3[1] * math.cos(rot_angle) - c3[2] * math.sin(rot_angle)
                        Z_new_c3 = c3[1] * math.sin(rot_angle) + c3[2] * math.cos(rot_angle)
                        
                        X_new_c4 = c4[0] = 1
                        Y_new_c4 = c4[1] * math.cos(rot_angle) - c4[2] * math.sin(rot_angle)
                        Z_new_c4 = c4[1] * math.sin(rot_angle) + c4[2] * math.cos(rot_angle)
                
                        all_4points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3), (X_new_c4, Y_new_c4, Z_new_c4))
                        all_4points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3)) + '\n' + str((X_new_c4, Y_new_c4, Z_new_c4))
                        print(all_4points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_4points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0], c3[0], c4[0]]
                        yline2 = [c1[1], c2[1], c3[1], c4[1]]
                        zline3 = [c1[2], c2[2], c3[2], c4[2]]
                        xline1.append[0]
                        yline2.append[0]
                        zline3.append[0]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('4 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_4points[0][0], all_4points[1][0], all_4points[2][0], all_4points[3][0]]
                        yline = [all_4points[0][1], all_4points[1][1], all_4points[2][1], all_4points[3][1]]
                        zline = [all_4points[0][2], all_4points[1][2], all_4points[2][2], all_4points[3][2]]
                        xline.append[0]
                        yline.append[0]
                        zline.append[0]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('4 Coodinates (X Rotated)')
                        
                    elif ax == "y-axis":
                        
                        X_new_c1 = c1[2] * math.sin(rot_angle) + c1[0] * math.cos(rot_angle)
                        Y_new_c1 = c1[1] = 2
                        Z_new_c1 = c1[1] * math.cos(rot_angle) - c1[0] * math.sin(rot_angle)
        
                        X_new_c2 = c2[2] * math.sin(rot_angle) + c2[0] * math.cos(rot_angle)
                        Y_new_c2 = c2[1] = 2
                        Z_new_c2 = c2[1] * math.cos(rot_angle) - c2[0] * math.sin(rot_angle)
                        
                        
                        X_new_c3 = c3[2] * math.sin(rot_angle) + c3[0] * math.cos(rot_angle)
                        Y_new_c3 = c3[1] = 2
                        Z_new_c3 = c3[1] * math.cos(rot_angle) - c3[0] * math.sin(rot_angle)
                        
                        X_new_c4 = c4[2] * math.sin(rot_angle) + c4[0] * math.cos(rot_angle)
                        Y_new_c4 = c4[1] = 2
                        Z_new_c4 = c4[1] * math.cos(rot_angle) - c4[0] * math.sin(rot_angle)
                        
                        all_4points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3), (X_new_c4, Y_new_c4, Z_new_c4))
                        all_4points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3)) + '\n' + str((X_new_c4, Y_new_c4, Z_new_c4))
                        print(all_4points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_4points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0], c3[0], c4[0]]
                        yline2 = [c1[1], c2[1], c3[1], c4[1]]
                        zline3 = [c1[2], c2[2], c3[2], c4[2]]
                        xline1.append[0]
                        yline2.append[0]
                        zline3.append[0]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('4 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_4points[0][0], all_4points[1][0], all_4points[2][0], all_4points[3][0]]
                        yline = [all_4points[0][1], all_4points[1][1], all_4points[2][1], all_4points[3][1]]
                        zline = [all_4points[0][2], all_4points[1][2], all_4points[2][2], all_4points[3][2]]
                        xline.append[0]
                        yline.append[0]
                        zline.append[0]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('4 Coodinates (Y Rotated)')
                        
                        
                    elif ax == "z-axis":
                        
                        X_new_c1 = c1[0] * math.cos(rot_angle) - c1[1] * math.sin(rot_angle)
                        Y_new_c1 = c1[0] * math.sin(rot_angle) + c1[1] * math.cos(rot_angle)
                        Z_new_c1 = c1[2] = 3
        
                        X_new_c2 = c2[0] * math.cos(rot_angle) - c2[1] * math.sin(rot_angle)
                        Y_new_c2 = c2[0] * math.sin(rot_angle) + c2[1] * math.cos(rot_angle)
                        Z_new_c2 = c2[2] = 3

                        X_new_c3 = c3[0] * math.cos(rot_angle) - c3[1] * math.sin(rot_angle)
                        Y_new_c3 = c3[0] * math.sin(rot_angle) + c3[1] * math.cos(rot_angle)
                        Z_new_c3 = c3[2] = 3
                        
                        X_new_c4 = c4[0] * math.cos(rot_angle) - c4[1] * math.sin(rot_angle)
                        Y_new_c4 = c4[0] * math.sin(rot_angle) + c4[1] * math.cos(rot_angle)
                        Z_new_c4 = c4[2] = 3
                                                
                        all_4points = ((X_new_c1, Y_new_c1, Z_new_c1), (X_new_c2, Y_new_c2, Z_new_c2), (X_new_c3, Y_new_c3, Z_new_c3), (X_new_c4, Y_new_c4, Z_new_c4))
                        all_4points_text = "New Coordinates \n" + '\n' + str((X_new_c1, Y_new_c1, Z_new_c1)) + '\n' + str((X_new_c2, Y_new_c2, Z_new_c2)) + '\n' + str((X_new_c3, Y_new_c3, Z_new_c3)) + '\n' + str((X_new_c4, Y_new_c4, Z_new_c4))
                        print(all_4points)
                        
                        text=scrolledtext.ScrolledText(Frame3, height=1, width=60)
                        text.insert(tk.END, all_4points_text)
                        text.grid(column=0, row=6, padx=(200,0), pady=(10,0))
                        
                        import numpy as np
                        import matplotlib.pyplot as plt
                        from mpl_toolkits.mplot3d import Axes3D
                        xline1 = [c1[0], c2[0], c3[0], c4[0]]
                        yline2 = [c1[1], c2[1], c3[1], c4[1]]
                        zline3 = [c1[2], c2[2], c3[2], c4[2]]
                        xline1.append[0]
                        yline2.append[0]
                        zline3.append[0]
#                    pts1 = [[c1[0], c1[1]],[c2[0], c2[1]]]
 #                   pts2 = [[all_2points[0][0], all_2points[0][1]],[all_2points[1][0], all_2points[1][1]]]
                        figure1 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                    #figure = plt.figure(figsize=(6,3))
                        ax1 = figure1.add_subplot(1,1,1, projection="3d")
                        scatter1 = FigureCanvasTkAgg(figure1, Frame2)
                        scatter1.get_tk_widget().grid()
                        ax1.scatter(xline1, yline2, zline3, c='b')
                        ax1.plot(xline1, yline2, zline3, color='b')
                        ax1.set_title('4 Coordinates (Original)')
                    #plot1.axis('equal')
                    
                        figure2 = plt.Figure(figsize=(4.4,3.4), dpi=100)
                        ax2 = figure2.add_subplot(1,1,1, projection="3d")
                        scatter2 = FigureCanvasTkAgg(figure2, Frame4)
                        scatter2.get_tk_widget().grid()
                    #plot1 = figure.add_subplot(1, 2, 2, projection="3d")
                        xline = [all_4points[0][0], all_4points[1][0], all_4points[2][0], all_4points[3][0]]
                        yline = [all_4points[0][1], all_4points[1][1], all_4points[2][1], all_4points[3][1]]
                        zline = [all_4points[0][2], all_4points[1][2], all_4points[2][2], all_4points[3][2]]
                        xline.append[0]
                        yline.append[0]
                        zline.append[0]
                        ax2.scatter(xline, yline, zline, c='r')
                        ax2.plot(xline, yline, zline, color='r')
                        ax2.set_title('4 Coodinates (Z Rotated)')
                        
                        Frame4.update()
                        Frame2.update()
                tk.Button(Frame1, text="Calculate", width=20, command=define_4coordinates).grid(row=5, column=0, padx=(320,0), pady = 10)
        tk.Button(Frame1, text="Compute", command=comando, width=20).grid(row=2, column=0, padx=(320,0), pady=5)

#def destroy_frame():
 #   Frame2.destroy()
#tk.Button(Frame1, text='Reload Graph', width=10, command=destroy_frame).grid(row=5, column=1)
        
word1 = 'Select the transformation type: '
Label1 = tk.Label(Frame1, text=word1, fg = 'black', font=font)
Label1.grid(row=0, column=0, sticky=tk.W, pady=2, padx=(190,0))

radVar = tk.IntVar()
translation = tk.Radiobutton(Frame1, text='2D Translation', variable = radVar, value=1, fg='black',
                            activeforeground='black', selectcolor='white', command=radCall)
translation.grid(column=0, row=0, sticky=tk.W, padx=(370, 0))
rotation = tk.Radiobutton(Frame1, text='3D Rotation', variable = radVar, value=2, fg='black',
                      activeforeground='black', selectcolor='white', command = radCall)
rotation.grid(column=0, row=0, sticky=tk.W, padx=(480,0))
win.update()
win.mainloop()
