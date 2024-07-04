import hashlib
import requests
import flask
import json
from urllib.parse import urlparse
from uuid import uuid4

from time import time 
from flask import Flask, jsonify, request

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        
        self.new_block(previous_hash='1', proof=100)
        
    def register_node(self, address):
        """
        Tambahkan node A baru ke daftar node
        
        :param address: Alamat dari node. Contohnya ''http://192.168.0.5:5000''
        
        """
        
        parsed_url = urlparse(address)
        
        if parsed_url.metloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')
        
    def valid_chain(self, chain):
        """
        Tentukan apakah blockchain yang diberikan valid
        
        :param chain: Sebuah Blockchain
        :return: Benar jika valid, salah jika tidak
        """
        
        last_block = chain[0]
        current_index = 1
        
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block.hash:
                return False
            
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1
            
        return True
    
    def resolve_conflicts(self):
        """
        Ini adalah algoritma konsensus kami, ia menyelesaikan konferensi dengan mengganti rantai kami dengan yang terpanjang di jaringan.
        
        :return: Benar jika rantai kami diganti, salah jika tidak
        """
        
        neighbours = self.nodes
        new_chain = None
        
        # ! Kami hanya mencari rantai lebih lama dari kami
        max_length = len(self.chain)
        
        # ! Ambil dan verifikasi rantai dari semua node di jaringan Anda
        
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                
                # ! Periksa apakah panjangnya lebih panjang dan rantai itu valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain


    def new_block(self, proof, previous_hash=None):
        """
        Membuat blok baru dan menambahkannya ke blockchain
        :param proof: <int> Bukti yang diberikan oleh Bukti Algoritma Kerja
        :param previous_hash: (Optional) <str> Hash dari blok sebelumnya
        :return: <dict> Blok baru
        """
        
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(), 
            'transactions' : self.current_transaction,
            'proof' :  proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        
        # ! Setel ulang daftar transaksi saat ini
        self.current_transactions = []
        self.chain.append(block)
        
        return block
        
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
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        """
        Membuat hash SHA-256 dari satu blok
        :param blockk: <dict> Blok
        :return: <str>
        """
    
        # ! We must make sure that the dictionary is Ordered, or we'll have inconist 
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
        

    
    