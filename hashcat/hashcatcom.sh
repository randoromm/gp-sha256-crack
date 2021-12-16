#! /bin/bash
hashcat -a 3 -m 1400 -1 diglet.hcchr -2 ot.hcchr -3 zon.hcchr -4 em.hcchr sha.hash '?1?1?1?1 N59 20.?d?d?d E024 4?4.?d?d?d' -O --force
