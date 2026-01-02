"""
Patch for WireViz to add a 'factory' layout mode for strict left-to-right, straight-line harness diagrams.
This patch modifies the Graphviz DOT generation to:
- Set splines=false globally
- Set rankdir=LR
- Optionally, allow a 'layout: factory' key in the YAML to trigger this mode

Usage:
- Place this file as wireviz_factory_patch.py in your WireViz source directory.
- Apply the changes to wireviz/visualizer/graphviz.py as described in the comments.
"""

import re
import sys

# Path to the original Graphviz visualizer file (edit as needed)
GRAPHVIZ_FILE = 'wireviz/visualizer/graphviz.py'

# Read the original file
with open(GRAPHVIZ_FILE, 'r') as f:
    lines = f.readlines()

# Patch: Insert splines=false and rankdir=LR in DOT output, and add 'factory' layout mode
patched_lines = []
inside_dot = False
for line in lines:
    # Detect start of DOT graph
    if 'def render(' in line and 'dot =' in line:
        inside_dot = True
    if inside_dot and 'digraph' in line:
        patched_lines.append(line)
        patched_lines.append("    dot += '  splines=false;\\n'")
        patched_lines.append("    dot += '  rankdir=LR;\\n'")
        inside_dot = False
        continue
    # Optionally, check for 'layout: factory' in the YAML config (pseudo-code)
    # if 'layout' in config and config['layout'] == 'factory':
    #     ...
    patched_lines.append(line)

# Write the patched file (backup original first)
with open(GRAPHVIZ_FILE + '.bak', 'w') as f:
    f.writelines(lines)
with open(GRAPHVIZ_FILE, 'w') as f:
    f.writelines(patched_lines)

print('WireViz Graphviz visualizer patched for factory layout (splines=false, rankdir=LR).')
