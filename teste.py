import argparse

argumentos = argparse.ArgumentParser()

argumentos.add_argument("-n", "--nome", required=True)
argumentos.add_argument("-i", "--idade", required=True)

args = vars(argumentos.parse_args())

print(f'Nome {args["nome"]}')
print(f'Idade {args["idade"]}')
