import curses


class MenuOpciones:

    def __init__(self, stdscr, y=0, x=0, submenu=False, descripcion=False):
        # set menu parameter as class property
        self._item          = []
        self._subMenu      = submenu
        self.__win         = stdscr
        self._descripcion  = descripcion
        self.__y, self.__x = y , x
        # get screen height and width
        self.screen_height, self.screen_width = self.__win.getmaxyx()
        self._selected_opc_idx = 0

        # color scheme
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)   # Color Opciones
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Color Selección

    def __str__(self):
        if self._subMenu:
            return 'SubMenu'
        else:
            return 'Menu'

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def add_item(self, item):
        self._item.append(item)
        # Preparamos los str de los Nombres (Opciones de menu)
        self._prep_opc()        
    
    def del_item(self, item):
        self._item.remove(item)

    def _prep_opc(self):
        self._mas_largo = 0
        for opc in self._item:
            if len(opc.nombre) > self._mas_largo:
                self._mas_largo = len(opc.nombre)

        for idx, opc in enumerate(self._item):
            if opc.nombre in [' - ', ' = ', ' * ', ' ─ ', ' ═ ']:
                self._item[idx].nombre = opc.nombre.strip()*self._mas_largo
            else:
                self._item[idx].nombre = opc.nombre.center(self._mas_largo)

    def _print_menuh(self):
        x = self.__x
        self.__win.attron(curses.color_pair(1))
        self.__win.addstr(self.__y,self.__x, ' '*self.screen_width)
        self.__win.attroff(curses.color_pair(1))
        for idx, opc in enumerate(self._item):
            if idx == self._selected_opc_idx:
                # opción Seleccionada
                self.__win.attron(curses.color_pair(2))
                self.__win.addstr(self.__y,x, opc.nombre)
                self.__win.attroff(curses.color_pair(2))
            else:
                self.__win.attron(curses.color_pair(1))
                self.__win.addstr(self.__y,x, opc.nombre)
                self.__win.attroff(curses.color_pair(1))
            x += len(opc.nombre)
        # Imprime la descripcion de las opciones, si esta seleccionado
        # if self.descripcion:
        #     self.__win.addstr(self.screen_height-1, 1, opc.des)

    def _print_menuv(self):
        for idx, opc in enumerate(self._item):
            x = self.__x
            y = self.__y + idx
            if idx == self._selected_opc_idx:
                self.__win.attron(curses.color_pair(2))
                self.__win.addstr(y, x, opc.nombre)
                self.__win.attroff(curses.color_pair(2))
            else:
                self.__win.attron(curses.color_pair(1))
                self.__win.addstr(y, x, opc.nombre)
                self.__win.attroff(curses.color_pair(1))
        # Imprime la descripcion de las opciones, si esta seleccionado
        # if self.descripcion:
        #     self.__win.addstr(self.screen_height-1, 1, self.desc[selected_opc_idx])

    def _print_menu(self):
        if not self._subMenu:
            self._print_menuh()
        else:
            self._print_menuv()

    def _borra_menuv(self):
        for idx, opc in enumerate(self._item):
            x = self.__x
            y = self.__y + idx
            
            self.__win.addstr(y, x, ' '*self._mas_largo)

    def show_menu(self):
        # print the menu
        self._print_menu()

        while 1:
            key = self.__win.getch()
            if (key == curses.KEY_UP or key == curses.KEY_LEFT) and self._selected_opc_idx > 0:
                self._selected_opc_idx -= 1
            elif (key == curses.KEY_DOWN or key == curses.KEY_RIGHT) and self._selected_opc_idx < len(self._item) - 1:
                self._selected_opc_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if str(self._item[self._selected_opc_idx].accion) == 'SubMenu':
                    self._item[self._selected_opc_idx].accion.x = self._mas_largo * self._selected_opc_idx
                    self._item[self._selected_opc_idx].accion.y = self.__y + 1
                    self._item[self._selected_opc_idx].accion.show_menu()
                # Si la accion es '' es una separación no hacemos nada
                elif self._item[self._selected_opc_idx].accion != '':
                    # Si es submenu, lo borramos y ejecutamos la Accion
                    if self._subMenu:
                        self._borra_menuv()  
                    return self._item[self._selected_opc_idx].accion()
            self._print_menu()



if __name__ == "__main__":
    print ('Es una clase')