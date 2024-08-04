import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

#reportlab imports - Using Platypus for simplicity 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Frame, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm


def main():
    #Create PDF
    pdf = SimpleDocTemplate("EQNR.pdf", pagesize=letter)

    #Leading style
    line_spacing = ParagraphStyle(
        'line_spacing',
        leading = 24
    )

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("Equinor (EQNR) Report", title_style)

    #YFinance DATA
    stock = yf.Ticker("EQNR")
    elements = []
    elements.append(title)

    elements.append(Paragraph('<strong>Sector: </strong>' + stock.info['sector'], ParagraphStyle('info_p_1', spaceBefore=2 * cm)))
    elements.append(Paragraph('<strong>Industry: </strong>' + stock.info['industry'], line_spacing))
    elements.append(Paragraph('<strong>Description: </strong><br/>' + stock.info['longBusinessSummary'], line_spacing))

    print(stock.info)

    pdf.build(elements)

if __name__ == "__main__":
    main()