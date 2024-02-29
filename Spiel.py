from random import shuffle


fragen_antworten = {
    "Sozialismus": {
        "Denkst du, dass es keine grossen Unternehmen geben sollte welche die Wirtschaft kontrollieren?": "ja",
        "Sind Sie der Meinung, dass der Staat eine Rolle dabei spielen sollte, die soziale Sicherheit und das Wohlergehen der Bürger zu gewährleisten?": "ja",
        "Stimmen Sie der Idee zu, dass Bildung und Gesundheitsversorgung grundlegende Rechte für alle Bürger sein sollten?": "ja",
        "Findest du, dass eine gerechte Verteilung der Güter inerhalb eines Landes wichtig ist?": "ja",
        "Befürworten Sie die Idee von öffentlichem Eigentum?": "ja",
    },
    "Anarchismus": {
        "Findest du der Staat ist dein Feind?": "ja",
        "Denkst du, dass der Staat dich beim drucken von Wertpapieren indirekt beraubt, wenn dadurch die Infaltion steigt?": "ja",
        "Ich mag es nicht, dass ich dem Staat steuern zahlen muss, ich kann ja auch eine Security Firma oder Versicherung anheuern - Stimmst du dem zu?": "ja",
        "Ich will nicht, dass der Staat und die Exekutive so viel macht haben und aus so wenigen leuten besteht!": "ja",
        "Ich bin eine Freie Person, mir steht niemand über ! - stimmst du dem zu?": "ja",
    },
    "Kommunismus": {
        "Befürwortest du die Idee einer klassenlosen Gesellschaft, in der alle Menschen gleiche Rechte und Chancen haben?": "ja",
        "Glaubst du, das die Ressourcen eines Landes Gerecht inerhalb aller Bewohner aufgeteilt werden müssen?": "ja",
        "Unterstützt du radikale Wege um an ein Ziel zu gelangen, wenn diese im Interesse aller sind?" "ja",
        "Fändest du es gut, wenn alle Kinder die gleichen Kleidung tragen würden?": "ja",
        "Stell dir vor, man würde überall das gleiche Lernen. Wäre das besser für die Bevölkerung?": "ja",
    }
}


def shuffle_fragen(kategorie):
    fragen = list(fragen_antworten[kategorie].keys())
    shuffle(fragen)
    return fragen


def spiele_spiel():
    punktzahl_sozialismus = 0
    punktzahl_kommunismus = 0
    punktzahl_anarchismus = 0


    for kategorie in fragen_antworten.keys():
        print("\n{20*'='}\n{'> Kategorie:', kategorie, '<'}\n{20*'='}")
        fragen = shuffle_fragen(kategorie)
        
        for frage in fragen:
            antwort = input(frage)
            if antwort.lower() == fragen_antworten[kategorie][frage].lower():
                print("Spannend!")

                if kategorie == "Sozialismus":
                    punktzahl_sozialismus += 1
                elif kategorie == "Kommunismus":
                    punktzahl_kommunismus += 1
                elif kategorie == "Anarchismus":
                    punktzahl_anarchismus += 1
            else:
                print("Spannend!", fragen_antworten[kategorie][frage])

    print("\nPunktzahl Sozialismus:", punktzahl_sozialismus)
    print("Punktzahl Kommunismus:", punktzahl_kommunismus)
    print("Punktzahl Anarchismus:", punktzahl_anarchismus)
        
    if punktzahl_sozialismus > punktzahl_kommunismus and punktzahl_sozialismus > punktzahl_anarchismus:
        print("Du bist eher ein Sozialist")
    if punktzahl_kommunismus > punktzahl_sozialismus and punktzahl_kommunismus > punktzahl_anarchismus:
        print("Du bist eher ein Kommunist")
    if punktzahl_anarchismus > punktzahl_kommunismus and punktzahl_anarchismus > punktzahl_sozialismus:
        print("Du bist eher ein Anarchist")
    if punktzahl_sozialismus == punktzahl_kommunismus and punktzahl_sozialismus > punktzahl_anarchismus:
        print("Du bist eine Mischung aus Sozialismus und Kommunismus")
    if punktzahl_kommunismus == punktzahl_anarchismus and punktzahl_kommunismus > punktzahl_sozialismus:
        print("Du bist eine Mischung aus Kommunsit und Anarchist")
    if punktzahl_anarchismus == punktzahl_sozialismus and punktzahl_anarchismus > punktzahl_kommunismus:
        print("Du bist eine Mischung aus Anarchist und Sozialist")
    if punktzahl_sozialismus == punktzahl_kommunismus and punktzahl_sozialismus == punktzahl_anarchismus:
        print("Du bist zu ungebildet, um dir eine ausgeprägte Meinung zu bilden.")


spiele_spiel()