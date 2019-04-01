#!/bin/sh

echo "Escriba el path del directorio a modificar"
read path
cd ${path}
list="$(ls ${path})"

for arch in *
do 
    nombreActual=$arch
    eval mv \'${nombreActual}\' \'${nombreActual^^}\'    
    
done


