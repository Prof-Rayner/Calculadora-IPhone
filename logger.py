import logging

class LogManagement:
    def __init__(self, nome):
        self.formato = logging.Formatter( '%(asctime)s | %(levelname)s | %(name)s : %(message)s', datefmt='%d/%m/%y %H:%M:%S' )
        self.logger = logging.getLogger(nome)
        self.logger.setLevel(logging.INFO)

        terminal = logging.StreamHandler()
        terminal.setFormatter(self.formato)
        self.logger.addHandler(terminal)

        arquivo = logging.FileHandler('Registros.log')
        arquivo.setLevel(logging.INFO)
        arquivo.setFormatter(self.formato)
        self.logger.addHandler(arquivo)



    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)

if __name__ == "__main__":
    mgmt = LogManagement(__file__)

    mgmt.info('Apenas um registro!')
    mgmt.warning('Cuidado pode gerar erro')
    mgmt.error('Aconteceu um erro Grave!')
    mgmt.critical('Falha Geral no Sistema!')