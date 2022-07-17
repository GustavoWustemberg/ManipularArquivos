import os
import shutil

opcao = 0

while opcao < 6:
    opcao = int(input('Escolha uma das opções abaixo\n'
                      '1 - Renomear arquivos\n'
                      '2 - Mover arquivos\n'
                      '3 - Copiar arquivos\n'
                      '4 - Deletar arquivos\n'
                      '5 - Criar nova pasta\n'
                      '6 - Sair\n'))
    if(opcao == 1):
        folder = input('Selecione a pasta onde será alterados os arquivos: ')
        folderLink = r'{}\\'.format(folder)
        name = input('Digite o novo nome do arquivo: ')
        tipo = input('Digite o tipo do arquivo: ')
        contador = 0
        numaux = ''
        numinicial = int(input('Digite o valor inicial a ser acrescentado ao nome: '))

        for file_name in os.listdir(folderLink):
            if (numinicial == 1):
                contador += 1
            else:
                contador = numinicial
                numinicial += 1
            if (contador < 10):
                numaux = 0
            else:
                numaux = ''
            old_name = folderLink + file_name
            new_name = folderLink + f'{name}-{numaux}{contador}.{tipo}'
            os.rename(old_name, new_name)

        print(os.listdir(folderLink))

    elif(opcao == 2):
        caminho_1 = input('Informe o caminho da pasta onde estão os arquivos: ')
        destino_inicial = r'{}//'.format(caminho_1)
        caminho_2 = input('Informe o caminho da pasta onde serão movidos os arquivos: ')
        destino_novo = r'{}//'.format(caminho_2)

        for root, dirs, files in os.walk(destino_inicial):
            for file in files:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(destino_novo, file)

                # mover arquivos
                shutil.move(old_file_path, new_file_path)
                print(f'Arquivos movidos com sucesso.')

    elif(opcao == 3):
        caminho_1 = input('Informe o caminho da pasta onde estão os arquivos: ')
        destino_inicial = r'{}//'.format(caminho_1)
        caminho_2 = input('Informe o caminho da pasta onde serão copiados os arquivos: ')
        destino_novo = r'{}//'.format(caminho_2)

        for root, dirs, files in os.walk(destino_inicial):
            for file in files:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(destino_novo, file)

                # copiar arquivos
                shutil.copy(old_file_path, new_file_path)
                print(f'Arquivo {file} copiado com sucesso.')
                print(f'Arquivos copiados com sucesso.')

    elif(opcao == 4):
        recebe_pasta = input('Informe o caminho da pasta onde estão os arquivos: ')
        caminho_pasta = r'{}//'.format(recebe_pasta)

        for root, dirs, files in os.walk(caminho_pasta):
            for file in files:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(caminho_pasta, file)
                #apagar arquivos
                os.remove(new_file_path)
                print(f'Arquivos deletados com sucesso.')

    if(opcao == 5):
        caminho = input('Informe o caminho a pasta será criada: ')
        nome_pasta = input('Informe o nome que deseja dar pasta: ')
        nova_pasta = r'{}/{}'.format(caminho, nome_pasta)
        try:
            os.mkdir(nova_pasta)
            print('Pasta criada com sucesso.')
        except FileExistsError as e:
            print(f'Pasta {nome_pasta} já existe.')
