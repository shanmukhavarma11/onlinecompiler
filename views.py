from django.shortcuts import render
import re
import os
from django.shortcuts import render
from django.http import HttpResponse
from .forms import GetForm
import subprocess
def index(request):
	if request.method=="GET":
		form=GetForm()
		return render(request,'compile.html',{'form':form})
	else:
		form =GetForm(request.POST)
		if form.is_valid() and form.lang=="java":
			main_class_name=""
			text=form.cleaned_data["code"]
			print("text:",text)
			for i in re.split('class ',text)[1:]:
				if re.search('public static void main',i):
					main_class_name=re.search('(\w*)',i).group(1)
			os.chdir('C:\\Users\\Varma\\Desktop\\projectcompiler\\onlinecompiler\\codes\\')
			sd=open(main_class_name+".java","w+")
			sd.write(text)
			proc = subprocess.Popen(['javac',main_class_name+'.java'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
			cmd=['java', main_class_name]
			print(proc)
			output =subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
			out, inp = output.communicate(form.input1)
            try:
				print(output.stdout.read())
				print (subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read())
			except:
				print("########")
				pass
			form.save()
        if form.is_valid() and form.lang=="python 3.9":
			main_class_name=""
			text=form.cleaned_data["code"]
			os.chdir('C:\\Users\\Varma\\Desktop\\projectcompiler\\onlinecompiler\\codes\\')
			sd=open(main_class_name+".py","w+")
			sd.write(text)
			proc = subprocess.Popen(['python',main_class_name+'.py'],shell=True,stdin=PIPE,stdout=PIPE)
            out,inp = proc.communicate(form.input1)
			form.save()
		return render(request,'compile.html',{'form1':out})
