import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import io
import sys

#reportlab imports - Using Platypus for simplicity 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Frame, Flowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm

import makeGraphs as mg

ticker = sys.argv[1]


def main():
    #YFinance DATA
    stock = yf.Ticker(f"{ticker}")

    #Create PDF
    pdf = SimpleDocTemplate(f'{ticker}.pdf', pagesize=letter)

    #Leading style
    line_spacing = ParagraphStyle(
        'line_spacing',
        leading = 24
    )

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph(f"{stock.info['shortName']} ({ticker}) Report", title_style)

    elements = []
    elements.append(title)

    elements.append(Paragraph('<strong>Sector: </strong>' + stock.info['sector'], ParagraphStyle('info_p_1', spaceBefore=2 * cm)))
    elements.append(Paragraph('<strong>Industry: </strong>' + stock.info['industry'], line_spacing))
    elements.append(Paragraph('<strong>Description: </strong><br/>' + stock.info['longBusinessSummary'], line_spacing))

    #Add graphs to PDF doc
    income_graph_image = Image(plot_to_buffer(mg.makeIncomeGraph(stock)), 15*cm, 10*cm)
    debt_graph_image = Image(plot_to_buffer(mg.makeDebtGraph(stock)), 15*cm, 10*cm)
    dividend_graph_image = Image(plot_to_buffer(mg.makeDividendGraph(stock)), 15*cm, 10*cm)

    elements.append(income_graph_image)
    elements.append(debt_graph_image)
    elements.append(dividend_graph_image)

    pdf.build(elements)

#Rendering plots returned from makeGraphs to a Buffer, so that it can be put in the PDF / Using a buffer so the image does not have to be saved
def plot_to_buffer(fig):
    buffer = io.BytesIO() 
    fig.savefig(buffer, format='jpg')
    buffer.seek(0)
    return buffer




if __name__ == "__main__":
    main()