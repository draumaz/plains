# Automated non-Linux patchfile creation
# Execute in project root.

PATCH_PATH="./patches/non_linux.patch"
MAKEFILE_PROTECT="Makefile-ref"
MAKEFILE_NORMAL="Makefile"

cp -fv $MAKEFILE_NORMAL $MAKEFILE_PROTECT
rm -fv $PATCH_PATH | sed 's/removed/removed existing/g'
sed -i 's/-pv/-p/g' $MAKEFILE_NORMAL; echo "replacing -pv -> -p"
sed -i 's/-ltinfo//g' $MAKEFILE_NORMAL; echo "removing -ltinfo"
diff $MAKEFILE_PROTECT $MAKEFILE_NORMAL > $PATCH_PATH; echo "created patchfile -> '$PATCH_PATH'"
rm -vf $MAKEFILE_NORMAL
mv -vf $MAKEFILE_PROTECT $MAKEFILE_NORMAL
