#!/usr/bin/env python3
# vim:ts=4:sw=4:expandtab
import sys
import tkinter as tk

# Based on i3-sticky:
# MIT License, Copyright (c) 2016 Ingo Bürk

"""
Opens a placeholder window for a sticky group.

This utility opens a mostly empty window to be used as a placeholder container
with i3-sticky. It takes an optional argument describing the group for which
the container should be, defaulting to '1'. i3-sticky will pick up on this
window and automatically mark it as a placeholder container for the
corresponding group.

(C) 2016 Ingo Bürk
Licensed under The MIT License (https://opensource.org/licenses/MIT), see LICENSE.
"""

def create_text_widget(root, label):
    widget = tk.Text(root, height = 1, borderwidth = 0, highlightthickness = 0)
    widget.place(relx = .5, rely = .5, anchor = 'c')

    widget.tag_configure('tag-center', justify = 'center')
    widget.insert('end', label, 'tag-center')

if __name__ == '__main__':
    group = "1"
    if len(sys.argv) > 1:
        group = sys.argv[1]

    win = tk.Tk(className="I3-sticky-%s" % group)
    create_text_widget(win, 'Sticky Placeholder – Group %s' % group)
    win.mainloop()
