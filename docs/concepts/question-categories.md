# Question Categories

When we demonstrate CoPilot we want to show a variety of types of questions.
We often start with simple questions and proceed to more complex questions.

1.  **Metrics** - These are simple questions that usually return the count
of the number of items in the database.  Example: *"How many customers do we have in the database?"*
2.  **Metadata** - These questions ask about the structure of the database or the meanings
of different items.  Example: *"Show the data model for customers and products"*
3.  **Rules** - Describe business rules.  Example: *"What are the calculations for LTV?"*
4.  **Instance Questions** - Questions that ask for information about a single item in the database
when a unique identifier is given.  Example: *"Show details for Store #4747"*
5.  **Non-Traversal Questions** - These are questions that can be answered by listing
items of a homogeneous type with a simple qualifier.  *"How many products are there with a Category of Beverage?"*
6.  **Path** - These queries traverse multiple relationships.  Example: *"How many customers purchased more than three beverage products?"*
7.  **Report** - These queries run canned reports.  Example: *"Show me the sales for beverage products by  last year"*
8.  **Complex** - These questions execute more complex queries. Example: "Who are the most influential reviewers of products A, B and C"

## Questions that Map to Builtin Queries



## Questions that Count Vertices with a WHERE

```gsql
CREATE QUERY countVertices() FOR GRAPH MyGraph {
  SumAccum<INT> @@vertexCount;
  results = SELECT v FROM MyVertex:v
             WHERE v.some_attribute == "some_value"
             ACCUM @@vertexCount += 1;
  PRINT @@vertexCount;
}
```