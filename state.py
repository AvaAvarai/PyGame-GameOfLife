#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: Alice 'Ava' Williams
Date: July 29, 2021
File: State.py
Desc: State enum class.
"""

import enum

#Cellular Automata state, not important for ALIVE/DEAD dual state model
#but more complex automata require more possible states.
class State(enum.IntEnum):
    DEAD = 0
    ALIVE = 1
