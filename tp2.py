#-*- encoding:utf-8 -*-
######## fichier XML##################
fichierXML= open("resultatXML.xml", "w")
textXML ='<classeMaster1>'

######## fichier HTML##################
fichierHTML = open("resultat.html", "w")
textHTML ='<HTML><HEAD><TITLE>Master Informatique </TITLE></HEAD><BODY>'
textHTML+='<H3><Center><u>Les resultats des etudiants de premiere annee Master </u></Center></H3><BR> <B><I><table BORDER align="center"> '
textHTML+='<thead><tr><th>Prenom</th><th>Nom</th><th>Matricul</th><th>Semster I</th><th>Semster II</th><th>Credit </th><th>Moyenne </th><th>Evaluation </th></tr></thead>'

######## fichier TXT #############
file=open("D:\\1er année Génie Systeme Informatiques 2019.2020\\S1\\MTI\\Tp N02\\data.txt",'r')
######## declaration des variables ###########
nbrEtudiant=0
nbrAdmis=0
nbrAjourner=0
nbrAdmisAvecDette=0
data=file.readlines()
tableMoyenne = []
######### debut de traitement
for line in data:
	#print(line)
        line=line.strip('\n') #élimine \n a lafin des lignes recuperer par la fonction
        items=line.split('\t') #recupere les element separer par tabulation
        #print(items)

        print("***********L'etudient N: ",nbrEtudiant+1,"***************" )
        print("Nom :",items[0],"\nPrenom :",items[1],"\nMatricule :",items[2],"\nMoyenne S1 :",items[3],"\nMoyenne S2 :",items[4],"\nCredit :",items[5])

        nbrEtudiant+=1 #incrimanter le nombre d'etudiant
	#eviter le cas ou l'un des chemps MoyenneS1,MoyenneS2 et Credit n'est pas rempli (initialiser par default a 0)
        try:
                float(items[3])
        except:
                items[3]=0
        try:
                float(items[4])
        except:
                items[4]=0
        try:
                int(items[5])
        except:
                items[5]=0
        moyennes= round((float (items[3])+float(items[4]))/2,2) #caluler la moyenne de chaque etudiant
                #affichage XML
        textXML+='<etudiant>'

        textXML += '<matricule>' + items[0] + '</matricule>'
        textXML+='<nom>'+items[1]+ '</nom>'
        textXML+= '<prenom>' + items[2] + '</prenom>'
        textXML+='<moyenneS1>' +items[3]+ '</moyenneS1>'
        textXML+='<moyenneS2>' +items[4]+'</moyenneS2>'
        textXML+= '<moyenneGenerale>' +str(moyennes)+ '</moyenneGenerale>'
        textXML+='<credit1>'+items[5]+'</credit1>'
        textXML+= '<credit2>' +items[6]+ '</credit2>'

#affichage HTML
        textHTML+='<tbody><tr>'
        textHTML+='<td>'+items[0]+' </td>'
        textHTML+='<td>'+items[1]+' </td>'
        textHTML+='<td>'+items[2]+' </td>'
        textHTML+='<td>'+items[3]+' </td>'
        textHTML+='<td>'+items[4]+' </td>'
        textHTML+='<td>'+items[5]+' </td>'
        textHTML += '<td>' + items[6] + ' </td>'
        textHTML+='<td>'+str(moyennes)+' </td>'
        print("La moyenne :",moyennes)
        tableMoyenne+=[moyennes] # ajouter chaque moyenne ou tableMoyenne et les stocker en ordre coissant
        #les condition de chaque cas ("Admis","Ajourner","Admis avec dette") ..
        if float (items[3])>=10 and float(items[4])>=10:
                print("Remarque : Admis")
                nbrAdmis+=1
                textXML+='<evaluation> Admis </evaluation>'
                textHTML+='<td> Admis </td>'
        elif int(items[5])>=45:
                print("Remarque : Admis avec dette ")
                nbrAdmisAvecDette+=1
                textXML+='<evaluation> Admis avec dette </evaluation>'
                textHTML+='<td> Admis avec dette </td>'
        else:
                print("Remarque : Ajourner")
                nbrAjourner+=1
                textXML+='<evaluation> Ajourner </evaluation>'
                textHTML+='<td> Ajourner </td>'
        textXML+='</etudiant>' #fermetteur de balise etudiant
tableMoyenne.sort() #fermer la tableMoyenne

textHTML+='</tr></tbody></table>'
############### calcule les statistique ########################
pourcentageAdmis=round(((float(nbrAdmis)/float(nbrEtudiant))*100),2)
pourcentageAjourner=round(((float(nbrAjourner)/float(nbrEtudiant))*100),2)
pourcentageAdmisAvecDette=round(((float(nbrAdmisAvecDette)/float(nbrEtudiant))*100),2)
############### affichage du resultats en mode console ################################
print("\n ############################ les statistiques ############################\n")
print("LE MEILLEUR MOYENNE OBTENU EST  : ",tableMoyenne[nbrEtudiant-1])
print ('\nLE MOUVAISE  MOYENNE   EST : ', tableMoyenne[0] ,"\n")
print("\t  \t  \t **************** ")
print ('le nombre des etudients admis est     : ',nbrAdmis , " ==> le percentage est : (",pourcentageAdmis,"% )")
print ('le nombre des etudients ajourne  est  : ' ,nbrAjourner , "==> le percentage est : (",pourcentageAjourner,"% )")
print ('le nombre des etudients admis avec dette  est :',nbrAdmisAvecDette  , "==> le percentage est : (",pourcentageAdmisAvecDette,"% )")
############### affichage txt XML des resultats ################################
textXML+='<meilleureMoyenne>'+str(tableMoyenne[nbrEtudiant-1])+'</meilleurMoyenne>'
textXML+='<mauvaiseMoyenne>' +str(tableMoyenne[0])+ '</mauvaiseMoyenne>'
textXML+='<statistique>'
textXML+='<lesAdmis>'
textXML+='<nombre>' +str(nbrAdmis)+ '</nombre>'
textXML+='<pourcentage>' +str(pourcentageAdmis)+'% </pourcentage>'
textXML+='</lesAdmis>'
textXML+='<lesAdmisAvecDette>'
textXML+='<nombre>' +str(nbrAdmisAvecDette)+ '</nombre>'
textXML+='<pourcentage>'+str(pourcentageAdmisAvecDette)+'% </pourcentage>'
textXML+='</lesAdmisAvecDette>'
textXML+='<lesAjourné>'
textXML+='<nombre>' +str(nbrAjourner)+ '</nombre>'
textXML+='<pourcentage>' +str(pourcentageAjourner)+'% </pourcentage>'
textXML+='</lesAjourner>'
textXML+='</statistique>'
textXML+='</classeMaster1>'
############### affichage txt HTML des resultats ################################
textHTML+='<HR><H3><Center><u> Les statistiques </u></Center></H3> '
textHTML+='<p>la meilleure moyenne obtenue : '+str(tableMoyenne[nbrEtudiant-1])+'</p>'
textHTML+='<p>la mauvaise moyenne obtenue : '+str(tableMoyenne[0])+'</p>'
textHTML+='<p>le nombre des etudiants admis est     : '+str(nbrAdmis)+ ' ==> le percentage est : ('+str(pourcentageAdmis)+'% )</p>'
textHTML+='<p>le nombre des etudiants ajourné  est  : '+str(nbrAjourner)+ ' ==> le percentage est : ('+str(pourcentageAjourner)+'% )</p>'
textHTML+='<p>le nombre des etudiants admis avec dette  est : '+str(nbrAdmisAvecDette)+ ' ==> le percentage est : ('+str(pourcentageAdmisAvecDette)+'% )</p>'
textHTML+=' </BODY></HTML>' #fermetteur de balise body et html
fichierXML.write(textXML)   #efectuer ecriture de tout le textXML
fichierHTML.write(textHTML) #effectuer ecriture de tout le textHTML
file.close() #fermetteur de fichier
