      implicit double precision (a-h,o-z)
      dimension tp(10000),fp(10000),a(10000),nm(10000)
      dimension xf(10000),yt(10000)
      character * 16 c16
      character * 20 c20
c
      read(5,*)ttp,tfp
      nl = ttp+tfp
      key = 0
      atot = 0.0
      do i = 1,nl
c       read(5,*)c20,s1,s1,c16,s1,s1,s1,s1,tp(i),fp(i)
        read(5,*)c16,s1,s1,s1,s1,tp(i),fp(i)
         xf(i) = fp(i)/tfp
         yt(i) = tp(i)/ttp
      end do
c
      do i = 1,nl-1
        atot = atot + yt(i+1)*(xf(i+1)-xf(i))
c        write(6,100)nm(i),fp(i),tp(i),xf(i),yt(i),atot
      end do
c
      write(6,200)atot 
c
100   format(i5,8f8.4)
200   format(f8.3)
      stop
      end
