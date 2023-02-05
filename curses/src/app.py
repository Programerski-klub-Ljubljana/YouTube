import curses
import time

from curses.domain import Svet


class Terminal:
	def __init__(self):
		self._stdscr = None
		self.svet = None

	def run(self):
		print('RUN')
		self._start()
		self._main()
		self._end()

	def _start(self):
		self._stdscr = curses.initscr()
		self.svet = Svet(height=curses.LINES, width=curses.COLS)
		curses.start_color()
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
		curses.curs_set(False)
		curses.noecho()
		curses.cbreak()

		self._stdscr.nodelay(True)
		self._stdscr.keypad(True)

	def _main(self):
		print('---------')
		for i in range(1000):
			char = self._stdscr.getch()
			if char == 97:
				self.svet.plosca.move(dx=-1, dy=0)
			if char == 100:
				self.svet.plosca.move(dx=1, dy=0)
			self._stdscr.erase()
			self._stdscr.addstr(self.svet.plosca.y, self.svet.plosca.x, self.svet.plosca.simbol * self.svet.plosca.sirina, curses.A_BOLD | curses.A_STANDOUT | curses.color_pair(1))
			self._stdscr.addstr(self.svet.zoga.y, self.svet.zoga.x, self.svet.zoga.simbol, curses.A_BOLD | curses.A_STANDOUT | curses.color_pair(1))
			self._stdscr.refresh()
			time.sleep(0.01)
			can_move = self.svet.move(i=i)
			if not can_move:
				break

	def _end(self):
		curses.nocbreak()
		self._stdscr.keypad(False)
		curses.echo()
		curses.endwin()
