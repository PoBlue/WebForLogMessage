# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask,render_template,url_for,request,redirect,flash,jsonify,make_response
import subprocess

app = Flask(__name__)

@app.route('/<string:action>')
def logLastMsg(action):
	filePath = '/Users/blues/Desktop/rqcli-master/Log/'
	fileName = 'd16-6-19.log'

	cmds = ['cat' , 'tail']
	if action in cmds:
		cmd = action
	elif action == 'tac':
		lines = subprocess.check_output(['tail','-r',filePath+fileName]).split('\n')
		return render_template('showMessages.html',lines=lines)
	else:
		return 'unvailad action'

	lines = subprocess.check_output([cmd , filePath+fileName]).split('\n')
	

	return render_template('showMessages.html',lines=lines)

@app.route('/')
def mainPage():
	return render_template('mainPage.html')


if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.debug = True 
	app.run()