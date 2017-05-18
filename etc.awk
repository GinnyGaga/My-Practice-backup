#!/usr/bin/awk -f
BEGIN {FS=":";
       if(ARGC>2) {
                   user=ARGV[1];
                   delete ARGC[1]}
         print NR,$1,$6
}
