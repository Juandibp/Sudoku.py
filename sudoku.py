from tkinter import *
from tkinter import messagebox
import webbrowser as wb

ventana = Tk()
ventana.title("Sudoku")
ventana.resizable(width=FALSE, height=FALSE)
ventana.geometry("450x450")
ventana.config(bg="Black")

imagen_sudoku = PhotoImage(file="img_sdk.png")
dis_menu = PhotoImage(file="dis_menu.png")
regresa = PhotoImage(file="regresar.png")
label_imagen = Label(ventana, image=imagen_sudoku, bg="Black").place(x=125, y=0)
label_dis = Label(ventana, image=dis_menu, bg="Black").place(x=-2, y=400)

barramenu = Menu(ventana)
ventana.config(menu=barramenu)
barramenu.add_cascade(label="Ayuda", command=lambda: None)
barramenu.add_cascade(label="Acerca de", command=lambda: acerca_de())
barramenu.add_cascade(label="Salir", command=lambda: salir())

bot_jugar = Button(ventana, text="J u g a r", fg="Black", bg="#00f0ff", font="Helvetica 20 bold",
                command=lambda: (jugar(), tamanno("jugar"))).place(x=165, y=225)

bot_conf = Button(ventana, text="Configurar", fg="Black", bg="#00f0ff", font="Helvetica 16 bold",
                command=lambda: (config(), tamanno("conf"))).place(x=75, y=325)

bot_parti = Button(ventana, text="Partidas", fg="Black", bg="#00f0ff", font="Helvetica 16 bold",
                command=lambda: None).place(x=275, y=325)
matriz1 = [5, 3, '', 6, '', '', '', 9, 8]
matriz2 = ['', 7, '', 1, 9, 5, '', '', '']
matriz3 = ['', '', '', '', '', '', '', 6, '']
matriz4 = [8, '', '', 4, '', '', 7, '', '']
matriz5 = ['', 6, '', 8, '', 3, '', 2, '']
matriz6 = ['', '', 3, '', '', 1, '', '', 6]
matriz7 = ['', 6, '', '', '', '', '', '', '']
matriz8 = ['', '', '', 4, 1, 9, '', 8, '']
matriz9 = [2, 8, '', '', '', 5, '', 7, 9]

matriz = [matriz1, matriz2, matriz3,
        matriz4, matriz5, matriz6,
        matriz7, matriz8, matriz9]
botones = [["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF"]]
b_editar = ""
tipo = 0


def jugar():
    frame_jugar = Frame(ventana, bg="Black", width=750, height=600)
    frame_jugar.place(x=0, y=0)

    bot_menu1 = Button(frame_jugar, image=regresa, bg="Black", command=lambda: (frame_jugar.destroy(), tamanno("menu")))
    bot_menu1.place(x=595, y=535)

    bot_ini_juego = Button(frame_jugar, text="Iniciar\n Juego", bg="#0cd4c4", font="blond", width=10,
                        command=lambda: None)
    bot_ini_juego.place(x=575, y=95)

    bot_bor_jugada = Button(frame_jugar, text="Borrar\n Jugada", bg="#94ece4", font="blond", width=10,
                        command=lambda: None)
    bot_bor_jugada.place(x=575, y=155)

    bot_ter_juego = Button(frame_jugar, text="Terminar\n Juego", bg="#b2b4ce", font="blond", width=10,
                        command=lambda: None)
    bot_ter_juego.place(x=575, y=215)

    bot_bor_juego = Button(frame_jugar, text="Borrar\n Juego", bg="#0b788e", font="blond", width=10,
                        command=lambda: None)
    bot_bor_juego.place(x=575, y=275)

    bot_top10 = Button(frame_jugar, text="Top\n 10", bg="Blue", fg="#8ca058", font="blond", width=10,
                    command=lambda: None)
    bot_top10.place(x=575, y=335)

    bot_gua_juego = Button(frame_jugar, text="Guardar\n Juego", bg="#acccc4", font="blond", width=10,
                        command=lambda: None)
    bot_gua_juego.place(x=575, y=395)

    bot_car_juego = Button(frame_jugar, text="Cargar\n Juego", bg="#2c5b47", font="blond", width=10,
                        command=lambda: None)
    bot_car_juego.place(x=575, y=455)

    bot_a = Button(frame_jugar, text=botones[0][0], bg=botones[1][0], width=6, height=2,
                command=lambda: boton_a())
    bot_a.place(x=10, y=550)
    bot_b = Button(frame_jugar, text=botones[0][1], bg=botones[1][1], width=6, height=2,
                command=lambda: boton_b())
    bot_b.place(x=67, y=550)
    bot_c = Button(frame_jugar, text=botones[0][2], bg=botones[1][2], width=6, height=2,
                command=lambda: boton_c())
    bot_c.place(x=124, y=550)
    bot_d = Button(frame_jugar, text=botones[0][3], bg=botones[1][3], width=6, height=2,
                command=lambda: boton_d())
    bot_d.place(x=187, y=550)
    bot_e = Button(frame_jugar, text=botones[0][4], bg=botones[1][4], width=6, height=2,
                command=lambda: boton_e())
    bot_e.place(x=244, y=550)
    bot_f = Button(frame_jugar, text=botones[0][5], bg=botones[1][5], width=6, height=2,
                command=lambda: boton_f())
    bot_f.place(x=301, y=550)
    bot_g = Button(frame_jugar, text=botones[0][6], bg=botones[1][6], width=6, height=2,
                command=lambda: boton_g())
    bot_g.place(x=364, y=550)
    bot_h = Button(frame_jugar, text=botones[0][7], bg=botones[1][7], width=6, height=2,
                command=lambda: boton_h())
    bot_h.place(x=421, y=550)
    bot_i = Button(frame_jugar, text=botones[0][8], bg=botones[1][8], width=6, height=2,
                command=lambda: boton_i())
    bot_i.place(x=478, y=550)

# ----------------------------------------------------------------------------------------------------------------------
    label_11 = Label(frame_jugar, text=matriz[0][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_11.bind("<Button-1>", lambda e:edit_bot(11))
    label_11.place(x=10, y=10)
    label_12 = Label(frame_jugar, text=matriz[0][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_12.bind("<Button-1>", lambda e:edit_bot(12))
    label_12.place(x=67, y=10)
    label_13 = Label(frame_jugar, text=matriz[0][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_13.bind("<Button-1>", lambda e:edit_bot(13))
    label_13.place(x=124, y=10)
    label_14 = Label(frame_jugar, text=matriz[0][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_14.bind("<Button-1>", lambda e:edit_bot(14))
    label_14.place(x=10, y=67)
    label_15 = Label(frame_jugar, text=matriz[0][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_15.bind("<Button-1>", lambda e:edit_bot(15))
    label_15.place(x=67, y=67)
    label_16 = Label(frame_jugar, text=matriz[0][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_16.bind("<Button-1>", lambda e:edit_bot(16))
    label_16.place(x=124, y=67)
    label_17 = Label(frame_jugar, text=matriz[0][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_17.bind("<Button-1>", lambda e:edit_bot(17))
    label_17.place(x=10, y=124)
    label_18 = Label(frame_jugar, text=matriz[0][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_18.bind("<Button-1>", lambda e:edit_bot(18))
    label_18.place(x=67, y=124)
    label_19 = Label(frame_jugar, text=matriz[0][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_19.bind("<Button-1>", lambda e:edit_bot(19))
    label_19.place(x=124, y=124)

    label_21 = Label(frame_jugar, text=matriz[1][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_21.bind("<Button-1>", lambda e:edit_bot(21))
    label_21.place(x=187, y=10)
    label_22 = Label(frame_jugar, text=matriz[1][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_22.bind("<Button-1>", lambda e:edit_bot(22))
    label_22.place(x=244, y=10)
    label_23 = Label(frame_jugar, text=matriz[1][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_23.bind("<Button-1>", lambda e:edit_bot(23))
    label_23.place(x=301, y=10)
    label_24 = Label(frame_jugar, text=matriz[1][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_24.bind("<Button-1>", lambda e:edit_bot(24))
    label_24.place(x=187, y=67)
    label_25 = Label(frame_jugar, text=matriz[1][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_25.bind("<Button-1>", lambda e:edit_bot(25))
    label_25.place(x=244, y=67)
    label_26 = Label(frame_jugar, text=matriz[1][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_26.bind("<Button-1>", lambda e:edit_bot(26))
    label_26.place(x=301, y=67)
    label_27 = Label(frame_jugar, text=matriz[1][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_27.bind("<Button-1>", lambda e:edit_bot(27))
    label_27.place(x=187, y=124)
    label_28 = Label(frame_jugar, text=matriz[1][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_28.bind("<Button-1>", lambda e:edit_bot(28))
    label_28.place(x=244, y=124)
    label_29 = Label(frame_jugar, text=matriz[1][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_29.bind("<Button-1>", lambda e:edit_bot(29))
    label_29.place(x=301, y=124)

    label_31 = Label(frame_jugar, text=matriz[2][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_31.bind("<Button-1>", lambda e:edit_bot(31))
    label_31.place(x=364, y=10)
    label_32 = Label(frame_jugar, text=matriz[2][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_32.bind("<Button-1>", lambda e:edit_bot(32))
    label_32.place(x=421, y=10)
    label_33 = Label(frame_jugar, text=matriz[2][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_33.bind("<Button-1>", lambda e:edit_bot(33))
    label_33.place(x=478, y=10)
    label_34 = Label(frame_jugar, text=matriz[2][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_34.bind("<Button-1>", lambda e:edit_bot(34))
    label_34.place(x=364, y=67)
    label_35 = Label(frame_jugar, text=matriz[2][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_35.bind("<Button-1>", lambda e:edit_bot(35))
    label_35.place(x=421, y=67)
    label_36 = Label(frame_jugar, text=matriz[2][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_36.bind("<Button-1>", lambda e:edit_bot(36))
    label_36.place(x=478, y=67)
    label_37 = Label(frame_jugar, text=matriz[2][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_37.bind("<Button-1>", lambda e:edit_bot(37))
    label_37.place(x=364, y=124)
    label_38 = Label(frame_jugar, text=matriz[2][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_38.bind("<Button-1>", lambda e:edit_bot(38))
    label_38.place(x=421, y=124)
    label_39 = Label(frame_jugar, text=matriz[2][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_39.bind("<Button-1>", lambda e:edit_bot(39))
    label_39.place(x=478, y=124)
# ----------------------------------------------------------------------------------------------------------------------
    label_41 = Label(frame_jugar, text=matriz[3][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_41.bind("<Button-1>", lambda e:edit_bot(41))
    label_41.place(x=10, y=187)
    label_42 = Label(frame_jugar, text=matriz[3][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_42.bind("<Button-1>", lambda e:edit_bot(42))
    label_42.place(x=67, y=187)
    label_43 = Label(frame_jugar, text=matriz[3][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_43.bind("<Button-1>", lambda e:edit_bot(43))
    label_43.place(x=124, y=187)
    label_44 = Label(frame_jugar, text=matriz[3][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_44.bind("<Button-1>", lambda e:edit_bot(44))
    label_44.place(x=10, y=244)
    label_45 = Label(frame_jugar, text=matriz[3][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_45.bind("<Button-1>", lambda e:edit_bot(45))
    label_45.place(x=67, y=244)
    label_46 = Label(frame_jugar, text=matriz[3][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_46.bind("<Button-1>", lambda e:edit_bot(46))
    label_46.place(x=124, y=244)
    label_47 = Label(frame_jugar, text=matriz[3][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_47.bind("<Button-1>", lambda e:edit_bot(47))
    label_47.place(x=10, y=301)
    label_48 = Label(frame_jugar, text=matriz[3][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_48.bind("<Button-1>", lambda e:edit_bot(48))
    label_48.place(x=67, y=301)
    label_49 = Label(frame_jugar, text=matriz[3][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_49.bind("<Button-1>", lambda e:edit_bot(49))
    label_49.place(x=124, y=301)

    label_51 = Label(frame_jugar, text=matriz[4][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_51.bind("<Button-1>", lambda e:edit_bot(51))
    label_51.place(x=187, y=187)
    label_52 = Label(frame_jugar, text=matriz[4][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_52.bind("<Button-1>", lambda e:edit_bot(52))
    label_52.place(x=244, y=187)
    label_53 = Label(frame_jugar, text=matriz[4][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_53.bind("<Button-1>", lambda e:edit_bot(53))
    label_53.place(x=301, y=187)
    label_54 = Label(frame_jugar, text=matriz[4][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_54.bind("<Button-1>", lambda e:edit_bot(54))
    label_54.place(x=187, y=244)
    label_55 = Label(frame_jugar, text=matriz[4][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_55.bind("<Button-1>", lambda e:edit_bot(55))
    label_55.place(x=244, y=244)
    label_56 = Label(frame_jugar, text=matriz[4][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_56.bind("<Button-1>", lambda e:edit_bot(56))
    label_56.place(x=301, y=244)
    label_57 = Label(frame_jugar, text=matriz[4][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_57.bind("<Button-1>", lambda e:edit_bot(57))
    label_57.place(x=187, y=301)
    label_58 = Label(frame_jugar, text=matriz[4][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_58.bind("<Button-1>", lambda e:edit_bot(58))
    label_58.place(x=244, y=301)
    label_59 = Label(frame_jugar, text=matriz[4][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_59.bind("<Button-1>", lambda e:edit_bot(59))
    label_59.place(x=301, y=301)

    label_61 = Label(frame_jugar, text=matriz[5][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_61.bind("<Button-1>", lambda e:edit_bot(61))
    label_61.place(x=364, y=187)
    label_62 = Label(frame_jugar, text=matriz[5][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_62.bind("<Button-1>", lambda e:edit_bot(62))
    label_62.place(x=421, y=187)
    label_63 = Label(frame_jugar, text=matriz[5][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_63.bind("<Button-1>", lambda e:edit_bot(63))
    label_63.place(x=478, y=187)
    label_64 = Label(frame_jugar, text=matriz[5][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_64.bind("<Button-1>", lambda e:edit_bot(64))
    label_64.place(x=364, y=244)
    label_65 = Label(frame_jugar, text=matriz[5][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_65.bind("<Button-1>", lambda e:edit_bot(65))
    label_65.place(x=421, y=244)
    label_66 = Label(frame_jugar, text=matriz[5][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_66.bind("<Button-1>", lambda e:edit_bot(66))
    label_66.place(x=478, y=244)
    label_67 = Label(frame_jugar, text=matriz[5][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_67.bind("<Button-1>", lambda e:edit_bot(67))
    label_67.place(x=364, y=301)
    label_68 = Label(frame_jugar, text=matriz[5][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_68.bind("<Button-1>", lambda e:edit_bot(68))
    label_68.place(x=421, y=301)
    label_69 = Label(frame_jugar, text=matriz[5][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_69.bind("<Button-1>", lambda e:edit_bot(69))
    label_69.place(x=478, y=301)
# ----------------------------------------------------------------------------------------------------------------------
    label_71 = Label(frame_jugar, text=matriz[6][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_71.bind("<Button-1>", lambda e:edit_bot(71))
    label_71.place(x=10, y=364)
    label_72 = Label(frame_jugar, text=matriz[6][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_72.bind("<Button-1>", lambda e:edit_bot(72))
    label_72.place(x=67, y=364)
    label_73 = Label(frame_jugar, text=matriz[6][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_73.bind("<Button-1>", lambda e:edit_bot(73))
    label_73.place(x=124, y=364)
    label_74 = Label(frame_jugar, text=matriz[6][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_74.bind("<Button-1>", lambda e:edit_bot(74))
    label_74.place(x=10, y=421)
    label_75 = Label(frame_jugar, text=matriz[6][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_75.bind("<Button-1>", lambda e:edit_bot(75))
    label_75.place(x=67, y=421)
    label_76 = Label(frame_jugar, text=matriz[6][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_76.bind("<Button-1>", lambda e:edit_bot(76))
    label_76.place(x=124, y=421)
    label_77 = Label(frame_jugar, text=matriz[6][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_77.bind("<Button-1>", lambda e:edit_bot(77))
    label_77.place(x=10, y=478)
    label_78 = Label(frame_jugar, text=matriz[6][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_78.bind("<Button-1>", lambda e:edit_bot(78))
    label_78.place(x=67, y=478)
    label_79 = Label(frame_jugar, text=matriz[6][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_79.bind("<Button-1>", lambda e:edit_bot(79))
    label_79.place(x=124, y=478)

    label_81 = Label(frame_jugar, text=matriz[7][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_81.bind("<Button-1>", lambda e:edit_bot(81))
    label_81.place(x=187, y=364)
    label_82 = Label(frame_jugar, text=matriz[7][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_82.bind("<Button-1>", lambda e:edit_bot(82))
    label_82.place(x=244, y=364)
    label_83 = Label(frame_jugar, text=matriz[7][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_83.bind("<Button-1>", lambda e:edit_bot(83))
    label_83.place(x=301, y=364)
    label_84 = Label(frame_jugar, text=matriz[7][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_84.bind("<Button-1>", lambda e:edit_bot(84))
    label_84.place(x=187, y=421)
    label_85 = Label(frame_jugar, text=matriz[7][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_85.bind("<Button-1>", lambda e:edit_bot(85))
    label_85.place(x=244, y=421)
    label_86 = Label(frame_jugar, text=matriz[7][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_86.bind("<Button-1>", lambda e:edit_bot(86))
    label_86.place(x=301, y=421)
    label_87 = Label(frame_jugar, text=matriz[7][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_87.bind("<Button-1>", lambda e:edit_bot(87))
    label_87.place(x=187, y=478)
    label_88 = Label(frame_jugar, text=matriz[7][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_88.bind("<Button-1>", lambda e:edit_bot(88))
    label_88.place(x=244, y=478)
    label_89 = Label(frame_jugar, text=matriz[7][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_89.bind("<Button-1>", lambda e:edit_bot(89))
    label_89.place(x=301, y=478)

    label_91 = Label(frame_jugar, text=matriz[8][0], bg="white", font="Helvetica 16", width=4, height=2)
    label_91.bind("<Button-1>", lambda e:edit_bot(91))
    label_91.place(x=364, y=364)
    label_92 = Label(frame_jugar, text=matriz[8][1], bg="white", font="Helvetica 16", width=4, height=2)
    label_92.bind("<Button-1>", lambda e:edit_bot(92))
    label_92.place(x=421, y=364)
    label_93 = Label(frame_jugar, text=matriz[8][2], bg="white", font="Helvetica 16", width=4, height=2)
    label_93.bind("<Button-1>", lambda e:edit_bot(93))
    label_93.place(x=478, y=364)
    label_94 = Label(frame_jugar, text=matriz[8][3], bg="white", font="Helvetica 16", width=4, height=2)
    label_94.bind("<Button-1>", lambda e:edit_bot(94))
    label_94.place(x=364, y=421)
    label_95 = Label(frame_jugar, text=matriz[8][4], bg="white", font="Helvetica 16", width=4, height=2)
    label_95.bind("<Button-1>", lambda e:edit_bot(95))
    label_95.place(x=421, y=421)
    label_96 = Label(frame_jugar, text=matriz[8][5], bg="white", font="Helvetica 16", width=4, height=2)
    label_96.bind("<Button-1>", lambda e:edit_bot(96))
    label_96.place(x=478, y=421)
    label_97 = Label(frame_jugar, text=matriz[8][6], bg="white", font="Helvetica 16", width=4, height=2)
    label_97.bind("<Button-1>", lambda e:edit_bot(97))
    label_97.place(x=364, y=478)
    label_98 = Label(frame_jugar, text=matriz[8][7], bg="white", font="Helvetica 16", width=4, height=2)
    label_98.bind("<Button-1>", lambda e:edit_bot(98))
    label_98.place(x=421, y=478)
    label_99 = Label(frame_jugar, text=matriz[8][8], bg="white", font="Helvetica 16", width=4, height=2)
    label_99.bind("<Button-1>", lambda e:edit_bot(99))
    label_99.place(x=478, y=478)

    def boton_a():
        global  b_editar
        print("Me Cago en franco")
        print(type(b_editar))
        if b_editar == 11:
            if tipo == 0:
                label_11['text'] = botones[0][0]
                matriz[0][0]=botones[0][0]

            else:
                label_11['bg'] = botones[1][0]
                matriz[0][0] = botones[1][0]
        elif b_editar == 12:
            pass

        elif b_editar == 13:
            pass

        elif b_editar == 14:
            pass

        elif b_editar == 15:
            pass

        elif b_editar == 16:
            pass

        elif b_editar == 17:
            pass

        elif b_editar == 18:
            pass

        elif b_editar == 19:
            pass

        elif b_editar == 21:
            pass

        elif b_editar == 22:
            pass

        elif b_editar == 23:
            pass

        elif b_editar == 24:
            pass

        elif b_editar == 25:
            pass

        elif b_editar == 26:
            pass

        elif b_editar == 27:
            pass

        elif b_editar == 28:
            pass

        elif b_editar == 29:
            pass

        elif b_editar == 31:
            pass

        elif b_editar == 32:
            pass

        elif b_editar == 33:
            pass

        elif b_editar == 34:
            pass

        elif b_editar == 35:
            pass

        elif b_editar == 36:
            pass

        elif b_editar == 37:
            pass

        elif b_editar == 38:
            pass

        elif b_editar == 39:
            pass

        elif b_editar == 41:
            pass

        elif b_editar == 42:
            pass

        elif b_editar == 43:
            pass

        elif b_editar == 44:
            pass

        elif b_editar == 45:
            pass

        elif b_editar == 46:
            pass

        elif b_editar == 47:
            pass

        elif b_editar == 48:
            pass

        elif b_editar == 49:
            pass

        elif b_editar == 51:
            pass

        elif b_editar == 52:
            pass

        elif b_editar == 53:
            pass

        elif b_editar == 54:
            pass

        elif b_editar == 55:
            pass

        elif b_editar == 56:
            pass

        elif b_editar == 57:
            pass

        elif b_editar == 58:
            pass

        elif b_editar == 59:
            pass

        elif b_editar == 61:
            pass

        elif b_editar == 62:
            pass

        elif b_editar == 63:
            pass

        elif b_editar == 64:
            pass

        elif b_editar == 65:
            pass

        elif b_editar == 66:
            pass

        elif b_editar == 67:
            pass

        elif b_editar == 68:
            pass

        elif b_editar == 69:
            pass

        elif b_editar == 71:
            pass

        elif b_editar == 72:
            pass

        elif b_editar == 73:
            pass

        elif b_editar == 74:
            pass

        elif b_editar == 75:
            pass

        elif b_editar == 76:
            pass

        elif b_editar == 77:
            pass

        elif b_editar == 78:
            pass

        elif b_editar == 79:
            pass

        elif b_editar == 81:
            pass

        elif b_editar == 82:
            pass

        elif b_editar == 83:
            pass

        elif b_editar == 84:
            pass

        elif b_editar == 85:
            pass

        elif b_editar == 86:
            pass

        elif b_editar == 87:
            pass

        elif b_editar == 88:
            pass

        elif b_editar == 89:
            pass

        elif b_editar == 91:
            pass

        elif b_editar == 92:
            pass

        elif b_editar == 93:
            pass

        elif b_editar == 94:
            pass

        elif b_editar == 95:
            pass

        elif b_editar == 96:
            pass

        elif b_editar == 97:
            pass

        elif b_editar == 98:
            pass

        elif b_editar == 99:
            pass


def config():
    frame_conf = Frame(ventana, bg="#010111", width=750, height=450)
    frame_conf.place(x=0, y=0)

    bot_menu2 = Button(frame_conf, image=regresa, bg="#010111", command=lambda: (frame_conf.destroy(), tamanno("menu")))
    bot_menu2.place(x=675, y=400)

    label_nivel = Label(frame_conf, text="Nivel", bg="#010111", fg="White", font=("Arial ", 15))
    label_nivel.place(x=100, y=50)
    label_reloj = Label(frame_conf, text="Reloj", bg="#010111", fg="White", font=("Arial", 15))
    label_reloj.place(x=600, y=50)
    label_casilla = Label(frame_conf, text="Casillas", bg="#010111", fg="White", font=("Arial", 15))
    label_casilla.place(x=350, y=200)
    nivel_vr = IntVar()
    nivel_vr.set(0)
    reloj_vr = IntVar()
    reloj_vr.set(1)
    casilla_vr = IntVar()
    casilla_vr.set(0)

    Radiobutton(frame_conf, text="Facil", variable=nivel_vr, value=0, bg="#010111", fg="Green",
                font=("Arial", 15), command=lambda: None).place(x=50, y=75)
    Radiobutton(frame_conf, text="Intermedio", variable=nivel_vr, value=1, bg="#010111", fg="Yellow",
                font=("Arial", 15), command=lambda: None).place(x=50, y=115)
    Radiobutton(frame_conf, text="Dificil", variable=nivel_vr, value=2, bg="#010111", fg="Red",
                font=("Arial", 15), command=lambda: None).place(x=50, y=155)

    Radiobutton(frame_conf, text="Si", variable=reloj_vr, value=1, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: None).place(x=550, y=75)
    Radiobutton(frame_conf, text="No", variable=reloj_vr, value=0, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: None).place(x=550, y=115)
    Radiobutton(frame_conf, text="Timer", variable=reloj_vr, value=2, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: None).place(x=550, y=155)

    Radiobutton(frame_conf, text="Numeros", variable=reloj_vr, value=0, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: casillas(0)).place(x=100, y=250)
    Radiobutton(frame_conf, text="Letras", variable=reloj_vr, value=1, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: casillas(1)).place(x=100, y=300)
    Radiobutton(frame_conf, text="Colores", variable=reloj_vr, value=2, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: casillas(2)).place(x=100, y=350)
    Radiobutton(frame_conf, text="Signos", variable=reloj_vr, value=3, bg="#010111", fg="White",
                font=("Arial", 15), command=lambda: casillas(3)).place(x=100, y=400)

    label_n1 = Label(frame_conf, text="1", font="Helvetica 16", width=3)
    label_n1.place(x=210, y=255)
    label_n2 = Label(frame_conf, text="2", font="Helvetica 16", width=3)
    label_n2.place(x=255, y=255)
    label_n3 = Label(frame_conf, text="3", font="Helvetica 16", width=3)
    label_n3.place(x=300, y=255)
    label_n4 = Label(frame_conf, text="4", font="Helvetica 16", width=3)
    label_n4.place(x=345, y=255)
    label_n5 = Label(frame_conf, text="5", font="Helvetica 16", width=3)
    label_n5.place(x=390, y=255)
    label_n6 = Label(frame_conf, text="6", font="Helvetica 16", width=3)
    label_n6.place(x=435, y=255)
    label_n7 = Label(frame_conf, text="7", font="Helvetica 16", width=3)
    label_n7.place(x=480, y=255)
    label_n8 = Label(frame_conf, text="8", font="Helvetica 16", width=3)
    label_n8.place(x=525, y=255)
    label_n9 = Label(frame_conf, text="9", font="Helvetica 16", width=3)
    label_n9.place(x=570, y=255)

    label_la = Label(frame_conf, text="A", font="Helvetica 16", width=3)
    label_la.place(x=210, y=305)
    label_lb = Label(frame_conf, text="B", font="Helvetica 16", width=3)
    label_lb.place(x=255, y=305)
    label_lc = Label(frame_conf, text="C", font="Helvetica 16", width=3)
    label_lc.place(x=300, y=305)
    label_ld = Label(frame_conf, text="D", font="Helvetica 16", width=3)
    label_ld.place(x=345, y=305)
    label_le = Label(frame_conf, text="E", font="Helvetica 16", width=3)
    label_le.place(x=390, y=305)
    label_lf = Label(frame_conf, text="F", font="Helvetica 16", width=3)
    label_lf.place(x=435, y=305)
    label_lg = Label(frame_conf, text="G", font="Helvetica 16", width=3)
    label_lg.place(x=480, y=305)
    label_lh = Label(frame_conf, text="H", font="Helvetica 16", width=3)
    label_lh.place(x=525, y=305)
    label_li = Label(frame_conf, text="I", font="Helvetica 16", width=3)
    label_li.place(x=570, y=305)

    label_la = Label(frame_conf, bg="#FF6666", font="Helvetica 16", width=3)
    label_la.place(x=210, y=355)
    label_lb = Label(frame_conf, bg="#FFC066", font="Helvetica 16", width=3)
    label_lb.place(x=255, y=355)
    label_lc = Label(frame_conf, bg="#FFE866", font="Helvetica 16", width=3)
    label_lc.place(x=300, y=355)
    label_ld = Label(frame_conf, bg="#A2FF66", font="Helvetica 16", width=3)
    label_ld.place(x=345, y=355)
    label_le = Label(frame_conf, bg="#66FF84", font="Helvetica 16", width=3)
    label_le.place(x=390, y=355)
    label_lf = Label(frame_conf, bg="#66FFBC", font="Helvetica 16", width=3)
    label_lf.place(x=435, y=355)
    label_lg = Label(frame_conf, bg="#6697FF", font="Helvetica 16", width=3)
    label_lg.place(x=480, y=355)
    label_lh = Label(frame_conf, bg="#9B66FF", font="Helvetica 16", width=3)
    label_lh.place(x=525, y=355)
    label_li = Label(frame_conf, bg="#FF66FF", font="Helvetica 16", width=3)
    label_li.place(x=570, y=355)

    label_la = Label(frame_conf, text="!", font="Helvetica 16", width=3)
    label_la.place(x=210, y=405)
    label_lb = Label(frame_conf, text="@", font="Helvetica 16", width=3)
    label_lb.place(x=255, y=405)
    label_lc = Label(frame_conf, text="#", font="Helvetica 16", width=3)
    label_lc.place(x=300, y=405)
    label_ld = Label(frame_conf, text="$", font="Helvetica 16", width=3)
    label_ld.place(x=345, y=405)
    label_le = Label(frame_conf, text="%", font="Helvetica 16", width=3)
    label_le.place(x=390, y=405)
    label_lf = Label(frame_conf, text="&", font="Helvetica 16", width=3)
    label_lf.place(x=435, y=405)
    label_lg = Label(frame_conf, text="+", font="Helvetica 16", width=3)
    label_lg.place(x=480, y=405)
    label_lh = Label(frame_conf, text="<", font="Helvetica 16", width=3)
    label_lh.place(x=525, y=405)
    label_li = Label(frame_conf, text=">", font="Helvetica 16", width=3)
    label_li.place(x=570, y=405)


# ----------------------------------------------------------------------------------------------------------------------
# esta funcion despliega el manual de usuario
def ayuda():
    wb.open_new(r'C:\Users\rd740\Desktop\Progras\Programa3_Rohi_Prendas\manual_de_usuario_sudoku.pdf')


# Esta funcion abri una casilla la cual muestra informacion sobre el porgrama y su autor
def acerca_de():
    messagebox.showinfo("Acerca del programa", "Sudoku\n"
                                               "Versión 1.0\n"
                                               "Fecha de creacion: 26/11/2019\n"
                                               "Rohi Daniel Prendas")


# Esta funcion se sale del programa
def salir():
    valor = messagebox.askquestion("SALIR", "¿ ESTA SEGURO DE TERMINAR EL JUEGO ?")
    if valor == "yes":
        ventana.destroy()


# Esta funcion se encarga de cambiar el tamaño del interfaz
def tamanno(tam):
    if tam == "menu":
        ventana.geometry("450x450")

    elif tam == "jugar":
        ventana.geometry("750x600")

    elif tam == "conf":
        ventana.geometry("750x450")


# Esta funcion cambia el texto/color de las casillas
def casillas(x):
    global botones, tipo
    if x == 0:
        tipo = 0
        botones = [["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                ["#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF"]]

    elif x == 1:
        tipo = 0
        botones = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                ["#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF"]]

    elif x == 2:
        tipo = 1
        botones = [["", "", "", "", "", "", "", "", ""],
                ["#FF6666", "#FFC066", "#FFE866", "#A2FF66", "#66FF84", "#66FFBC", "#6697FF", "#9B66FF", "#FF66FF"]]

    elif x == 3:
        tipo = 0
        botones = [["!", "@", "#", "$", "%", "&", "+", "<", ">"],
                ["#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF", "#66FFFF"]]


def edit_bot(x):
    print(x)
    global b_editar
    b_editar = x


ventana.mainloop()
