import os
import click

from automato.npdaAutomato import npdaAutomato


@click.command()
@click.option(
    '--path',
    '-p',
    help='Caminho para o arquivo de execução.',
    required=True
)
def main(path):
    if not os.path.isfile(path):
        print('O caminho {} não existe'.format(path))
        return

    file = open(path, "r")

    try:
        if npdaAutomato.accepts_input(file.read()):
            print('Aceito')
        else:
            print('Rejeitado')
    except:
        print('Não foi possível verificar se a gramática é aceita...')

    file.close()


if __name__ == "__main__":
    main()
