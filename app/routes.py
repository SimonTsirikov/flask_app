from flask import request, jsonify
from app import app

titles = list()
contents = list()


@app.route('/notes', methods=['GET'])
def getnotes():
    if (len(titles) == 0):
        return jsonify({}), 204
    else:
        return jsonify({"id":i, "title": titles[i], "content": contents[i]} for i in range(len(titles))), 200


@app.route('/notes', methods=['POST'])
def postnotes():
    content = request.get_json()
    if (content['content'] == None):
        return jsonify({}), 400
    contents.append(content['content'])
    if (content['title'] != None):
        titles.append(content['title'])
    else:
        titles.append(content['content'][0:app.config['N']])
    return jsonify({"id":len(titles) - 1, "title":titles[counter], "content":contents[counter]}), 201


@app.route('/notes/<id>', methods=['GET'])
def getnotesid(id):
    if (id < 0 or id >= len(titles)):
        return jsonify({}), 404
    else:
        return jsonify({"id":id, "title": titles[id], "content": contents[id]}), 200


@app.route('/notes/<id>', methods=['PUT'])
def putnotesid(id):
    if (id < 0 or id >= len(titles)):
        return jsonify({}), 404
    else:
        content = request.get_json()
        if (content['content'] == None):
            return jsonify({}), 400
        contents[id] = content['content']
        if (content['title'] != None):
            titles[id] = content['title']
        else:
            titles[id] = content['content'][0:app.config['N']]
        return jsonify({"id":id, "title":titles[id], "content":contents[id]}), 202


@app.route('/notes/<id>', methods=['DELETE'])
def deletenotesid(id):
    if (id < 0 or id >= len(titles)):
        return jsonify({}), 404
    else:
        contents.pop(id)
        titles.pop(id)


@app.route('/notes?query=<string>', methods=['GET'])
def getnotesquery(string):
    return jsonify({"id":i, "title": titles[i], "content": contents[i]} for i in range(len(titles)) if string in titles[i] or string in contents[i]), 200
