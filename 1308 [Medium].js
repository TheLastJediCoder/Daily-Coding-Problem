/*
 	This problem was asked by Samsung.

	A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

	For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:

	A <--> B <--> C <--> plant

	Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

	In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

	pipes = {
			'plant': {'A': 1, 'B': 5, 'C': 20},
			'A': {'C': 15},
			'B': {'C': 10},
			'C': {}
	}
*/

const pipes = {
  plant: { A: 1, B: 5, C: 20 },
  A: { C: 15 },
  B: { C: 10 },
  C: {},
};

const edges = [];
const parent = {};
const rank = {};

let totalCost = 0;

for (const node in pipes) {
  parent[node] = node;
  rank[node] = 0;

  for (const neighbor in pipes[node]) {
    edges.push([pipes[node][neighbor], node, neighbor]);
  }
}

edges.sort((a, b) => {
  return a[0] - b[0];
});

function findParent(node) {
  if (parent[node] !== node) {
    parent[node] = findParent(parent[node]);
  }
  return parent[node];
}

for (const [cost, node1, node2] of edges) {
  const node1Parent = findParent(node1);
  const node2Parent = findParent(node2);

	// If parents are same we will skip it.
  if (node1Parent !== node2Parent) {
    if (rank[node1Parent] > rank[node2Parent]) {
      parent[node2Parent] = node1Parent;
    } else if (rank[node2Parent > rank[node1Parent]]) {
      parent[node1Parent] = node2Parent;
    } else {
      parent[node2Parent] = node1Parent;
      rank[node1Parent] += 1;
    }

    totalCost += cost;
  }
}

console.log(totalCost);
