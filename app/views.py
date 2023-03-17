from django.shortcuts import render

# Create your views here.
def ifcon(request):
    d={'a':121,'b':231,'c':1223}
    return render(request,'ifcon.html',context=d)
