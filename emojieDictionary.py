import re

def replaceEmojis(input_string):
    if not (input_string):
        return (None)

    emoji_dict = {
        'ud83dudd75ufe0fu2642ufe0f': '🕵️‍♂️',
        'ud83cudf1f': '🌟',
        'u266c': '🎵',
        'ud83eudd32ud83cudffb': '🤲🏻',
        'ud83cudde6ud83cuddea': '🇦🇪',
        'u2665': '♥',
        'u2018': '‘',
        'u2019': '’',
        'u2764ufe0f': '❤️',
        'ud83dude02': '😂',
        'ud83dude0a': '😊',
        'ud83dude0d': '😍',
        'ud83dude14': '😔',
        'ud83dude0c': '😌',
        'ud83dude01': '😁',
        'ud83dude0f': '😏',
        'ud83dude2d': '😭',
        'ud83dude29': '😩',
        'ud83dude2a': '😪',
        'ud83dude22': '😢',
        'ud83dude2c': '😬',
        'ud83dude21': '😡',
        'ud83dude20': '😠',
        'ud83dude30': '🌀',
        'ud83dude31': '🌧️',
        'ud83cudf08': '🌈',
        'ud83dude37': '😷',
        'ud83dude33': '🌷',
        'ud83dude32': '🌲',
        'ud83dude23': '😣',
        'ud83dude25': '😥',
        'ud83dude13': '😓',
        'ud83dude10': '😐',
        'ud83dude11': '😑',
        'ud83dude15': '😕',
        'ud83dude12': '😖',
        'ud83dude3b': '😻',
        'ud83dude09': '😉',
        'ud83dude2b': '😫',
        'ud83dude03': '😃',
        'ud83dude1c': '😜',
        'ud83dude18': '😘',
        'ud83dude17': '😗',
        'ud83dude19': '😙',
        'ud83dude1d': '😝',
        'ud83dude24': '😤',
        'ud83dude16': '😖',
        'ud83dude0b': '😋',
        'ud83dude05': '😅',
        'ud83dude1e': '😞',
        'ud83dude0e': '😎',
        'ud83dude2f': '😯',
        'ud83dude21': '😡',
        'ud83dude26': '😦',
        'ud83dude28': '😨',
        'ud83dude27': '😧',
        'ud83dude2e': '😮',
        'ud83dude35': '😵',
        'ud83dude08': '😈',
        'ud83dude07': '😇',
        'ud83dude06': '😆',
        'ud83dude1a': '😚',
        'ud83dude0c': '😌',
        'ud83dude0f': '😏',
        'ud83dude31': '🌧️',
        'ud83dude34': '😴',
        'ud83cudf89': '🎉',
        'ud83dude4c': '👌',
        'ud83dude4f': '👏',
        'ud83dude46': '👆',
        'ud83dude45': '👅',
        'ud83dude4e': '👎',
        'ud83dude47': '👇',
        'ud83dude4d': '👍',
        'ud83dude4a': '👊',
        'ud83dude48': '👈',
        'ud83dude49': '👉',
        'ud83dude4b': '👋',
        'ud83dude4c': '👌',
        'ud83dude50': '👐',
        'ud83dude51': '👑',
        'ud83dude52': '👒',
        'ud83dude54': '👔',
        'ud83dude53': '👓',
        'ud83dude55': '👕',
        'ud83dude56': '👖',
        'ud83dude57': '👗',
        'ud83dude58': '👘',
        'ud83dude59': '👙',
        'ud83dude5a': '👚',
        'ud83dude5b': '👛',
        'ud83dude5c': '👜',
        'ud83dude5d': '👝',
        'ud83dude5e': '👞',
        'ud83dude5f': '👟',
        'ud83dude60': '👠',
        'ud83dude61': '👡',
        'ud83dude62': '👢',
        'ud83dude63': '👣',
        'ud83dude64': '👤',
        'ud83dude65': '👥',
        'ud83dude66': '👦',
        'ud83dude67': '👧',
        'ud83dude68': '👨',
        'ud83dude69': '👩',
        'ud83dude6a': '👪',
        'ud83dude6b': '👫',
        'ud83dude6c': '👬',
        'ud83dude6d': '👭',
        'ud83dude6e': '👮',
        'ud83dude6f': '👯',
        'ud83dude70': '👰',
        'ud83dude71': '👱',
        'ud83dude72': '👲',
        'ud83dude73': '👳',
        'ud83dude74': '👴',
        'ud83dude75': '👵',
        'ud83dude76': '👶',
        'ud83dude77': '👷',
        'ud83dude78': '👸',
        'ud83dude79': '👹',
        'ud83dude7a': '👺',
        'ud83dude7b': '👻',
        'ud83dude7c': '👼',
        'ud83dude7d': '👽',
        'ud83dude7e': '👾',
        'ud83dude7f': '👿',
        'ud83dude81': '💁',
        'ud83dude82': '💂',
        'ud83dude83': '💃',
        'ud83dude84': '💄',
        'ud83dude85': '💅',
        'ud83dude86': '💆',
        'ud83dude87': '💇',
        'ud83dude88': '💈',
        'ud83dude89': '💉',
        'ud83dude8a': '💊',
        'ud83dude8b': '💋',
        'ud83dude8c': '💌',
        'ud83dude8d': '💍',
        'ud83dude8e': '💎',
        'ud83dude8f': '💏',
        'ud83dude90': '💐',
        'ud83dude91': '💑',
        'ud83dude92': '💒',
        'ud83dude93': '💓',
        'ud83dude94': '💔',
        'ud83dude95': '💕',
        'ud83dude96': '💖',
        'ud83dude97': '💗',
        'ud83dude98': '💘',
        'ud83dude99': '💙',
        'ud83dude9a': '💚',
        'ud83dude9b': '💛',
        'ud83dude9c': '💜',
        'ud83dude9d': '💝',
        'ud83dude9e': '💞',
        'ud83dude9f': '💟',
        'ud83dudea0': '💠',
        'ud83dudea1': '💡',
        'ud83dudea2': '💢',
        'ud83dudea3': '💣',
        'ud83dudea4': '💤',
        'ud83dudea6': '💦',
        'ud83dudea7': '💧',
        'ud83dudea8': '💨',
        'ud83dudea9': '💩',
        'ud83dudeaa': '💪',
        'ud83dudeab': '💫',
        'ud83dudeac': '💬',
        'ud83dudead': '💭',
        'ud83dudeae': '💮',
        'ud83dudeaf': '💯',
        'ud83dudeb0': '💰',
        'ud83dudeb1': '💱',
        'ud83dudeb2': '💲',
        'ud83dudeb3': '💳',
        'ud83dudeb4': '💴',
        'ud83dudeb5': '💵',
        'ud83dudeb6': '💶',
        'ud83dudeb7': '💷',
        'ud83dudeb8': '💸',
        'ud83dudeb9': '💹',
        'ud83dudeba': '💺',
        'ud83dudebb': '💻',
        'ud83dudebc': '💼',
        'ud83dudebd': '💽',
        'ud83dudebe': '💾',
        'ud83dudebf': '💿',
        'ud83dudec0': '📀',
        'ud83dudec1': '📁',
        'ud83dudec2': '📂',
        'ud83dudec3': '📃',
        'ud83dudec4': '📄',
        'ud83dudec5': '📅',
        'ud83dudec6': '📆',
        'ud83dudec7': '📇',
        'ud83dudec8': '📈',
        'ud83dudec9': '📉',
        'ud83dudeca': '📊',
        'ud83dudecb': '📋',
        'ud83dudecc': '📌',
        'ud83dudecd': '📍',
        'ud83dudece': '📎',
        'ud83dudecf': '📏',
        'ud83duded0': '📐',
        'ud83duded1': '📑',
        'ud83duded2': '📒',
        'ud83duded3': '📓',
        'ud83duded4': '📔',
        'ud83duded5': '📕',
        'ud83duded6': '📖',
        'ud83duded7': '📗',
        'ud83duded8': '📘',
        'ud83duded9': '📙',
        'ud83dudeda': '📚',
        'ud83dudedb': '📛',
        'ud83dudedc': '📜',
        'ud83dudedd': '📝',
        'ud83dudede': '📞',
        'ud83dudedf': '📟',
        'ud83dudca8': '💨',
        'ud83dudca7': '💧',
        'ud83dudca6': '💦',
        'ud83dudcaa': '💪',
        'ud83dudca5': '💥',
        'ud83dudca3': '💣',
        'ud83dudca2': '💢',
        'ud83dudca4': '💤',
        'ud83dudc8a': '🎊',
        'ud83dudc8b': '🎋',
        'ud83dudc8c': '🎌',
        'ud83dudc8d': '🎍',
        'ud83dudc8e': '🎎',
        'ud83dudc8f': '🎏',
        'ud83dudc90': '🎐',
        'ud83dudc91': '🎑',
        'ud83dudc92': '🎒',
        'ud83dudc93': '🎓',
        'ud83dudc94': '🎔',
        'ud83dudc95': '🎕',
        'ud83dudc96': '🎖️',
        'ud83dudc97': '🎗️',
        'ud83dudc98': '🎘',
        'ud83dudc99': '🎙️',
        'ud83dudc9a': '🎚️',
        'ud83dudc9b': '🎛️',
        'ud83dudc9c': '🎜',
        'ud83dudc9d': '🎝',
        'ud83dudc9e': '🎞️',
        'ud83dudc9f': '🎟️',
        'ud83dudca0': '🎠',
        'ud83dudca1': '🎡',
        'ud83dudca2': '🎢',
        'ud83dudca3': '🎣',
        'ud83dudca4': '🎤',
        'ud83dudca5': '🎥',
        'ud83dudca6': '🎦',
        'ud83dudca7': '🎧',
        'ud83dudca8': '🎨',
        'ud83dudca9': '🎩',
        'ud83dudcaa': '🎪',
        'ud83dudcab': '🎫',
        'ud83dudcac': '🎬',
        'ud83dudcad': '🎭',
        'ud83dudcae': '🎮',
        'ud83dudcaf': '🎯',
        'ud83dudcb0': '🎰',
        'ud83dudcb1': '🎱',
        'ud83dudcb2': '🎲',
        'ud83dudcb3': '🎳',
        'ud83dudcb4': '🎴',
        'ud83dudcb5': '🎵',
        'ud83dudcb6': '🎶',
        'ud83dudcb7': '🎷',
        'ud83dudcb8': '🎸',
        'ud83dudcb9': '🎹',
        'ud83dudcba': '🎺',
        'ud83dudcbb': '🎻',
        'ud83dudcbc': '🎼',
        'ud83dudcbd': '🎽',
        'ud83dudcbe': '🎾',
        'ud83dudcbf': '🎿',
        'ud83dudcc0': '🏀',
        'ud83dudcc1': '🏁',
        'ud83dudcc2': '🏂',
        'ud83dudcc3': '🏃',
        'ud83dudcc4': '🏄',
        'ud83dudcc5': '🏅',
        'ud83dudcc6': '🏆',
        'ud83dudcc7': '🏇',
        'ud83dudcc8': '🏈',
        'ud83dudcc9': '🏉',
        'ud83dudcca': '🏊',
        'ud83dudccb': '🏋️',
        'ud83dudccc': '🏌️',
        'ud83dudccd': '🏍️',
        'ud83dudcce': '🏎️',
        'ud83dudccf': '🏏',
        'ud83dudccf': '🔥',
        'ud83eudef6': '🛶',
        'ud83dudcf7': '📷',
        'ud83dudc47': '👇',
        'ud83dudc49': '👉',
        'ud83dudce5': '📍',
        'ud83eudd23': '🤣',
        'ud83dudd25': '🔥',
        'ud83euddd1u200d': '🧑‍',
        'ud83dude80': '🚀',
        'ud83dudc47': '👇',
        'ud83euddd1': '🧑‍🚀',
        'ud83dudcf2': '📲',
        'u2b07ufe0f': '⬇️',
        'u2022':      '•', 
        'u2019':      '’', 
        'u26a0': '⚠️',
        'u00a9': '©',
        'u274c': '❌',
        'u27a1ufe0f': '➡️',
        'ud83dude00': '😀',
        'ud83dude04': '😄',
        'ud83dude42': '😂',
        'ud83dude43': '😃',
        'ud83eudee0': '📰',
        'ud83eudee3': '📣',
        'ud83eudee2': '📢',
        'ud83eudee1': '📡',
        'ud83eude00': '📀',
        'ud83dude2a': '🌀',
        'u263aufe0f': '⚓',
        'ud83dude11': '😔',
        'ud83dude17': '😗',
        'ud83eudee2': '📢',
        'ud83eudee3': '📣',
        'ud83eudee1': '📡',
        'ud83eude10': '📐',
        'ud83eudd28': '😨',
        'ud83eudee8': '📨',
        'ud83eudee5': '📥',
        'ud83eudee6': '📦',
        'ud83dude36': '😶',
        'ud83dude37': '😷',
        'ud83dude38': '😸',
        'ud83dude39': '😹',
        'ud83dude3a': '😺',
        'ud83dude3b': '😻',
        'ud83dude3c': '😼',
        'ud83dude3d': '😽',
        'ud83dude3e': '😾',
        'ud83dude3f': '😿',
        'ud83dude40': '🙀',
        'ud83eude8': '📨',
        'ud83eudee8': '📨',
        'ud83eudd23': '📣',
        'ud83eudee8': '📨',
        'ud83eudee5': '📥',
        'ud83eudee6': '📦',
        'ud83eudee2': '📢',
        'ud83eudee3': '📣',
        'ud83eudee1': '📡',
        'ud83eudd22': '📢',
        'ud83eudd2e': '📦',
        'ud83eudd27': '📨',
        'ud83eudd75': '📣',
        'ud83eudd76': '📦',
        'ud83eudd74': '📨',
        'ud83eudd2f': '🚯',
        'ud83eudd20': '🚠',
        'ud83eudd73': '🛳️',
        'ud83eudd78': '🛸',
        'ud83dude80': '🚀',
        'ud83eudee4': '📤',
        'ud83dude1f': '📟',
        'ud83dude41': '🕁',
        'u2639ufe0f': '☹️',
        'ud83eudee4': '📤',
        'ud83dude1f': '📟',
        'ud83dude41': '🕁',
        'u2639ufe0f': '☹️',
        'ud83dude44': '💄',
        'ud83eudea2': '🛢️',
        'ud83dudeac': '💬',
        'ud83eudd79': '🛹',
        'ud83eude83': '📃',
        'ud83eude75': '📵',
        'ud83eude76': '📶',
        'ud83eude8e': '📎',
        'ud83eudeec': '🗬',
        'ud83eudeed': '🗭',
        'ud83eudeeb': '🗫',
        'ud83eudee0': '🗠',
        'ud83eudee1': '🗡️',
        'ud83eudd10': '🌐',
        'ud83eudd28': '🌨',
        'ud83eudd11': '🌑',
        'ud83eudee2': '🗢',
        'ud83eudee3': '🗣️',
        'ud83eudee2': '🗢',
        'ud83eudee3': '🗣️',
        'ud83eudee1': '🗡️',
        'ud83eudd10': '🌐',
        'ud83eudd36': '🌶️',
        'ud83eudee5': '🗥',
        'ud83eudd2f': '🚯',
        'ud83eudd20': '🚠',
        'ud83eudd73': '🛳️',
        'ud83eudd78': '🛸',
        'ud83eudea2': '🛢️',
        'ud83dude44': '💄',
        'ud83eudd25': '📥',
        'u200d': '',
    }
    for code, emoji_char in emoji_dict.items():
        input_string = input_string.replace(code, emoji_char)
    
    pattern = re.compile(r'ud83[^\s]*')
    
    
    input_string = re.sub(pattern, ' ', input_string)
    return input_string