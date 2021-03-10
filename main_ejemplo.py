#!/usr/bin/env python3

import curses

from classmenu.itemmenu     import ItemMenu
from classmenu.menuopciones import MenuOpciones
from classmenu.actionlist   import ActionList


def main(stdscr):
    curses.curs_set(0)
    def opc1():
        stdscr.addstr(1,30, 'Opción 1 ....')

    def opc2():
        stdscr.addstr(1,30, 'Opción 2 ....')

    def opc3():
        stdscr.addstr(1,30, 'Opción 3 ....')    

    submnu = MenuOpciones(stdscr, submenu=True)
    submnu.add_item(ItemMenu('Opc1',opc1))
    submnu.add_item(ItemMenu('Opcion2',opc2))
    submnu.add_item(ItemMenu('─',''))
    submnu.add_item(ItemMenu('Opc3',opc3))


    mnu = MenuOpciones(stdscr)
    mnu.add_item(ItemMenu('Archivo',submnu, 'Menu Archivo'))
    mnu.add_item(ItemMenu('Editar',submnu, 'Edita el Archivo'))
    mnu.add_item(ItemMenu('Ayuda',opc3, 'Acerca de...'))


    # acciones = ActionList()
    # acciones.add_accion(opc1)
    # acciones.add_accion(opc2)
    # acciones.add_accion(opc3)


    k=0
    while (k != ord('q')):
        seleccion = mnu.show_menu()
        # if str(seleccion) == 'SubMenu':
        #     stdscr.addstr(8,0, 'Es un SubMenu')
        # else:
        #     stdscr.addstr(8,0, str(seleccion))
        #subsel = submnu.show_menu()
        k = stdscr.getch()




if __name__ == "__main__":
    curses.wrapper(main)

