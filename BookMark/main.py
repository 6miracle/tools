import os
import json

def dfs(bookmap, bookmarks):
    if bookmarks['type'] == 'url':
        bookmap[bookmarks['name']] = bookmarks['url']
    else:
        for bookmark in bookmarks['children']:
            bookmap[bookmark['name']] = {}
            dfs(bookmap[bookmark['name']], bookmark)



if __name__ == '__main__':
    path = os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks'

    bookmarkMap = {}
    with open(path, encoding="utf-8") as f:
        content = f.read()
        dict = json.loads(content)
        bookmarkDirs = dict['roots']['bookmark_bar']['children']  # 书签栏
        for bookmarkDir in bookmarkDirs:
            name = bookmarkDir['name']
            if bookmarkDir['type'] == 'url':
                bookmarkMap[bookmarkDir['name']] = bookmarkDir['url']
            else:
                bookmarkMap[name] = {}
                dfs(bookmarkMap[name], bookmarkDir)

    with open("bookmark.json", 'w', encoding="utf-8") as f:
        json.dump(bookmarkMap, f, ensure_ascii=False)

