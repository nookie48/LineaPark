from src.POH.Trusta.attestA import attest_a
from src.POH.Trusta.attestB import attest_b
from src.POH.Ruby.attest import attest_ruby
import settings
from random import shuffle
from src.Helpers.gasPriceChecker import check_limit


def proof_op(wallet):
    if settings.poh_enable == 1:
        proof_list = list()

        if settings.trusta_a_switch == 1:
            proof_list.append('trustaA')
            shuffle(proof_list)

        if settings.trusta_a_switch == 1:
            proof_list.append('trustaB')
            shuffle(proof_list)

        if settings.ruby_switch == 1:
            proof_list.append('ruby')
            shuffle(proof_list)

        for attest in proof_list:
            if attest == 'trustaA':
                check_limit()
                attest_a(wallet)

            if attest == 'trustaB':
                check_limit()
                attest_b(wallet)

            if attest == 'ruby':
                check_limit()
                attest_ruby(wallet)
