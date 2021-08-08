#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def GetContent():
	content = {
		"info": {
			"show_sources": """ Sources/Inspirations

			Source of most commans: https://wiki.archlinux.org/title/Pacman/Tips_and_tricks)
			Inspiration for wildcard implementation: https://bbs.archlinux.org/viewtopic.php?id=135649)
			"""
		},
		"commands": {
			# syntax: "ID",["Pkglistcommand","Command"]
			"upgrade": ["echo none","sudo pacman -Syu"],
			"install": ["pacman -Ssq | grep INPUT","sudo pacman -Sy PKGS --needed"],
			"force_install": ["pacman -Ssq | grep INPUT","sudo pacman -Sy PKGS"],
			"remove": ["pacman -Qq | grep INPUT","sudo pacman -Rsu"],
			"autoremove": ["pacman -Qtdq","sudo pacman -Rns PKGS"]
		}
	}
	content["info"]["show_commands"] = """
After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found.
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:

"""
	for k, v in content['commands'].items():
		cmd = str(v[1]).replace("PKGS", "$(" + v[1] + ")")
		content["info"]["show_commands"] += k + ": " + cmd + "\n"
	return content
