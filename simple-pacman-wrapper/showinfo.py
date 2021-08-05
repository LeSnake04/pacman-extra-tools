class ShowInfo:
   def commands():
      print("""
After having to search for many pacman hidden functions myself, i decided to help others by giving them by giving them an easy way to use the functions i found. :)
If you dont trust my program want to use the functions directly instead, you more are welcome to copy the lines from here:

Autoremove:
sudo pacman -Rns $(pacman -Qtdq)

Install:
sudo pacman -Sy $(pacman -Ssq | grep SEARCH_TERM )

Remove:
sudo pacman -Rsu $(pacman -Qq | grep SEARCH_TERM )"
      """)
   
   def sources():    
      print("""
Sources/Inspirations:

Most of the commands: https://wiki.archlinux.org/title/Pacman/Tips_and_tricks

wildcard: (https://bbs.archlinux.org/viewtopic.php?id=135649)
      """)
   def wildcard():   
      print("""
         Wildcard
      """)
