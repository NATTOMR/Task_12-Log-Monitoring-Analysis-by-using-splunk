import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 756, "SOC Log Monitoring & Incident Detection Analysis Report | Task 12")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 750, letter[0] - 36, 750)
        
        # Footer (All Pages)
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 36, 25, page_text)
        self.drawString(36, 25, "Splunk Enterprise SIEM | Confidential SOC Report — NATTOMR")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 36, letter[0] - 36, 36)
        
        self.restoreState()


def md_to_pdf(md_filepath, pdf_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#475569"),
        spaceAfter=14
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0D9488"),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'Heading3_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        leftIndent=15,
        spaceAfter=4
    )
    
    quote_style = ParagraphStyle(
        'Quote_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0F766E"),
        backColor=colors.HexColor("#F0FDF4"),
        borderColor=colors.HexColor("#99F6E4"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )
    
    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#1E293B"),
        backColor=colors.HexColor("#F8FAFC"),
        borderColor=colors.HexColor("#E2E8F0"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#334155")
    )

    story = []
    
    in_code_block = False
    code_lines = []
    in_table = False
    table_lines = []
    
    def process_text_formatting(text):
        # Convert markdown bold, italic, code tags
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        text = re.sub(r'`(.*?)`', r'<font face="Courier" color="#0D9488">\1</font>', text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n\r')
        
        # Code block handling
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                code_text = "\n".join(code_lines)
                # Escape XML chars in code block
                code_text = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                code_text = code_text.replace('\n', '<br/>').replace(' ', '&nbsp;')
                story.append(Paragraph(code_text, code_style))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue
            
        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Table handling
        if '|' in line and not line.strip().startswith('>'):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            # End of table
            in_table = False
            # Render table
            rows = []
            for tline in table_lines:
                if '---' in tline:
                    continue
                cells = [c.strip() for c in tline.strip('|').split('|')]
                rows.append(cells)
            
            if rows:
                table_data = []
                for r_idx, row in enumerate(rows):
                    row_data = []
                    for c_idx, cell in enumerate(row):
                        formatted_cell = process_text_formatting(cell)
                        if r_idx == 0:
                            p = Paragraph(formatted_cell, table_header_style)
                        else:
                            p = Paragraph(formatted_cell, table_cell_style)
                        row_data.append(p)
                    table_data.append(row_data)
                
                # Available width = 612 - 72 = 540pt
                col_count = len(rows[0])
                col_w = 540.0 / col_count if col_count > 0 else 540.0
                
                t = Table(table_data, colWidths=[col_w]*col_count)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0F172A")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('LEFTPADDING', (0, 0), (-1, -1), 4),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ]))
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 6))
            table_lines = []

        # Empty line
        if not line.strip():
            story.append(Spacer(1, 4))
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ('---', '***', '___'):
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CBD5E1"), spaceBefore=6, spaceAfter=8))
            i += 1
            continue

        # Headings
        if line.startswith('# '):
            text = process_text_formatting(line[2:].strip())
            story.append(Paragraph(text, title_style))
            i += 1
            continue
        elif line.startswith('## '):
            text = process_text_formatting(line[3:].strip())
            story.append(Paragraph(text, h1_style))
            i += 1
            continue
        elif line.startswith('### '):
            text = process_text_formatting(line[4:].strip())
            story.append(Paragraph(text, h2_style))
            i += 1
            continue
        elif line.startswith('#### '):
            text = process_text_formatting(line[5:].strip())
            story.append(Paragraph(text, h3_style))
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            text = process_text_formatting(line[2:].strip())
            story.append(Paragraph(text, quote_style))
            i += 1
            continue

        # Bullet list
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            item_text = line.strip()[2:].strip()
            text = process_text_formatting(item_text)
            story.append(Paragraph(f"• {text}", bullet_style))
            i += 1
            continue
            
        if re.match(r'^\d+\.\s+', line.strip()):
            m = re.match(r'^(\d+\.)\s+(.*)', line.strip())
            num_prefix = m.group(1)
            item_text = m.group(2)
            text = process_text_formatting(item_text)
            story.append(Paragraph(f"{num_prefix} {text}", bullet_style))
            i += 1
            continue

        # Normal paragraph
        text = process_text_formatting(line.strip())
        story.append(Paragraph(text, body_style))
        i += 1

    # Document setup
    doc = SimpleDocTemplate(
        pdf_filepath,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {pdf_filepath}")

if __name__ == '__main__':
    md_file = 'Log_Analysis_Report.md'
    pdf_file = 'Log_Analysis_Report.pdf'
    md_to_pdf(md_file, pdf_file)
