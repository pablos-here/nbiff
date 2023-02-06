#!/usr/bin/python3

#
# Copyright © 2023 Pablo Sanchez
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# The Software is provided "as is", without warranty of any kind,
# express or implied, including but not limited to the warranties of
# merchantability, fitness for a particular purpose and
# noninfringement. In no event shall the authors or copyright holders be
# liable for any claim, damages or other liability, whether in an action
# of contract, tort or otherwise, arising from, out of or in connection
# with the Software or the use or other dealings in the Software.
#

#
# We rely on the shell wrapper to handle parameter validation.
#
# Arg # Description
# ===== =============================================================================
#  1    Script/program which provides `unread message' count - see below
#  2    Debug flag (0 or greater than zero)
#  3    Image file: `0 unread messages' icon
#  4    Image file: `+1 unread messages' icon
#  5    Image file: `unexpected issue' icon (e.g. the count was not an integer)
#  6    Image file: MUA is not running
#  7    Script/program mouse-click handler for the MUA
#  8    Flag to swap mouse-click mapping
#
# Processing
# ==========
# This program processes the output of the script/program specified.
#
# Intentionally, we keep it simple.  Per line, we substring search the following
# strings and act accordingly:
#
#    MUA is down
#    MUA is up
#    Unread count = N
#
#       Note:  We expect, but do not fail, if N is not provided or not an integer.
#
# All other strings are ignored.
#
# Mouse-clicks
# ============
# o No DE handles mouse-clicks the same.  Of course.  :[
# o Generally then:
#   + click:        Swap desktops between the current and main Thunderbird
#                   desktop.  If needed, de-iconify all Thunderbird windows.
#
#   + middle-click: o If not on the main Thunderbird desktop, switch to it and
#                     de-iconify all Thunderbird windows.  If `click`, return
#                     to the desktop.
#                   o If on the main Thunderbird desktop, iconify/activate.
#
# Mouse-handler
# =============
# Exit status | Description               | Return string
# ------------+---------------------------+--------------
#     0       | On main, iconify/activate | // ignore //
#    10       | Not on main, activate     | The non-Main desktop number
#    11       | Swap                      | Either the non-Main desktop number
#             |                           | or '' (when returning from Main)
#

#
# Cobbled together from several posts with a wee bit of special sauce tossed in
#
# Some of the core pages:
#
# o https://stackoverflow.com/questions/56307711/why-icon-of-qsystemtrayicon-not-hide-in-my-system
# o https://www.mfitzp.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/
# o https://stackoverflow.com/questions/42814093/how-to-handle-ctrlc-in-python-app-with-pyqt
# o https://stackoverflow.com/questions/16670125/python-format-string-thousand-separator-with-spaces
#

from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess, QTimer
import sys, signal, locale, os.path, psutil, subprocess

#
# Find the starting index of `sl' within `l'
#
# https://stackoverflow.com/questions/17870544/find-starting-and-ending-indices-of-sublist-in-list
#
def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind,ind+sll-1

#
# Qprocess() doesn't kill the children of the process it kills.  We use this code to kill the children.
#
# Note:  we rely on the script/program to handle its own cleanup.
#
# https://stackoverflow.com/questions/22291434/pyqt-application-closes-successfully-but-process-is-not-killed/22305331
#
def kill_proc_tree(pid, including_parent=False):
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    if including_parent:
        parent.kill()

#
# At some point, we'll want to set up proper debugging (e.g. accept a flag)
# This is the start.
#
def print_debug(s):
    if debug == 1:
        print(s, flush=True)

class MainWindow():

    def __init__(self):
        super().__init__()

        self.p = None
        # If we're on the way to gonner-ville, flip the switch
        self.in_quit_cleanup = 0
        self.unread_msgs_count = 0
        self.unread_msgs_is_int = 1
        self.MUA_state = 'Down'
        self.tooltip_msg = 'Unread messages count is '
        self.tooltip_error_msg_not_int = 'Non-integer received:  '
        self.process_name = os.path.basename(sys.argv[1])

        self.tooltip_error_msg_process_died = "'" + self.process_name + "' stopped running"
        self.tooltip_error_msg_MUA_is_down = 'The mail client is not running'

        # The strings we can process
        self.unread_count = 'Unread count ='
        self.MUA_is_down = 'MUA is down'
        self.MUA_is_up = 'MUA is up'

        self.menu = None
        self.process_state = None

        # Create the icon menus
        self.gen_menu()

        self.icon_read         = sys.argv[3]
        self.icon_unread       = sys.argv[4]
        self.icon_error        = sys.argv[5]
        self.icon_MUA_is_down  = sys.argv[6]
        self.MUA_affect_window = sys.argv[7]
        self.swap_mouse_action = sys.argv[8]
        self.icon = QIcon(self.icon_read)

        # Creating tray
        self.trayIcon = QSystemTrayIcon(self.icon, app)
        self.trayIcon.setContextMenu(self.menu)

        # Initialize the tool tip, show the icon and ready it for mouse events
        self.trayIcon.setToolTip(self.tooltip_msg + str(self.unread_msgs_count))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.mouse_click)

        # Either 'iconify' or not ('activate')
        self.MUA_window_iconify  = 'iconify'
        self.MUA_window_activate = 'activate'
        self.MUA_window_swap     = 'swap'
        self.last_desktop        = ''
        self.MUA_window_now = self.MUA_window_activate

        # Number formatting
        locale.setlocale(locale.LC_ALL, '')
        locale._override_localeconv["mon_thousands_sep"] = ","

        # Start the `new_msgs' process
        self.start_process()

        # These signals match with the parent scripts
        signal.signal(signal.SIGHUP, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGQUIT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    #
    # If any mouse click is caught, we'll iconify/activate the MUA
    # window(s).
    #
    def mouse_click(self, reason):
        print_debug('> mouse_click()')
        if reason == QSystemTrayIcon.Trigger:
            print_debug('> mouse_click() > Trigger')
        elif reason == QSystemTrayIcon.DoubleClick:
            print_debug('> mouse_click() > Double-click')
        elif reason == QSystemTrayIcon.MiddleClick:
            print_debug('> mouse_click() > Middle-click')
        elif reason == QSystemTrayIcon.Context:
            print_debug('> mouse_click() > Context')
        elif reason == QSystemTrayIcon.Unknown:
            print_debug('> mouse_click() > Unknown')

        # Process the type of mouse-click
        if self.swap_mouse_action == '0': # default mouse actions
            if reason != QSystemTrayIcon.MiddleClick and reason != QSystemTrayIcon.DoubleClick:
                self.MUA_window_now = self.MUA_window_swap
            elif self.MUA_window_now == self.MUA_window_iconify:
                self.MUA_window_now = self.MUA_window_activate
            else:
                self.MUA_window_now = self.MUA_window_iconify
        else:                            # flipped the mouse actions
            if reason == QSystemTrayIcon.MiddleClick or reason == QSystemTrayIcon.DoubleClick:
                self.MUA_window_now = self.MUA_window_swap
            elif self.MUA_window_now == self.MUA_window_iconify:
                self.MUA_window_now = self.MUA_window_activate
            else:
                self.MUA_window_now = self.MUA_window_iconify

        run_status = subprocess.run([self.MUA_affect_window, self.MUA_window_now, self.last_desktop], capture_output=True)
        if run_status.stdout is None:
            run_stdout = ''
        else:
            run_stdout = bytes(run_status.stdout).decode('utf8')
            run_stdout = run_stdout.rstrip()

        print_debug('> mouse_click() > ' + self.MUA_window_now + '; Exit status = ' + str(run_status.returncode) +
                    '; Return to desktop ' + (run_stdout if run_stdout != '' else 'main' ))

        if run_status.returncode == 10:   # We were on a different Desktop as main:  we activated
            print_debug('> mouse_click() > flipped to the main Desktop, staying activated; can return to ' +
                        (run_stdout if run_stdout != '' else 'main' ))
            self.MUA_window_now = self.MUA_window_activate
            self.last_desktop = run_stdout
        elif run_status.returncode == 11: # `swap' desktop
            self.last_desktop = run_stdout
            print_debug('> mouse_click() > will return to ' + (run_stdout if run_stdout != '' else 'main' ) )
        elif run_status.returncode == 1:  # Ooops
            print_debug('> mouse_click() > exit status 1 - ' + run_stdout)

    #
    # For some DEs, there is no tool tip.  We set up a NULL menu entry to also provide the tool tip
    # details.  ;)
    #
    def gen_menu(self):
        print_debug('> gen_menu()')
        if self.menu is None:
            self.menu = QMenu()
        else:
            self.menu.clear()

        if self.process_state == 'Not running':
            self.unreadAction = self.menu.addAction(self.tooltip_error_msg_process_died)
        elif self.MUA_state == 'Down':
            self.unreadAction = self.menu.addAction(self.tooltip_error_msg_MUA_is_down)
        elif self.unread_msgs_is_int == 1:
            self.unreadAction = self.menu.addAction(self.tooltip_msg +
                                                    str(locale.format_string('%d', self.unread_msgs_count, grouping=True, monetary=True)))
        else:
            self.unreadAction = self.menu.addAction(self.tooltip_error_msg_not_int + str(self.unread_msgs_count))

        self.separator = self.menu.addSeparator()
        self.quitAction = self.menu.addAction("Quit")
        self.quitAction.triggered.connect(self.quit_cleanup)

    def start_process(self):
        print_debug('> start_process()')
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished) # Clean up once complete.
            self.p.start(sys.argv[1])
            self.p.waitForStarted(5000)

    def handle_stderr(self):
        print_debug('> handle_stderr()')
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode('utf8')

    #
    # This is where we process the output of the script/program - see our tombstone for details.
    #
    def handle_stdout(self):
        print_debug('> handle_stdout()')
        if self.p is None:  # we're probably in the process of dying ...
            return
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode('utf8')
        print_debug('>> ' + stdout.rstrip())
        if self.MUA_is_down in stdout:      # Flip to our down state and set all corresponding user alerts
            self.trayIcon.setIcon(QIcon(self.icon_MUA_is_down))
            self.trayIcon.setToolTip(self.tooltip_error_msg_MUA_is_down)
            self.MUA_state = "Down"
            self.gen_menu()
            return
        if self.MUA_is_up in stdout:        # We don't action on this state, ignore it
            self.MUA_state = "Up"
            return
        if not self.unread_count in stdout: # No unread count in the line, ignore it
            return

        # Return the list, [start_of_magic_cookie, end_of_magic_cookie]
        stdout_list = stdout.split() + ['no value']  # The split() also puts a newline in its own cell
        unread_msgs_count_index = find_sub_list(self.unread_count.split(), stdout_list)

        # The next cell after the `magic_cookie' in `stdout_list' is our `Unread count'
        self.unread_msgs_count = stdout_list[unread_msgs_count_index[1] + 1]

        # Ensure it's an integer
        try:
            self.unread_msgs_is_int = 1
            self.unread_msgs_count = int(self.unread_msgs_count)

        except ValueError:
            self.unread_msgs_is_int = 0
            pass

        # Process N - systray icon, menu text and tool tip
        if self.unread_msgs_is_int == 1:
            if self.unread_msgs_count > 0:
                self.trayIcon.setIcon(QIcon(self.icon_unread))
            else:
                self.trayIcon.setIcon(QIcon(self.icon_read))
            self.trayIcon.setToolTip(self.tooltip_msg +
                                     str(locale.format_string('%d', self.unread_msgs_count, grouping=True, monetary=True)))
        else:
            self.trayIcon.setIcon(QIcon(self.icon_error))
            self.trayIcon.setToolTip(self.tooltip_error_msg_not_int + str(self.unread_msgs_count))

        self.gen_menu()

    def handle_state(self, state):
        print_debug('> handle_state()')
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting:   'Starting',
            QProcess.Running:    'Running',
        }
        self.process_state = states[state]
        print_debug('state changed to ' + self.process_state)
        if self.in_quit_cleanup == 0 and self.process_state == 'Not running': # if we didn't intend to die ...
            self.trayIcon.setIcon(QIcon(self.icon_error))
            self.trayIcon.setToolTip(self.tooltip_error_msg_process_died)
            self.gen_menu()

    def process_finished(self):
        print_debug('> process_finished()')
        self.p = None

    def quit_cleanup(self):
        print_debug('> quit_cleanup()')
        if self.p is not None:
            self.in_quit_cleanup = 1
            self.p.terminate()
            kill_proc_tree(self.p.pid())
            self.p.waitForFinished(4000) # give it 10s to end.  Our pollihg is 1s so that's more than adequate.

            if self.p is not None:
                self.p.kill() # nail the sucker
                self.p.waitForFinished(2000)
        app.quit()

    def signal_handler(self, signum, frame):
        print_debug('> signal_handler()')
        MainWindow.quit_cleanup(self)

debug = int(sys.argv[2])
app = QApplication(sys.argv)

# Let the python interpreter run to catch signals
timer = QTimer()
timer.start(500) # Set the timer to 500ms ...
timer.timeout.connect(lambda: None)

w = MainWindow()
app.exec_()
