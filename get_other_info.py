import googlemaps
import random
from pprint import pprint

# 各々のAPIKeyを使用する
path = '../apikey.txt'
f = open(path)

API_KEY = f.read()
CLIENT = googlemaps.Client(API_KEY)


def check_include_text(text, place_result):
    included = False
    for str in place_result:
        if text in str:
            included = True

    return included


def create_text(place_result):
    text = ''
    # TODO
    # スポットを参照して台詞を選択
    if check_include_text('山口大学', place_result):
        text += '山大だね! 山大生ってホントにイケメンが多いよね!'
    elif check_include_text('ラーメン祐三', place_result):
        text += 'ラーメン祐三がある! このアプリを作成したメンバーは祐三が大好きみたいだよ!'
    elif check_include_text('Trial', place_result):
        text += 'トライアルだね！24時間営業なのは嬉しいけど品出しのタイミングで行っちゃうんだよなあ'
    elif check_include_text('Hotto Motto', place_result):
        text += 'ごはんに困ったらほっともっとだね．ここでの待ち時間は案外嫌いじゃないな'
    elif check_include_text('Joyfull', place_result):
        text += '近くにジョイフルがある！私も学生の頃はそこでだべってたなあ'
    elif check_include_text('Sukiya', place_result):
        text += 'すいません．三種のチーズ牛丼に温玉付きをお願いします．'
    elif check_include_text('寿司', place_result):
        text += '寿司屋さんがある！これを作った人はカニ味噌の軍艦が大好きみたいだよ'
    elif check_include_text('焼肉', place_result):
        text += '焼肉屋さんが近いね！ 焼肉は高いから手が出ないんだよなあ'
    elif check_include_text('ウォンツ', place_result):
        text += 'ウォンツは意外とラインペイが使えるから便利だよね！'
    elif check_include_text('Mos Burger', place_result):
        text += 'モスがあるやん！ちょっと高いお金払ってでも食べたいよね！'
    elif check_include_text('居酒屋', place_result):
        text += '居酒屋だ！飲んだら運転しないでね'
    elif check_include_text('UNIQLO', place_result):
        text += 'ユニクロじゃん！ユニクロの本社は山口にあるんだよ！'
    elif check_include_text('Matsuya', place_result):
        text += '松屋があるね！チー牛は無いよ！'
    elif check_include_text('McDonald', place_result):
        cand = ['マックここにもあるじゃん! ちなみにマクドと、マックどっち派？',
                'マックあるね！ドナルドは31の言語を喋れるらしい・・・',
                '知ってた？アメリカのマックはドリンクのSサイズが日本のLサイズくらいあるらしいよ']
        i = random.randint(0, len(cand)-1)
        text += cand[i]
    elif check_include_text('Lawson', place_result):
        cand = ['ローソンあるね、トイレとか大丈夫？',
                'あっ，ローソン！ pontaはポイントターミナルの略って知ってた？',
                'ローソンだね．Lチキの旨塩は間違いないね！']
        i = random.randint(0, len(cand)-1)
        text += cand[i]
    elif check_include_text('7-Eleven', place_result):
        cand = ['セブンが見えるね! ちなみに, 私が好きなセブンイレブンの商品はシャキシャキレタスサンドだよ!',
                'セブン前を通過したよ! セブンイレブンの売上1位の商品は,「旨みスープの野菜盛りタンメン」らしいよ!']
        i = random.randint(0, len(cand)-1)
        text += cand[i]
    else:
        cand = ['あまり目につくものが無いなあ．',
                'ひょっとしてすごい田舎に来てる? 私の仕事が無くなってしまうので困るよ！',
                'なかなか閑静な場所だね．',
                '眠らないように運転頑張ってね！私も会話を繋ぐように頑張るよ',
                '暇ですね、しりとりでもしますか。じゃあ、きりん。あっ・・・',
                'ながらスマホに注意してね！ずっと喋り続けるよ！',
                '日本が左側通行なのは明治時代，武士が左側に刀を持っていた習慣から由来してるらしいよ！'
                ]
        i = random.randint(0, len(cand) - 1)
        text += cand[i]
    return text


def get_around_spot(latitude, longitude):
    loc = {'lat': latitude, 'lng': longitude}
    place_result = CLIENT.places_nearby(
        location=loc, radius=500, type='food')
    store_list = []
    for store in place_result['results']:
        store_list.append(store['name'])
    print(store_list)

    text = create_text(store_list)
    return text
