# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask,render_template,url_for,request,redirect,flash,jsonify,make_response
import subprocess

app = Flask(__name__)

@app.route('/<string:action>')
def logLastMsg(action):
	filePath = '/Users/blues/Desktop/rqcli-master/Log/'
	fileName = 'd16-6-19.log'
	f = open(filePath+fileName)
	
	lines = tail(f).split('\n')
	return render_template('showMessages.html',lines=lines)

@app.route('/')
def mainPage():
	return render_template('mainPage.html')

def tail( f, lines=20 ):
    total_lines_wanted = lines

    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = [] # blocks of size BLOCK_SIZE, in reverse order starting
                # from the end of the file
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            # read the last block we haven't yet read
            f.seek(block_number*BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = ''.join(reversed(blocks))
    return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])

if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.debug = True 
	app.run()