#include <cstdlib>
#include <iostream>
#include <dirent.h>
#include <string>
#include <cctype>

using namespace std;

void cambiarStringMayusculas(string s);

int main(int argc, char *argv[])
{
    
    DIR *dir;
    dirent *ent;
    
    // pedir path de directior a modificar
    string path;
    cout << "Escriba el path del directorio a modifcar" <<endl;
    cin >> path;
    
    // verifica path del directorio
    if(DIR* dir = opendir(path.c_str()))
    {             
        // recorre cada elelmtno del directorio
        while (dirent* ent = readdir(dir) ){
              
              // verifica si un elento del directorio es un . o .., y estos no lo tienen en cuenta     
              if(!(strcmp(ent->d_name, "..") == 0 || strcmp(ent->d_name, ".") == 0)){
                    
                    // nombre del archivo o carpeta
                    string archivo = ent->d_name;
                    
                    //path del directorio mas el nombre del archivo o carpeta
                    string pathArchivo = path+"/"+archivo;
                                        
                    cout << archivo << "a ";
                    
                    // cambio de mayusculas a minusculas
                    cambiarStringMayusculas(archivo); 
                    
                    archivo = " R_"+archivo;
                    
                    //path del directorio mas el nombre del archivo renobrado o carpeta
                    string nuevoPathArchivo = path+"/"+archivo;
                    
                    cout << archivo;
                    // verificacion de renombre de carpeta o archivo
                    if(rename(pathArchivo.c_str(),nuevoPathArchivo.c_str())==0)
                    {
                     cout << " (renombrado)" << endl;                                                                                                                                                  
                    }
                    else
                    {   
                       cout << " (no renombrado)" << endl;  
                    }                  
                    
                    // /home/alvaruto/Documentos/UNIVERSIDAD/CURSOS/2019/BashLinux/carpeta
                }           
            
                                    
        }
        closedir (dir);   
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}

// funcion de pasar texto a mayusculas
void cambiarStringMayusculas(string s){
       for(int i=0;i<s.size();i++){
               s[i] = toupper(s[i]);       
       }    
}
