import sys
sys.path.append(r".")

# dispatcher.py
from com.andreidsaene7.framework.src.main.python.interface.i_reader.i_file_reader import IFileReader
from com.andreidsaene7.framework.src.main.python.interface.i_saver.i_dataframe_saver import IDataFrameSaver
from com.andreidsaene7.framework.src.main.python.common.core.builder.email_builder import EmailBuilder
from com.andreidsaene7.framework.src.main.python.common.core.sender.email_sender import OutlookEmailSender
from com.andreidsaene7.framework.src.main.python.interface.i_dispatcher.i_report_dispatcher import IDispatcher

class Dispatcher(IDispatcher):
    def __init__(self, readers: list[IFileReader], saver: IDataFrameSaver, sender: OutlookEmailSender):
        self.readers = readers
        self.saver = saver
        self.sender = sender

    def execute(self):
        attachments = []
        for reader in self.readers:
            df, filename = reader.read()
            self.saver.save(df, filename)
            attachments.append(filename)

        email = (
            EmailBuilder()
            .with_subject("Relatório de Ficheiros")
            .with_body("Segue os ficheiros gerados em anexo.")
            .with_to(["andre@empresa.co.mz"])
            .with_cc(["gestor@empresa.co.mz"])
            .with_attachments(attachments)
            .build()
        )

        self.sender.send(email)
