gcc -o exploit exploit.c -static -lpthread
rm -rf ./initramfs && mkdir ./initramfs
cd ./initramfs
cp ../initramfs.cpio.gz ./
gzip -d initramfs.cpio.gz
cpio -i -F initramfs.cpio
rm initramfs.cpio
cp ../exploit ./home/spark/
find . | cpio -H newc -o > ../initramfs.cpio
cd ../
rm -rf initramfs.cpio.gz
gzip initramfs.cpio
