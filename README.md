# BlockChain
**Cara tercepat untuk untuk belajar BlockChain adalah langsung dengan praktek**

Kita akan coba praktek BlockChain dengan bahasa pemrograman yang paling mudah dan paling populer, yaitu Python.

**Siap?**

Poin apa saja yang akan kita pelajari?
- [x] BlockChain
- [x] Smart Contract
- [x] BlockChain Technology
- [x] BlockChain DApps
- [x] BlockChain Consensus
- [x] BlockChain Network
- [x] BlockChain Mining
- [x] BlockChain Wallet
- [x] BlockChain Token

# BlockChain?
<details>
<summary>
    Klik Untuk Melihat Penjelasan lebih detail
</summary>

### Apa itu Blockchain?

BlockChain adalah teknologi buku besar terdistribusi dan terdesentrallisasi yang mencatat transaksi dengan cara yang aman dan transparan. Setiap blok dalam rantai berisi hash kriptografi dari blok sebelumny, stempel waktu, dan data transaksi. Struktur ini memastikan integritas dan ketidakubahan data.

### Fitur Utama Blockchain

- **Desentralisasii** : Data tidak disimpan di lokasi pusat tetapi didistribusikan di seluruh jaringan Komputer.
- **Transparansi** : Semua peserta dalam jaringan dapat melihat transaksi yang tercatat di block chain.
- **Ketidakubahan** : Setelah blok ditambahkan ke blockchain. Tidak dapat diubahh ataupun dihapus.
- **Keamanan** : Penggunaan hash Kriptografi dan mekanisme konsensus membuat BlockChain sangat aman terhadap manipulasi dan penipuan.

### Bagaimana Blockchain Bekerja ?
- **Transaksi** : Pengguna memulai transaksi.
- **Verifikasi** : Transaksi diverifikasi oleh peserta jaringan.
- **Pembuatan Blok** : Setelah diverifikasi, transaksi dikelompokkan dengan transaksi lain ke dalam blok.
- **Konsensus** : Jaringan mencapai konsensus tentang validitas blok.
- **Penambahan Rantai** : Blok ditambahkan ke blockchain, dan transaksi tercatat secara permanen.

### Jenis Blockchain
- **Blockchain Publik** : Terbuka untuk semua orang, tanpa batasan siapa yang dapat berpartisipasi.
- **Blockchain Pribadi** : Terbatas untuk  sekelompok peserta tertentu.
- **Blockchain Konsorsium** : Model hibrida di mana sekelompook organisasi mengontrol jaringan.

### Kasus Penggunaan Blockchain
- **Kriptokurensi** : Bitcoin, Ethereum,  dll.
- **Manajemen Rantai Pasokan** : Pelacakan barang dari asal ke tujuan.
- **Verifikasi Identitas** : Manajemen identitas yang aman dan terdesentralisasi.
- **Sistem Pemungutan Suara** : Proses pemungutan suara yang aman dan transparan.
- **Kontrak Cerdas** : Eksekusi otomatis kontrak berdasarkan kondisi yang telah ditentukan.

### Link untuk lebih detail tentang Crpyto
- [Dokumentasi Python Resmi](https://docs.python.org/3/)
- [Dokumentasi Ethereum](https://ethereum.org/en/developers/docs/)
- [Blockchain di Berkeley](https://blockchain.berkeley.edu/)
- [Kursus Blockchain di Coursera](https://www.coursera.org/courses?query=blockchain)

</details>

<br>

# Let's Start !!
<details>
<summary>
    Klik Untuk Melihat Penjelasan lebih detail
</summary>

<br>

Sebelum itu aku ingin kalian untuk menginstall beberapa library python terlebih dahulu

``pip install Flask `` dan ``pip install requests ``,
``pip install hashlib`` ini dapat kalian install melalui command prompt jika kalian sudah selesai menginstall libraryny, maari kita mulai


## Step 1. Membangun Blockchain

<p>Buka text editor ataupun IDE yang kalian suka, Disini saya memakai Visual Studio Code (VSCode), Buat file baru dengan nama </p>

```blockchain.py``` 

### Representing a Blockchain

Kita akan membuat sebuah **Blockchain** class yang konstruktorny membuat daftar kosong awal (untuk menyimpan blockchain) dan kelas lainnya untuk menyimpan transaksi, 
Ini adalah kodingan blueprint untuk class ``blockchain.py`` <br>

```python
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # Menambahkan sebuah blok baru dan menambahkanny ke rantai
        pass
    
    def new_transaction(self):
        # Menambahkan beberapa transaksi baru ke list transaksi
        pass
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
```

``Blockchain``
class bertanggung jawab untuk mengontrol rantai, dimana akan menyimpan transaksi dan beberapa metode untuk menambahkan blok baru ke rantai, 

**Seperti apa block itu terlihat sih?**

<p>Setiap blok memiliki indeks, stempel waktu, daftar transaksi , bukti, dan hash dari blok sebelumnya. Berikut ini contoh tampilan satu blok : </p>


```bash
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```
Pada titik ini, gagasan tentang rantai seharusnya sudah jelas setiap blok baru berisi hash dari blok sebelumny. **Hal ini penting karena hal inilah yang membuat blockchain tidak dapat diubah. :** Jika penyerang merusak Blok sebelumny dalam rantai, maka semua blok berikutnya akan berisi hash yang salah. jadi blockchain tidak dapat diubah.

*Apakah ini masuk akal? jika tidak silahkan untuk kalian pahamin dulu mksduny ide inti dari sistem blockchain ini.*

Kita memerlukan cara untuk menambahkan transaksi ke blok.

``new_transaction()`` method bertanggung jawab untuk hal ini, dan itu cukup mudah

```python
class Blockchain(object):
    ...
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
```
Setelah ``new_transaction()`` menambahkan transaksi ke dalam daftar, fungsi ini akan mengembalikan indeks blok tempat transaksi akan ditambahkan - yang berikutnya akan ditambang. dan ini akan berguna nantinya , bagi pengguna yang mengirimkan transaksi

### Membuat block baru
Ketika ``Blockchain`` sudah dipakai, kita perlu menyamainya dengan blok genesis - blok tanpa pendahulunya. Kita juga perlu menambahkan bukti ke blok genesis kita yang merupakan hasil penmabangan (atau bukti kerja). Kita akan jelaskan lebih detail lagi nanti

Selain membuat blok genesis di konstruktor , kita juga akan menyempurnakan metodenya.
``new block`` ``new_transaction`` dan ``hash()``

```python
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
```


Kode di atas adalah metode ``new_transaction`` dalam kelas ``Blockchain``. Metode ini digunakan untuk membuat transaksi baru yang akan dimasukkan ke dalam blok berikutnya yang akan ditambang

### Memahami Bukti Pekerjaan

Algoritma kerja bukti adalah bagaimana blok baru dibuat atau ditambang di blockchain tujuan POW adalah untuk menemukan angka yang memecahkan masalah.Jumlahnya harus sulit ditemukan tetapi mudah diverifikasi oleh siapa pun di netwowrk.Ini adalah ide inti di balik bukti kerja.

Mari kita putuskan bahwa hash dari beberapa integer x dikalikan dengan y lain harus berakhir dengan 0.
``hash(x * y) = ac23dc...0`` dan ini untuk Dan untuk contoh yang disederhanakan ini, mari kita perbaiki
``x = 5``. Implementasikan ini di Python : 

```python
from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')

```
The solution here is ``y=21`` . Karena, hash yang diproduksi berakhir di 0: 
```
hash(5 * 21) = 1253e9373e...5e3600155e860
```

Dalam Bitcoin, Algoritma Bukti Kerja disebut Hashcash.Dan itu tidak terlalu berbeda dari contoh dasar kami di atas.Ini adalah algoritma yang harus dipecahkan oleh penambang untuk membuat blok baru.Secara umum, kesulitan ditentukan oleh jumlah karakter yang dicari dalam string.Para penambang kemudian dihargai atas solusi mereka dengan menerima koin - dalam transaksi.

Jaringan dapat dengan mudah memverifikasi solusinya.

**Menerapkan bukti dasar kerja**

Mari kita terapkan algoritma serupa untuk blockchain kita .Aturan yang akan kita buat mirip dengan contoh di atas:


```python
import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    ...
        
    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
```

Untuk menyesuaikan kesulitan algoritma, kita dapat memodifikasi jumlah nol terkemuka.Tapi 4 sudah cukup.Anda akan mengetahui bahwa penambahan nol tunggal tunggal membuat perbedaan besar pada waktu yang diperlukan untuk menemukan solusi.

Kelas kita hampir lengkap dan kita siap untuk mulai berinteraksi dengan itu menggunakan permintaan HTTP.

## Step 2: Blockhain sebagai sebuah API


</details>


