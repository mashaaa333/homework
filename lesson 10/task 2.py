file = open("poem.txt", "w")
file.write("Не выходи из комнаты, не совершай ошибку.\n"
           "Зачем тебе Солнце, если ты куришь Шипку?\n"
           "За дверью бессмысленно всё, особенно — возглас счастья.\n"
           "Только в уборную — и сразу же возвращайся.\n"
           "\n"
           "О, не выходи из комнаты, не вызывай мотора.\n"
           "Потому что пространство сделано из коридора\n"
           "и кончается счетчиком. А если войдет живая\n"
           "милка, пасть разевая, выгони не раздевая.\n"
           "\n"
           "Не выходи из комнаты; считай, что тебя продуло.\n"
           "Что интересней на свете стены и стула?\n"
           "Зачем выходить оттуда, куда вернешься вечером\n"
           "таким же, каким ты был, тем более — изувеченным?\n"
           "\n"
           "О, не выходи из комнаты. Танцуй, поймав, боссанову\n"
           "в пальто на голое тело, в туфлях на босу ногу.\n"
           "В прихожей пахнет капустой и мазью лыжной.\n"
           "Ты написал много букв; еще одна будет лишней.\n"
           "\n"
           "Не выходи из комнаты. О, пускай только комната\n"
           "догадывается, как ты выглядишь. И вообще инкогнито\n"
           "эрго сум, как заметила форме в сердцах субстанция.\n"
           "Не выходи из комнаты! На улице, чай, не Франция.\n"
           "\n"
           "Не будь дураком! Будь тем, чем другие не были.\n"
           "Не выходи из комнаты! То есть дай волю мебели,\n"
           "слейся лицом с обоями. Запрись и забаррикадируйся\n"
           "шкафом от хроноса, космоса, эроса, расы, вируса.")
file = open("poem.txt", "r")
print(file.read())


def count_words(file_name):
    with open(file_name, 'r') as file_new:
        content = file_new.read()
        word_count = len(content.split())
        return word_count


file_name = "poem.txt"

word_count = count_words(file_name)

if word_count:
    print(f"Number of words:\t {word_count}")