#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def GetContent():
    content = {
        "info": {
            "show-sources": """ Sources/Inspirations

            Source of most commans: https://wiki.archlinux.org/title/Pacman/Tips_and_tricks)
            Inspiration for wildcard implementation: https://bbs.archlinux.org/viewtopic.php?id=135649)"""
        },
        "commands": {
            # syntax: "ID":"Command"
            "install": "sudo pacman -Sy $(pacman -Ssq | grep INPUT)",
            "autoremove": "sudo pacman -Rns $(pacman -Qtdq)",
            "remove": "sudo pacman -Rsu $(pacman -Qq | grep INPUT)"
        }
    }
    content["info"]["show-commands"] = """After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found.
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:

"""
    for k, v in content['commands'].items():
        content["info"]["show-commands"] += k + ": " + v + "\n"
    return content
