# from django.http import HttpResponse
import io

from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from .models import LoginTotalUsers

# from .forms import DateForm


def home(request):
    for i in range(1000):
        dic = {}
        for i in range(1000):
            dic.setdefault(i, i)
        LoginTotalUsers.objects.create(employee_ids=dic)
    return render(request, 'home.html')


def format_data(request):

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    text_obj = p.beginText()
    text_obj.setTextOrigin(inch, inch)
    text_obj.setFont('Helvetica', 14)

    lst = [
        'this is first line',
        'this is second line',
        'this is third line',
    ]
    for line in lst:
        text_obj.textLine(line)

    p.drawText(text_obj)
    p.showPage()
    p.save()
    buffer.seek(0)

    # # Draw things on the PDF. Here's where the PDF generation happens.
    # # See the ReportLab documentation for the full list of functionality.
    # # p.drawString(100, 100, "Hello world.")
    # # p.drawString(100, 200, "Hello world.")
    # # p.drawString(100, 300, "Hello world.")

    # # # Close the PDF object cleanly, and we're done.
    # # p.showPage()
    # # p.save()

    # # FileResponse sets the Content-Disposition header so that browsers
    # # present the option to save the file.
    # buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='hello.pdf')
