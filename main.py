#user Transaction blockchain
#user (privateK publicK name timeMade)
#Transaction (from to money time_Transaction)-->check
#blockchain
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import time
import numpy as np
class User():

    """docstring for User."""

    def __init__(self, name):
        self.id = None
        self.name = name
        self.__privateKey = None
        self.publicKey = None
        self.bornTime = None
        # self.noCoins = None

    def createKey(id):
        '''
        Generate an RSA keypair with an exponent of 65537 in PEM format
        param: bits The key length in bits
        Return private key and public key
        '''
        # from Crypto.PublicKey import RSA
        self.id = id
        self.bornTime = time.ctime()
        new_key = RSA.generate(2048, e=65537)
        self.publicKey = new_key.publickey().exportKey("PEM")
        self.__privateKey = new_key.exportKey("PEM")
        # return __privateKey, publicKey

    def signTransaction(hashData):
        key = self.__privateKey
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        sign = signer.sign(hashData)
        return b64encode(sign)

class  Transaction():
    """docstring for Transaction."""
    def __init__(self):
        self.id = id
        self.fromPublickey = None
        self.toPublickey = None
        self.tCoins = None
        self.tTime = None
        self.tValied = False
        self.tMessage = None
        self.tHash = None
        self.tSignature = None

    # def checkTransaction():
    #     # check if transaction is right #weather it is suffecant
    #     return (t f)

    def verify_sign(pub_key, signature, hashData):
        '''
        Verifies with a public key from whom the data came that it was indeed
        signed by their private key
        param: public_key_loc Path to public key
        param: signature String signature to be verified
        return: Boolean. True if the signature is valid; False otherwise.
        '''
        # pub_key = open(public_key_loc, "r").read()
        rsakey = RSA.importKey(pub_key)
        signer = PKCS1_v1_5.new(rsakey)
        # digest = SHA256.new()
        # # Assumes the data is base64 encoded to begin with
        # digest.update(b64decode(data))
        if signer.verify(hashData, b64decode(signature)):
            return True
        return False

    def coinTransaction(id,goofy,coins):
        # coin based transaction which is goofy creating coins
        userTransaction( id , goofy.publicKey, goofy.publicKey , coins ,goofy)

    def createHash(data):

        digest = SHA256.new()
        # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
        digest.update(b64decode(data))
        return digest

    def userTransaction( id , fromPublickey , toPublickey , coins ,fromObj):

        self.id = id
        self.fromPublickey = fromPublickey
        self.toPublickey = toPublickey
        self.tCoins = coins
        self.tTime = time.ctime() #use time.time() to use time in numbers
        self.tValied = True
        self.tMessage = fromPublickey + toPublickey + coin + self.tTime
        self.tHash = createHash(self.tMessage) # Assumes the data is base64 encoded to begin with
        self.tSignature = fromObj.signTransaction(self.tHash)

class Blockchain():

    """docstring for Blockchain."""

    def __init__(self, arg):
        self.arg = arg

    def condition():
        print "1 ==> coin based Transaction (add money to goofy)"
        print "2 ==> user Transaction (transfer money from one user to another)"
        print "3 ==> list of users "
        print "4 ==> list of Transaction"

    def getUser(userPublicKey ,allUsers):
        for user in allUsers:
            if user.publicKey == userPublicKey :
                return user

    def verifyTranaction(From , To, cost):
        # see if the transation is on his name (signature)
        # verify if he has money
        ballence_amount = 0
        for transaction in allTransactions:
            if(transation.toPublickey == From.publicKey ):
                if (transaction.verify_sign(transaction.fromPublickey , transaction.tSignature , transaction.tHash)):
                    if(transaction.tValied == True):
                        ballence_amount = transaction.tCoins
        if ballence_amount > cost :
            return True
        else:
            return False

    def main():

        condition()

        no_users = 0
        no_transaction = 0

        goofy = User("Goofy")
        goofy.createKey(no_users)
        no_users = no_users + 1

        allUsers = []
        allTransactions = []

        allUsers.append(goofy)



        while true:

            if raw_input() == "1" :
                # coin based Transaction (add money to goofy)
                t = Transaction()
                t.coinTransaction(no_transaction,goofy,coins)
                allTransactions.append(t)
                no_transaction = no_transaction + 1

            elif raw_input() == "2" :
                # user Transaction (transfer money from one user to another)
                FromId = int(raw_input("transver from"))
                ToId = int(raw_input("transver to"))
                coins = int(raw_input("coins to be transfered "))

                if verifyTranaction(allUsers[FromId] , allUsers[ToId], coins):
                    dept_to_pay = coins
                    for transaction in allTransactions:
                        if(transaction.tValied == True and transation.toPublickey == allUsers[FromId].publicKey):
                            if(transaction.tCoins <= dept_to_pay):
                                transaction.tValied = False
                                t = Transaction()
                                t.userTransaction( id , allUsers[FromId].publicKey,allUsers[ToId].publicKey , transaction.tCoins ,allUsers[FromId])
                                allTransactions.append(t)
                                no_transaction = no_transaction + 1
                                dept_to_pay = dept_to_pay - transaction.tCoins
                            else:
                                transaction.tValied = False
                                t1 = Transaction()
                                t1.userTransaction(no_transaction,allUsers[FromId].publicKey,allUsers[ToId].publicKey , dept_to_pay ,allUsers[FromId])
                                allTransactions.append(t1)
                                no_transaction = no_transaction + 1
                                t2 = Transaction()
                                remaning_balance = transaction.tCost-dept_to_pay
                                t2.userTransaction(no_transaction,allUsers[FromId].publicKey,allUsers[FromId].publicKey,remaning_balance,allUsers[FromId])
                                dept_to_pay = 0
                                allTransactions.append(t2)
                                no_transaction = no_transaction + 1

                    # t = Transaction()
                    # t.userTransaction( id , allUsers[FromId].publicKey,allUsers[ToId].publicKey , coins ,allUsers[FromId])


            elif raw_input() == "3" :
                # list of users
                for user in allUsers:
                    print "user id ==> "+ user.id +"user name ==>" + user.name

            elif raw_input() == "4" :
                # list of Transaction
                for transaction in allTransactions:
                    From = getUser(transaction.fromPublickey,allUsers)
                    To = getUser(transaction.toPublickey,allUsers)
                    print "Transaction was from "+From.name+" to "+To.name+"of worth"+transaction.tCoins

            elif raw_input() == "5":
                # add user
                name = raw_input("Name of the user")
                u = User(name)
                u.createKey(no_users)
                no_users = no_users + 1



if __name__== "__main__":

    B = Blockchain()
    B.main()
