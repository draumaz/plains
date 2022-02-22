# Automated non-Linux patchfile creation
# Execute in project root.

cp -fv Makefile Makefile-ref
sed -i 's/-pv/-p/g' Makefile; echo "replacing -pv -> -p"
sed -i 's/-ltinfo//g' Makefile; echo "removing -ltinfo"
diff Makefile-ref Makefile > patches/non_linux.patch; echo "created patchfile"
rm -vf Makefile
mv -vf Makefile-ref Makefile
