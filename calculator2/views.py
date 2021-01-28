from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    arr =['1','2','3','4','5','6','7','8','9','0','.']
    inp = []
    opr =''
    inp1 = ''
    if request.method == "POST":
        inputVal = request.POST.get('inputVal')
        for i in range(len(inputVal)):
               if inputVal[i] in arr:
                  inp1 += inputVal[i]
               else:
                   inp.append(inp1)
                   inp1 = ''
                   opr += inputVal[i]
        inp.append(inp1)
        inp1 = ''
        if opr == '':
            output = ""
        else:
            if opr[0] =="+":
                output = float(inp[0]) + float(inp[1])
                print(output)
            elif opr[0] =="-":
                output = float(inp[0]) - float(inp[1])
                print(output)
            elif opr[0] == "*":
                output = float(inp[0]) * float(inp[1])
                print(output)
            elif opr[0] == "/":
                output = float(inp[0]) / float(inp[1])
                print(output)
            elif opr[0] == "%":
                output = float(inp[0]) % float(inp[1])
                print(output)
    else:
        output = ""
        inputVal = ''
    return render(request,'index.html',{'output':output,'invalue':inputVal})
