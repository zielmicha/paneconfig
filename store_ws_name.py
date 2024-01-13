#!/usr/bin/env python3
import i3ipc
import json
import re, os
import pane_tools

path = os.path.expanduser('~/var/paneconfig/current_workspace')

def on_workspace_change(i3, event):
    for ws in i3.get_workspaces():
        if ws.focused:
            pane_tools.write_file(path, ws.name + '\n')
        
if __name__ == '__main__':
    i3 = i3ipc.Connection()
    i3.on('workspace::focus', on_workspace_change)

    i3.main()

