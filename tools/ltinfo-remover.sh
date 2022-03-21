echo "moving up one directory" && cd ..
echo "creating temporary compliant Makefile" && sed 's/-ltinfo//g' Makefile | sed 's/-pv/-p/g' > Makefile.tmp
echo "making patchfile" && diff Makefile Makefile.tmp > patches/no_ltinfo.patch
echo "remove compliant Makefile" && rm Makefile.tmp
