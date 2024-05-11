import networkx as nx
import matplotlib.pyplot as plt
print("\t\t\tGraph Bridge Finder Algorithm")
input_vertex=int(input("Enter the total number of Vertices:\n\t"))
node_list=[]
for i in range(1, input_vertex+1):
    node_list.append(i)
print("Your vertices nodes are:")
for i in node_list:
    print(i, end="   ")
input_edge=int(input("\nEnter the total number of edges:\n\t"))
print("\t--> Graph has", input_vertex, "vertices and", input_edge, "edges!")
print("\n\t\tInput edges between these Vertices\n\t\tFor example\n\t\t-->  From 1 to 2.")
component_node_list=[]
for i in node_list:
    component_node_list.append([i])
T_component=len(component_node_list)
print("Total components are:", T_component)


def component_check(first_node, second_node, C_list):
    for i in range(len(C_list)):
        if first_node in C_list[i] or second_node in C_list[i]:
            C_list[i].append(first_node)
            C_list[i].append(second_node)
            return C_list
    C_list.append([first_node, second_node])
    return C_list


def component_check1(clist):
    if clist != []:
        for i in range(len(clist)):
            if i+1<len(clist):
                for p in clist[i]:
                    for y in range(i + 1, len(clist)):
                        for o in clist[y]:
                            if p==o:
                                for u in clist[y]:
                                    clist[i].append(u)
                                clist.remove(clist[y])
                                return len(clist)
    return len(clist)
edge_number=1
edge_list=[]
while input_edge>0:
    print("Edge", edge_number, ":")
    first_node=int(input("\tFrom: "))
    second_node=int(input("\tTo:   "))
    if first_node in node_list and second_node in node_list:
        if (first_node, second_node) in edge_list:
            print("This edge already exist.")
        else:
            edge_list.append((first_node, second_node))
            input_edge-=1
            edge_number+=1
            component_node_list=component_check(first_node, second_node, component_node_list)
            T_component=component_check1(component_node_list)
            print("Total components are:", T_component)
    else:
        print("Wrong Node_edge !")
bridge_list=[]
non_bridge_list=[]


def checkbridge(edge_list):
    temporary_component=0
    for i in range(0, len(edge_list)):
        temporary_list = []
        list_bridge_check = []
        for s in node_list:
            list_bridge_check.append([s])
        for e in edge_list:
            temporary_list.append(e)
        temporary_list.remove(temporary_list[i])
        for j in temporary_list:
            list_bridge_check=component_check(j[0], j[1], list_bridge_check)
            temporary_component=component_check1(list_bridge_check)
        if temporary_component==T_component:
            non_bridge_list.append(edge_list[i])
        else:
            bridge_list.append(edge_list[i])
checkbridge(edge_list)
print("\t\tGraph Details")
print("Bridges are:", bridge_list)
print("Non_bridges are:", non_bridge_list)
print("Total components are:", T_component)
input_graph=nx.DiGraph()
input_graph.add_nodes_from(node_list)
input_graph.add_edges_from(edge_list)
plt.title('Your given Graph', fontsize=16, color='red')
graph_form = nx.circular_layout(input_graph)
nx.draw(input_graph, pos=graph_form, with_labels=True, node_color='lightblue', node_size=1000, width=2,
        edge_color='gray')
plt.show()
bridge_graph = nx.DiGraph()
bridge_graph.add_nodes_from(node_list)
bridge_graph.add_edges_from(bridge_list, color='red')
bridge_graph.add_edges_from(non_bridge_list, color='blue')
plt.title('Graph with Bridge and Non-bridge Edges', fontsize=16, color='red')
edge_colors = [bridge_graph[u][v]['color'] for u, v in bridge_graph.edges()]
plt.axis('off')
nx.draw(bridge_graph, pos=graph_form, with_labels=True, node_color='lightblue', node_size=1000, width=2,
        edge_color=edge_colors)
red_label = plt.Line2D([], [], color='red', linewidth=3, label='Bridge')
blue_label = plt.Line2D([], [], color='blue', linewidth=3, label='Non-bridge')
plt.legend(handles=[red_label, blue_label])
plt.show()
