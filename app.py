from binary import Binary
from buffer import Buffer
from folder import Folder
from log import Log

from flask import Flask, request, jsonify
app = Flask(__name__)
deleted = []

root = Folder('root', 0, None)


@app.route('/binary', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def binary():
    if request.method == 'POST':
        if any(bina.name == request.args.get('name') for bina in root.children):
            return jsonify({
                "message": "Binary file with this name already exists",
            }), 400
        bina = Binary(root, request.args.get('name'), request.args.get('content'))
        return jsonify({
            "message": "Binary file was created",
            "binary": {
                "parent": str(bina.parent.name),
                "name": str(bina.name),
                "content": str(bina.content)
            }
        }), 201

    elif request.method == 'GET':
        if any(bina.name == request.args.get('name') for bina in root.children):
            bina = next(x for x in root.children if x.name == request.args.get('name'))
            return jsonify({
                "message": "Binary file was read",
                "binary": {
                    "parent": str(bina.parent.name),
                    "name": str(bina.name),
                    "content": str(bina.content)
                }
            }), 200
        return jsonify({
            "message": "Binary file does not exist",
        }), 400

    elif request.method == 'PATCH':
        if any(bina.name == request.args.get('name') for bina in root.children):
            bina = next(x for x in root.children if x.name == request.args.get('name'))
            bina.move(root)
            return jsonify({
                "message": "Binary file was moved",
                "binary": {
                    "parent": str(bina.parent.name),
                    "name": str(bina.name),
                    "content": str(bina.content)
                }
            }), 200
        return jsonify({
            "message": "File doesn't exist.",
        }), 400

    elif request.method == 'DELETE':
        if request.args.get('name') not in deleted and any(
                bina.name == request.args.get('name') for bina in root.children):
            bina = next(x for x in root.children if x.name == request.args.get('name'))
            del bina
            deleted.append(request.args.get('name'))
            return jsonify({
                "message": "Binary file was deleted",
            }), 200
        return jsonify({
            "message": "Binary file was not deleted",
        }), 400


@app.route('/buffer', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def buffer():
    if request.method == 'POST':
        if any(buf.name == request.args.get('name') for buf in root.children):
            return jsonify({
                "message": "Buffer file with this name already exists",
            }), 400
        buf = Buffer(root, request.args.get('size'), request.args.get('name'))
        return jsonify({
            "message": "Buffer file was created",
            "buffer": {
                "parent": str(buf.parent),
                "name": str(buf.name),
                "size": int(buf.size),
                "content": list(buf.content)
            }
        }), 201

    elif request.method == 'GET':
        if any(buf.name == request.args.get('name') for buf in root.children):
            buf = next(x for x in root.children if x.name == request.args.get('name'))
            return jsonify({
                "message": "Buffer file was created",
                "buffer": {
                    "parent": str(buf.parent),
                    "name": str(buf.name),
                    "size": int(buf.size),
                    "content": list(buf.content)
                }
            }), 200
        return jsonify({
            "message": "Buffer file does not exist",
        }), 400

    elif request.method == 'PATCH':
        if any(buf.name == request.args.get('name') for buf in root.children):
            buf = next(x for x in root.children if x.name == request.args.get('name'))
            if request.args.get('parent'):
                buf.move(root)
                return jsonify({
                    "message": "Buffer file was moved",
                    "buffer": {
                        "parent": str(buf.parent),
                        "name": str(buf.name),
                        "size": int(buf.size),
                        "content": list(buf.content)
                    }
                }), 200
            if request.args.get('append'):
                buf.push(request.args.get('append'))
                return jsonify({
                    "message": "Line was added to buffer file",
                    "buffer": {
                        "parent": str(buf.parent),
                        "name": str(buf.name),
                        "size": int(buf.size),
                        "content": list(buf.content)
                    }
                }), 201
            if request.args.get('consume'):
                if len(buf.content) > 0:
                    buf.consume()
                return jsonify({
                    "message": "Line was consumed from buffer file",
                    "buffer": {
                        "parent": str(buf.parent),
                        "name": str(buf.name),
                        "size": int(buf.size),
                        "content": list(buf.content)
                    }
                }), 200
            return jsonify({
                "message": "Bad request",
            }), 400
        return jsonify({
            "message": "Buffer file does not exist",
        }), 400

    elif request.method == 'DELETE':
        if request.args.get('name') not in deleted and any(
                buf.name == request.args.get('name') for buf in root.children):
            buf = next(x for x in root.children if x.name == request.args.get('name'))
            del buf
            deleted.append(request.args.get('name'))
            return jsonify({
                "message": "Buffer file was deleted",
            }), 200
        return jsonify({
            "message": "Buffer file was not deleted",
        }), 400


@app.route('/folder', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def folder():
    if request.method == 'POST':
        if any(fold.name == request.args.get('name') for fold in root.children) or request.args.get('name') == 'root':
            return jsonify({
                "message": "Folder with this name already exists",
            }), 400
        fold = Folder(request.args.get('name'), request.args.get('lim'), root)
        return jsonify({
            "message": "Folder was created",
            "folder": {
                "parent": str(fold.parent),
                "name": str(fold.name),
                "lim": int(fold.lim),
                "count": int(fold.count),
                "children": str(fold.children),
            }
        }), 201

    elif request.method == 'GET':
        if any(fold.name == request.args.get('name') for fold in root.children) or request.args.get('name') == 'root':
            if request.args.get('name') == 'root':
                fold = root
            else:
                fold = next(x for x in root.children if x.name == request.args.get('name'))
            return jsonify({
                "message": "Folder was read",
                "folder": {
                    "parent": str(fold.parent),
                    "name": str(fold.name),
                    "lim": int(fold.lim),
                    "count": int(fold.count),
                    "children": str(fold.children)
                }
            }), 200
        return jsonify({
            "message": "Folder does not exist",
        }), 400

    elif request.method == 'PATCH':
        if any(fold.name == request.args.get('name') for fold in root.children):
            fold = next(x for x in root.children if x.name == request.args.get('name'))
            fold.move(root)
            return jsonify({
                "message": "Folder was moved",
                "folder": {
                    "parent": str(fold.parent),
                    "name": str(fold.name),
                    "lim": int(fold.lim),
                    "count": int(fold.count),
                    "children": str(fold.children)
                }
            }), 200
        return jsonify({
            "message": "Folder does not exist",
        }), 400

    elif request.method == 'DELETE':
        if request.args.get('name') not in deleted and any(
                fold.name == request.args.get('name') for fold in root.children):
            fold = next(x for x in root.children if x.name == request.args.get('name'))
            del fold
            deleted.append(request.args.get('name'))
            return jsonify({
                "message": "Directory was deleted",
            }), 200
        return jsonify({
            "message": "Directory was not deleted",
        }), 400


@app.route('/log', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def log():
    if request.method == 'POST':
        if any(logf.name == request.args.get('name') for logf in root.children):
            return jsonify({
                "message": "Log file with this name already exists",
            }), 400
        logf = Log(root, request.args.get('name'), request.args.get('content'))
        return jsonify({
            "message": "Log file was created",
            "log": {
                "parent": str(logf.parent.name),
                "name": str(logf.name),
                "info": str(logf.content)
            }
        }), 201

    elif request.method == 'GET':
        if any(logf.name == request.args.get('name') for logf in root.children):
            logf = next(x for x in root.children if x.name == request.args.get('name'))
            return jsonify({
                "message": "File was read successfully.",
                "log": {
                    "parent": str(logf.parent.name),
                    "name": str(logf.name),
                    "info": str(logf.content)
                }
            }), 200
        return jsonify({
            "message": "Log file does not exist",
        }), 400

    elif request.method == 'PATCH':
        if any(logf.name == request.args.get('name') for logf in root.children):
            logf = next(x for x in root.children if x.name == request.args.get('name'))
            if request.args.get('parent'):
                logf.move(root)
                return jsonify({
                    "message": "Log file was moved",
                    "log": {
                        "parent": str(logf.parent.name),
                        "name": str(logf.name),
                        "info": str(logf.content)
                    }
                }), 200
            if request.args.get('append'):
                logf.append(request.args.get('append'))
                return jsonify({
                    "message": "Line was appended to log file",
                    "log": {
                        "parent": str(logf.parent.name),
                        "name": str(logf.name),
                        "info": str(logf.content)
                    }
                }), 201
            return jsonify({
                "message": "Bad request",
            }), 400
        return jsonify({
            "message": "Log file does not exist",
        }), 400

    elif request.method == 'DELETE':
        if request.args.get('name') not in deleted and any(
                logf.name == request.args.get('name') for logf in root.children):
            logf = next(x for x in root.children if x.name == request.args.get('name'))
            del logf
            deleted.append(request.args.get('name'))
            return jsonify({
                "message": "Log file was deleted",
            }), 200
        return jsonify({
            "message": "Log file was not deleted",
        }), 400


if __name__ == '__main__':
    app.run(debug=True)

