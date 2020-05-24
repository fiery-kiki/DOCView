from django.shortcuts import render

def value_convertor(row, type):
    value = []
    for j in range(len(row)):
        value.append({'value':row[j], 'type':type[j]})
    return value

        
def your_appointments(request):
    data = {}
    data['title'] = ['Date', 'Time', 'Consulting Doctor', 'Status']
    data['value'] = [
        ['12 june', '11:30 AM ', 'Nikesh', 'SORRY!'],
        ['12 june', '11:30 AM ', 'Nikesh', 'SORRY!'],
        ['12 june', '11:30 AM ', 'Nikesh', 'SORRY!'],
    ]
    type = ['text', 'text', 'text', 'text']
    data['value'] = [ value_convertor(row, type) for row in data['value']]
    return render(request, 'accounts/your_appointments.html', {'data':data})

def invoice_and_payment(request):
    data = {}
    data['title'] = ['Invoice', 'Paid', 'Date', 'Outstanding']
    data['value'] = [
        ['https://www.google.com', '11:30 AM ', 'Nikesh', 'SORRY!'],
        ['www.google.com', '11:30 AM ', 'Nikesh', 'SORRY!'],
        ['www.google.com', '11:30 AM ', 'Nikesh', 'SORRY!'],
    ]
    type = ['link', 'text', 'text', 'text']
    data['value'] = [ value_convertor(row, type) for row in data['value']]
    return render(request, 'accounts/your_appointments.html', {'data':data})
