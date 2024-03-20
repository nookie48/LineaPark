from src.networks import linea_net
from src.logger import cs_logger
from src.Helpers.txnHelper import get_txn_dict
from src.Quests.questHelper import Quest


class OmniZone(Quest):
    title = 'Минтим OmniZone'

    def build_txn(self, wallet):
        try:
            txn = get_txn_dict(wallet.address, linea_net)
            txn['to'] = linea_net.web3.to_checksum_address('0x7136Abb0fa3d88E4B4D4eE58FC1dfb8506bb7De7')
            txn['data'] = '0x1249c58b'
            return txn
        except Exception as ex:
            cs_logger.info(f'Ошибка в (OmniZone/mint: build_txn) {ex.args}')


omni_zone = OmniZone()
