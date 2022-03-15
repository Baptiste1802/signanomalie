from fpdf import FPDF

length = 148
width = 105

def generationPDF(bat, salle, materiel, qr):

    class PDF(FPDF):
        
        def header(self):
            self.set_font('arial', 'B', 11)

            # Titre
            if salle == None:
                self.cell(0, 10, 'Fiche QR bâtiment ' + bat , True, ln=True, align='C')
            elif materiel == None:
                self.cell(0, 10, 'Fiche QR salle ' + salle , True, ln=True, align='C')
            else :
                self.cell(0, 10, 'Fiche QR matériel ' + materiel , True, ln=True, align='C')

        def footer(self):
            self.set_font('arial', '', 8)

            # QR code
            self.image(qr, x=width/2-20, y=35, w=40)

            # Espacement
            self.cell(0, 70, ln=True)

            # Infos
            self.cell(0, 5, 'Bâtiment ' + bat, ln=True, align='C')
            if salle != None:
                self.cell(0, 5, 'Salle ' + salle, ln=True, align='C')
            if materiel != None :
                self.cell(0, 5, "Machine " + salle, ln=True, align='C')

            # Logo IUT'O
            self.image("img/iut.jpeg", x=width/2-20, y=length-23, w=40)


    pdf = PDF('P', 'mm', (105,148))
    pdf.add_page()

    # Création du PDF
    if salle == None:
        pdf.output('Fiche_info_bat_' + bat + '.pdf')
    elif materiel == None:
        pdf.output('Fiche_info_salle_' + salle + '.pdf')
    else :
        pdf.output('Fiche_info_materiel_' + materiel + '.pdf')