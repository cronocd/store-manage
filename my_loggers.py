import logging as log

log.basicConfig(level=log.DEBUG, format= '%(asctime)s - %(levelname)s - [%(filename)s : %(lineno)s] - %(message)s',
                datefmt= '%H:%M:%S',
                handlers = [
                    log.FileHandler('stats.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('It\'s debug')
    log.info('It\'s info')
    log.warning('It\'s warning')
    log.error('It\'s error')
    log.critical('It\'s critical')