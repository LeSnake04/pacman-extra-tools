from log import log
from argparse import ArgumentParser
from showinfo import ShowInfo

def main():
   
   parser = ArgumentParser(description='Simple, yet powerfull pacman wrapper')
   parser.add_argument('-v','--verbose', action='store_true', help='Enable verbose output')

   general = parser.add_argument_group('genaral','General Package Management')
   general.add_argument('-i','--install', help='Install programms', nargs='+', type=list)
   general.add_argument('-a','--autoremove', action='store_true', help='Remove unsed programms')

   info = parser.add_argument_group('info', 'informations about the Program')
   info.add_argument('--show-commands', action='store_true', help="Show commands used by the program")
   
   args=parser.parse_args()
   parser.print_help()
   #l=log(args.verbose.test, 'MAIN')
   print(args)
   if args.autoremove:
      print('autoremove')

   print(args.__dict__)
   testlist=[1,2,3]
   #for i in testlist:
      #print(args."testlist[i]")

   
if __name__ == "__main__":
   exit(main())