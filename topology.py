import json

def preprocessData(data):
    apps = {}

    for record in data:
        id = record['ID'].strip()
        if id not in apps:
            apps[id] = {'to': [], 'inDegree': 0, 'outDegree': 0}
        if record['Depend']:
            depends = record['Depend'].split(',')

            for depend in depends:
                d = depend.strip()
                if d in apps:
                    apps[id]['inDegree'] += 1
                    apps[d]['outDegree'] += 1
                    apps[d]['to'].append(id)
                else:
                    apps[id]['inDegree'] += 1
                    apps[d] = {'to': [id], 'inDegree': 0, 'outDegree': 1}
    return apps


def topologicalSort(apps):
    queue = []
    top_order = []
    cnt = 0

    current_x = 10
    current_y = 100

    free_apps = []
    current_free_x = 0
    current_free_y = 0

    for id in apps:
        if apps[id]['inDegree'] == 0:
            if apps[id]['outDegree'] == 0:
                free_apps.append(id)
                apps[id]['x'] = current_free_x
                current_free_x = (current_free_x + 40) % 120
                if apps[id]['x'] == 0:
                    current_free_y += 10
                apps[id]['y'] = current_free_y
                cnt += 1
            else:
                queue.append(id)
                if 'x' not in apps[id]:
                    apps[id]['x'] = current_x
                    apps[id]['y'] = current_y
                    current_y += 40

    queue.sort(key=lambda id: apps[id]['outDegree'], reverse=True)

    while queue:
        delta_y = -25
        u = queue.pop(0)
        top_order.append(u)

        for id in apps[u]['to']:
            apps[id]['inDegree'] -= 1
            if apps[id]['inDegree'] == 0:
                queue.append(id)
                if 'x' not in apps[id]:
                    apps[id]['x'] = apps[u]['x'] + 40
                    apps[id]['y'] = apps[u]['y'] + delta_y
                    delta_y -= 15

        queue.sort(key=lambda id: apps[id]['outDegree'], reverse=True)
        cnt += 1

    if cnt != len(apps):
        return ('Error', "There exists a cycle in the graph")
    else:
        return ('OK', top_order)


def prepareToDraw(apps):
    list_nodes = []
    list_edges = []

    index = 0
    for id in apps:
        list_nodes.append({
            "id": id,
            "label": id,
            "size": 3,
            "x": apps[id]['x'],
            "y": apps[id]['y'],
        })

        for d in apps[id]['to']:
            list_edges.append({
                "id": str(index),
                "source": id,
                "target": d,
                'type': "arrow",
                'size': 5,
                'color': "#94aa2a",
            })
            index += 1

    return list_nodes, list_edges

def drawGraph(list_apps, list_edges):
    result = {
        "nodes": list_apps,
        "edges": list_edges
    }

    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)