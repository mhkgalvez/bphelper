# -*- coding: utf-8 -*-
import os
import sys
import json
import uuid
import datetime
import bible


# Main
if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            sys.exit('Argumentos insuficientes na linha de comando.')
        option = sys.argv[1]
        if option == '-today':
            bible.get_curr_reading()
        elif option == '-day':
            if len(sys.argv) >= 3:
                datestr = sys.argv[2]
                date = None
                try:
                    date = datetime.datetime.strptime(datestr,'%d/%m/%y')
                except Exception as detail:
                    print("Erro na linha de comando. Data não segue o formato padrão dd/mm/yy.")
                date
            else:
                print("Erro na linha de comando. Você deve informar a data após a opção '-day'.")
    except Exception as detail:
        sys.exit('Ocorreu um erro ao executar o programa. Detalhe: ' + str(detail))