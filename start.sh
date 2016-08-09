while true
do

cd src && make -j3 -f makefile.osx
cd .. && src/fibocoind -debug=1 -printtoconsole -server -regtest

done
