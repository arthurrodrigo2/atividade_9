'''
Crie um programa que exiba o nome do sistema operacional do usuário e informe os dados de todos os programas instalados na máquina. Ao terminar, envie para o GitHub e poste o link.
'''

import platform
import subprocess

# função para obter sistema operacional
def obter_sistema_operacional():
    return platform.system() + " " + platform.release()

# lista os programas instalados
def listar_programas_instalados():
    sistema = obter_sistema_operacional()
    
    if sistema.startswith("Windows"):
        # Para Windows
        return subprocess.check_output("wmic product get name", shell=True, text=True).splitlines()[1:]
    elif sistema.startswith("Linux"):
        # Para Linux
        return subprocess.check_output("dpkg --get-selections", shell=True, text=True).splitlines()
    elif sistema.startswith("Darwin"):
        # Para macOS
        return subprocess.check_output("ls /Applications", shell=True, text=True).splitlines()
    else:
        return ["Sistema operacional não suportado."]

# programa
def main():
    sistema = obter_sistema_operacional()
    print(f"Sistema Operacional: {sistema}\n")
    
    print("Programas Instalados:")
    programas = listar_programas_instalados()
    
    for programa in programas:
        print(programa.strip())

if __name__ == "__main__":
    main()
