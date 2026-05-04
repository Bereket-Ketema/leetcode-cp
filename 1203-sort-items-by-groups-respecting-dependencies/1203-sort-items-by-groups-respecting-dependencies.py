from collections import defaultdict, deque

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        # Assign unique groups to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Graphs
        item_graph = defaultdict(list)
        group_graph = defaultdict(list)

        item_indegree = [0] * n
        group_indegree = [0] * m

        # Items in each group
        group_items = defaultdict(list)
        for i in range(n):
            group_items[group[i]].append(i)

        # Build graphs
        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(nodes, graph, indegree):
            q = deque([x for x in nodes if indegree[x] == 0])
            order = []

            while q:
                node = q.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

            return order if len(order) == len(nodes) else []

        # Topological sort groups
        group_order = topo_sort(list(range(m)), group_graph, group_indegree)
        if not group_order:
            return []

        # Topological sort items
        item_order = topo_sort(list(range(n)), item_graph, item_indegree)
        if not item_order:
            return []

        # Group items according to item topo order
        ordered_items_by_group = defaultdict(list)
        for item in item_order:
            ordered_items_by_group[group[item]].append(item)

        # Build final answer following group order
        result = []
        for g in group_order:
            result.extend(ordered_items_by_group[g])

        return result