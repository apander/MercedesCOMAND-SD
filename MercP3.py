import os
import sys
import eyed3
import re
import shutil
from operator import itemgetter

'''
Script to create a playlist file for the Comand system to oraganise
and play tracks from a memory card

FILE FORMAT EXAMPLE
 [playlist]
   File1=\Beastie Boys\Ill Communication\01 Sure Shot.mp3
   Title1=Beastie Boys - Sure Shot
   Length1=199
   File2=\Beastie Boys\Ill Communication\02 Tough Guy.mp3
   Title2=Beastie Boys - Tough Guy
   Length2=199
   NumberOfEntries=2
   Version=2

FLOW
- Get the target directory
- Read the files and metadata
- Build the file data in a list
- Write the file
- Copy PLS and files to memory stick
- Do a Chewbacca

'''

def order_album(tracklist):
   return sorted(tracklist, key=itemgetter('seq'))

def load_album(src_dir, dest_dir, tracklist):
   for (dirpath, dirnames, filenames) in os.walk(src_dir):
      for files in filenames:
         if files.endswith('mp3'):
            mp3file = eyed3.load(dirpath + "\\" + files)
            track={"artist": mp3file.tag.artist
                   ,"title": mp3file.tag.title
                   ,"seq": mp3file.tag.track_num[0]
                   ,"path": "\\" + dest_dir + "\\" + files}
            tracklist.append(track)
   return tracklist

def write_playlist(tracklist, drive_letter, pls_name):
   file_pls = open(drive_letter + pls_name,'w')
   file_pls.write("playlist\n")
   pls_cnt=0

   for t in tracklist:
      pls_cnt+=1
      file_pls.write("File" + str(pls_cnt) + "=" + t['path'] + "\n")
      file_pls.write("Title" + str(pls_cnt) + "=" + t['title'] + " - " + t['artist'] + "\n")
      file_pls.write("Length" + str(pls_cnt) + "=" + "\n")
      
   file_pls.write("NumberOfEntries=" + str(pls_cnt) + "\n")
   file_pls.write("Version=2" + "\n")
   file_pls.close()

def copy_tracks(src_dir, drive_letter, dest_dir):
   try:
      shutil.copytree(src_dir, drive_letter + dest_dir)
   except OSError as exc: # python >2.5
      shutil.rmtree(drive_letter + dest_dir)
      shutil.copytree(src_dir, drive_letter + "\\" + dest_dir)

def main(drive, dirs):
   drive=drive + ":\\"
   for d in dirs:
      tracklist=[]
      pls_name=str(d).rsplit('\\', 1)[1] + ".pls"
      dest_dir=str(d).rsplit('\\', 1)[1]
      load_album(d, dest_dir, tracklist)
      tracklist=order_album(tracklist)
      write_playlist(tracklist, drive, pls_name)
      copy_tracks(d, drive, dest_dir)


if __name__ == '__main__':
   main(sys.argv[1], sys.argv[2:])

