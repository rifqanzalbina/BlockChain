class Blockchain(object):
    def new_transaction(self, sender, recipient, amount):
        
        """
        Membuat transaksi baru yang akan dimasukkan ke dalam blok berikutnya yang akan ditambang
        :param sender: <str> Alamat Pengirim 
        :param recipient: <str> Alamat Penerima
        :param amount: <int> Jumlah
        :return: <int> Indeks Blok yang akan menyimpan transaksi ini
        """
        
        self.current_transaction.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
        })
        
        return self.last_block['index'] + 1
    
    