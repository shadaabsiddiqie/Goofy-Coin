from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import time
class User():

    """docstring for User."""

    def __init__(self, name):
        self.id = None
        self.name = name
        self.__privateKey = None
        self.publicKey = None
        self.bornTime = None
        # self.noCoins = None

    def createKey(self,id):
        self.id = id
        self.bornTime = time.ctime()
        new_key = RSA.generate(2048, e=65537)
        self.publicKey = new_key.publickey().exportKey("PEM")
        self.__privateKey = new_key.exportKey("PEM")
        # return __privateKey, publicKey

    def signTransaction(self,hashData):
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
        self.tValied = True
        self.tMessage = None
        self.tHash = None
        self.tSignature = None

    # def checkTransaction():
    #     # check if transaction is right #weather it is suffecant
    #     return (t f)

    def verify_sign(self,pub_key, signature, hashData):
        '''
        Verifies with a public key from whom the data came that it was indeed
        signed by their private key
        param: public_key_loc Path to public key
        param: signature String signature to be verified
        return: Boolean. True if the signature is valid; False otherwise.
        '''
        # pub_key = open(public_key_loc, "r").read()
        rsakey = RSA.importKey(self.fromPublickey)
        signer = PKCS1_v1_5.new(rsakey)
        # digest = SHA256.new()
        # # Assumes the data is base64 encoded to begin with
        # digest.update(b64decode(data))
        if signer.verify(self.tHash, b64decode(self.tSignature)):
            return True
        return False

    def coinTransaction(self,id,goofy,coins):
        # coin based transaction which is goofy creating coins
        self.userTransaction( id , goofy.publicKey, goofy.publicKey , coins ,goofy)

    def createHash(self,data):

        digest = SHA256.new()
        # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
        digest.update(b64decode(data))
        return digest

    def userTransaction( self,id , fromPublickey , toPublickey , coins ,fromObj):

        self.id = id
        self.fromPublickey = fromPublickey
        self.toPublickey = toPublickey
        self.tCoins = coins
        self.tTime = time.ctime() #use time.time() to use time in numbers
        self.tValied = True
        self.tMessage = b64encode(fromPublickey + toPublickey + str(self.tCoins) + self.tTime)
        self.tHash = self.createHash(self.tMessage) # Assumes the data is base64 encoded to begin with
        self.tSignature = fromObj.signTransaction(self.tHash)

class Blockchain():

    """docstring for Blockchain."""

    def __init__(self,):
       self.no_users = 0
       self.no_transaction = 0
       self.allUsers = []
       self.allTransactions = []

    def condition(self):
        print "1 ==> coin based Transaction (add money to goofy)"
        print "2 ==> user Transaction (transfer money from one user to another)"
        print "3 ==> list of users "
        print "4 ==> list of Transaction"
        print "5 ==> add user"

    def getUser(self,userPublicKey):
        for user in self.allUsers:
            if user.publicKey == userPublicKey :
                return user

    def verifyTranaction(self,From , To ,cost):
        # see if the transation is on his name (signature)
        # verify if he has money
        ballence_amount = 0
        for transaction in self.allTransactions:
            if(transaction.tValied == True and transaction.toPublickey == From.publicKey ):
                if(transaction.verify_sign(transaction.fromPublickey , transaction.tSignature , transaction.tHash)):
                    ballence_amount += transaction.tCoins
        if ballence_amount >= cost :
            return True
        else:
            return False

    def main(self):
        goofy = User("Goofy")
        goofy.createKey(self.no_users)
        self.no_users = self.no_users + 1
        self.allUsers.append(goofy)

        while True:
            self.condition()
            choice = None
            choice = raw_input()

            if choice == "1" :
                coins = int(raw_input("coins to be transfered "))
                t = Transaction()
                t.coinTransaction(self.no_transaction,goofy,coins)
                self.allTransactions.append(t)
                self.no_transaction = self.no_transaction + 1

            elif choice == "2" :
                # user Transaction (transfer money from one user to another)
                FromId = int(raw_input("transver from"))
                ToId = int(raw_input("transver to"))
                coins = int(raw_input("coins to be transfered "))

                if self.verifyTranaction(self.allUsers[FromId] , self.allUsers[ToId], coins):
                    print "tranction is verified and proceding"
                    dept_to_pay = coins
                    N = self.no_transaction
                    print N
                    for x in range(N-1, -1, -1):
                        print x
                        transaction = self.allTransactions[x]
                        if(transaction.tValied == True and transaction.toPublickey == self.allUsers[FromId].publicKey):
                            if(transaction.tCoins <= dept_to_pay):
                                transaction.tValied = False
                                t = Transaction()
                                t.userTransaction( self.no_transaction, self.allUsers[FromId].publicKey,self.allUsers[ToId].publicKey , transaction.tCoins ,self.allUsers[FromId])
                                self.allTransactions.append(t)
                                self.no_transaction = self.no_transaction + 1
                                dept_to_pay = dept_to_pay - transaction.tCoins
                            else:
                                transaction.tValied = False
                                t1 = Transaction()
                                t1.userTransaction(self.no_transaction,self.allUsers[FromId].publicKey,self.allUsers[ToId].publicKey , dept_to_pay ,self.allUsers[FromId])
                                self.allTransactions.append(t1)
                                self.no_transaction = self.no_transaction + 1
                                t2 = Transaction()
                                remaning_balance = transaction.tCoins - dept_to_pay
                                t2.userTransaction(self.no_transaction,self.allUsers[FromId].publicKey,self.allUsers[FromId].publicKey,remaning_balance,self.allUsers[FromId])
                                dept_to_pay = 0
                                self.allTransactions.append(t2)
                                self.no_transaction = self.no_transaction + 1
                                break;

                    # t = Transaction()
                    # t.userTransaction( id , allUsers[FromId].publicKey,allUsers[ToId].publicKey , coins ,allUsers[FromId])
                print "trancation compleated :-)"

            elif choice == "3" :
                # list of users
                for user in self.allUsers:
                    print "user id ==> "+ str(user.id) +" user name ==>" + user.name

            elif choice == "4" :
                # list of Transaction
                for transaction in self.allTransactions:
                    From = self.getUser(transaction.fromPublickey)
                    To = self.getUser(transaction.toPublickey)
                    print "Transaction was from "+From.name+" to "+To.name+" of worth "+ str(transaction.tCoins) +" and this block's validity is " + str(transaction.tValied)

            elif choice == "5":
                # add user
                name = raw_input("Name of the user ")
                u = User(name)
                u.createKey(self.no_users)
                self.allUsers.append(u)
                self.no_users = self.no_users + 1



if __name__== "__main__":

    B = Blockchain()
    B.main()
