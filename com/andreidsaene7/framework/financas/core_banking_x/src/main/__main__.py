import sys
sys.path.append(r".")

from com.andreidsaene7.framework.src.main.python.common.core.reader.excel_file_reader import ExcelFileReader
from com.andreidsaene7.framework.src.main.python.common.core.saver.dataframe_saver import DataFrameSaver
from com.andreidsaene7.framework.src.main.python.common.core.sender.email_sender import OutlookEmailSender
from com.andreidsaene7.framework.src.main.python.common.core.dispatcher.report_dispatcher import Dispatcher

def main():
    # 1. Criar os leitores
    readers = [
        ExcelFileReader("dados/ficheiro1.xlsx"),
        ExcelFileReader("dados/ficheiro2.xlsx"),
        ExcelFileReader("dados/ficheiro3.xlsx"),
    ]

    # 2. Criar o salvador de DataFrames
    saver = DataFrameSaver(output_dir="resultados/")

    # 3. Criar o sender de e-mails
    sender = OutlookEmailSender()

    # 4. Criar o dispatcher
    dispatcher = Dispatcher(readers=readers, saver=saver, sender=sender)

    # 5. Executar
    dispatcher.execute()

if __name__ == "__main__":
    main()
