#! /bin/sh

for FILE in *.txt
do 
  sed -f sed1.sed $FILE > 1.tmp
  python2.7 tpfp.py 1.tmp > rock.tmp2
  cat rock.tmp1 rock.tmp2 > rock.tmp
  sed -f sed2.sed rock.tmp > 2.tmp
  mv 2.tmp rock.tmp
  echo $FILE
  ./areaR.x < rock.tmp
  rm *.tmp *.tmp2
done



