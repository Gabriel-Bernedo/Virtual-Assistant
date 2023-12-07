from ..models.Section import Section

def getDataTree(rootName : str, function : any, node : Section = None) -> dict:
    data = {}
    queryset = Section.objects.filter(section_root=node).order_by("section_index")
    #Section nodes of the Tree

    nodes = []
    for section in queryset:
        nodes.append(getDataTree(rootName,function,section))

    #Information of the Tree

    if len(nodes) == 0:
        data["isEnd"] = True
        data[rootName] = function(node)
    else:
        if node == None:
            data[rootName] = nodes
        else:
            data["title"] = node.section_name
            data["isEnd"] = False
            data[rootName] = nodes
    
    

    return data