# Goofy-Coin

# User #
     * this class contain user info this is created when a new user is added to
     blockchain structure this class contain :

## id
     * this has id of user
## name
     * name of user     
## __privateKey
     * Generate an RSA keypair with an exponent of 65537 in PEM format
   param: bits The key length in bits
   Return private key and public key
## publicKey
     * Generate an RSA keypair with an exponent of 65537 in PEM format
param: bits The key length in bits
Return private key and public key
## bornTime
     * time at which user was created
## createKey(id)
     * Generate an RSA keypair with an exponent of 65537 in PEM format
   param: bits The key length in bits
   Return private key and public key

## signTransaction(hashData)     
     * user signs on a message

# Transaction #
     * this is a part of ledger and it contain details of the transaction
## id
     * transaction id which helps to store transaction in an array which is considered as leaguer
## fromPublickey
     * publicKey of the person who is giving money
## toPublickey
     * publicKey of the person who is getting money
## tCoins
     * coins present in this block of transaction
## tTime
     * time at which transaction was done
## tValied
     * if tranction is expired or not
## tMessage
     * whole tranction data
## tHash
     * hash of(message)
## tSignature
     * signature of the person making the traction
## verify_sign(pub_key, signature, hashData)
     * check if the trancation block is legit througn the signature of its creater
## coinTransaction(id,goofy,coins)
     * coin based trancation (adding money to goofy's wallert)     
## userTransaction(id , fromPublickey , toPublickey , coins ,fromObj)
     * trancation from one user to another
     * old block is distroied in blockchain and new block is added

# Blockchain #

## allUsers
## allTransactions
## condition()
## getUser(userPublicKey)
## verifyTranaction(From , To ,cost)
     * verify is the trancation is tValied
     * weather he has money
     * weather all his trancation are legit
## main()
