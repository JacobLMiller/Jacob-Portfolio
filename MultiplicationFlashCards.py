import genanki

myModel = genanki.Model(1851810099, "Jacob Model",
                        fields=[{"name": "Question"},
                                {"name": "Answer"},],
                        templates=[{"name": "Card 1",
                                    "qfmt": "{{Question}}",
                                    "afmt": '{{FrontSide}}<hr ide="answer">{{Answer}}',
                                    },])
#Add to deck here
myDeck = genanki.Deck(2084900200, "Sadie Flash Cards")

#Add notes here

for x in range(1,13):
    for y in range(1,13):
        myDeck.add_note(genanki.Note(model=myModel,fields=[str(x) + " X " + str(y),str(x*y)]))

genanki.Package(myDeck).write_to_file("SadieFlashCards.apkg")
